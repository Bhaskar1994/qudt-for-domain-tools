//
// Autogenerated by Thrift Compiler (1.0.0-dev)
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//


//HELPER FUNCTIONS AND STRUCTURES

qudt4dt.thrift.Qudt4dt_base_query_args = function(args) {
  this.url = null;
  if (args) {
    if (args.url !== undefined) {
      this.url = args.url;
    }
  }
};
qudt4dt.thrift.Qudt4dt_base_query_args.prototype = {};
qudt4dt.thrift.Qudt4dt_base_query_args.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.STRING) {
        this.url = input.readString().value;
      } else {
        input.skip(ftype);
      }
      break;
      case 0:
        input.skip(ftype);
        break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

qudt4dt.thrift.Qudt4dt_base_query_args.prototype.write = function(output) {
  output.writeStructBegin('Qudt4dt_base_query_args');
  if (this.url !== null && this.url !== undefined) {
    output.writeFieldBegin('url', Thrift.Type.STRING, 1);
    output.writeString(this.url);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

qudt4dt.thrift.Qudt4dt_base_query_result = function(args) {
  this.success = null;
  this.err = null;
  if (args instanceof qudt4dt.thrift.InvalidOperation) {
    this.err = args;
    return;
  }
  if (args) {
    if (args.success !== undefined) {
      this.success = args.success;
    }
    if (args.err !== undefined) {
      this.err = args.err;
    }
  }
};
qudt4dt.thrift.Qudt4dt_base_query_result.prototype = {};
qudt4dt.thrift.Qudt4dt_base_query_result.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 0:
      if (ftype == Thrift.Type.STRUCT) {
        this.success = new qudt4dt.thrift.Unit();
        this.success.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.err = new qudt4dt.thrift.InvalidOperation();
        this.err.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

qudt4dt.thrift.Qudt4dt_base_query_result.prototype.write = function(output) {
  output.writeStructBegin('Qudt4dt_base_query_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.STRUCT, 0);
    this.success.write(output);
    output.writeFieldEnd();
  }
  if (this.err !== null && this.err !== undefined) {
    output.writeFieldBegin('err', Thrift.Type.STRUCT, 1);
    this.err.write(output);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

qudt4dt.thrift.Qudt4dt_base_quantity_convert_args = function(args) {
  this.src = null;
  this.dst_url = null;
  if (args) {
    if (args.src !== undefined) {
      this.src = args.src;
    }
    if (args.dst_url !== undefined) {
      this.dst_url = args.dst_url;
    }
  }
};
qudt4dt.thrift.Qudt4dt_base_quantity_convert_args.prototype = {};
qudt4dt.thrift.Qudt4dt_base_quantity_convert_args.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.src = new qudt4dt.thrift.Quantity();
        this.src.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 2:
      if (ftype == Thrift.Type.STRING) {
        this.dst_url = input.readString().value;
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

qudt4dt.thrift.Qudt4dt_base_quantity_convert_args.prototype.write = function(output) {
  output.writeStructBegin('Qudt4dt_base_quantity_convert_args');
  if (this.src !== null && this.src !== undefined) {
    output.writeFieldBegin('src', Thrift.Type.STRUCT, 1);
    this.src.write(output);
    output.writeFieldEnd();
  }
  if (this.dst_url !== null && this.dst_url !== undefined) {
    output.writeFieldBegin('dst_url', Thrift.Type.STRING, 2);
    output.writeString(this.dst_url);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

qudt4dt.thrift.Qudt4dt_base_quantity_convert_result = function(args) {
  this.success = null;
  this.err = null;
  if (args instanceof qudt4dt.thrift.InvalidOperation) {
    this.err = args;
    return;
  }
  if (args) {
    if (args.success !== undefined) {
      this.success = args.success;
    }
    if (args.err !== undefined) {
      this.err = args.err;
    }
  }
};
qudt4dt.thrift.Qudt4dt_base_quantity_convert_result.prototype = {};
qudt4dt.thrift.Qudt4dt_base_quantity_convert_result.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 0:
      if (ftype == Thrift.Type.STRUCT) {
        this.success = new qudt4dt.thrift.Quantity();
        this.success.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.err = new qudt4dt.thrift.InvalidOperation();
        this.err.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

qudt4dt.thrift.Qudt4dt_base_quantity_convert_result.prototype.write = function(output) {
  output.writeStructBegin('Qudt4dt_base_quantity_convert_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.STRUCT, 0);
    this.success.write(output);
    output.writeFieldEnd();
  }
  if (this.err !== null && this.err !== undefined) {
    output.writeFieldBegin('err', Thrift.Type.STRUCT, 1);
    this.err.write(output);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

qudt4dt.thrift.Qudt4dt_base_list_domain_unitset_args = function(args) {
  this.input = null;
  if (args) {
    if (args.input !== undefined) {
      this.input = args.input;
    }
  }
};
qudt4dt.thrift.Qudt4dt_base_list_domain_unitset_args.prototype = {};
qudt4dt.thrift.Qudt4dt_base_list_domain_unitset_args.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.input = new qudt4dt.thrift.Quantity();
        this.input.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      case 0:
        input.skip(ftype);
        break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

qudt4dt.thrift.Qudt4dt_base_list_domain_unitset_args.prototype.write = function(output) {
  output.writeStructBegin('Qudt4dt_base_list_domain_unitset_args');
  if (this.input !== null && this.input !== undefined) {
    output.writeFieldBegin('input', Thrift.Type.STRUCT, 1);
    this.input.write(output);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

qudt4dt.thrift.Qudt4dt_base_list_domain_unitset_result = function(args) {
  this.success = null;
  this.err = null;
  if (args instanceof qudt4dt.thrift.InvalidOperation) {
    this.err = args;
    return;
  }
  if (args) {
    if (args.success !== undefined) {
      this.success = args.success;
    }
    if (args.err !== undefined) {
      this.err = args.err;
    }
  }
};
qudt4dt.thrift.Qudt4dt_base_list_domain_unitset_result.prototype = {};
qudt4dt.thrift.Qudt4dt_base_list_domain_unitset_result.prototype.read = function(input) {
  input.readStructBegin();
  while (true)
  {
    var ret = input.readFieldBegin();
    var fname = ret.fname;
    var ftype = ret.ftype;
    var fid = ret.fid;
    if (ftype == Thrift.Type.STOP) {
      break;
    }
    switch (fid)
    {
      case 0:
      if (ftype == Thrift.Type.MAP) {
        var _size0 = 0;
        var _rtmp34;
        this.success = {};
        var _ktype1 = 0;
        var _vtype2 = 0;
        _rtmp34 = input.readMapBegin();
        _ktype1 = _rtmp34.ktype;
        _vtype2 = _rtmp34.vtype;
        _size0 = _rtmp34.size;
        for (var _i5 = 0; _i5 < _size0; ++_i5)
        {
          if (_i5 > 0 ) {
            if (input.rstack.length > input.rpos[input.rpos.length -1] + 1) {
              input.rstack.pop();
            }
          }
          var key6 = null;
          var val7 = null;
          key6 = input.readString().value;
          val7 = new qudt4dt.thrift.Quantity();
          val7.read(input);
          this.success[key6] = val7;
        }
        input.readMapEnd();
      } else {
        input.skip(ftype);
      }
      break;
      case 1:
      if (ftype == Thrift.Type.STRUCT) {
        this.err = new qudt4dt.thrift.InvalidOperation();
        this.err.read(input);
      } else {
        input.skip(ftype);
      }
      break;
      default:
        input.skip(ftype);
    }
    input.readFieldEnd();
  }
  input.readStructEnd();
  return;
};

qudt4dt.thrift.Qudt4dt_base_list_domain_unitset_result.prototype.write = function(output) {
  output.writeStructBegin('Qudt4dt_base_list_domain_unitset_result');
  if (this.success !== null && this.success !== undefined) {
    output.writeFieldBegin('success', Thrift.Type.MAP, 0);
    output.writeMapBegin(Thrift.Type.STRING, Thrift.Type.STRUCT, Thrift.objectLength(this.success));
    for (var kiter8 in this.success)
    {
      if (this.success.hasOwnProperty(kiter8))
      {
        var viter9 = this.success[kiter8];
        output.writeString(kiter8);
        viter9.write(output);
      }
    }
    output.writeMapEnd();
    output.writeFieldEnd();
  }
  if (this.err !== null && this.err !== undefined) {
    output.writeFieldBegin('err', Thrift.Type.STRUCT, 1);
    this.err.write(output);
    output.writeFieldEnd();
  }
  output.writeFieldStop();
  output.writeStructEnd();
  return;
};

qudt4dt.thrift.Qudt4dt_baseClient = function(input, output) {
    this.input = input;
    this.output = (!output) ? input : output;
    this.seqid = 0;
};
qudt4dt.thrift.Qudt4dt_baseClient.prototype = {};
qudt4dt.thrift.Qudt4dt_baseClient.prototype.query = function(url, callback) {
  this.send_query(url, callback); 
  if (!callback) {
    return this.recv_query();
  }
};

qudt4dt.thrift.Qudt4dt_baseClient.prototype.send_query = function(url, callback) {
  this.output.writeMessageBegin('query', Thrift.MessageType.CALL, this.seqid);
  var args = new qudt4dt.thrift.Qudt4dt_base_query_args();
  args.url = url;
  args.write(this.output);
  this.output.writeMessageEnd();
  if (callback) {
    var self = this;
    this.output.getTransport().flush(true, function() {
      var result = null;
      try {
        result = self.recv_query();
      } catch (e) {
        result = e;
      }
      callback(result);
    });
  } else {
    return this.output.getTransport().flush();
  }
};

qudt4dt.thrift.Qudt4dt_baseClient.prototype.recv_query = function() {
  var ret = this.input.readMessageBegin();
  var fname = ret.fname;
  var mtype = ret.mtype;
  var rseqid = ret.rseqid;
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(this.input);
    this.input.readMessageEnd();
    throw x;
  }
  var result = new qudt4dt.thrift.Qudt4dt_base_query_result();
  result.read(this.input);
  this.input.readMessageEnd();

  if (null !== result.err) {
    throw result.err;
  }
  if (null !== result.success) {
    return result.success;
  }
  throw 'query failed: unknown result';
};
qudt4dt.thrift.Qudt4dt_baseClient.prototype.quantity_convert = function(src, dst_url, callback) {
  this.send_quantity_convert(src, dst_url, callback); 
  if (!callback) {
    return this.recv_quantity_convert();
  }
};

qudt4dt.thrift.Qudt4dt_baseClient.prototype.send_quantity_convert = function(src, dst_url, callback) {
  this.output.writeMessageBegin('quantity_convert', Thrift.MessageType.CALL, this.seqid);
  var args = new qudt4dt.thrift.Qudt4dt_base_quantity_convert_args();
  args.src = src;
  args.dst_url = dst_url;
  args.write(this.output);
  this.output.writeMessageEnd();
  if (callback) {
    var self = this;
    this.output.getTransport().flush(true, function() {
      var result = null;
      try {
        result = self.recv_quantity_convert();
      } catch (e) {
        result = e;
      }
      callback(result);
    });
  } else {
    return this.output.getTransport().flush();
  }
};

qudt4dt.thrift.Qudt4dt_baseClient.prototype.recv_quantity_convert = function() {
  var ret = this.input.readMessageBegin();
  var fname = ret.fname;
  var mtype = ret.mtype;
  var rseqid = ret.rseqid;
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(this.input);
    this.input.readMessageEnd();
    throw x;
  }
  var result = new qudt4dt.thrift.Qudt4dt_base_quantity_convert_result();
  result.read(this.input);
  this.input.readMessageEnd();

  if (null !== result.err) {
    throw result.err;
  }
  if (null !== result.success) {
    return result.success;
  }
  throw 'quantity_convert failed: unknown result';
};
qudt4dt.thrift.Qudt4dt_baseClient.prototype.list_domain_unitset = function(input, callback) {
  this.send_list_domain_unitset(input, callback); 
  if (!callback) {
    return this.recv_list_domain_unitset();
  }
};

qudt4dt.thrift.Qudt4dt_baseClient.prototype.send_list_domain_unitset = function(input, callback) {
  this.output.writeMessageBegin('list_domain_unitset', Thrift.MessageType.CALL, this.seqid);
  var args = new qudt4dt.thrift.Qudt4dt_base_list_domain_unitset_args();
  args.input = input;
  args.write(this.output);
  this.output.writeMessageEnd();
  if (callback) {
    var self = this;
    this.output.getTransport().flush(true, function() {
      var result = null;
      try {
        result = self.recv_list_domain_unitset();
      } catch (e) {
        result = e;
      }
      callback(result);
    });
  } else {
    return this.output.getTransport().flush();
  }
};

qudt4dt.thrift.Qudt4dt_baseClient.prototype.recv_list_domain_unitset = function() {
  var ret = this.input.readMessageBegin();
  var fname = ret.fname;
  var mtype = ret.mtype;
  var rseqid = ret.rseqid;
  if (mtype == Thrift.MessageType.EXCEPTION) {
    var x = new Thrift.TApplicationException();
    x.read(this.input);
    this.input.readMessageEnd();
    throw x;
  }
  var result = new qudt4dt.thrift.Qudt4dt_base_list_domain_unitset_result();
  result.read(this.input);
  this.input.readMessageEnd();

  if (null !== result.err) {
    throw result.err;
  }
  if (null !== result.success) {
    return result.success;
  }
  throw 'list_domain_unitset failed: unknown result';
};
