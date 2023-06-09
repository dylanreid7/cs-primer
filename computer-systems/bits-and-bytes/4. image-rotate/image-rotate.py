
with open('teapot.bmp', 'rb') as f:
    data = f.read()

print(data[:2].hex())

# output a bmp file with 420 x 420, but all in black!
# black rgb is 000000 btw

# starting at 138, it should do 420 x 420 x 3 places, all 0's

blackBitmap = data
offset = 138
end = offset + 420 * 420 * 3

for x in range(offset, end):
    blackBitmap[x] = bytes(0x00)

with open('black.bmp', 'wb') as f:
    f.write(blackBitmap)
