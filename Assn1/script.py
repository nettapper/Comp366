import DoubleQ
import numpy as np

def run():
    outfile = open("output.txt", "w")

    eps = .9
    epsStepSize = 0.1
    alphaStepSize = 0.1
    numTrainingEpisodes = 1000000
    numEvaluationEpisodes = 10000000

    print("Starting script with {:,} traing episodes and {:,} evaulation episodes".format(numTrainingEpisodes, numEvaluationEpisodes))

    while(eps <= 1):
        alpha = 0.001
        while (alpha < 2):
            DoubleQ.learn(alpha, eps, numTrainingEpisodes)
            average = DoubleQ.evaluate(numEvaluationEpisodes)
            print("Finished episode with eps=%s, alpha=%s" % (eps, alpha))
            outfile.write("%s, %s, %s\n" % (eps, alpha, average))
            outfile.flush()
            DoubleQ.Q1 = 0.00001 * np.random.random((181, 2)) # NumPy array of correct size w/ random values
            DoubleQ.Q2 = 0.00001 * np.random.random((181, 2)) # NumPy array of correct size w/ random values
            alpha = round(alpha + alphaStepSize, 5)
        eps = round(eps + epsStepSize, 5)

    outfile.close()

if __name__ == "__main__":
    run()
