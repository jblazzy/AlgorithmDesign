## Josh Blaz
## 3/7/19
## Sort and Count Algorithm

'''
Function that implements the Sort and Count Algorithm.
L - List of integers.
Returns a sorted list and the number of inversions in the list.
'''
def SC(L):
    iL = 0 # Left inversions
    iR = 0 # Right inversions
    iB = 0 # Between (combined) inversions
    LL = []
    LR = []
    LB = []

    if len(L)==1:
        return(0,L)

    L1,L2 = splitty(L) # Split evenly into two lists (Left and Right)

    (iL, LL) = SC(L1)
    (iR, LR) = SC(L2)
    (iB, LB) = merge(LL,LR)

    return(iL + iR + iB, LB)



'''
Function that merges and counts inversions.
Returns the list and the inversions between.
'''
def merge(LL,LR):
    L = [] # Solution
    i = 0
    j = 0
    iB = 0 

    while(i < len(LL) and j < len(LR)):
        L.append(min(LL[i],LR[j])) # Append the smaller of LL[i] and LR[i] to L

        if(LL[i] > LR[j]):
            iB += len(LL) - i
            j += 1
        else:
            i += 1

    if i < len(LL): 
        L = L + LL[i:] # Add the rest of LL to L 
    else: # if i is not less than len(LL), j must be less than len(LR)
        L = L + LR[j:]

    return(iB, L)


'''
Function that splits a list in half.
L - List of integers.
Returns two halves of a list.
'''
def splitty(L):
    temp1 = [] # First half
    temp2 = [] # First half

    temp1 = L[:len(L)//2]
    temp2 = L[len(L)//2:]
    return temp1,temp2

'''
Function that reads input from standard input.
'''
def In():
    length = int(input()) ## Length of original list

    S = input().split() # Split up list to convert into integers
    L = []

    for num in S:
        L.append(int(num))

    return L

def main():
    L = In()
    ret1 = 0
    ret2 = []

    ret1, ret2 = SC(L)

    print(ret1) ## Only print the number of inversions (not the list)

    

if __name__ == "__main__":
    main()

