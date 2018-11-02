# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from coconut.protos.backend import backend_pb2 as coconut_dot_protos_dot_backend_dot_backend__pb2
from coconut.protos.tasks import task_pb2 as coconut_dot_protos_dot_tasks_dot_task__pb2


class TaskBackendStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RPCPublishTask = channel.unary_unary(
        '/backend.TaskBackend/RPCPublishTask',
        request_serializer=coconut_dot_protos_dot_tasks_dot_task__pb2.Signature.SerializeToString,
        response_deserializer=coconut_dot_protos_dot_tasks_dot_task__pb2.Signature.FromString,
        )
    self.RPCSetTaskStateStarted = channel.unary_unary(
        '/backend.TaskBackend/RPCSetTaskStateStarted',
        request_serializer=coconut_dot_protos_dot_tasks_dot_task__pb2.State.SerializeToString,
        response_deserializer=coconut_dot_protos_dot_backend_dot_backend__pb2.TaskStateSetResp.FromString,
        )
    self.RPCSetTaskStateReceived = channel.unary_unary(
        '/backend.TaskBackend/RPCSetTaskStateReceived',
        request_serializer=coconut_dot_protos_dot_tasks_dot_task__pb2.State.SerializeToString,
        response_deserializer=coconut_dot_protos_dot_backend_dot_backend__pb2.TaskStateSetResp.FromString,
        )
    self.RPCSetTaskStatePending = channel.unary_unary(
        '/backend.TaskBackend/RPCSetTaskStatePending',
        request_serializer=coconut_dot_protos_dot_tasks_dot_task__pb2.State.SerializeToString,
        response_deserializer=coconut_dot_protos_dot_backend_dot_backend__pb2.TaskStateSetResp.FromString,
        )
    self.RPCSetTaskStateSuccess = channel.unary_unary(
        '/backend.TaskBackend/RPCSetTaskStateSuccess',
        request_serializer=coconut_dot_protos_dot_tasks_dot_task__pb2.State.SerializeToString,
        response_deserializer=coconut_dot_protos_dot_backend_dot_backend__pb2.TaskStateSetResp.FromString,
        )
    self.RPCSetTaskStateRetry = channel.unary_unary(
        '/backend.TaskBackend/RPCSetTaskStateRetry',
        request_serializer=coconut_dot_protos_dot_tasks_dot_task__pb2.State.SerializeToString,
        response_deserializer=coconut_dot_protos_dot_backend_dot_backend__pb2.TaskStateSetResp.FromString,
        )
    self.RPCSetTaskStateFailure = channel.unary_unary(
        '/backend.TaskBackend/RPCSetTaskStateFailure',
        request_serializer=coconut_dot_protos_dot_tasks_dot_task__pb2.State.SerializeToString,
        response_deserializer=coconut_dot_protos_dot_backend_dot_backend__pb2.TaskStateSetResp.FromString,
        )
    self.RPCGetTaskState = channel.unary_unary(
        '/backend.TaskBackend/RPCGetTaskState',
        request_serializer=coconut_dot_protos_dot_tasks_dot_task__pb2.UUID.SerializeToString,
        response_deserializer=coconut_dot_protos_dot_tasks_dot_task__pb2.State.FromString,
        )


class TaskBackendServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RPCPublishTask(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RPCSetTaskStateStarted(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RPCSetTaskStateReceived(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RPCSetTaskStatePending(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RPCSetTaskStateSuccess(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RPCSetTaskStateRetry(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RPCSetTaskStateFailure(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RPCGetTaskState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TaskBackendServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RPCPublishTask': grpc.unary_unary_rpc_method_handler(
          servicer.RPCPublishTask,
          request_deserializer=coconut_dot_protos_dot_tasks_dot_task__pb2.Signature.FromString,
          response_serializer=coconut_dot_protos_dot_tasks_dot_task__pb2.Signature.SerializeToString,
      ),
      'RPCSetTaskStateStarted': grpc.unary_unary_rpc_method_handler(
          servicer.RPCSetTaskStateStarted,
          request_deserializer=coconut_dot_protos_dot_tasks_dot_task__pb2.State.FromString,
          response_serializer=coconut_dot_protos_dot_backend_dot_backend__pb2.TaskStateSetResp.SerializeToString,
      ),
      'RPCSetTaskStateReceived': grpc.unary_unary_rpc_method_handler(
          servicer.RPCSetTaskStateReceived,
          request_deserializer=coconut_dot_protos_dot_tasks_dot_task__pb2.State.FromString,
          response_serializer=coconut_dot_protos_dot_backend_dot_backend__pb2.TaskStateSetResp.SerializeToString,
      ),
      'RPCSetTaskStatePending': grpc.unary_unary_rpc_method_handler(
          servicer.RPCSetTaskStatePending,
          request_deserializer=coconut_dot_protos_dot_tasks_dot_task__pb2.State.FromString,
          response_serializer=coconut_dot_protos_dot_backend_dot_backend__pb2.TaskStateSetResp.SerializeToString,
      ),
      'RPCSetTaskStateSuccess': grpc.unary_unary_rpc_method_handler(
          servicer.RPCSetTaskStateSuccess,
          request_deserializer=coconut_dot_protos_dot_tasks_dot_task__pb2.State.FromString,
          response_serializer=coconut_dot_protos_dot_backend_dot_backend__pb2.TaskStateSetResp.SerializeToString,
      ),
      'RPCSetTaskStateRetry': grpc.unary_unary_rpc_method_handler(
          servicer.RPCSetTaskStateRetry,
          request_deserializer=coconut_dot_protos_dot_tasks_dot_task__pb2.State.FromString,
          response_serializer=coconut_dot_protos_dot_backend_dot_backend__pb2.TaskStateSetResp.SerializeToString,
      ),
      'RPCSetTaskStateFailure': grpc.unary_unary_rpc_method_handler(
          servicer.RPCSetTaskStateFailure,
          request_deserializer=coconut_dot_protos_dot_tasks_dot_task__pb2.State.FromString,
          response_serializer=coconut_dot_protos_dot_backend_dot_backend__pb2.TaskStateSetResp.SerializeToString,
      ),
      'RPCGetTaskState': grpc.unary_unary_rpc_method_handler(
          servicer.RPCGetTaskState,
          request_deserializer=coconut_dot_protos_dot_tasks_dot_task__pb2.UUID.FromString,
          response_serializer=coconut_dot_protos_dot_tasks_dot_task__pb2.State.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'backend.TaskBackend', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
