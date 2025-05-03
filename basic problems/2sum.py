def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


nums_input = input("Enter numbers separated by spaces: ")
nums = list(map(int, nums_input.split()))

target = int(input("Enter target value: "))


result = two_sum(nums, target)

if result:
    print(f"Indices: {result}")
else:
    print("No two numbers add up to the target.")