class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        lst=[]
        no_repeat = set(nums)
        for i in range (len(no_repeat)):
            no_repeat_lst = list(no_repeat)

            c = nums.count(no_repeat_lst[i])
            dic[no_repeat_lst[i]] = c
        for j in range (k):
            max_key = max(dic,key=dic.get)
            dic.pop(max_key)
            lst.append(max_key)


        
            
               
        return lst
