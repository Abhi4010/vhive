# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import stacking_training_pb2 as stacking__training__pb2


class TrainerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Train = channel.unary_unary(
                '/stacking.Trainer/Train',
                request_serializer=stacking__training__pb2.TrainRequest.SerializeToString,
                response_deserializer=stacking__training__pb2.TrainReply.FromString,
                )


class TrainerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Train(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrainerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Train': grpc.unary_unary_rpc_method_handler(
                    servicer.Train,
                    request_deserializer=stacking__training__pb2.TrainRequest.FromString,
                    response_serializer=stacking__training__pb2.TrainReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'stacking.Trainer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Trainer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Train(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stacking.Trainer/Train',
            stacking__training__pb2.TrainRequest.SerializeToString,
            stacking__training__pb2.TrainReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class ReducerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Reduce = channel.unary_unary(
                '/stacking.Reducer/Reduce',
                request_serializer=stacking__training__pb2.ReduceRequest.SerializeToString,
                response_deserializer=stacking__training__pb2.ReduceReply.FromString,
                )


class ReducerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Reduce(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReducerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Reduce': grpc.unary_unary_rpc_method_handler(
                    servicer.Reduce,
                    request_deserializer=stacking__training__pb2.ReduceRequest.FromString,
                    response_serializer=stacking__training__pb2.ReduceReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'stacking.Reducer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Reducer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Reduce(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stacking.Reducer/Reduce',
            stacking__training__pb2.ReduceRequest.SerializeToString,
            stacking__training__pb2.ReduceReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class MetaTrainerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MetaTrain = channel.unary_unary(
                '/stacking.MetaTrainer/MetaTrain',
                request_serializer=stacking__training__pb2.MetaTrainRequest.SerializeToString,
                response_deserializer=stacking__training__pb2.MetaTrainReply.FromString,
                )


class MetaTrainerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MetaTrain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MetaTrainerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MetaTrain': grpc.unary_unary_rpc_method_handler(
                    servicer.MetaTrain,
                    request_deserializer=stacking__training__pb2.MetaTrainRequest.FromString,
                    response_serializer=stacking__training__pb2.MetaTrainReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'stacking.MetaTrainer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MetaTrainer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MetaTrain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stacking.MetaTrainer/MetaTrain',
            stacking__training__pb2.MetaTrainRequest.SerializeToString,
            stacking__training__pb2.MetaTrainReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
