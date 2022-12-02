# Ans Q1 - The purpose of Python's OOP is to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming.

# Ans Q2 - An inheritance search looks for an attribute first in the instance object, then in the class the instance was created from, 
#          then in all higher superclasses, progressing from left to right . The search stops at the first place the attribute is found.

# Ans Q3 - The basic concept of OOP is this: Class >> Object >> Instance. The class = the blue print. The Object is an actual thing that is built based on the 'blue print' (like the house). 
#          An instance is a virtual copy (but not a real copy) of the object.

# Ans Q4 - In object-oriented programming, whenever we define methods for a class, we use self as the first parameter in each case. And this Self argument is special because 
#          since the class is just a blueprint, self allows access to the attributes and methods of each object in python. This allows each object to have its own attributes and methods. 
#          Thus, even long before creating these objects, we reference the objects as self while defining the class.

# Ans Q5 - The __init__ method lets the class initialize the object's attributes and serves no other purpose.

# Ans Q6 - To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts.

# Ans Q7 - To create a class, use the keyword class: (Ex:- class MyClass:
#                                                            x = 5)

# Ans Q8 -  The class from which a class inherits is called the parent or superclass. A class which inherits from a superclass is called a subclass, also called heir class or child class. 
#           Superclasses are sometimes called ancestors as well. 

# Ans Q9 - module in python is simply a way to organize the code, and it contains either python classes or just functions. If you need those classes or functions in your project, you just import them. 
#          For instance, the math module in python contains just a bunch of functions, and you just call those needed one.

# Ans Q10 - same as Q7 and Q6.

# Ans Q11 - A class attribute is shared by all instances of the class. To define a class attribute, you place it outside of the __init__() method.
'''           Ex :- class Test:
                    x = 10
                    def __init__(self):
                        self.x = 20
                    
                    test = Test()
                    print(test.x)  # 20
                    print(Test.x)  # 10.     '''

# Ans Q12 - In the above Example the Test class has two attributes with the same name (x) one is the instance attribute and the other is a class attribute.  
#           When we access the x attribute via the instance of the Test class, it returns 20 which is the variable of the instance attribute.
#           However, when we access the x attribute via the Test class, it returns 10 which is the value of the x class attribute.

# Ans Q13 - The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

#Ans Q14 - Python class handle operator overloading by change the behavior of the existing operator through operator overloading, 
#          you have to redefine the special function that is invoked automatically when the operator is used with the objects.

# Ans Q15 - Operator overloading is mostly useful when you're making a new class that falls into an existing 
#           "Abstract Base Class" (ABC) -- indeed, many of the ABCs in standard library module collections rely on the presence of certain special methods (and special methods, 
#           one with names starting and ending with double underscores AKA "dunders", are exactly the way you perform operator overloading in Python).

# Ans Q16 - A very popular and convenient example is the Addition (+) operator. Just think how the '+' operator operates on two numbers and the same operator operates on two strings. 
#           It performs “Addition” on numbers whereas it performs “Concatenation” on strings.

# Ans Q17 - Both inheritance and polymorphism are fundamental concepts of object oriented programming. These concepts help us to create code that can be extended and easily maintainable.

# Ans Q18 - Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program
#           or system crashing, and without this process, exceptions would disrupt the normal operation of a program.Exceptions occur for numerous reasons, including invalid user input, 
#.          code errors, device failure, the loss of a network connection, insufficient memory to run an application, a memory conflict with another program, a program attempting to divide 
#           by zero or a user attempting to open files that are unavailable.

# Ans Q19 - When an exception occurred, if you don't handle it, the program terminates abruptly and the code past the line that caused the exception will not get executed.

# Ans Q20 - You can also provide a generic except clause, which handles any exception. After the except clause(s), you can include an else-clause. 
#           The code in the else-block executes if the code in the try: block does not raise an exception. The else-block is a good place for code that does not need the try: block's protection.

# Ans Q21 - The try-catch is the simplest method of handling exceptions. Put the code you want to run in the try block, and any Java exceptions that the code throws are caught by one or more catch blocks.
#           This method will catch any type of Python  exceptions that get thrown. This is the simplest mechanism for handling exceptions.

# Ans Q22 - Finally Statement in Python . Finally block always executes irrespective of an exception being thrown or not. The final keyword allows you to create a block of code that follows a try-catch block. 
#           Finally, clause is optional. It is intended to define clean-up actions which should be that executed in all conditions.

# Ans Q23 - The try statement allows you to define a block of code to be tested for errors while it is being executed. The catch statement allows you to define a block of code to be executed, if an error occurs in the try block.

# Ans Q24 - The Different Try/Except Variations. So far we've used a try / except and even a try / except / except , but this is only two-thirds of the story. There are two other optional segments to a try block: else and finally . 
#           Both of these optional blocks will come after the try and the except .

# Ans Q25 - Python raise Keyword is used to raise exceptions or errors. The raise keyword raises an error and stops the control flow of the program. It is used to bring up the current exception in an exception handler so that it can be handled further up the call stack.

# Ans Q26 - The assert keyword is used when debugging code. The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError. You can write a message to be written if the code returns False.

# Ans Q27 - The with statement is a replacement for commonly used try/finally error-handling statements. A common example of using the with statement is opening a file. To open and write to a file in Python.

# Ans Q28 - The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-key worded, variable-length argument list and *kwargs in function definitions in python is used to pass a keyworded, 
#           variable-length argument list. We use the name kwargs with the double star. The reason is that the double star allows us to pass through keyword arguments (and any number of them).

# Ans Q29 - Users can either pass their values or can pretend the function to use theirs default values which are specified. In this way, the user can call the function by either passing those optional parameters or just passing the required parameters. Without using keyword arguments. 

# Ans Q30 - A lambda function is a small anonymous function.A lambda function can take any number of arguments, but can only have one expression.

''' Ans Q31 - class Person(object):
                def __init__(self, name, id):
                self.name = name
                self.id = id
 
            def Display(self):
            print(self.name, self.id)
 
            emp = Person("Satyam", 102) # An Object of Person
            emp.Display()  '''

# Ans Q32 - It invoked version of class A . If ClassC is declared as ClassC(B, A) then the output  will be version of B. 

# Ans Q33 - Use isinstance() to check an instance's type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int .
#           Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int .

# Ans Q34- The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function. 
#          Use the keyword nonlocal to declare that the variable is not local.

# Ans Q35 - The global keyword is used to create global variables from a no-global scope, e.g. inside a function.