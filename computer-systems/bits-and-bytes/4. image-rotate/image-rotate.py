def le(bs):
    n = 0
    for i, b in enumerate(bs):
        n += b << (i * 8)
    return n


with open('teapot.bmp', 'rb') as f:
    data = f.read()

print(data[:2].hex())
offset = data[10]
print(offset)
print(data[offset:offset + 6])

offset, width, height = le(data[10:14]), le(data[18:22]), le(data[22:26])
print(offset, height, width)

# output a bmp file with 420 x 420, but all in black!
# black rgb is 000000 btw

# starting at 138, it should do 420 x 420 x 3 places, all 0's

# blackBitmap = stuff
offset = 138
end = offset + 420 * 420 * 3

# for x in range(offset, end):
    # print(x)
    # blackBitmap[x] = bytes(0x00)

# spixels = data[offset:]
pixels = []

# iterate through in expected order
# place the value from the pixel that needs to go in that spot
for ty in range(width):
    for tx in range(width):
        sx = width - ty - 1
        sy = tx
        n = offset + 3 * (sy * width * sx)
        pixels.append(data[n:n+3])


with open('black.bmp', 'wb') as f:
    f.write(data[:offset])
    f.write(b''.join(pixels))
