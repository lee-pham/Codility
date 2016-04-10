# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
def solution(N):
    # write your code in Python 2.7
    gaps = []
    c = 0
    for i in bin(N)[2:]:
        if i == '0':
            c += 1
        else:
            gaps.append(c)
            c = 0
    return max(gaps)
