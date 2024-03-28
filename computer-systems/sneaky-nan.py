import struct

def conceal(n):
  # translate value to bits
  bs = n.encode('utf8')
  l = len(bs)
  if l > 6:
    raise ValueError()
  # transform the bits in some way, so that the value is nan
  first = b'\x7f'
  second = (0xf8 ^ l).to_bytes(1, 'big')
  padding = b'\x00' * (6 - l)
  payload = bs
  result = first + second + padding + payload
  return struct.unpack('>d', result)[0]

def extract(n):
  # get the bytes value
  bs = struct.pack('>d', n)
  # get the length (last 3 bits of the 2nd byte)
  length = bs[1] & 0x07
  print(length)
  return bs[-length:].decode('utf8')
  # pull that many bytes starting at the end
  # translate those bytes to utf8

x = conceal('hello')
print(x)
x = extract(x)
print(x)

"""
-1 ^ first bit * 2 ^ (next 8 bits - 127) * (1 + sum of each bit * 2 ^ -1 ... aka 2^-1 (1/2), 2^-2 (1/4), etc.)
"""

