import blackjack
from pylab import *


Q1 = np.zeros((181,2)) # NumPy array of correct size
Q2 = np.zeros((181,2)) # NumPy array of correct size


def learn(alpha, eps, numTrainingEpisodes):
    pass
    # ... # Fill in Q1 and Q2


def evaluate(numEvaluationEpisodes):
    returnSum = 0.0
    alpha = 0.001
    eps = 1
    for episodeNum in range(numEvaluationEpisodes):
        G = episode(0, eps)
        returnSum = returnSum + G
    return returnSum/numEvaluationEpisodes


def episode(G, eps):
    currentState = blackjack.init() # returns the initial state
    while(True):  # repeate for each step
        (reward, currentState) = blackjack.sample(currentState, epsGreedyPolicy(currentState, eps))
        G += reward
        if(not currentState): # if currentState is false (we know its the end of the episode)

            return G

def epsGreedyPolicy(currentState, eps):  # given a state this will return an action
    if(np.random.random() > eps):
        combined = Q1[currentState] + Q2[currentState]
        return ....
    else:
        return alwaysGreedyPolicy(currentState)


def alwaysGreedyPolicy(currentState):  # given a state this will return an action
    combined = Q1[currentState] + Q2[currentState]
    return np.argmax(combined)



print("Average:", evaluate(10000))
