## Josh Blaz
## 1/29/19
## Radix Sort implemenetation using Bucket Sort

'''
Bucket sort algorithm.
L - unsorted list of numbers
M - upper bound of the range of number in the list (0...M)
x - position in each word/name in L to be sorted.
Returns sorted list ret
'''
def Bucket(L, x):

    M = 128 ## Set to 128 for # ASCII chars
    B = []
    for i in range(M): ## Initalize empty ASCII matrix
        B.append([]*M)  

    for i in range(len(L)):
        ascii_num = ord(L[i][x]) ## ASCII num of the character at position x
        B[ascii_num].append(L[i])
         
    ret = [] ## Initialize list for sorted values
    for i in range(len(L)):
        ret.append([])

    ## Class notes ##
    i = 0
    for j in range(M):
        for k in range(len(B[j])):
            ret[i] = B[j][k]
            i+=1        

    return ret

'''
Radix Sort Algorithm, implemented using Bucket Sort.
L - Unsorted list of strings.
k - Upper bound of the length of each string in the list.
Returns a sorted list of strings.
'''
def RadixSort(L, k):
    # Strings must be exactly length k.
    ret = [] # list to be returned
    # ret_ascii = []

    for word in L:
        if len(word) < k:
            # add 0's to make word length equal to k
            word = word + ('0' * (k-len(word)))
        ret.append(word)

    for i in range(k-1,-1,-1):
        ret = Bucket(ret, i)

    ret2 = []
    for word in ret:
        ret2.append(word.strip("0"))

    return ret2 

'''
Function to handle Kattis input and output formatting.

IE:
(In)              (Out)
3                 Bach
Mozart            Beethoven
Beethoven         Mozart 
Bach
'''
def In():
    n = int(input()) ## Number of iterations given by input (the following n inputs are to be sorted)
                     ## Convert user str input to int

    for i in range(0, n):
        L = [] ## Initialize list to store input words
        k = 0  ## Initialize k value to 0

        for i in range(n):  ## n = len(L)
            word = input()
            L.append(word)
            if len(word) > k: ## Set k to the length of the longest word in L
                k = len(word)
        
        ret = RadixSort(L, k)
        print("")
        for word in ret:
            print(word)

        n = int(input()) ## Take next n for next set of name inputs
        if n == 0:       ## End input once a '0' is received     
            break

def main():    
    In()
    
if __name__ == "__main__":
    main()
