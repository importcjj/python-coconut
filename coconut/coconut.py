from __future__ import absolute_import

from concurrent import futures
import time
import json
import functools

import grpc

from coconut import registry
from coconut.rpc_server import Runner
from coconut.protos.runner import runner_pb2_grpc
from coconut.protos.tasks import task_pb2
from coconut.service import Service
from coconut.task import Task
from coconut.utils import get_lan_ip, new_uuid


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Coconut(object):
    def __init__(
            self,
            name='coconut-python-runner',
            host=None,
            port=6666,
            registry_host=None,
            registry_port=0):

        self.name = name
        if host is None:
            self.host = get_lan_ip()
        else:
            self.host = host
        self.port = port
        self.kind = 'coconut-runner'

        self.registry = registry.Consul(registry_host, registry_port)
        self.funcs = {}

    def __process(self, request, context):
        if request.key not in self.funcs:
            context.set_code(500)
            context.set_details("Task not found")
            return task_pb2.Reply()

        f = self.funcs[request.key]

        try:
            task = Task(f, request)
            results = task.call()

            return task_pb2.Reply(results=[task_pb2.Result(type=result.type, value=result.encode()) for result in results])
        except Exception as e:
            print("Call task failed {}".format(e))
            context.set_code(500)
            context.set_details(str(e))
            return task_pb2.Reply()

    def serve(self):
        """
        serve task request
        """
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        runner_pb2_grpc.add_RunnerServicer_to_server(
            Runner(self.__process), server)
        server.add_insecure_port('{}:{}'.format(self.host, self.port))
        server.start()

        self.server = server

        print('grpc Server started on {}:{}'.format(self.host, self.port))
        self.__register_service()

        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            self.__deregister_service()
            server.stop(0)

    def register(self, *args, **kwargs):
        """
        register task function
        """
        def wrapper(f):

            key = kwargs.get('key') or f.__name__
            self.funcs[key] = f

            @functools.wraps(f)
            def __func(*args, **kwargs):
                return f(*args, **kwargs)

            return __func
        return wrapper

    def __register_service(self):
        service = Service(
            self.name,
            new_uuid(),
            self.kind,
            self.host,
            self.port
        )
        print("Registering {}: {}".format(service.kind, service.service_id))
        self.registry.register(service)
        self.service = service

    def __deregister_service(self):
        if self.service is not None:
            print("Deregistering {}...".format(self.service.kind))
            self.registry.deregister(self.service)
