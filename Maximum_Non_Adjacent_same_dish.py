
def func(nums, n, val):
    if n < 0:
        return 0
    
    if n == 0:
        if nums[n] == val:
            return 1
        return 0

    pick = 0
    
    if nums[n] == val:
        pick = 1 + func(nums, n-2, val)

    not_pick = func(nums, n-1, val)

    return max(pick, not_pick)


def dish(nums):
    my_dict = {}
    my_set = set(nums)

    for i in my_set:
        my_dict[i] = func(nums, len(nums)-1, i)

    max_dish = 0
    dish_type = None
    for key,val in my_dict.items():
        if max_dish<val:
            max_dish = val
            dish_type = key

    return dish_type


    
nums = [1,2,2,1,2,1,1,1,1,3,3,]
print(dish(nums))
