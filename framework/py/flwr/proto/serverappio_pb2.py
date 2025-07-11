# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flwr/proto/serverappio.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import heartbeat_pb2 as flwr_dot_proto_dot_heartbeat__pb2
from flwr.proto import log_pb2 as flwr_dot_proto_dot_log__pb2
from flwr.proto import node_pb2 as flwr_dot_proto_dot_node__pb2
from flwr.proto import message_pb2 as flwr_dot_proto_dot_message__pb2
from flwr.proto import run_pb2 as flwr_dot_proto_dot_run__pb2
from flwr.proto import fab_pb2 as flwr_dot_proto_dot_fab__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x66lwr/proto/serverappio.proto\x12\nflwr.proto\x1a\x1a\x66lwr/proto/heartbeat.proto\x1a\x14\x66lwr/proto/log.proto\x1a\x15\x66lwr/proto/node.proto\x1a\x18\x66lwr/proto/message.proto\x1a\x14\x66lwr/proto/run.proto\x1a\x14\x66lwr/proto/fab.proto\"!\n\x0fGetNodesRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\"3\n\x10GetNodesResponse\x12\x1f\n\x05nodes\x18\x01 \x03(\x0b\x32\x10.flwr.proto.Node\"\x8a\x01\n\x16PushInsMessagesRequest\x12*\n\rmessages_list\x18\x01 \x03(\x0b\x32\x13.flwr.proto.Message\x12\x0e\n\x06run_id\x18\x02 \x01(\x04\x12\x34\n\x14message_object_trees\x18\x03 \x03(\x0b\x32\x16.flwr.proto.ObjectTree\"\xcc\x01\n\x17PushInsMessagesResponse\x12\x13\n\x0bmessage_ids\x18\x01 \x03(\t\x12O\n\x0fobjects_to_push\x18\x02 \x03(\x0b\x32\x36.flwr.proto.PushInsMessagesResponse.ObjectsToPushEntry\x1aK\n\x12ObjectsToPushEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.flwr.proto.ObjectIDs:\x02\x38\x01\"=\n\x16PullResMessagesRequest\x12\x13\n\x0bmessage_ids\x18\x01 \x03(\t\x12\x0e\n\x06run_id\x18\x02 \x01(\x04\"\xe3\x01\n\x17PullResMessagesResponse\x12*\n\rmessages_list\x18\x01 \x03(\x0b\x32\x13.flwr.proto.Message\x12O\n\x0fobjects_to_pull\x18\x02 \x03(\x0b\x32\x36.flwr.proto.PullResMessagesResponse.ObjectsToPullEntry\x1aK\n\x12ObjectsToPullEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.flwr.proto.ObjectIDs:\x02\x38\x01\"\x1c\n\x1aPullServerAppInputsRequest\"\x7f\n\x1bPullServerAppInputsResponse\x12$\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x13.flwr.proto.Context\x12\x1c\n\x03run\x18\x02 \x01(\x0b\x32\x0f.flwr.proto.Run\x12\x1c\n\x03\x66\x61\x62\x18\x03 \x01(\x0b\x32\x0f.flwr.proto.Fab\"S\n\x1bPushServerAppOutputsRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\x12$\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x13.flwr.proto.Context\"\x1e\n\x1cPushServerAppOutputsResponse2\xd7\t\n\x0bServerAppIo\x12G\n\x08GetNodes\x12\x1b.flwr.proto.GetNodesRequest\x1a\x1c.flwr.proto.GetNodesResponse\"\x00\x12Y\n\x0cPushMessages\x12\".flwr.proto.PushInsMessagesRequest\x1a#.flwr.proto.PushInsMessagesResponse\"\x00\x12Y\n\x0cPullMessages\x12\".flwr.proto.PullResMessagesRequest\x1a#.flwr.proto.PullResMessagesResponse\"\x00\x12\x41\n\x06GetRun\x12\x19.flwr.proto.GetRunRequest\x1a\x1a.flwr.proto.GetRunResponse\"\x00\x12\x41\n\x06GetFab\x12\x19.flwr.proto.GetFabRequest\x1a\x1a.flwr.proto.GetFabResponse\"\x00\x12h\n\x13PullServerAppInputs\x12&.flwr.proto.PullServerAppInputsRequest\x1a\'.flwr.proto.PullServerAppInputsResponse\"\x00\x12k\n\x14PushServerAppOutputs\x12\'.flwr.proto.PushServerAppOutputsRequest\x1a(.flwr.proto.PushServerAppOutputsResponse\"\x00\x12\\\n\x0fUpdateRunStatus\x12\".flwr.proto.UpdateRunStatusRequest\x1a#.flwr.proto.UpdateRunStatusResponse\"\x00\x12S\n\x0cGetRunStatus\x12\x1f.flwr.proto.GetRunStatusRequest\x1a .flwr.proto.GetRunStatusResponse\"\x00\x12G\n\x08PushLogs\x12\x1b.flwr.proto.PushLogsRequest\x1a\x1c.flwr.proto.PushLogsResponse\"\x00\x12_\n\x10SendAppHeartbeat\x12#.flwr.proto.SendAppHeartbeatRequest\x1a$.flwr.proto.SendAppHeartbeatResponse\"\x00\x12M\n\nPushObject\x12\x1d.flwr.proto.PushObjectRequest\x1a\x1e.flwr.proto.PushObjectResponse\"\x00\x12M\n\nPullObject\x12\x1d.flwr.proto.PullObjectRequest\x1a\x1e.flwr.proto.PullObjectResponse\"\x00\x12q\n\x16\x43onfirmMessageReceived\x12).flwr.proto.ConfirmMessageReceivedRequest\x1a*.flwr.proto.ConfirmMessageReceivedResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.serverappio_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PUSHINSMESSAGESRESPONSE_OBJECTSTOPUSHENTRY']._options = None
  _globals['_PUSHINSMESSAGESRESPONSE_OBJECTSTOPUSHENTRY']._serialized_options = b'8\001'
  _globals['_PULLRESMESSAGESRESPONSE_OBJECTSTOPULLENTRY']._options = None
  _globals['_PULLRESMESSAGESRESPONSE_OBJECTSTOPULLENTRY']._serialized_options = b'8\001'
  _globals['_GETNODESREQUEST']._serialized_start=187
  _globals['_GETNODESREQUEST']._serialized_end=220
  _globals['_GETNODESRESPONSE']._serialized_start=222
  _globals['_GETNODESRESPONSE']._serialized_end=273
  _globals['_PUSHINSMESSAGESREQUEST']._serialized_start=276
  _globals['_PUSHINSMESSAGESREQUEST']._serialized_end=414
  _globals['_PUSHINSMESSAGESRESPONSE']._serialized_start=417
  _globals['_PUSHINSMESSAGESRESPONSE']._serialized_end=621
  _globals['_PUSHINSMESSAGESRESPONSE_OBJECTSTOPUSHENTRY']._serialized_start=546
  _globals['_PUSHINSMESSAGESRESPONSE_OBJECTSTOPUSHENTRY']._serialized_end=621
  _globals['_PULLRESMESSAGESREQUEST']._serialized_start=623
  _globals['_PULLRESMESSAGESREQUEST']._serialized_end=684
  _globals['_PULLRESMESSAGESRESPONSE']._serialized_start=687
  _globals['_PULLRESMESSAGESRESPONSE']._serialized_end=914
  _globals['_PULLRESMESSAGESRESPONSE_OBJECTSTOPULLENTRY']._serialized_start=839
  _globals['_PULLRESMESSAGESRESPONSE_OBJECTSTOPULLENTRY']._serialized_end=914
  _globals['_PULLSERVERAPPINPUTSREQUEST']._serialized_start=916
  _globals['_PULLSERVERAPPINPUTSREQUEST']._serialized_end=944
  _globals['_PULLSERVERAPPINPUTSRESPONSE']._serialized_start=946
  _globals['_PULLSERVERAPPINPUTSRESPONSE']._serialized_end=1073
  _globals['_PUSHSERVERAPPOUTPUTSREQUEST']._serialized_start=1075
  _globals['_PUSHSERVERAPPOUTPUTSREQUEST']._serialized_end=1158
  _globals['_PUSHSERVERAPPOUTPUTSRESPONSE']._serialized_start=1160
  _globals['_PUSHSERVERAPPOUTPUTSRESPONSE']._serialized_end=1190
  _globals['_SERVERAPPIO']._serialized_start=1193
  _globals['_SERVERAPPIO']._serialized_end=2432
# @@protoc_insertion_point(module_scope)
