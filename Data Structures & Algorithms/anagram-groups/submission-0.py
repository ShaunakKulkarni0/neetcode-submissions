class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == []:
            return []
        
        hashmap = {}
        for string in strs:
            arr = 26*[0]
            for char in string:
                arr[ord(char) - ord("a")] +=1
            tuple_arr = tuple(arr)
            if tuple_arr in hashmap:
                hashmap[tuple_arr].append(string)
            else:
                hashmap[tuple_arr] = [string]
        return list(hashmap.values())
                
        