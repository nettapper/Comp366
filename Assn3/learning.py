import mountaincar
from Tilecoder import numTilings, numTiles, tilecode
from pylab import *  # includes numpy

numRuns = 1
n = numTiles * 3


def learn(alpha=.1/numTilings, epsilon=0, numEpisodes=200):
    gamma = 1
    theta1 = -0.001*rand(n) # q1?  defined as an array with 3 partitions [ 243 elem for action 1 | 243 for action 2 | 243 action 3 ]
    theta2 = -0.001*rand(n) # q2?
    returnSum = 0.0
    for episodeNum in range(numEpisodes):
        G, step = learnEpisode(alpha, epsilon, gamma, theta1, theta2)
        print("Episode: ", episodeNum, "Steps:", step, "Return: ", G)
        returnSum = returnSum + G
    print("Average return:", returnSum / numEpisodes)
    return returnSum, theta1, theta2


def learnEpisode(alpha, eps, gamma, theta1, theta2):
        in1, in2 = mountaincar.init()
        currentStates = tilecode(in1, in2, [-1]*numTilings) # returns the initial state
        episodeReturn = 0
        step = 0
        while(True): # continue until we reach terminal state (None)
            action = epsGreedyPolicy(currentStates, eps, theta1, theta2)
            reward, nextStatePosVel = mountaincar.sample((in1, in2), action)
            episodeReturn += reward
            step += 1
            if nextStatePosVel:
                nextIn1, nextIn2 = nextStatePosVel
                nextStates = tilecode(nextIn1, nextIn2, [-1]*numTilings)
                if(np.random.randint(0,2)):  # will return ints between [0,2)
                    updateTheta(theta1, theta2, currentStates, nextStates, action, reward, alpha, gamma)
                else:
                    updateTheta(theta2, theta1, currentStates, nextStates, action, reward, alpha, gamma)
                currentStates = nextStates
                in1, in2 = nextIn1, nextIn2
            else: # next state is terminal state
                if(np.random.randint(0,2)):  # will return ints between [0,2)
                    updateTheta(theta1, theta2, currentStates, nextStates, action, reward, alpha, gamma)
                else:
                    updateTheta(theta2, theta1, currentStates, nextStates, action, reward, alpha, gamma)
                return episodeReturn, step


def updateThetaOld(thetaA, thetaB, stateList, nextStateList, action, reward, alpha, gamma):
    if nextStateList:
        for state in stateList:
            for nextState in nextStateList:
                Qa[state, action] = Qa[state, action] + alpha * ( reward + gamma * Qb[nextState , np.argmax(Qa[nextState])] - Qa[state, action])
    else:
        for state in stateList:
            Qa[state, action] = Qa[state, action] + alpha * ( reward - Qa[state, action])


def updateTheta(thetaA, thetaB, stateList, nextStateList, action, reward, alpha, gamma):
    nextStateSum = 0
    if nextStateList:
        bestAction = alwaysGreedyPolicy(nextStateList, thetaA, thetaA)
        for nextState in nextStateList:
            nextStateSum += thetaB[nextState + (numTiles * bestAction)]

    for state in stateList:
        index = state + (numTiles * action)
        thetaA[index] = thetaA[index] + alpha * ( reward + gamma * nextStateSum - thetaA[index] )


def epsGreedyPolicy(currentStates, eps, theta1, theta2):  # given a state this will return an action
    if(np.random.random() < eps):  # random should return floats b/w [0,1)
        # can be either 0, 1, 2 or decelerate, coast, accelerate
        # randomly choose one of those actions
        return np.random.randint(0,3)  # will return ints between [0,3) (explore)
    else:
        return alwaysGreedyPolicy(currentStates, theta1, theta2)  # (greedy)


def alwaysGreedyPolicy(currentStates, theta1, theta2):  # given a state this will return an action
    action1, action2, action3 = 0, 0, 0
    for state in currentStates:
        action1 += theta1[state] + theta2[state]
        action2 += theta1[state + numTiles] + theta2[state + numTiles]
        action3 += theta1[state + (numTiles * 2)] + theta2[state + (numTiles * 2)]
    return np.argmax([action1, action2, action3])


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

def main():
    runSum = 0.0
    for run in range(numRuns):
        returnSum, theta1, theta2 = learn()
        runSum += returnSum
    print("Overall performance: Average sum of return per run:", runSum/numRuns)

if __name__ == '__main__':
    main()
