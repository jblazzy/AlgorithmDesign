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

    L1,L2 = split(L) # Split evenly into two lists (Left and Right)

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
        L.append(min(LL[i],LR[i])) # Append the smaller of LL[i] and LR[i] to L

        if(LL[i] > LR[j]):
            iB += len(LL) - i
            i += 1
        else:
            iB += len(LR) - j
            j += 1

    return(iB, L)


'''
Function that splits a list in half.
L - List of integers.
Returns two halves of a list.
'''
def split(L):
    temp1 = [] # First half
    temp2 = [] # First half

    temp1 = L[:len(L)//2]
    temp2 = L[len(L)//2:]
    return temp1,temp2


def main():
    L = [1,2,3,4,5,6,7,8]

    print(L)

    print(split(L))

if __name__ == "__main__":
    main()

