#Q.1 - Ans : Phython is called as general-purpose programming language because it is the one that’s usable for solving a very wide range of different kinds of problems.
#            Phython is called high-level programming language because it is an object-oriented, high-level programming language. Object-oriented means this language 
#            is based around objects (such as data) rather than functions, and high-level means it's easy for humans to understand.


#Q.2 - Ans : Phython is called as dynamically typed language because It doesn’t know about the type of the variable until the code is run. So declaration is of no use. 
#            What it does is, It stores that value at some memory location and then binds that variable name to that memory container. And makes the contents of the  
#            container accessible through that variable name. So the data type does not matter. As it will get to know the type of the value at run-time.


#Q.3 - Ans : Pros
#            1.It's Simple.
#            2.It's Free.
#            3.It's Easy to Use.
#            4.It's Highly Compatible.
#            5.It is Object-Oriented.
#            Cons
#           1.Poor Memory Efficiency.
#           2.Slow Speed.
#           3.Database Access.
#           4.Weak in Mobile Computing.
#           5.Runtime Errors.


#Q.4 - Ans :Python is the go-to programming language for domains such as artificial intelligence, machine learning and deep learning.


#Q.5 - Ans :Variables are the basic unit of storage in any programming language. These variables consist of a data type, the variable name, and the value to be assigned to the variable.
#           Unless and until the variables are declared and initialized, they cannot be used in the program.Ex:-num=10(Here 'num' is Variable)
             

#Q.6 - Ans :In python we take input from user using input() function.Ex:-val = input("Enter your value: ").


#Q.7 -Ans :Default datatype of the value that has been taken as an input using input() function is STRING.

#Q.8 -Ans :Type Casting is the method to convert the variable data type into a certain data type in order to the operation required to be performed by users.

#Q.9 -Ans :Yes we can take more than one input from the user using single input() function by using  two methods.
#     Using split() method(Syntex-input().split(separator, maxsplit))
#     Using List comprehension.

#Q.10 -Ans :In all languages there are special reserved words that have specific meanings and purposes and can't be used for anything but those specific purposes
#           These resrved words are called Keywords.


#Q.11 -Ans: No because keywords are used to define the syntax of the coding. The keyword cannot be used as an identifier, function, and variable name. 
#           All the keywords in python are written in lower case except True and False.

#Q.12 -Ans : Indentation is a very important concept of Python because without properly indenting the Python code, you will end up seeing IndentationError 
#            and the code will not get compiled.
#            Python indentation refers to adding white space before a statement to a particular block of code. In another word, all the statements with the 
#            same space to the right, belong to the same code block.

#Q.13 -Ans: we throw some output in Python by using print() function. Ex-(print('Hello world')).

#Q.14 - Ans: In Python, operators are special symbols that designate that some sort of computation should be performed. The values that an operator acts on are called operands.
#            Ex- +,-,*,>,<,= and /....


#Q.15 - Ans: In Python programming, you can perform division in two ways. The first one is Float Division("/") and the second is Integer Division("//") or Floor Division.
#            Float Division("/"): Divides left hand operand by right hand operand.

#Q.16 - Ans: str = 'iNeuron'
#            print(str*3)

#Q.17 - Ans : num = int (input (“Enter any number to test whether it is odd or even: “)
#             if (num % 2) == 0:
#             print (“The number is even”)
#             else:
#             print (“The provided number is odd”)


#Q.18 - Ans: Boolean Operators are simple words (AND, OR, NOT or AND NOT) used as conjunctions to combine or exclude keywords in a search, resulting in more focused and productive results.


#Q.19 - Ans : 1 or 0 =>  1.

#             0 and 0 => 0.

#             True and False and True => False.

#             1 or 0 or 0 => 1.


#Q.20 - Ans : A conditional statement as the name suggests itself, is used to handle conditions in your program. These statements guide the program while making decisions based on the 
#              conditions encountered by the program. Python has 3 key Conditional Statements that you should know: if statement. if-else statement.else statement.


#Q.21 -Ans : Python if...elif...else Statement. It allows us to check for multiple expressions. If the condition for if is False , it checks the condition of the next elif block and so on. 
#            If all the conditions are False , the body of else is executed.


#Q.22 -Ans : age = input("Enter your age")
#            if(age>=18):
#                    print(""I can vote"")
#            else:
#                    print("I can't vote")


#Q.23 -Ans : numbers = [12, 75, 150, 180, 145, 525, 50]
#            sum = 0
#            for no in numbers:
#                  if(no%2):
#                       sum += no
#            print(sum)


#Q.24 -Ans : num1 = float(input("Enter first number: "))
#            num2 = float(input("Enter second number: "))
#            num3 = float(input("Enter third number: "))

#            if (num1 >= num2) and (num1 >= num3):
#                 largest = num1
#            elif (num2 >= num1) and (num2 >= num3):
#                 largest = num2
#            else:
#                 largest = num3
#            print("The largest number is", largest)


#Q.25 -Ans : numbers = [12, 75, 150, 180, 145, 525, 50]
#            for no in numbers:
#               if(no%5==0):
#                   if(no>500):
#                       break
#                   else:
#                       if(no<150):
#                           print(no)
