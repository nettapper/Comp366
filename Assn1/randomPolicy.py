import blackjack
import numpy as np


def run(numEvaluationEpisodes):
    returnSum = 0.0
    for episodeNum in range(numEvaluationEpisodes):
        discount = 1
        G = episode(0, discount)
        print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G
    return returnSum/numEvaluationEpisodes


def episode(G, discount):
    currentState = blackjack.init() # returns the initial state
    counter = 0
    while(True):
        (reward, currentState) = blackjack.sample(currentState, chooseActionFromState(currentState))
        G += (discount ** counter) * reward
        counter += 1  # Need to inc after using it to calculate the return (G)
        if(not currentState): # if currentState is false (we know its the end of the episode)
            return G


def chooseActionFromState(S): # aka the policy
    # 0 is to sick and 1 is to hit
    # randomly choose one of those actions
    return np.random.randint(0,2)  # will return ints between [0,2)
