"""
Wk02 lecture - 25/02/20 

- Project iteration 1 due in 13 days
- Python resources available now on webcms3
- Lab01/lab02 due this sunday
- Autotests only check if your pytest works
- 

Requirements 
Definition:
- Agreement of work to be completed by stakeholders 
- Descriptions and constraints of a proposed system
- 2 types: check guru99 Functional v Non-Functional
- Functional: what something should do, eg. background 
  colour for windows, 5" screen on phone, etc. (product
  feature)
- Non-functional: How something can achieve that, eg.
  Making sure the camera is able to be used for an hr 
  before battery dies. (more descriptive, constraint 
  of a system)
- In an exam, they will assess this in terms of general
  difference.

lab02 pass:
- pass does nothing, won't do anything

Requirements engineering:
A set of activities focused on identifying the purpose and 
goal of a software system, here are 4 steps
1) Elicitation - Questions and discovery
2) Analysis - building the picture
3) Specification - refining the picture
4) Validation - Go back and ensure 

Challenges in RE:
- Others are in a rush, they might not respect the process
- Conflicting ideas, lack of understanding
- Timing 
- Developers might not understand the subject domain
  i.e. might not understand the legal principles 
- XY problem: Jumping into details or solutions too early
- 

"""
"""
2.2 Dictionaries and exceptions:
Importing and modules: 
- 

"""
def daysIntoYear(month, day):
    total = day
    if month > 0:
        total += 31
    if month > 1:
        total += 28
    if month > 2:
        total += 31
    if month > 3:
        total += 30
    if month > 4:
        total += 31
    if month > 5:
        total += 30
    if month > 6:
        total += 31
    if month > 7:
        total += 30
    if month > 8:
        total += 31
    if month > 9:
        total += 30
    if month > 10:
        total += 31
    return total
""" 
Below is mostly just a print function, it calls the 
function 
- We also open importto.py, which imports sys and calmath
- 

"""
def quickTest():
    print(f"month 0, day 0 = {daysIntoYear(0,0)}")
    print(f"month 11, day 31 = {daysIntoYear(11,31)}")

#if __name__ == '__main__':
#    quickTest()

quickTest()
"""
- We print error if sys.argv != 3
- If we run the below program, we also run quicktest()
- The commented above code: __name__ is name of file 
  if we use import, otherwise __main__ if by orginal
  code
- If we run it NOT directly, via import, it will get to
  the point. i.e. above output = 56 if imported with 
  quicktest() commented out code
- from ____ import ____

"""
import sys

import calmath

if len(sys.argv) != 3:
    print("Usage: importto.py month dayofmonth")
else:
    print(calmath.daysIntoYear(int(sys.argv[1]), \
                               int(sys.argv[2])))

"""
Importing
"""
# auth.py 
def login():
	return 'token'

# auth_test.py
from stubs.auth import login 
def test_login1():
	assert login() == 'token'

"""
Python path:
- We need to make pytest work
  eg. if your project is in ~/cs1531/project use:
"""
export PYTHONPATH = "$PYTHONPATH:~/cs1531/project"
# python path = curr python path + more i.e append it 
"""
- add this line to your ~/.bashrc if you don't want to type 
  it in every time you open a terminal
  nano ~/.bash_profile
- profile = user account 
- we can use * for all function runs, instead of "login"
"""

"""
Python dictionaries:
- In python we use lists and dictionaries
- Lists are sequential containers, using an index with 
  ordered location
- Dictionaries have no sense of order, similar to structs
"""
#list.py
lst = {'p', 'r', 'o', 'b', 'e'}
print([lst[1], lst[2], lst[3]])
print(lst[1:4])
"""
Above does the same, doesnt include 4, if there is no 
number after n:, it goes forever, if there is no number
before :n, prints all
- We can also use negative index (end = -1, decreases
  to LHS)
"""
#dictionary.py
lst = {'p', 'r', 'o', 'b', 'e'}
studentData = {
	'name' : 'Hayden'
	'age' : 2,
	'height' : 8888, 
}
print(studentData)
print(stubs['name'])
# OR
studentData = {} # This is a dictionary
studentData['name'] = 'Hayden'
# Nested dictionary: You need to define ['name']
# as also a dictionary, if we intend on storing things

"""
Loops with dictionary:

"""

userData = {'name' : 'Sally','age' : 18, \
            'height' : '186cm'}
for user in userData:
	print(user)
print("====================")
# Above prints all the keys, we use it often
for user in userData.items():
    print(user)
print("====================")

for user in userData.keys():
    print(user)

print("====================")
for user in userData.values():
    print(user)

"""
Exceptions:
- An action that disrupts normal flow of a program
- Representative of errors being thrown
- We use exceptions to elegantly recover from errors 
- "stop right now, something happened, needa go back"
"""

import sys
# sqrt functiom
def sqrt(x):
    if x < 0:
        sys.stderr.write("Error Input < 0\n")
        sys.exit(1)
    return x**0.5

