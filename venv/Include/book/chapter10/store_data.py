import json
numbers = [2, 3, 5, 7, 11, 13]
file_name = "numbers.json"
with open(file_name, 'w') as f_obj:
    json.dump(numbers, f_obj)

print("------------------------")
nums = []
with open(file_name) as f_obj:
    nums = json.load(f_obj)

print(nums)