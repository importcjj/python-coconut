from __future__ import absolute_import
import json
from coconut.protos.tasks import task_pb2


class Arg(object):
    def __init__(self, value, typ=None):
        self.name = ''
        if isinstance(value, int):
            self.type = 'int64'
            self.value = value
        elif isinstance(value, float):
            self.type = 'float64'
            self.value = value
        elif isinstance(value, bool):
            self.type = 'bool'
            self.value = value
        elif isinstance(value, str):
            self.type = 'string'
            self.value = value
        elif isinstance(value, Arg):
            self.type = value.type
            self.value = value.value
        else:
            self.__dict__ = value.__dict__

        if typ is not None:
            self.type = typ


class Result(object):
    def __init__(self, ret):
        if isinstance(ret, int):
            self.type = 'int64'
            self.value = ret
        elif isinstance(ret, float):
            self.type = 'float64'
            self.value = ret
        elif isinstance(ret, bool):
            self.type = 'bool'
            self.value = ret
        elif isinstance(ret, str):
            self.type = 'string'
            self.value = ret
        else:
            self.type = 'string'
            self.value = ret

    def encode_value(self):
        return json.dumps(self.value).encode()


class Task(object):
    def __init__(self, f, request):

        self.f = f
        self.request = request
        self.args = json.loads(request.args.decode())

    def __task_args(self):
        return [arg.get('value') for arg in self.args]

    def call(self):
        args = self.__task_args()
        rets = self.f(*args)

        if not isinstance(rets, tuple):
            rets = (rets, )

        results = []
        for ret in rets:
            results.append(Result(ret))

        return results
