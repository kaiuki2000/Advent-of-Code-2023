"""
************************** Note: **********************************
Alternative, much more efficient solution is given in 'Day9.ipynb'.
*******************************************************************
"""

# My initial method, using a recursively defined function, "diff".
# It doesn't seem to be working 100%. I suspect it is because of cases like these:
# 2 4 3 3
#  2 1 0 
# My algorithm stops here, but it shouldn't (!), since not all numbers are 0.
# Either way, I present the technique here, since it is a good example of recursion.
# Update from 01:29, 10/12/2023: I have confirmed that what is described above is indeed the problem.

# def diff(l, i, O):
#     return l[-i] if O == 0 else (diff(l, i, O - 1) - diff(l, i + 1, O - 1))

# L, R = [], []
# with open('Input.txt', 'r') as file:
#     for line in file: L.append([int(num) for num in line.split()])

# def M1(L):
#     for l in L:
#         i, D, V = 1, [], [l[-1]]
#         while(D != 0):
#             D = diff(l, 1, i)
#             V.append(D); i += 1 
#         R.append(sum(V))
#     print(f'Sum of the extrapolated values = {sum(R)}.')

# To run, use the following:
# M1(L)

# Update from 01:42, 10/12/2023: I have "finally" corrected the bug.
def diff(l, i, O):
    return l[-i] if O == 0 else (diff(l, i, O - 1) - diff(l, i + 1, O - 1))

L, R = [], []
with open('Input.txt', 'r') as file:
    for line in file: L.append([int(num) for num in line.split()])

def M1(L):
    E = []
    for l in L:
        i, D, V = 1, [], [l[-1]]
        while(True):
            D = diff(l, 1, i)
            V.append(D); i += 1
            if(D == 0):
                if(all(n == 0 for n in [diff(l, x, i - 1) for x in range(1, len(l) - i + 2)])): break
                else: continue
        E.append(sum(V))
    print(f'Sum of the extrapolated values = {sum(E)}.')

def M2(L):
    E = []
    for l in L:
        i, D, V = 1, [], [l[0]]
        while(True):
            D = diff(l, len(l) - i, i)
            V.append(D); i += 1
            if(D == 0):
                if(all(n == 0 for n in [diff(l, x, i - 1) for x in range(1, len(l) - i + 2)])): break
                else: continue
        f = lambda x: sum([n if i%2 == 0 else -n for i, n in enumerate(x)])
        E.append(f(V))
    print(f'Sum of the extrapolated values = {sum(E)}.')

# Run functions
# M1(L); M2(L)