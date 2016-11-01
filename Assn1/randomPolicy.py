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
    currentState = blackjack.init() # returns the initial state
    while(True):
        (reward, currentState) = blackjack.sample(currentState, chooseActionFromState(currentState))
        G += reward
        if(not currentState): # if currentState is false (we know its the end of the episode)
            return G


def chooseActionFromState(S): # aka the policy
    # 0 is to sick and 1 is to hit
    # randomly choose one of those actions
    return np.random.randint(0,2)  # will return ints between [0,2)


run(10)
