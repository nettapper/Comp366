import numpy as np
import threading

outfile = open("multioutput.txt", "w")
numEvaluationEpisodes = 1000000
numTrainingEpisodes = 10000000

class myThread(threading.Thread):
    def __init__(self, threadID, eps, alpha):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.eps = eps
        self.alpha = alpha
        self.Q1 = 0.00001 * np.random.random((181, 2)) # NumPy array of correct size w/ random values
        self.Q2 = 0.00001 * np.random.random((181, 2)) # NumPy array of correct size w/ random values
        self.playerSum = 0
        self.dealerCard = 0
        self.usableAce = False

    def run(self):
        self.learn(self.alpha, self.eps, numTrainingEpisodes)
        average = self.evaluate(numEvaluationEpisodes)
        outfile.write("%s, %s, %s\n" % (self.eps, self.alpha, average))
        outfile.flush()

    def learn(self, alpha, eps, numTrainingEpisodes):
        gamma = 1
        for episodeNum in range(numTrainingEpisodes):
            G = self.learnEpisode(alpha, eps, gamma)

    def learnEpisode(self, alpha, eps, gamma):
            currentState = self.init() # returns the initial state
            episodeReturn = 0
            while(True):  # repeate for each step of the episode
                action = self.epsGreedyPolicy(currentState, eps)
                (reward, nextState) = self.sample(currentState, action)
                episodeReturn += reward
                if(nextState):
                    if(np.random.randint(0,2)):  # will return ints between [0,2)
                        self.Q1[currentState, action] = self.Q1[currentState, action] + alpha * ( reward + gamma * self.Q2[nextState, np.argmax(self.Q1[nextState])] - self.Q1[currentState, action])
                    else:
                        self.Q2[currentState, action] = self.Q2[currentState, action] + alpha * ( reward + gamma * self.Q1[nextState, np.argmax(self.Q2[nextState])] - self.Q2[currentState, action])
                    currentState = nextState
                else: # we know its the terminal state so the 'next rewards' simplify to 0 and can be ommited
                    if(np.random.randint(0,2)):  # will return ints between [0,2)
                        self.Q1[currentState, action] = self.Q1[currentState, action] + alpha * ( reward - self.Q1[currentState, action])
                    else:
                        self.Q2[currentState, action] = self.Q2[currentState, action] + alpha * ( reward - self.Q2[currentState, action])
                    return episodeReturn # if nextState is false (we know its the end of the episode)

    def evaluate(self, numEvaluationEpisodes):
        if(numEvaluationEpisodes > 0):
            returnSum = 0.0
            eps = 0  # 0 is fully greedy, where as 1 is fully exploratory
            for episodeNum in range(numEvaluationEpisodes):
                G = self.evaluateEpisode(0, eps)
                returnSum = returnSum + G
            return returnSum/numEvaluationEpisodes
        else:
            return "Please call with a number of episodes greater than 0"

    def evaluateEpisode(self, G, eps):
        currentState = self.init() # returns the initial state
        while(True):  # repeate for each step
            (reward, currentState) = self.sample(currentState, self.epsGreedyPolicy(currentState, eps))
            G += reward
            if(not currentState): # if currentState is false (we know its the end of the episode)
                return G

    def epsGreedyPolicy(self, currentState, eps):  # given a state this will return an action
        if(np.random.random() < eps):  # random should return floats b/w [0,1)
            # 0 is to sick and 1 is to hit
            # randomly choose one of those actions
            return np.random.randint(0,2)  # will return ints between [0,2) (explore)
        else:
            return self.alwaysGreedyPolicy(currentState)  # (greedy)

    def alwaysGreedyPolicy(self, currentState):  # given a state this will return an action
        return np.argmax(self.Q1[currentState] + self.Q2[currentState])

    def card(self):
        return min(10, np.random.randint(1,14))

    def encode(self):
        return 1 + (90 if self.usableAce else 0) + 9*(self.dealerCard-1) + (self.playerSum-12)

    def decode(self,  state):
        if state==0: return
        state = state - 1
        self.usableAce = state >= 90
        state = state % 90
        self.dealerCard = 1 + state // 9
        self.playerSum = (state % 9) + 12

    def init(self):
        return 0

    def numActions(self,  s):
        return 2

    def sample(self, s, a):
        self.decode(s)
        if s==0: return self.firstSample()
        if a==0: return self.dealerPlaySample()   # sticking
        self.playerSum += self.card()                  # hitting
        if self.playerSum==21: return self.dealerPlaySample()
        if self.playerSum > 21:
            if self.usableAce:
                self.playerSum -= 10
                self.usableAce = False
                return 0, self.encode()
            else:
                return -1, False
        return 0, self.encode()

    def firstSample(self):
        """ deal first cards and check for naturals """
        playerCard1 = self.card()
        playerCard2 = self.card()
        self.playerSum = playerCard1 + playerCard2
        self.usableAce = playerCard1==1 or playerCard2==1
        if self.usableAce: self.playerSum += 10
        self.dealerCard = self.card()
        if self.playerSum==21:    # player has natural
            self.dealerCard2 = self.card()
            dealerSum = self.dealerCard + self.dealerCard2
            if (self.dealerCard==1 or self.dealerCard2==1) and dealerSum==11:  # dealer has a natural too
                return 0, False
            else:
                return 1, False
        while self.playerSum < 12:
            c = self.card()
            self.playerSum += c
            if (c == 1) and (self.playerSum <= 11):
                self.playerSum += 10
                self.usableAce = True
        if self.playerSum==21: return self.dealerPlaySample()
        return 0, self.encode()

    def dealerPlaySample(self):
        self.dealerCard2 = self.card()
        dealerSum = self.dealerCard + self.dealerCard2
        self.usableAce = self.dealerCard==1 or self.dealerCard2==1  # now self.usableAce refers to the dealer
        if self.usableAce: dealerSum += 10
        if dealerSum==21: return -1, False  # dealer has a natural
        while dealerSum < 17:
            dealerSum += self.card()
            if dealerSum > 21:
                if self.usableAce:
                    dealerSum -= 10
                    self.usableAce = False
                else:
                    return 1, False
        if dealerSum < self.playerSum: return 1, False
        elif dealerSum > self.playerSum: return -1, False
        else: return 0, False

    def printPolicy(self, policy):
        for self.usableAce in [True, False]:
            print()
            print("" if self.usableAce else " No", "Usable Ace:")
            for self.playerSum in range(20, 11, -1):
                for self.dealerCard in range(1,11):
                    print("S" if policy(self.encode())==0 else "H", end=' ')
                print(self.playerSum)
            for self.dealerCard in range(1,11): print(self.dealerCard, end=' ')
            print()


def main():
    threads = []
    eps = .5
    epsStepSize = 0.1
    alphaStepSize = 0.000033
    counter = 0
    while(eps <= 1):
        alpha = 0.00001
        while (alpha < 0.001):
           thread = myThread(counter, eps, alpha)
           thread.start()
           threads.append(thread)
           counter += 1
           alpha = round(alpha + alphaStepSize, 8)
        eps = round(eps + epsStepSize, 8)

    print("Starting script with {:,} traing episodes and {:,} evaulation episodes".format(numTrainingEpisodes, numEvaluationEpisodes))
    print("Threads created: ", counter)

    for t in threads:
        t.join()

    print("All threads finished, Exiting...")


if __name__ == "__main__":
    main()
