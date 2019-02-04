## Josh Blaz
## 2-D array problem (Chapter 2, Problem 6)

'''
Function to solve Problem 6, Chapter 2 of "Algorithm Design"
'''
def array(A):
    n = len(A)
    print(A)
    
    B = []
    # Initialize result matrix
    for i in range(n):
        B.append([0]*n)   ## n^2 (n within for loop to n)

    # Set top row
    for i in range(0,n):
        for j in range(0, i+1):
            B[0][i] += A[j]  ## n^2 (nested for loop)

    for i in range(1, n):
        for j in range(i, n):  ## iterate from i,n because when i >= j, nothing changes (0).
            #print(B[i-1][j], " - ", A[i-1], " = ", B[i-1][j] - A[i-1])
            B[i][j] = B[i-1][j] - A[i-1]  ## n^2 (nested for loop)

    ## Running time of the algorithm is at most 3n^2

    print("Output matrix:")
    for row in B:
        print(row)

    return B

def main():
    A = [1,3,3,2,9,9,0]
    array(A)

if __name__ == "__main__":
    main()