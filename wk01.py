""" Lecture 1:
CLI: Command line interface 
Use “python3” to run programs 
I.e python3 -c ‘print(“Hello”)’ #

Strings 
Python strings are unchangeable, i.e immutable 
Here's a program: 
"""

sentence = “My”
sentence = sentence + “name is” 
sentence += “ Pikachu”
print(sentence)
print(“Hi!!” * 10)

 # Control structures, argc/argv

import sys 
argc = len(sys.argv)

Empty = true 
if argc > 0:
	Empty = false
if not empty:
	If argc == 2:
		print(“Nearly there”)
	elif argc == 3:
		If sys.argv[1] == “H” and sys.argv[2] == “I”:
			print(“Hi to you too”)
		Else:
			pass 
else:
	print('Please enter two letters command line')
"""
List and loops:
Python lists are very complicated arrays under the hood. Lists are also mutable
names = [“Hayden”, “Rob”, “Isaac”]
names.append(“Vivian”);
"""
for names in names:	
	print(names)
print(“===”)

Names+= [“Eve”, “Mia”]
For i in range(0,len(names)):
	Print(names[i])
"""	
NOTE: The range() is a built-in function of Python which returns a range object, 
which is nothing but a sequence of integers

Tuples 
Lists and Tuples store one or more objects or values in a specific order. The objects stored in a list or tuple can be of any type including the nothing type defined by the None Keyword. 
Syntax is slightly different: Lists use square brackets, tuples use brackets. 
"""
list_num = [1,2,3,4]
tup_num = (1,2,3,4)

print(list_num)
print(tup_num) 
"""
[1,2,3,4]
(1,2,3,4)
"""

"""
Basic python testing: 
- pytest is a library that helps us write small tests, can
  be used to write more complex tests
- it detects any function prefixed with test and runs
  the function, processing the assertions 
"""
# test1_nopytest.py
def sum(x,y):
	return x*y
def test_sum1():
	assert sum(1,2) == 3
test_sum1()
# Run as: python3 test1_nopytest.py
# test1_pytest.py
import pytest 

def sum(x,y):
	return x*y
def test_sum1():
	assert sum(1,2) == 3, "1 + 2 == 3"
 """
Run as: pytest-3 test1_pytest.py
 """

 """
More complex: 

 """
 import pytest
 
def sum(x, y):
    return x + y
 
def test_small():
    assert sum(1, 2) == 3, "1, 2 == "
    assert sum(3, 5) == 8, "3, 5 == "
    assert sum(4, 9) == 13, "4, 9 == "
 
def test_small_negative():
    assert sum(-1, -2) == -3, "-1, -2 == "
    assert sum(-3, -5) == -8, "-3, -5 == "
    assert sum(-4, -9) == -13, "-4, -9 == "
 
def test_large():
    assert sum(84*52, 99*76) == 84*52 + 99*76, "84*52, 99*76 == "
    assert sum(23*98, 68*63) == 23*98 + 68*63, "23*98, 68*63 == "

"""
pytest - particular files
- We can run specific functions without your test files
  use the -k command, i.e running the following
test_small
test_small_negative
test_large x
 
We could run

$ pytest-3 -k small

or try

$ pytest-3 -k small -v
"""

"""
Pytest - markers
- We can use a range of decorators to specify tests in 
  python: 
"""

import pytest 

def pointchange (point, change):
	x, y = point
	x += change
	y += change
	return (x,y)

@pytest.fixture 
def supply_point():
	return (1,2)
@pytest.mark.up
def test1(supply_point):
	assert pointchange(supply_point, 1) == (2,3)

@pytest.mark.up
def test2(supply_point):
	assert pointchange(supply_point, 5) == (6,7)
@pytest.mark.up
def test3(supply_point):
	assert pointchange(supply_point, 100) == (101,102)
@pytest.mark.down 
def test4(supply_point):
	assert pointchange(supply_point, -5) == (-4,-3)
@pytest.mark.skip
def test5(supply_point):
	assert False == True, "This test is skipped"
@pytest.mark.xfail 
def test_6(supply_point):
	assert False == True, "This test's output is muted"
"""
Importing and modules: 
calmath.py and importto.py
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

def quickTest():
    print(f"month 0, day 0 = {daysIntoYear(0,0)}")
    print(f"month 11, day 31 = {daysIntoYear(11,31)}")

#if __name__ == '__main__':
#    quickTest()

quickTest()

import sys

import calmath

if len(sys.argv) != 3:
    print("Usage: importto.py month dayofmonth")
else:
    print(calmath.daysIntoYear(int(sys.argv[1]), \
                               int(sys.argv[2])))