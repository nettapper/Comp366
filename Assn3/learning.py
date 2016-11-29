import mountaincar
from Tilecoder import numTilings, numTiles, tilecode
from pylab import *  # includes numpy

numRuns = 1
n = numTiles * 3

def learn(alpha=.1/numTilings, epsilon=0, numEpisodes=200):
    gamma = 1
    step = 0
    theta1 = -0.001*rand(n)
    theta2 = -0.001*rand(n)
    returnSum = 0.0
    for episodeNum in range(numEpisodes):
        G = learnEpisode(alpha, epsilon, gamma):
        print("Episode: ", episodeNum, "Steps:", step, "Return: ", G)
        returnSum = returnSum + G
    print("Average return:", returnSum / numEpisodes)
    return returnSum, theta1, theta2


def learnEpisode(alpha, eps, gamma):
        currentState = mountaincar.init() # returns the initial state
        episodeReturn = 0
        while(True):  # repeat for each step of the episode
            action = epsGreedyPolicy(currentState, eps)
            (reward, nextState) = mountaincar.sample(currentState, action)
            episodeReturn += reward
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
                return episodeReturn # if nextState is false (we know its the end of the episode)


def epsGreedyPolicy(currentState, eps):  # given a state this will return an action
    if(np.random.random() < eps):  # random should return floats b/w [0,1)
        # 0 is to sick and 1 is to hit
        # randomly choose one of those actions
        return np.random.randint(0,3)  # will return ints between [0,3) (explore)
    else:
        return alwaysGreedyPolicy(currentState)  # (greedy)


def alwaysGreedyPolicy(currentState):  # given a state this will return an action
    return np.argmax(Q1[currentState] + Q2[currentState])


#Additional code here to write average performance data to files for plotting...
#You will first need to add an array in which to collect the data

def writeF(theta1, theta2):
    fout = open('value', 'w')
    steps = 50
    for i in range(steps):
        for j in range(steps):
            F = tilecode(-1.2 + i * 1.7 / steps, -0.07 + j * 0.14 / steps)
            height = -max(Qs(F, theta1, theta2))
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()


if __name__ == '__main__':
    runSum = 0.0
    for run in range(numRuns):
        returnSum, theta1, theta2 = learn()
        runSum += returnSum
    print("Overall performance: Average sum of return per run:", runSum/numRuns)
