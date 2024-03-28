class Solution(object):
    def twoSum(self, nums, target):
        
        length_of_nums = len(nums)
        
        first_element_to_the_second_to_last_element = length_of_nums - 1
        
        for i in range(first_element_to_the_second_to_last_element):
            
            next_element_to_the_last_element = i + 1
            
            for j in range(next_element_to_the_last_element, length_of_nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
        target_not_found= []
        
        return target_not_found
