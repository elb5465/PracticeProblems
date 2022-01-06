# Python coding questions for Amazon 

# ------------------ QUESTION 1: --------------------
# Password Strength (how many subgroupings of vowels and consonants are there)

password = "thisisbeautiful"
vowels = {'a', 'e', 'i', 'o', 'u'}
cnt = 0

vf, cf = False, False  #vowel found and consonant found flags
for c in password:
	if c in vowels:
		vf = True
	else:
		cf = True
	if cf and vf:
		cnt += 1
		cf = vf = False
print(cnt)


# ------------------ QUESTION 2: --------------------
# Number of ways to select 3 pages such that no two adjacent selected pages are of the same type (ordinary or bookmarked)
# Required: Permutations

''' notes:
        - find all permutations of 3 digits 
        - filter out only the ones that are have alternating binary (101 or 010)
        - count all that are left including duplicates
        - OR
        - (sliding window / pointer mxethod)
        - ...
'''

# def number_of_ways(s):
            

