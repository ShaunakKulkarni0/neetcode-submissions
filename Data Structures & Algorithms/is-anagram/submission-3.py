import numpy as np
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arr = np.zeros(26)
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] +=1
            arr[ord(t[i]) - ord('a')] -=1
        return np.array_equal(arr, np.zeros(26))


