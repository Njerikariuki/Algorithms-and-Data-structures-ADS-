def find_two_sum(nums, target):
    for item in nums:
        if not isinstance(item, int):
            raise TypeError(f"List 'nums' must contain only integers. Found element of type {type(item).__name__}.")

    num_map = {}
    
    for current_index, current_value in enumerate(nums):
        complement_value = target - current_value
        
        if complement_value in num_map:
            complement_index = num_map[complement_value]
            return [complement_index, current_index]
        
        num_map[current_value] = current_index
        
    return []

# Testing the code
numbers = [2,4,7,8,11]
target_int = 10

target_sum = find_two_sum(numbers,target_int)
print(target_sum)
