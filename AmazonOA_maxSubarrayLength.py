# O(n) refined solution 
def maxSubarrayLength(badges):
    l = len(badges)
    negCount = 0

    # store index of first and last negative came across
    # making -2 so modulo returns 0 if no negs in list
    firstNeg = -1
    lastNeg  = -1

    i = 0
    # get count of neg nums and store first and last index of negs
    for b in badges:
        if (b == -1 and firstNeg==-1):
            firstNeg = i

        if (b == -1):
            lastNeg = i  # update indx each time one is found, last one will be saved
            negCount += 1

        i += 1

    print("first neg idx: ", firstNeg)
    print("last neg idx: ",  lastNeg)
    print("neg count = ", negCount)

    #if count of negatives is even or 0, return whole list bc its product will be 1
    if (negCount % 2 == 0):
        return l
    
    #if only one neg number, these will equal, so return whichever side of list is longer
    if (firstNeg == lastNeg):
        left = len(badges[:firstNeg])
        right = len(badges[firstNeg+1:])
        return max(left, right)

    else: 
        #find diff between start of list and firstNeg (-1 for 0 index)
        firstDiff = l - 1 - firstNeg
        #find diff between end of list and lastNeg
        lastDiff  = l - 1 - lastNeg
        #return length of list minus whichever is smaller or either if equal
        print("first, last", firstDiff, lastDiff)
        return max(firstDiff, lastDiff)

# ---------- Tests ----------
badges = [1, -1, -1, 1, -1, 1]
print(maxSubarrayLength(badges))

badges = [-1, -1, -1, -1, -1, -1]
print(maxSubarrayLength(badges))

badges = [1, 1, 1, 1, 1, 1]
print(maxSubarrayLength(badges))

badges = []
print(maxSubarrayLength(badges))

badges = [1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1,
1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, -1]
print(maxSubarrayLength(badges))
