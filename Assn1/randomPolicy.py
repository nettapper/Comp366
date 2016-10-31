import blackjack
from pylab import *

def run(numEpisodes):
    returnSum = 0.0
    for episodeNum in range(numEpisodes):
        G = 0
        ...
        print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G
    return returnSum/numEpisodes
