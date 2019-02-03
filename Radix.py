## Josh Blaz
## 1/29/19
## Radix Sort implemenetation using Bucket Sort

'''
Bucket sort algorithm.
L - unsorted list of numbers
M - upper bound of the range of number in the list (0...M)
Returns sorted list s.
'''
def Bucket(L):
    # Should we find the max first and set that equal to M?
    maxx = 0
    for item in L:
        if item > maxx:
            maxx = item
    
    M = maxx + 1
    # Initialize bucket list and sorted list to all 0's
    s = []
    bucket = []
    for i in range(0, M):
        bucket.append(0)
    for i in range(0,len(L)):
        s.append(0)

    for i in L:
        bucket[i] = bucket[i] + 1

    i = 0
    for j in range(0, M):
        for k in range(0, bucket[j]):
            s[i] = j
            i = i + 1

    return s
'''
Radix Sort Algorith.
L - Unsorted list of strings.
k - Upper bound of the length of each string in the list.
Returns a sorted list of strings.
'''
def Radix(L, k):
    # Strings must be exactly length k. (k digits)
    ret = [] # list to be returned
    ret_ascii = []
    combined = []

    for word in L:
        if len(word) < k:
            # add 0's to make word length equal to k
            word = word + ('0' * (k-len(word)))
            ret.append(word)
        elif len(word) == k:
            ret.append(word)

    for i in range(k-1,-1,-1):
        temp = []
        for word in ret_ascii:
            temp.append(word[i])

        temp = Bucket(temp)



    #print(combined)
    #print(temp)
    return(ret)

def main():
    '''
    unsorted = [3,1,4,1,1,5, 9, 10, 8, 9, 4]
    print("input:", unsorted)
    print("output:", Bucket(unsorted))
    print("should be: [1,1,1,3,4,5]")
    '''
    
    namelist = ["robb", "jon","rickon", "bran"]
    Radix(namelist, 6)

if __name__ == "__main__":
    main()