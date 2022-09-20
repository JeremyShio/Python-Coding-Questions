# ------- Python Coding Questions -------




# ------- Question: 1 -------
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
    print(f"hello_{user_name}")

user_name = "Jeremy"
print('')
print('Question: 1')
print(hello_name(user_name))




# ------- Question: 2 -------
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing. def first_odds():

def first_odds():
    i = 0
    for i in range (1, 100):
        # Check if number is odd
        if i % 2 != 0:
            print(i)
            # Increment by 1 number at a time
            i += 1
        
print('')
print('Question: 2')
print(first_odds())




# ------- Question: 3 -------
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):
    print(max(a_list))

a_list = [11, 22, 42, 16, 25, 71, 10, 13, 89, 28]
print('')
print('Question: 3')
print(max_num_in_list(a_list))




# ------- Question: 4 -------
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year(a_year):
    # Possible leap year is divisible by 400 and 100 alogside each other
    if (a_year % 400 == 0) and (a_year % 100 == 0):
        print(f"{a_year} is a leap year!")
    # Possible leap year is not divisible by 100 but is divisible by 4
    elif (a_year % 4 == 0) and (a_year % 100 != 0):
        print(f"{a_year} is a leap year!")
    # Other years are NOT leap years
    else:
        print(f"{a_year} is NOT a leap year!")
        
a_year = 2020
print('')
print('Question: 4 -- Year 2020 Test')
print(is_leap_year(a_year))

a_year = 2022
print('')
print('Question: 4 -- Year 2022 Test')
print(is_leap_year(a_year))




# ------- Question: 5 -------
# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    # If there are no numbers in the list to iterate through
    if len(a_list) < 1:
        return False
    # Check if max number minus min number is equal to the length of the list
    return a_list == list(range(min(a_list), max(a_list)+1))

a_list = [2,3,4,5,6,7]
print('')
print('Question: 5 -- Consecutive Test -- [2,3,4,5,6,7]')
print(is_consecutive(a_list))

a_list = [1,2,4,5]
print('')
print('Question: 5 -- NON-Consecutive Test -- [1,2,4,5]')
print(is_consecutive(a_list))