placesToRoundTo = 6
numTilings = 4
minBound = -0.6
maxBound = -0.4
if(minBound < 0):
    normalizedMinBound = minBound + abs(minBound)
    normalizedMaxBound = maxBound + abs(minBound)
else:
    normalizedMinBound = minBound
    normalizedMaxBound = maxBound
widthOfTilingInTiles = 9
widthOfTiling = (normalizedMaxBound - normalizedMinBound) / (widthOfTilingInTiles - 1)


def tilecode(in1, in2, tileIndices):
    if(minBound < 0):
        in1 = in1 + abs(minBound)
        in2 = in2 + abs(minBound)
    for i in range(len(tileIndices)):
        topRightOfZerothTile = round(widthOfTiling + (((-widthOfTiling) / numTilings) * i), placesToRoundTo)
        x = in1 // widthOfTiling
        y = in2 // widthOfTiling
        modx = round(in1 % widthOfTiling, placesToRoundTo)
        mody = round(in2 % widthOfTiling, placesToRoundTo)
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


printTileCoderIndices(-0.6, -0.6)
printTileCoderIndices(-0.39, -0.39)
#printTileCoderIndices(5.99, 5.99)
#printTileCoderIndices(4.0, 2.1)
