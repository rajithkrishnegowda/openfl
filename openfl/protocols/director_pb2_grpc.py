# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import director_pb2 as director__pb2


class FederationDirectorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AcknowledgeShard = channel.unary_unary(
                '/FederationDirector/AcknowledgeShard',
                request_serializer=director__pb2.ShardInfo.SerializeToString,
                response_deserializer=director__pb2.ShardAcknowledgement.FromString,
                )
        self.WaitExperiment = channel.stream_stream(
                '/FederationDirector/WaitExperiment',
                request_serializer=director__pb2.WaitExperimentRequest.SerializeToString,
                response_deserializer=director__pb2.WaitExperimentResponse.FromString,
                )
        self.GetExperimentData = channel.unary_stream(
                '/FederationDirector/GetExperimentData',
                request_serializer=director__pb2.GetExperimentDataRequest.SerializeToString,
                response_deserializer=director__pb2.ExperimentData.FromString,
                )
        self.EnvoyHealthCheck = channel.unary_unary(
                '/FederationDirector/EnvoyHealthCheck',
                request_serializer=director__pb2.EnvoyStatus.SerializeToString,
                response_deserializer=director__pb2.EnvoyHealthCheckResponse.FromString,
                )
        self.SetExperimentFailed = channel.unary_unary(
                '/FederationDirector/SetExperimentFailed',
                request_serializer=director__pb2.SetExperimentFailedRequest.SerializeToString,
                response_deserializer=director__pb2.SetExperimentFailedResponse.FromString,
                )
        self.GetExperimentDescription = channel.unary_unary(
                '/FederationDirector/GetExperimentDescription',
                request_serializer=director__pb2.GetExperimentDescriptionRequest.SerializeToString,
                response_deserializer=director__pb2.GetExperimentDescriptionResponse.FromString,
                )
        self.GetExperimentsList = channel.unary_unary(
                '/FederationDirector/GetExperimentsList',
                request_serializer=director__pb2.GetExperimentsListRequest.SerializeToString,
                response_deserializer=director__pb2.GetExperimentsListResponse.FromString,
                )
        self.SetNewExperiment = channel.stream_unary(
                '/FederationDirector/SetNewExperiment',
                request_serializer=director__pb2.ExperimentInfo.SerializeToString,
                response_deserializer=director__pb2.SetNewExperimentResponse.FromString,
                )
        self.GetDatasetInfo = channel.unary_unary(
                '/FederationDirector/GetDatasetInfo',
                request_serializer=director__pb2.GetDatasetInfoRequest.SerializeToString,
                response_deserializer=director__pb2.ShardInfo.FromString,
                )
        self.GetTrainedModel = channel.unary_unary(
                '/FederationDirector/GetTrainedModel',
                request_serializer=director__pb2.GetTrainedModelRequest.SerializeToString,
                response_deserializer=director__pb2.TrainedModelResponse.FromString,
                )
        self.StreamMetrics = channel.unary_stream(
                '/FederationDirector/StreamMetrics',
                request_serializer=director__pb2.StreamMetricsRequest.SerializeToString,
                response_deserializer=director__pb2.StreamMetricsResponse.FromString,
                )
        self.RemoveExperimentData = channel.unary_unary(
                '/FederationDirector/RemoveExperimentData',
                request_serializer=director__pb2.RemoveExperimentRequest.SerializeToString,
                response_deserializer=director__pb2.RemoveExperimentResponse.FromString,
                )
        self.GetEnvoys = channel.unary_unary(
                '/FederationDirector/GetEnvoys',
                request_serializer=director__pb2.GetEnvoysRequest.SerializeToString,
                response_deserializer=director__pb2.GetEnvoysResponse.FromString,
                )


class FederationDirectorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AcknowledgeShard(self, request, context):
        """Envoy RPCs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WaitExperiment(self, request_iterator, context):
        """Shard owner could also provide some public data for tests
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExperimentData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnvoyHealthCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetExperimentFailed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExperimentDescription(self, request, context):
        """Experiments RPCs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExperimentsList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetNewExperiment(self, request_iterator, context):
        """API RPCs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDatasetInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrainedModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamMetrics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveExperimentData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEnvoys(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FederationDirectorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AcknowledgeShard': grpc.unary_unary_rpc_method_handler(
                    servicer.AcknowledgeShard,
                    request_deserializer=director__pb2.ShardInfo.FromString,
                    response_serializer=director__pb2.ShardAcknowledgement.SerializeToString,
            ),
            'WaitExperiment': grpc.stream_stream_rpc_method_handler(
                    servicer.WaitExperiment,
                    request_deserializer=director__pb2.WaitExperimentRequest.FromString,
                    response_serializer=director__pb2.WaitExperimentResponse.SerializeToString,
            ),
            'GetExperimentData': grpc.unary_stream_rpc_method_handler(
                    servicer.GetExperimentData,
                    request_deserializer=director__pb2.GetExperimentDataRequest.FromString,
                    response_serializer=director__pb2.ExperimentData.SerializeToString,
            ),
            'EnvoyHealthCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.EnvoyHealthCheck,
                    request_deserializer=director__pb2.EnvoyStatus.FromString,
                    response_serializer=director__pb2.EnvoyHealthCheckResponse.SerializeToString,
            ),
            'SetExperimentFailed': grpc.unary_unary_rpc_method_handler(
                    servicer.SetExperimentFailed,
                    request_deserializer=director__pb2.SetExperimentFailedRequest.FromString,
                    response_serializer=director__pb2.SetExperimentFailedResponse.SerializeToString,
            ),
            'GetExperimentDescription': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExperimentDescription,
                    request_deserializer=director__pb2.GetExperimentDescriptionRequest.FromString,
                    response_serializer=director__pb2.GetExperimentDescriptionResponse.SerializeToString,
            ),
            'GetExperimentsList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExperimentsList,
                    request_deserializer=director__pb2.GetExperimentsListRequest.FromString,
                    response_serializer=director__pb2.GetExperimentsListResponse.SerializeToString,
            ),
            'SetNewExperiment': grpc.stream_unary_rpc_method_handler(
                    servicer.SetNewExperiment,
                    request_deserializer=director__pb2.ExperimentInfo.FromString,
                    response_serializer=director__pb2.SetNewExperimentResponse.SerializeToString,
            ),
            'GetDatasetInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDatasetInfo,
                    request_deserializer=director__pb2.GetDatasetInfoRequest.FromString,
                    response_serializer=director__pb2.ShardInfo.SerializeToString,
            ),
            'GetTrainedModel': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrainedModel,
                    request_deserializer=director__pb2.GetTrainedModelRequest.FromString,
                    response_serializer=director__pb2.TrainedModelResponse.SerializeToString,
            ),
            'StreamMetrics': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamMetrics,
                    request_deserializer=director__pb2.StreamMetricsRequest.FromString,
                    response_serializer=director__pb2.StreamMetricsResponse.SerializeToString,
            ),
            'RemoveExperimentData': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveExperimentData,
                    request_deserializer=director__pb2.RemoveExperimentRequest.FromString,
                    response_serializer=director__pb2.RemoveExperimentResponse.SerializeToString,
            ),
            'GetEnvoys': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEnvoys,
                    request_deserializer=director__pb2.GetEnvoysRequest.FromString,
                    response_serializer=director__pb2.GetEnvoysResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FederationDirector', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FederationDirector(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AcknowledgeShard(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FederationDirector/AcknowledgeShard',
            director__pb2.ShardInfo.SerializeToString,
            director__pb2.ShardAcknowledgement.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WaitExperiment(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/FederationDirector/WaitExperiment',
            director__pb2.WaitExperimentRequest.SerializeToString,
            director__pb2.WaitExperimentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExperimentData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/FederationDirector/GetExperimentData',
            director__pb2.GetExperimentDataRequest.SerializeToString,
            director__pb2.ExperimentData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnvoyHealthCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FederationDirector/EnvoyHealthCheck',
            director__pb2.EnvoyStatus.SerializeToString,
            director__pb2.EnvoyHealthCheckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetExperimentFailed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FederationDirector/SetExperimentFailed',
            director__pb2.SetExperimentFailedRequest.SerializeToString,
            director__pb2.SetExperimentFailedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExperimentDescription(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FederationDirector/GetExperimentDescription',
            director__pb2.GetExperimentDescriptionRequest.SerializeToString,
            director__pb2.GetExperimentDescriptionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExperimentsList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FederationDirector/GetExperimentsList',
            director__pb2.GetExperimentsListRequest.SerializeToString,
            director__pb2.GetExperimentsListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetNewExperiment(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/FederationDirector/SetNewExperiment',
            director__pb2.ExperimentInfo.SerializeToString,
            director__pb2.SetNewExperimentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDatasetInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FederationDirector/GetDatasetInfo',
            director__pb2.GetDatasetInfoRequest.SerializeToString,
            director__pb2.ShardInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTrainedModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FederationDirector/GetTrainedModel',
            director__pb2.GetTrainedModelRequest.SerializeToString,
            director__pb2.TrainedModelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/FederationDirector/StreamMetrics',
            director__pb2.StreamMetricsRequest.SerializeToString,
            director__pb2.StreamMetricsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveExperimentData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FederationDirector/RemoveExperimentData',
            director__pb2.RemoveExperimentRequest.SerializeToString,
            director__pb2.RemoveExperimentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEnvoys(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FederationDirector/GetEnvoys',
            director__pb2.GetEnvoysRequest.SerializeToString,
            director__pb2.GetEnvoysResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
