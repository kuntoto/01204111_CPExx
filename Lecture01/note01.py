'''
Lecture01 Python Basics
''' 

## 1: What's programming?
'''
  Programming is simply the act of entering instructions for the computer to follow and perform.
  - do this; then do that
  - if this condition is True, perform this action; otherwise (else) do that action
  - do this action exactly 27 times
  - if this condition is still True, keep doing this action 
''' 

## 2: What's source code?
'''
  A simple program written in the Python prgramming laguage.
  Python will interpret and understand those lines of code, and execute the instruction from the 1st line till the bottom.
'''

## 3: Programmers do not need to know much Math
'''
  I, Toto, do not quite agree with the author, since good knowledge in Mathematics will let you have good logic reasoning and problem solving skill that used in programming too.
  However, from the Sodoku example, the author specially show that Math such as Calculas, Trigonometry, etc. does not need in strategics game like Sodoku in which you have to follow some rules to put the numbers in row and column wise. 
  By the way, I believe that we will guide you thoroughly this 111 course till you can write a Python program to solve a simple Sodoku board. ;D
'''

## 4: What does REPL mean?
'''
  To let Python understand what we, programmer, need the computer to do, the command or instuction we put into the Python shell (ie., after the >>> sign prompt) need to be first [R]ead, then [E]valuate, and then [P]rint the result of that instruction to screen before [L]oop back to REPL again and again.
'''

## 5: What kind of expression can we enter into the Python shell to be evaluated?
'''
  Expression in Python could be:
  - constant value such as 2, 3.5, "Hello, World", None, True, (6,7),..
  - arithmetic expression with precedance (..), **, * / // %, + -
  - boolean expression (will cover this later)
  - function
  - mix between the above.. 
'''

## 6: What's arithmatic expression?
'''
  Expression that use these operators;
  ** such as 2**3 will evaluate to 8
  %  such as 22%8 will evaluate to 6
  // such as 22//8 will evaluate to 2
  /  such as 22/8 will evaluate to 2.75
  *  such as 3*5 will evaluate to 15
  +  such as 5+2 will evaluate to 7
  -  such as 5-2 will evaluate to 3
  Note that the order of operations (also called precedance) is important. The ** operator is evaluated first; the *, /, //, and % operators are evaluated next, from left to right; and the + and - operators are evaluated last (also from left to right). You can use parentheses to override the usual precedence if you need to.

  Your exercises:
  >>> 2 + 3 * 6
  >>> (2 + 3) * 6
  >>> 2**10
  >>> 22/7
  >>> 22%7
  >>> (5-1) * ((7+1) / (3-1))
  >>> 42 + 5 + * 2 # Explain what does happen?
''' 

## 7: Could you give sample values of integer, float, string, and Boolean data types?
'''
  Here are some sample data values.
    integer: -2, -1, 0, 1, 2, 3, 4, 5
    float: -1.25, -1., -0.5, 0.0, 0.5, 1., 2.25
    string: 'Hello', "World!", "7/11", '',    '\"Twenty-century\"'
    Boolean: True, False (Both are reserved words.)
  Note here that '' or "" called empty or null string.

  You have can use type() function, such as
    >>> type(1)
    <class 'int'>
    >>> type(True)
    <class 'bool'>
    >>> type(2/3)
    <class 'float'>

  When you evalute >>> 'Hello World PRESS_ENTER
  you will get a SybtaxError throw out since Python has never find the second single quote to delimit the "Hello World" string.
'''

## 8: What are string concatination and replication?
'''
  When one of the operands of the operator + is a string, Python will evaluate another operand whether it is also a string, and then collate (or concatenate) that two strings together.
  >>> 'Hello' + " World"
  'Hello World' 

  When one of the operands of the operator * is a string, and another is an integer N, string concatination of that string will occur. This mean, that string will replicate itself N times and collate one after another.
  >>> 'Hello' * 3
  'HelloHelloHello'
'''

### 9: How to store a value in a vaiable?
'''
  A variable is like a box in the computer’s memory where you can store a single value.
  
  We can store a value in a variable through assignment operator = using the assignment statement.

  VARNAME = EXPRESSION

  Left operand of the assignment operator is always the varible name or identifier. Right operand should be expression (that we have already explained and given examples).

  Variable identifier could begin with under-score _ or letter, and follow with _ or letter or number. Sample of good identifier are CurrentBalance, TOTAL_SUM, myName, _my_salary, VAR1, etc. 
  Variable identifiers are case-sensitive, meaning that spam, SPAM, Spam, and sPaM are four different variables.

  Variables written in Camel case style: rocketSpeed runningTime, timeConsume, minSpendEachDay

'''

### 10: Let try our first Python program today!
# This program says hello...
print('Hello, World')
myName = input('What is your name: ')
print('It\'s good to meet you, ' + myName)
print('Length of your name is: ', len(myName))
myAge = input('What\'s your age: ')
print('You\'ll be ' + str(int(myAge)+1) + ' in a year.')

### May the force of Universe be with you ###
