placesToRoundTo = 6
numTilings = 4
widthOfTilingInTiles = 9
numTiles = (widthOfTilingInTiles ** 2) * numTilings

# Position is [–1.2, 0.5) -> X
# Velocity is [-0.07, 0.07) -> Y
xMinBound = -1.2
xMaxBound = 0.5
yMinBound = -0.07
yMaxBound = 0.07

if(xMinBound < 0):
    normalizedXMinBound = xMinBound + abs(xMinBound)
    normalizedXMaxBound = xMaxBound + abs(xMinBound)
else:
    normalizedXMinBound = xMinBound - xMinBound
    normalizedXMaxBound = xMaxBound - xMinBound

if(yMinBound < 0):
    normalizedYMinBound = yMinBound + abs(yMinBound)
    normalizedYMaxBound = yMaxBound + abs(yMinBound)
else:
    normalizedYMinBound = yMinBound - yMinBound
    normalizedYMaxBound = yMaxBound - yMinBound

widthOfXTiling = (normalizedXMaxBound - normalizedXMinBound) / (widthOfTilingInTiles - 1)
widthOfYTiling = (normalizedYMaxBound - normalizedYMinBound) / (widthOfTilingInTiles - 1)


def tilecode(inX, inY, tileIndices):
    # Normalize the inputs to 0
    if(xMinBound < 0):
        inX = inX + abs(xMinBound)
    else:
        inX = inX - xMinBound
    if (yMinBound < 0):
        inY = inY + abs(yMinBound)
    else:
        inY = inY - yMinBound

    # Calculate indices
    for i in range(len(tileIndices)):
        topRightOfZerothXTile = round(widthOfXTiling + (((-widthOfXTiling) / numTilings) * i), placesToRoundTo)
        topRightOfZerothYTile = round(widthOfYTiling + (((-widthOfYTiling) / numTilings) * i), placesToRoundTo)
        x = inX // widthOfXTiling
        y = inY // widthOfYTiling
        modx = round(inX % widthOfXTiling, placesToRoundTo)
        mody = round(inY % widthOfYTiling, placesToRoundTo)
        if(modx >= topRightOfZerothXTile):
            x += 1
        if(mody >= topRightOfZerothYTile):
            y += 1
        tileIndices[i] = linearize(x, y) + ((widthOfTilingInTiles ** 2) * i)
    return tileIndices


def linearize(x, y):
    return int(x + (y * widthOfTilingInTiles))


def printTileCoderIndices(in1, in2):
    tileIndices = [-1]*numTilings
    tilecode(in1, in2, tileIndices)
    print('Tile indices for input (', in1, ',', in2, ') are : ', tileIndices)


printTileCoderIndices(-1.2, -0.07)
printTileCoderIndices(0.499, 0.0699)
#printTileCoderIndices(5.99, 5.99)
#printTileCoderIndices(4.0, 2.1)

def test():
    pass
    # print(tilecode(-0.6, -0.6, [-1]*numTilings) == [0,81,162, 243])  # testing the lower right boounds
    # print(tilecode(-0.401, -0.401, [-1]*numTilings) == [70, 161, 242, 323])  # testing the uppper right boounds

if __name__ == "__main__":
    test()
