# Ans Q-26: strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string. we declare string as a = "Hello, World!".

# Ans Q-27: a = "Hello, World!" we can access this string using index as like a[i] where i is from 0 to length of string - 1.

# Ans Q-28: string = "Big Data iNeuron"  
#           we get the desired output by running the code (print(string[9:])).

# Ans Q-29: string = "Big Data iNeuron"
#           we get the desired output by running the code (print(string[-1:-8:-1])).

# Ans Q-30: we get the desired output by running the code (print(string[::-1])).

# Ans Q-31: you can remove the entire string variable using the del command.

#Ans Q-32: An escape sequence is a sequence of characters that, when used inside a character or string, does not represent itself but is converted into another character or series of characters.
#          Ex:- \n-newline.

#Ans Q-33:  we get the desired output by running the code (string = "iNeuron's Big Data Course"
#                                                           print(string)).

#Ans Q-34: List. Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

#Ans Q-35: we can create list by simply writing this line of command (myList = []).

#Ans Q-36: we can access the element of list by indexing method.

#Ans Q-37: lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
#          print(lst[4][2]).

#Ans Q-38: lst = []
  
# number of elements as input
# n = int(input("Enter number of elements : "))
# iterating till the range
# for i in range(0, n):
#    ele = int(input())
#    lst.append(ele) # adding the element   
#print(lst)

#Ans Q-39: lst = ["Welcome", "to", "Data", "course"]
#           lst[2] = "Big"+lst[2]
#           print(lst)

#Ans Q-40:A tuple is a collection of objects which ordered and immutable. Tuples are sequences, just like lists.
# The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

#Ans Q-41:you can create a tuple by using parentheses in Python.

#Ans Q-42: No i can not able to add my name in tupple because tuple is immutable we can not perform addition and deletion action.

#Ans Q-43: You can combine tuples to form a new tuple. The addition operation simply performs a concatenation with tuples.
#           x = (1,2,3,4)
#           y = (5,6,7,8)
#           z = x + y 
#           print(z)

#Ans Q-44: vowels = ('a', 'e', 'i', 'o', 'i', 'u')
#          count = vowels.count('i')
#          print(count)

#Ans Q-45: Sets are used to store multiple items in a single variable. A set is a collection which is unordered, unchangeable*, and unindexed.
#          Set items are unchangeable, but you can remove items and add new items.

#Ans Q-46: we can create set by this command (mySet = {}).

#Ans Q-47: mySet = set()
#          mySet.add("iNeuron")
#          print(mySet)

#Ans Q-48:s = {'g', 'e', 'e', 'k', 's'}
#         t = ('f', 'o')
#         s.add(t).

#Ans Q-49:. add() is intended for a single element , while . update() is for the introduction of other sets.

#Ans Q-50:The clear() method removes all elements in a set.