import blackjack
import numpy as np

def run(numEpisodes):
    returnSum = 0.0
    for episodeNum in range(numEpisodes):
        G = episode(0)
        print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G
    return returnSum/numEpisodes


def episode(G):
    initialState = blackjack.init()
    return G


run(10)
