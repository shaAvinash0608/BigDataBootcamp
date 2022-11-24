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

#Ans Q-51: Python frozenset() Method creates an immutable Set object from an iterable. It is a built-in Python function. 
#          As it is a set object therefore we cannot have duplicate values in the frozenset.

#Ans Q-52: Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time,
#          elements of the frozen set remain the same after creation. Due to this, frozen sets can be used as keys in Dictionary or as elements of another set.

#Ans Q-53: The union() method returns a set that contains all items from the original set, and all items from the specified set(s).
#          You can specify as many sets you want, separated by commas.It does not have to be a set, it can be any iterable object.
#          If an item is present in more than one set, the result will contain only one appearance of this item.
#   Ex:-   x = {"a", "b", "c"},  y = {"f", "d", "a"}, z = {"c", "d", "e"}
#          result = x.union(y, z)
#          print(result) => output: {'d', 'b', 'a', 'c', 'e', 'f'}

#Ans Q-54: The intersection() method returns a new set with elements that are common to all sets.
# Ex:-     A = {2, 3, 5},B = {1, 3, 5}
#          print(A.intersection(B)) =>  Output: {3, 5}

#Ans Q-55: Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#Ans Q-56: Dictionaries is different from the other data structure in the way like in all the other data structure element are not in form of Key and value pair 
#          there only single type element but in dictionary there are set of keys with their value.

#Ans Q-57: We can declare the dictionary by simply (myDict = {}) or we can also use dict() constructor to declare dictionary.

#Ans Q-58: <class 'dict'>

#Ans Q-59: Adding an item to the dictionary is done by using a new index key and assigning a value to it. myDict["color"] = "red".

#Ans Q-60: car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
#}
#x = car.values()
#print(x)

#Ans Q-61: people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
#                    2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
#for p_id, p_info in people.items():
#    print("\nPerson ID:", p_id)
#    for key in p_info:
#        print(key + ':', p_info[key])

#Ans Q-62: The get() method returns the value of the item with the specified key.

#Ans Q-63: In Python Dictionary, items() method is used to return the list with all dictionary keys with values. 

#Ans Q-64: List pop in Python is a pre-defined, in-built function that removes an item at the specified index from the list.
#          You can also use pop in Python without mentioning the index value. In such cases, the pop() function will remove the last element of the list.

#Ans Q-65: The popitem() method removes the item that was last inserted into the dictionary. In versions before 3.7, the popitem() method removes a random item. 
#          The removed item is the return value of the popitem() method, as a tuple.

#Ans Q-66: The keys() method in Python Dictionary, returns a view object that displays a list of all the keys in the dictionary in order of insertion using Python. 
#          Parameters: There are no parameters. Returns: A view object is returned that displays all the keys.

#Ans Q-67: values() is an inbuilt method in Python programming language that returns a view object. The view object contains the values of the dictionary, as a list. 
#          If you use the type() method on the return value, you get “dict_values object”. It must be cast to obtain the actual list.

#Ans Q-68: Looping means repeating something over and over until a particular condition is satisfied. A for loop in Python is a control flow statement 
#          that is used to repeatedly execute a group of statements as long as the condition is satisfied. Such a type of statement is also known as an iterative statement.

#Ans Q-69: while Loop for Loop nested Loop.

#Ans Q-70: For loop is used when the number of iterations is already known. While loop is used when the number of iterations is already Unknown. 
#          In the while loop, it can be repeated at every iteration. To iterate, the range or xrange function is used.

#Ans Q-71: The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.

#Ans Q-72: 'Break' in Python is a loop control statement. It is used to control the sequence of the loop.
#           Suppose you want to terminate a loop and skip to the next code after the loop; break will help you do that. A typical scenario of using the Break in Python is when an external condition triggers the loop's termination.

#Ans Q-73: The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. 
#          Empty code is not allowed in loops, function definitions, class definitions, or in if statements.

#Ans Q-74: The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

#Ans Q-75: You can loop through a dictionary by using a for loop. When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
#          Loop through both keys and values, by using the items() function.