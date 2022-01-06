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
''' Number of ways to select 3 pages such that no two adjacent selected pages are of the same type (ordinary or bookmarked) '''

def number_of_ways(b):
	l = len(b)
	i = -1
	j = -1
	cnt = 0
	temp = ""
	k = 0

	while (i != l-2):
		if (i == -1):
			i = k
			k += 1
			# print(i,j,k)
			continue

		if (j == -1):
			j = k
			k += 1
			# print(i,j,k)
			continue

		if (i != -1) and (j != -1):
			temp = b[i]+b[j]+b[k]
			# print(temp)

			if (temp=="010" or temp=="101"):
				cnt += 1

			temp = ""

		if (k==l-1):
			if (j!=l-2):
				j += 1
				k = j+1
			else:
				i += 1
				j = i+1
				k = j+1
		else:
			k += 1

		#print(i,j,k)
	
	return cnt
			
print("expected: 3, actual: ", number_of_ways("10111"))
print("expected: 4, actual: ", number_of_ways("01001"))
print("expected: 0, actual: ", number_of_ways("0001"))
