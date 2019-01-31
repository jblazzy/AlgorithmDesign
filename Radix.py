## Josh Blaz
## 1/29/19
## Radix Sort implemenetation using Bucket Sort

'''
Bucket sort algorithm.
L - unsorted list of numbers
M - upper bound of the range of number in the list (0...M)
Returns sorted list s.
'''
def Bucket(L, M):

    # Initialize bucket list and sorted list to all 0's
    s = []
    bucket = []
    for i in range(0, M):
        bucket.append(0)
    for i in range(0,len(L)):
        s.append(0)

    for i in L:
        bucket[i] = bucket[i] + 1
    print("bucket:", bucket) # seems to be working

    i = 0
    for j in range(0, M):
        for k in range(0, bucket[j]):
            s[i] = j
            i = i + 1

    return s

'''
def Radix(L, k):
    # Strings must be exactly length k.

    for word in list:
        if len(word) > k:
            remove
        if len(word) < k:
            # add 0's to make length of words shorter than k equal to length k
            for i in range(0,(k-len(word))):
                word = word + '0'

    for i in range(k,1):
        Bucket(L,6)

'''

def main():
    unsorted = [3,1,4,1,1,5]
    print("input:", unsorted)
    print("output:", Bucket(unsorted, 6))
    print("should be: [1,1,1,3,4,5]")

if __name__ == "__main__":
    main()