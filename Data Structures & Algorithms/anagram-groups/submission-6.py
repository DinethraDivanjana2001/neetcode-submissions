class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst=[]
        n=len(strs)
        visited = set()
    
        for i in range (n):
            # If this word is already inside a group, skip it completely
            if i in visited:
                continue
            lst2 = [strs[i]]
            visited.add(i)
            # Use a flag to see if we find any matching anagrams further down the list
            found_anagram = False
            for j in range (i+1,n):
                if sorted(strs[i]) == sorted (strs[j]):
                    lst2.append(strs[j])
                    visited.add(j) # Mark it so the outer loop skips it later
                    found_anagram = True
                    
                    
            
            lst.append(lst2)
        return lst


     