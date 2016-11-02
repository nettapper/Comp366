import blackjack
from pylab import *


Q1 = np.zeros((181,2)) # NumPy array of correct size
Q2 = np.zeros((181,2)) # NumPy array of correct size


def learn(alpha, eps, numTrainingEpisodes):
    gamma = 1
    returnSum = 0.0
    for episodeNum in range(numTrainingEpisodes):
        G = 0 #TODO get return from leanrnEpisode
        learnEpisode(alpha, eps, gamma)
        # Fill in Q1 and Q2
        # print("Episode: ", episodeNum, "Return: ", G)
        returnSum = returnSum + G
        if episodeNum % 10000 == 0 and episodeNum != 0:
            print("Average return so far: ", returnSum/episodeNum)


def learnEpisode(alpha, eps, gamma):
        currentState = blackjack.init() # returns the initial state
        while(True):  # repeate for each step of the episode
            action = epsGreedyPolicy(currentState, eps)
            (reward, nextState) = blackjack.sample(currentState, action)
            if(nextState):
                if(np.random.randint(0,2)):  # will return ints between [0,2)
                    Q1[currentState, action] = Q1[currentState, action] + alpha * ( reward + gamma * Q2[nextState, np.argmax(Q1[nextState])] - Q1[currentState, action])
                else:
                    Q2[currentState, action] = Q2[currentState, action] + alpha * ( reward + gamma * Q1[nextState, np.argmax(Q2[nextState])] - Q2[currentState, action])
                currentState = nextState
            else: # we know its the terminal state so the 'next rewards' simplify to 0 and can be ommited
                if(np.random.randint(0,2)):  # will return ints between [0,2)
                    Q1[currentState, action] = Q1[currentState, action] + alpha * ( reward - Q1[currentState, action])
                else:
                    Q2[currentState, action] = Q2[currentState, action] + alpha * ( reward - Q2[currentState, action])
                return # if nextState is false (we know its the end of the episode)


def evaluate(numEvaluationEpisodes):
    if(numEvaluationEpisodes > 0):
        returnSum = 0.0
        alpha = 0.001
        eps = 0  # 0 is fully greedy, where as 1 is fully exploratory
        for episodeNum in range(numEvaluationEpisodes):
            G = evaluateEpisode(0, eps)
            returnSum = returnSum + G
        return returnSum/numEvaluationEpisodes
    else:
        return "Please call with a number of episodes greater than 0"


def evaluateEpisode(G, eps):
    currentState = blackjack.init() # returns the initial state
    while(True):  # repeate for each step
        (reward, currentState) = blackjack.sample(currentState, epsGreedyPolicy(currentState, eps))
        G += reward
        if(not currentState): # if currentState is false (we know its the end of the episode)
            return G

def epsGreedyPolicy(currentState, eps):  # given a state this will return an action
    if(np.random.random() < eps):  # random should return floats b/w [0,1)
        # 0 is to sick and 1 is to hit
        # randomly choose one of those actions
        return np.random.randint(0,2)  # will return ints between [0,2) (explore)
    else:
        return alwaysGreedyPolicy(currentState)  # (greedy)


def alwaysGreedyPolicy(currentState):  # given a state this will return an action
    return np.argmax(Q1[currentState] + Q2[currentState])


# TODO implement printPolicy
def run():
    alpha = 0.001
    eps = 1
    numTrainingEpisodes = 400000
    numEvaluationEpisodes = 400000
    learn(alpha, eps, numTrainingEpisodes)
    print("Evaluation Average:", evaluate(numEvaluationEpisodes))


run()
