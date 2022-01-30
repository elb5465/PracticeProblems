# O(n) bc just while loop and min is O(2) which is negligible
def findTotalPower_best(power):
    l = len(power)
    total = 0
    pMin = MAXINT
    pSum = 0

    i = 0 
    j = -1

    while (i!=l-1):
        if (j==l-1):
            i += 1
            j = i
            pSum = 0
            pMin = power[j]

        else:
            j += 1

        pMin  = min(pMin, power[j])
        pSum  += power[j]
        total += pMin * pSum

    return total


# O(n^2 / 2) ??? -> Seems to run in half the for loops as the slowest bruteforce, but this still is basically O(n^2) bc of the sum and min() methods in python
def findTotalPower(power):
    l = len(power)
    total = 0
    loopCnt = 0

    i = 0 
    j = -1

    while (i!=l-1):
        if (j==l-1):
            i += 1
            j = i

        else:
            j += 1

        nums = power[i:j+1]
        total += (min(nums) * sum(nums))

        #print(i, j)
        loopCnt += 1 # checking how many loops bruteforce had compared to two pointer

    print("2 ptr loop count: ", loopCnt)
    return total

def findTotalPowerBruteForce(power):
    #bruteforce solution (0(n'2) - Could be refined using 2 pointer method instead of nested for loop
    l = len(power)
    total = 0
    loopCnt = 0

    for i in range(l):
        for j in range(l):
            
            #print(i, j)
            loopCnt += 1 # checking how many loops bruteforce had compared to two pointer

            if (j>=i):
                nums = power[i:j+1]
                total += (min(nums) * sum (nums))

    print("nested loop count: ", loopCnt)
    return total 


# ---------- Run times / loops taken for each method -----------
# SUMMARY: 2 ptr ran in roughly half the cycles of bruteforce when scaling up the data set
# '2 ptr loop count: ',  10 / 'expected: 69, Actual: ', 69
# 'nested loop count: ', 16 / 'expected: 69, Actual: ', 69

# '2 ptr loop count: ',  303810 / 'big data set check for 2-ptr runtime: ', 1267607589
# 'nested loop count: ', 606841 / 'big data set check for brute force nested loop runtime: ', 1267607589
 
# '2 ptr loop count: ',  1209790 / 'bigger data set check for 2-ptr runtime: ', 9359607361
# 'nested loop count: ', 2418025 / 'bigger data set check for brute force nested loop runtime: ', 9359607361


# ---------- Tests -----------
power = [2,3,2,1]
print("\nexpected: 69, Actual: ", findTotalPower(power))
print("expected: 69, Actual: ", findTotalPowerBruteForce(power))

power = [2,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,1232,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,1]
print("\nbig data set check for 2-ptr runtime: ", findTotalPower(power))
print("big data set check for brute force nested loop runtime: ", findTotalPowerBruteForce(power))


power = [2,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,1232,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,23,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,1232,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,1]
print("\nbigger data set check for 2-ptr runtime: ", findTotalPower(power))
print("bigger data set check for brute force nested loop runtime: ", findTotalPowerBruteForce(power))



# power = [2,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,1232,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,13,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,1232,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,13,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,1232,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,13,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,1232,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,13,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,1232,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,13,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,1232,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,13,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,1232,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,13,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,1232,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,13,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,1232,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,13,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,1232,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,13,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,1232,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,
# 2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,
# 12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,
# 3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,12,3,2,1]
# print("\nMASSIVE data set check for 2-ptr runtime: ", findTotalPower(power))
# print("MASSIVE data set check for brute force nested loop runtime: ", findTotalPowerBruteForce(power))
