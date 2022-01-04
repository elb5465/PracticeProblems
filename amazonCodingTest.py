# Python coding questions for Amazon 

# ------------------ QUESTION 1: --------------------
# Password Strength (how many subgroupings of vowels and consonants are there)

password = "thisisbeautiful"
vowels = {'a', 'e', 'i', 'o', 'u'}
count = 0

v_found, c_found = False, False        
for char in password:
	if char in vowels:
		v_found = True
	else:
		c_found = True
	if v_found and c_found:
		count += 1
		v_found, c_found = False, False
# print(count)


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
            

