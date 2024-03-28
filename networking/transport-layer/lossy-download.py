import sys
import struct

f = open('lossy.pcap', 'rb')
magic, _, _, _, _, snl, llh = struct.unpack('IHHIIII', f.read(24))

parts = {}

while True:
    bs = f.read(16)
    if not bs:
        break
    _, _, n, untruncated_length = struct.unpack('IIII', bs)
    packet = f.read(n)
    
    ihl = packet[14] & 0b1111
    segment = packet[14+ihl*4:]
    src_port, dst_port, seq_num, _, flags = struct.unpack('!HHIIH', segment[:14])
    syn = flags & 0b10
    offset = flags >> 12
    if src_port == 80 and not syn:
        parts[seq_num] = segment[offset*4:]
    # with open('image.jpeg', 'wb') as new_file:
    #     new_file.write(segment)
    # assert packet[12:14] == b'\x08\x00'
    # protocol = packet[23]
    # assert protocol == 6
    # assert n == untruncated_length
        

res = b''.join(v for k, v in sorted(parts.items())).split(b'\r\n\r\n', 1)[1]
with open('image.jpeg', 'wb') as new_file:
    new_file.write(res)