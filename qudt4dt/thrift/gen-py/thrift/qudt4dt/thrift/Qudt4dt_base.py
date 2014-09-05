#
# Autogenerated by Thrift Compiler (1.0.0-dev)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def query(self, url):
    """
    Parameters:
     - url
    """
    pass

  def quantity_convert(self, src, dst_url):
    """
    Parameters:
     - src
     - dst_url
    """
    pass

  def list_domain_unitset(self, input):
    """
    Parameters:
     - input
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def query(self, url):
    """
    Parameters:
     - url
    """
    self.send_query(url)
    return self.recv_query()

  def send_query(self, url):
    self._oprot.writeMessageBegin('query', TMessageType.CALL, self._seqid)
    args = query_args()
    args.url = url
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_query(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = query_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.err is not None:
      raise result.err
    raise TApplicationException(TApplicationException.MISSING_RESULT, "query failed: unknown result");

  def quantity_convert(self, src, dst_url):
    """
    Parameters:
     - src
     - dst_url
    """
    self.send_quantity_convert(src, dst_url)
    return self.recv_quantity_convert()

  def send_quantity_convert(self, src, dst_url):
    self._oprot.writeMessageBegin('quantity_convert', TMessageType.CALL, self._seqid)
    args = quantity_convert_args()
    args.src = src
    args.dst_url = dst_url
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_quantity_convert(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = quantity_convert_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.err is not None:
      raise result.err
    raise TApplicationException(TApplicationException.MISSING_RESULT, "quantity_convert failed: unknown result");

  def list_domain_unitset(self, input):
    """
    Parameters:
     - input
    """
    self.send_list_domain_unitset(input)
    return self.recv_list_domain_unitset()

  def send_list_domain_unitset(self, input):
    self._oprot.writeMessageBegin('list_domain_unitset', TMessageType.CALL, self._seqid)
    args = list_domain_unitset_args()
    args.input = input
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_list_domain_unitset(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = list_domain_unitset_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.err is not None:
      raise result.err
    raise TApplicationException(TApplicationException.MISSING_RESULT, "list_domain_unitset failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["query"] = Processor.process_query
    self._processMap["quantity_convert"] = Processor.process_quantity_convert
    self._processMap["list_domain_unitset"] = Processor.process_list_domain_unitset

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_query(self, seqid, iprot, oprot):
    args = query_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = query_result()
    try:
      result.success = self._handler.query(args.url)
    except InvalidOperation, err:
      result.err = err
    oprot.writeMessageBegin("query", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_quantity_convert(self, seqid, iprot, oprot):
    args = quantity_convert_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = quantity_convert_result()
    try:
      result.success = self._handler.quantity_convert(args.src, args.dst_url)
    except InvalidOperation, err:
      result.err = err
    oprot.writeMessageBegin("quantity_convert", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_list_domain_unitset(self, seqid, iprot, oprot):
    args = list_domain_unitset_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = list_domain_unitset_result()
    try:
      result.success = self._handler.list_domain_unitset(args.input)
    except InvalidOperation, err:
      result.err = err
    oprot.writeMessageBegin("list_domain_unitset", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class query_args:
  """
  Attributes:
   - url
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'url', None, None, ), # 1
  )

  def __init__(self, url=None,):
    self.url = url

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.url = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('query_args')
    if self.url is not None:
      oprot.writeFieldBegin('url', TType.STRING, 1)
      oprot.writeString(self.url)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class query_result:
  """
  Attributes:
   - success
   - err
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Unit, Unit.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'err', (InvalidOperation, InvalidOperation.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, err=None,):
    self.success = success
    self.err = err

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = Unit()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.err = InvalidOperation()
          self.err.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('query_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.err is not None:
      oprot.writeFieldBegin('err', TType.STRUCT, 1)
      self.err.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class quantity_convert_args:
  """
  Attributes:
   - src
   - dst_url
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'src', (Quantity, Quantity.thrift_spec), None, ), # 1
    (2, TType.STRING, 'dst_url', None, None, ), # 2
  )

  def __init__(self, src=None, dst_url=None,):
    self.src = src
    self.dst_url = dst_url

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.src = Quantity()
          self.src.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.dst_url = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('quantity_convert_args')
    if self.src is not None:
      oprot.writeFieldBegin('src', TType.STRUCT, 1)
      self.src.write(oprot)
      oprot.writeFieldEnd()
    if self.dst_url is not None:
      oprot.writeFieldBegin('dst_url', TType.STRING, 2)
      oprot.writeString(self.dst_url)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class quantity_convert_result:
  """
  Attributes:
   - success
   - err
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Quantity, Quantity.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'err', (InvalidOperation, InvalidOperation.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, err=None,):
    self.success = success
    self.err = err

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = Quantity()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.err = InvalidOperation()
          self.err.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('quantity_convert_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.err is not None:
      oprot.writeFieldBegin('err', TType.STRUCT, 1)
      self.err.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class list_domain_unitset_args:
  """
  Attributes:
   - input
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'input', (Quantity, Quantity.thrift_spec), None, ), # 1
  )

  def __init__(self, input=None,):
    self.input = input

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.input = Quantity()
          self.input.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('list_domain_unitset_args')
    if self.input is not None:
      oprot.writeFieldBegin('input', TType.STRUCT, 1)
      self.input.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class list_domain_unitset_result:
  """
  Attributes:
   - success
   - err
  """

  thrift_spec = (
    (0, TType.MAP, 'success', (TType.STRING,None,TType.STRUCT,(Quantity, Quantity.thrift_spec)), None, ), # 0
    (1, TType.STRUCT, 'err', (InvalidOperation, InvalidOperation.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, err=None,):
    self.success = success
    self.err = err

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.MAP:
          self.success = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
          for _i4 in xrange(_size0):
            _key5 = iprot.readString();
            _val6 = Quantity()
            _val6.read(iprot)
            self.success[_key5] = _val6
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.err = InvalidOperation()
          self.err.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('list_domain_unitset_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.MAP, 0)
      oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.success))
      for kiter7,viter8 in self.success.items():
        oprot.writeString(kiter7)
        viter8.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.err is not None:
      oprot.writeFieldBegin('err', TType.STRUCT, 1)
      self.err.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)