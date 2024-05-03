# List Comprehension Syntax
# new_list = [new_item for item in list]

# Conditional List Comprehension Syntax
# new_list = [new_item for item in list if test]
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_num = [n**2 for n in numbers]
# even_num = [n for n in numbers if n % 2 == 0]
# print(squared_num, even_num)

# with open("file1.txt", mode="r") as f1:
#     file1_nums = [int(n) for n in f1.readlines()]
# with open("file2.txt", mode="r") as f2:
#     file2_nums = [int(n) for n in f2.readlines()]
#
# result = [num for num in file2_nums if num in file1_nums]
#
# print(file1_nums)
# print(file2_nums)
# print(result)


# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# list = [1,2,3]
# new_list = [n**2 for n in list]
# exit
# exit()
# name = "Aakash"
# new_list = [letter for letter in name]
# print(new_list)
# dobuled_list = [n*2 for n in range(1,5)]
# print(doubled_list)
# print(dobuled_list)
# clear
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# names
# short_names = [sn for sn in names if len(sn) == 4]
# short_names = [sn for sn in names if len(sn) < 5]
# short_names
# caps_names = [name.upper() for name in names if len(name) > 4]
# caps_names
# names = ["Alex", "Beth", "Dave", "Caroline", "Eleanor", "Freddie"]
# import random
# student_scores = {name:random.randint(1,100) for name in names}
# passed_students = {name:score for (name,score) in student_scores.items() if score > 33}
