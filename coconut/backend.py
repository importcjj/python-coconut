
from __future__ import absolute_import
from coconut.registry.selector import RandomService

import json
import grpc

from coconut.protos.backend import backend_pb2_grpc, backend_pb2
from coconut.protos.tasks import task_pb2
from coconut.task import Arg


class NoServiceAvailable(Exception):
    pass


_DEFAULT_BACKEND_SERVICE_NAME = 'coconut-backend'


class Backend(object):
    def __init__(self, registry=None):
        self.registry = registry

    def publish(
            self,
            service_name,
            key,
            args=None,
            countdown=0):
        services = self.registry.get_service(_DEFAULT_BACKEND_SERVICE_NAME)
        service = RandomService(services)

        if service is None:
            raise NoServiceAvailable

        address = '{}:{}'.format(service.address, service.port)
        with grpc.insecure_channel(address) as channel:
            stub = backend_pb2_grpc.TaskBackendStub(channel)
            request = task_pb2.Signature(
                service=service_name,
                key=key)

            if args is not None:
                request.args = json.dumps(
                    [Arg(arg).__dict__ for arg in args]).encode()
            response = stub.RPCPublishTask(request)
            return response
