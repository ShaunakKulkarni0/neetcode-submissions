class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arr = [0] * 26
        base = ord('a')

        for c1, c2 in zip(s, t):
            arr[ord(c1) - base] += 1
            arr[ord(c2) - base] -= 1

        return not any(arr)
