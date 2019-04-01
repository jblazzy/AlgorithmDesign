'''
Function that (attempts) to compute the OPT for each iteration.
'''
def OPT(n, M, NY, SF):
    OPT_NY = [0]*(n)
    OPT_SF = [0]*(n)
    ret = [0]*(n) # Initialize to start building soln.

    # Recursive definition
    for i in range(1, n):
        OPT_NY[i] = NY[i] + min(OPT_NY[i-1], OPT_SF[i] + M)
        OPT_SF[i] = SF[i] + min(OPT_SF[i-1], OPT_NY[i] + M)

    for i in range(n-1, -1, -1):
        if OPT_NY[i] < OPT_SF[i]:
            ret[i] = "NY"
        else:
            ret[i] = "SF"

    if NY[0] < SF[0]:
        ret[0] = "NY"
    else:
        ret[0] = "SF"

    return ret

'''
Function that reads input from standard input and sends it to the OPT function.
'''
def In():
    n = int(input()) # Months
    M = int(input()) # Move cost

    NY = input().split() # NY costs
    SF = input().split() # SF costs

    for i in range(n):
        NY[i] = int(NY[i] )
        SF[i] = int(SF[i])

    fin = OPT(n, M, NY, SF)
    print(fin)

def main():
    In() # Call input function

main()