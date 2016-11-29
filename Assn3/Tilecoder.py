numTilings = 8


def tilecode(in1, in2, tileIndices):
    for i in range(len(tileIndices)):
        topRightOfZerothTile = 0.6 + (((-0.6) / 8) * i)
        x = in1 // 0.6
        y = in2 // 0.6
        modx = round(in1 % 0.6, 6)
        mody = round(in2 % 0.6, 6)
        if(modx >= topRightOfZerothTile):
            x += 1
        if(mody >= topRightOfZerothTile):
            y += 1
        tileIndices[i] = linearize(x, y) + (121 * i)
    return tileIndices


def linearize(x, y):
    return int(x + (y * 11))


def printTileCoderIndices(in1, in2):
    tileIndices = [-1]*numTilings
    tilecode(in1, in2, tileIndices)
    print('Tile indices for input (', in1, ',', in2, ') are : ', tileIndices)


# printTileCoderIndices(0.1, 0.1)
# printTileCoderIndices(4.0, 2.0)
# printTileCoderIndices(5.99, 5.99)
# printTileCoderIndices(4.0, 2.1)
