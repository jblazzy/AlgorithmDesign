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
    # Initialize bucket list to all 0's
    # Also initalize s to all 0's -- this is where the sorted values will go
    s = []
    bucket = []
    for i in range(0,len(L)):
        bucket.append(0)
        s.append(0)

    for i in L:
        bucket[i] = bucket[i] + 1

    i = 0
    for j in range(0, M):
        for k in range(1, bucket[j]):
            s[i] = j
            i = i + 1

    return s

# def Radix(L):

def main():
    unsorted = [3,1,4,1,1,5]
    print("unsorted")
    print(unsorted)
    print("sorted")
    print(Bucket(unsorted, 6))

if __name__ == "__main__":
    main()