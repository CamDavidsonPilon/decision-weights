#generate data for mturks to classify

import numpy as np
from itertools import combinations

EV = 100.
P = [0.01, 0.02, 0.99, 0.98, 0.05,  0.1 ,  0.2, 0.25,  0.3,  0.4, 
         0.5,   0.6,  0.7,  0.75,  0.8, 0.9, 0.95]


def choose_lottery(prizes, chances):
    return """
-------------------------------------------------------------------------
Would you rather have a:

A:  %d%% chance to win $%d, 

B:  %d%% chance to win $%d, 

    """%(chances[0], prizes[0], chances[1], prizes[1])



def run():
    with open('HIT_data.csv','w') as csv:
        csv.write('percentA,percentB,prizeA,prizeB\n')
        for p1, p2 in combinations(P, 2):
            prize1, prize2 = int(round(EV/p1)), int(round(EV/p2))
            percent1,percent2 = int(100*p1), int(100*p2)
            print choose_lottery([prize1, prize2], [percent1, percent2])
            csv.write('%d,%d,%d,%d\n'%(percent1,percent2,prize1,prize2))

    return 

if __name__=="__main__":
    run()




    