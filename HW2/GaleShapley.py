## Josh Blaz
## 2/6/19
## Gale Shapley Algorithm

'''
Function that implements the Gale-Shapley Algorithm.
men - men's preference dictionary taken from input.
women - women's preference dictionary taken from input.
Returns a stable matching.
'''
def GS(men, women):

    # Create inverted preference list for each woman
    ranks = {} 
    for woman in women:
        index = 1
        ranks[woman] = {}
        for man in women[woman]:
            ranks[woman][man] = index
            index = index + 1
    
    # Initialize proposed index to 1 (most desirable woman man hasn't proposed to yet)
    lastProposed = {}
    for man in men:
        lastProposed[man] = 1

    #Initialize all to unpaired
    unpaired = []
    for man in men:
        unpaired.append(man)
    
    while len(unpaired) != 0: # While some unpaired man hasn't proposed to every woman
        man = unpaired.pop()



    

def In():
    n = int(input()) ## Number of iterations given by input (the following n inputs are to be sorted)

    men = {}
    women = {}

    print("Men preference array:")
    for i in range(0, n):
        split = input().split(" ")
        men[split[0]] = split[1:]
    
    print("Women preference array:")
    for i in range(0, n):
        split = input().split(" ")
        women[split[0]] = split[1:]

    print("men: ",men)
    print("women: ",women)
    
    return men, women

def main():    
    '''
    ## Men's preferences
    men = [['X','Y','Z'],['A','A','A'],['B','C','B'],['C','B','C']]
    ## Women's preferences
    women = [['A','B','C'],['Y','Z','Z'],['X','Y','X'],['Z','X','Y']]
    '''
    men, women = In()

    GS(men,women)


    
if __name__ == "__main__":
    main()

