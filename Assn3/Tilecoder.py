numTilings = 4
minBound = -0.6
maxBound = -0.4
widthOfTilingInTiles = 9
widthOfTiling = (abs(maxBound - minBound)) / (widthOfTilingInTiles - 1)


def tilecode(in1, in2, tileIndices):
    for i in range(len(tileIndices)):
        topRightOfZerothTile = widthOfTiling + (((-widthOfTiling) / numTilings) * i)
        x = in1 // widthOfTiling
        y = in2 // widthOfTiling
        modx = round(in1 % widthOfTiling, 6)
        mody = round(in2 % widthOfTiling, 6)
        if(modx >= topRightOfZerothTile):
            x += 1
        if(mody >= topRightOfZerothTile):
            y += 1
        tileIndices[i] = linearize(x, y) + (widthOfTilingInTiles**2 * i)
    return tileIndices


def linearize(x, y):
    return int(x + (y * widthOfTilingInTiles))


def printTileCoderIndices(in1, in2):
    tileIndices = [-1]*numTilings
    tilecode(in1, in2, tileIndices)
    print('Tile indices for input (', in1, ',', in2, ') are : ', tileIndices)


#printTileCoderIndices(-0.6, -0.6)
#printTileCoderIndices(4.0, 2.0)
#printTileCoderIndices(5.99, 5.99)
#printTileCoderIndices(4.0, 2.1)
