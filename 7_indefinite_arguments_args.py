# def tea_order(customer_name, tea_type, milk=None, sweetener=None):
#     print(customer_name, "ordered a", tea_type, "tea")
#     if milk!=None:
#         print(" - Add:", milk)
#     if sweetener!=None:
#         print(" - Add:", sweetener)
# tea_order("Alice", "chamomile")
# tea_order("Bob", "black", "oat")
# tea_order("Tony", "black", "oat", "honey")




def tea_order(customer_name, tea_type, **kwargs):
    print(customer_name, "ordered a", tea_type, "tea")
    for key, value in kwargs.items():
        print(" - Add", key, ":", value)
tea_order("Alice", "chamomile")
tea_order("Bob", "black", milk="oat")
tea_order("Tony", "black", milk="oat", sweetener="honey")


# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).
def sum_squares(*args):
    sum=0#Initialize sum to 0
    for num in args: # Iterate through each argument
        sum += num ** 2 #Square the number and add it to the sum
        #first time: sum = 0 + 4= 4
        #second time: sum= 4 + 25= 29
        #third time: sum = 29 + 36 = 65
    return sum

print(sum_squares(4, 5, 6, 7, 7, 7, 8, 9, 9, 9))

# For example for thes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    sum = 0 
    for num in args:
        sum += abs(num)
    return sum
list_of_numbers = [-10, 5, -3, 7, -2, 6, 7, -8, 9]
print(absolute_sum(*list_of_numbers))
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.
def personal_numbers(name, *args):
    sum_numbers = 0
    for num in args:
        sum_numbers += num
    return f"{name}, the sum of your numbers is {sum_numbers}"

print(personal_numbers("Alice", 3, 7, 2, 8))
# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"