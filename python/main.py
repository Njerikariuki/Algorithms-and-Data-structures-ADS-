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


#SOLUTION TO PROBLEM 2:
def max_subarray_sum(nums):
    # Handle the edge case of an empty array
    if not nums:
        return 0, []
    #Initialize maximum sum and boundary indices
    global_max = nums[0]
    global_start =0
    global_end = 0

    current_max = nums[0]
    current_start = 0 # Tracks the start index of the current maximum subarray

    # iteration
    for i in range(1,len(nums)):
        if nums[i] > current_max + nums[i]:
            current_max = nums[i]
            current_start = i
        else:
            current_max += nums[i]
        if current_max > global_max:
            global_max = current_max
            global_start = current_start
            global_end = i # The current index 'i' is the end of the new global maximum subarray   
    max_subarray = nums[global_start : global_end + 1]
    return global_max, max_subarray



# Code testing
List_1 = [2,4,3,9,8,1,2]
L_sum = max_subarray_sum(List_1)
print(L_sum)

List_2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
L_sum = max_subarray_sum(List_2)
print(L_sum)
