#List of favorite fruits
favorite_fruits = ["Mango", "Grapes", "Pineapple", "Apple", "Liche"]


#List of colors
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(colors[0])# First color
print(colors[2])# Third color
print(colors[-1])# Last color


#List of numbers
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
#Adding 60 to the end 
numbers.append(60)
print(numbers)


#list of names
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
#list containing the first three names
subset = names[:3]
print(subset)


#List of numbers from 1 to 10
numbers = list(range(1, 11))
#Loop through the list and print each number squared
for number in numbers:
    print(number ** 2)


shopping_cart = [] 
#items using append()
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs')
#more items using extend()
shopping_cart.extend(['butter', 'cheese'])
print(shopping_cart)


numbers = [45, 22, 88, 56, 92, 33]
#maximum and minimum values
max_value = max(numbers)
min_value = min(numbers)
#Print the results
print("Maximum value:", max_value)
print("Minimum value:", min_value)


#List of letters
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
#how many times 'a' appears in the list
count_a = letters.count('a')
#Print the result
print("The letter'a'appears", count_a,"times.")


#creating a list
list = [1,2,3,4,5,6,7,8,9,10]
square_list = [list **2 for list in list if list % 2 == 0]


nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
#Remove duplicates by converting the list to a set
unique_nums = list(set(nums))
#Print the unique elements
print(unique_nums)