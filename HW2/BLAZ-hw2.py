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
    
    # Initialize proposed index to 0 (most desirable woman man hasn't proposed to yet)
    lastProposed = {}
    for man in men:
        lastProposed[man] = 0
    
    # Dictionary to keep track of women pairings
    paired_women = {}
    for woman in women:
        paired_women[woman] = ""

    #Initialize all to unpaired
    unpaired = []
    for man in men:
        unpaired.insert(0, man)
    
    while len(unpaired) != 0: # While some unpaired man hasn't proposed to every woman
        man = unpaired.pop() # Man
        index = lastProposed[man] # Index of next woman to propose to on pref list
        woman = men[man][index] # Most desirable woman man hasn't proposed to

        if paired_women[woman] == "": # Woman is unpaired
            paired_women[woman] = man
            lastProposed[man] += 1 # Increment man's last proposed index

        elif (ranks[woman][man] < ranks[woman][paired_women[woman]]): # Woman prefers man to betrothed
                unpaired.insert(0, paired_women[woman]) # put betrothed back on stack
                lastProposed[man] += 1 # Increment man's last proposed index
                paired_women[woman] = man #Update paired women dictionary
        
        else: # Man still unmatched
            unpaired.insert(0, man) # Back on Stack
            lastProposed[man] += 1  # Next woman

    print("Stable Matching:")
    print("M - W")
    print("-----")
    for woman in paired_women:
        print(paired_women[woman], "-", woman)

    
'''
Function that takes men and women preference matrixes as input.

Example input:
--------------
3
Men preference matrix:
X A B C
Y A C B
Z A B C
Women preference matrix:
A Y X Z
B Z Y X
C Z X Y
'''
def In():
    n = int(input()) ## Number of iterations given by input (the following n inputs are to be sorted)

    men = {}
    women = {}

    print("Men preference matrix:")
    for i in range(0, n):
        split = input().split(" ")
        men[split[0]] = split[1:]
    
    print("Women preference matrix:")
    for i in range(0, n):
        split = input().split(" ")
        women[split[0]] = split[1:]
    
    print()
    #print("men: ",men)
    #print("women: ",women)
    
    return men, women

def main():    
    men, women = In()
    GS(men,women)

    
if __name__ == "__main__":
    main()