if __name__ == '__main__':
    print("Please enter a number: ",)
    inputNum = int(sys.stdin.readline())
    print(sqrt(inputNum))
"""
- if number < 0, says "error input < 0"
- we'd rather use a exception, stop executing functions
  till someone handles it. 
- We wanna handle the below exception to better handle it
"""
import sys

def sqrt(x):
    if x < 0:
        raise Exception(f"Error, sqrt input {x} < 0")
    return x**0.5

if __name__ == '__main__':
    print("Please enter a number: ",)
    inputNum = int(sys.stdin.readline())
    print(sqrt(inputNum))

"""
Inside the try, handle exception, like if statement
- 

"""
import sys

def sqrt(x):
    if x < 0:
        raise Exception(f"Error, sqrt input {x} < 0")
    return x**0.5

if __name__ == '__main__':
    try:
        print("Please enter a number: ",)
        inputNum = int(sys.stdin.readline())
        print(sqrt(inputNum))
    except Exception as e:
        print(f"Error when inputting! {e}. Please try again:")
        inputNum = int(sys.stdin.readline())
        print(sqrt(inputNum)) #throws exception, we can accept
"""
Make it more elegant below:
"""
import sys

def sqrt(x):
    if x < 0:
        raise Exception(f"Error, sqrt input {x} < 0")
    return x**0.5

if __name__ == '__main__':
    print("Please enter a number: ",)
    while True:
        try:
            inputNum = int(sys.stdin.readline())
            print(sqrt(inputNum)) # exception thrown 
            break
        except Exception as e:
            print(f"Error when inputting! {e}. Please try again:")
# We can keep entering numbers this way
"""
Our code should enter exceptions, i.e wrong email, ID, etc.

"""
import pytest

def sqrt(x):
    if x < 0:
        raise Exception(f"Input {x} is less than 0. Cannot sqrt a number < 0")
    return x**0.5

def test_sqrt_ok():
    assert sqrt(1) == 1
    assert sqrt(4) == 2
    assert sqrt(9) == 3
    assert sqrt(16) == 4

def test_sqrt_bad():
    with pytest.raises(Exception, match=r"*Cannot sqrt*"):
        sqrt(-1)
        sqrt(-2)
        sqrt(-3)
        sqrt(-4)
        sqrt(-5)
"""
we raise an exception above,then use pytest with -ve numbers
- We wanna get the correct behaviour
- Match is optional, just checks the message 
- We need to use this in our assignment 

"""
"""
Iteration 1 worth - 30%
- Mostly about testing

Creating pytests worth 40%

Good git practices worth 20%
- Tutor looks at git commits, branches and merge requests
  i.e. meaningful git commits
Project management 20%
- Talk about agile and slack
- Slack is an instant messaging platform/forum
Teamwork 10%
- Work effectively, talk, communication, etc. worth 10%
Assumptions and markdown files worth 10%
- Markdown is an easy language, i.e. here are the 
  assumptions made about the specification, are these 
  right?

Agile: 

auth_test.py
- this will get picked up by pytest
- don't change the functions in auth.py
"""
import pytest
from auth import register
def test_register():
	results = register('Hayden@unsw.edu.au', 'hayden123', 'hayden', 'smith')

def test_register_short_pw():
	with pytest.raises(InputError) as e:
	register('Hayden@unsw.edu.au', 'a', 'hayden', 'smith')

def test_register_valid_email():
	with pytest.raises(InputError) as e:
	register('Hayden', 'a', 'hayden', 'smith')

# Assume that register works 
def test_login():
	results1 = register('Hayden@unsw.edu.au', 'hayden123', 'hayden', 'smith')
	u_id = results1['u_id']
	token = results1['token']

	result2 = login('Hayden@unsw.edu.au', 'hayden123')
	u_id2 = results2['u_id']
	token2 = results['token']

	assert u_id1 == u_id2

def test_register_double():
	results1 = register('Hayden@unsw.edu.au', 'hayden123', 'hayden', 'smith')

	with pytest.raises(InputError) as e:
	# 'gobbles' it all up, i.e. waiting for an exception (e) to be thrown.
		register('Hayden@unsw.edu.au', 'a', 'hayden', 'smith')
"""		
def test_msg_send():
	results = register()
	channelInfo = channels_create(results['token'], 'Kool kids', False)
"""
"""
Agile: Philosophy, Practices, Processes, Cultural movement 
Its good for: Delivering software on time, changing 
requirements, your project and your resume. 

Agile Practices:
Standups: Frequent short progress update meetings, 
traditionally everyone stands up and answer 3 Q's
- What did I do?
- What problems did I face?
- What am i going to do?

Asynchronous standups 
Advantages: 
- No need to find suitable time for everyone
- May work better for big teams 
- Eg. slacks standup channel?
Disadvantages: 
- Easy to forget to forget to give updates 
- Less personal

Have a taskboard to upload tasks to do
"""
