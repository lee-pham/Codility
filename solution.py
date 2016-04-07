# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    c = 0
    lsum = 0
    rsum = sum(A)
    
    for i in range(0, len(A)):
        rsum -= A[i]
        if lsum == rsum:
            return i
            c += 1
        lsum += A[i]
        
    if c == 0:
        return -1
