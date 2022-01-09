class Solution:
    def validAnagram(self, s, t):
        map = {}
        for c in s:
            if c.isalpha():
                if c in map:
                    map[c] = map.get(c) + 1
                else:
                    map[c] = 1
        # print(map)

        for c in t:
            if c.isalpha():
                if c in map:
                    map[c] = map.get(c) - 1

        # print(map)

        for key in map:
            if map[key] != 0:
                return False
        return True

s = Solution()
print("expected: True, actual: ", s.validAnagram("naga, ram", "anagram"))
print("expected: True, actual: ", s.validAnagram("aba", "aab"))
print("expected: False, actual: ", s.validAnagram("car", "rat"))
print("expected: False, actual: ", s.validAnagram("racecar", "aab"))
print("expected: True, actual: ", s.validAnagram(" ", ""))
