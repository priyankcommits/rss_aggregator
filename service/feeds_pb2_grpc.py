# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import feeds_pb2 as feeds__pb2


class FeedsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAllFeeds = channel.unary_unary(
        '/core.feeds.Feeds/GetAllFeeds',
        request_serializer=feeds__pb2.Query.SerializeToString,
        response_deserializer=feeds__pb2.FeedList.FromString,
        )
    self.GetCustomFeeds = channel.unary_unary(
        '/core.feeds.Feeds/GetCustomFeeds',
        request_serializer=feeds__pb2.Query.SerializeToString,
        response_deserializer=feeds__pb2.FeedList.FromString,
        )
    self.GetFeed = channel.unary_unary(
        '/core.feeds.Feeds/GetFeed',
        request_serializer=feeds__pb2.Feed.SerializeToString,
        response_deserializer=feeds__pb2.Feed.FromString,
        )
    self.CreateFeedComment = channel.unary_unary(
        '/core.feeds.Feeds/CreateFeedComment',
        request_serializer=feeds__pb2.FeedComment.SerializeToString,
        response_deserializer=feeds__pb2.OperationStatus.FromString,
        )
    self.CreateFeedBookmark = channel.unary_unary(
        '/core.feeds.Feeds/CreateFeedBookmark',
        request_serializer=feeds__pb2.FeedBookmark.SerializeToString,
        response_deserializer=feeds__pb2.OperationStatus.FromString,
        )
    self.CreateFeedSource = channel.unary_unary(
        '/core.feeds.Feeds/CreateFeedSource',
        request_serializer=feeds__pb2.FeedSource.SerializeToString,
        response_deserializer=feeds__pb2.OperationStatus.FromString,
        )
    self.UpdateFeedSource = channel.unary_unary(
        '/core.feeds.Feeds/UpdateFeedSource',
        request_serializer=feeds__pb2.FeedSource.SerializeToString,
        response_deserializer=feeds__pb2.OperationStatus.FromString,
        )
    self.GetAllFeedSources = channel.unary_unary(
        '/core.feeds.Feeds/GetAllFeedSources',
        request_serializer=feeds__pb2.EmptyRequest.SerializeToString,
        response_deserializer=feeds__pb2.FeedSourceList.FromString,
        )


class FeedsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetAllFeeds(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCustomFeeds(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFeed(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateFeedComment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateFeedBookmark(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateFeedSource(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateFeedSource(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllFeedSources(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FeedsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAllFeeds': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllFeeds,
          request_deserializer=feeds__pb2.Query.FromString,
          response_serializer=feeds__pb2.FeedList.SerializeToString,
      ),
      'GetCustomFeeds': grpc.unary_unary_rpc_method_handler(
          servicer.GetCustomFeeds,
          request_deserializer=feeds__pb2.Query.FromString,
          response_serializer=feeds__pb2.FeedList.SerializeToString,
      ),
      'GetFeed': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeed,
          request_deserializer=feeds__pb2.Feed.FromString,
          response_serializer=feeds__pb2.Feed.SerializeToString,
      ),
      'CreateFeedComment': grpc.unary_unary_rpc_method_handler(
          servicer.CreateFeedComment,
          request_deserializer=feeds__pb2.FeedComment.FromString,
          response_serializer=feeds__pb2.OperationStatus.SerializeToString,
      ),
      'CreateFeedBookmark': grpc.unary_unary_rpc_method_handler(
          servicer.CreateFeedBookmark,
          request_deserializer=feeds__pb2.FeedBookmark.FromString,
          response_serializer=feeds__pb2.OperationStatus.SerializeToString,
      ),
      'CreateFeedSource': grpc.unary_unary_rpc_method_handler(
          servicer.CreateFeedSource,
          request_deserializer=feeds__pb2.FeedSource.FromString,
          response_serializer=feeds__pb2.OperationStatus.SerializeToString,
      ),
      'UpdateFeedSource': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateFeedSource,
          request_deserializer=feeds__pb2.FeedSource.FromString,
          response_serializer=feeds__pb2.OperationStatus.SerializeToString,
      ),
      'GetAllFeedSources': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllFeedSources,
          request_deserializer=feeds__pb2.EmptyRequest.FromString,
          response_serializer=feeds__pb2.FeedSourceList.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'core.feeds.Feeds', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
