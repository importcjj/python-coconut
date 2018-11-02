from __future__ import absolute_import
from coconut.protos.tasks import task_pb2
from coconut.protos.runner import runner_pb2_grpc

class Runner(runner_pb2_grpc.RunnerServicer):

    def __init__(self, processer=None):
        self.processer = processer
    
    def Call(self, request, context):
        if self.processer is not None:
            # print("Before call request", request.key)
            reply = self.processer(request, context)
            # print("After call request", request.key)
            return reply

        context.set_code(500)
        context.set_details("Not implement")
        return task_pb2.Reply()



    

