import sys

def truncate_file(file):
    with open(file, 'rb') as f:
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            sys.stdout.buffer.write(truncate_string(line[1:-1], line[0]) + b'\n')

def truncate_string(s, n):
    if len(s) <= n:
        return s
    while n > 0 and (s[n] & 0xc0) == 0x80:
        n -= 1
    return s[:n]