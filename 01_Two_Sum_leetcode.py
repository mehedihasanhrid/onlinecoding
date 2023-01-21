class Solution:
    def twoSum(self,nums,target):
        complimentMap = dict()
        for i in range(len(nums)):
            num=nums[i]
            compliment = target - num
            if num in complimentMap:
                return [complimentMap[num],i]
            else:
                complimentMap[compliment] = i
    
    def forceTwoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i]+nums[j]
                if sum == target:
                    return [i,j]