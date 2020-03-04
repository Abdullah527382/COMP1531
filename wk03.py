"""
3/03/2020 wk03 
3.1) Python objects:
Basic stuff only: 
- Eveything is an object which is similar to a struct 
- python string pythondocs (google search)/string methods
  shows:
  > string is an object 
  > we can use . property to access properties, i.e .count
  > objects are related to classes


"""
name = "Ian Jacobs"
print(name.count('J')) # --> 1 
print(name.capitalize()) # --> Ian jacobs
print(name.isdigit()) # checks if string is digit
print(name.swapcase()) # 

"""
Another example
- use dates in python (important library)
"""
from datetime import datetime
from math import floor
# Call the date function, today is an object, 
# as are others, they will have properties/methods
today = date(2020, 03, 3, 16, 5)
name = 'Ian Jacobs'
num = 1

timenow = datetime.now()
"""datetime is a class object which has a 
   now function which tells exact correct time
  'date' is its own type """
print(type(today))
print(type(name))
print(type(num))
diff = timenow - today
minutes = diff.total_seconds()/60
print(floor(minutes))


# Attributes/properties of 'today'
# Very similar to structs
print(today.year)
print(today.month)
print(today.day)

# Methods of 'today'
# we call functions on the objects: 
print(today.weekday()) # 0-->6
print(today.ctime())
# string representation of variables in object
"""
3.2) Verification and validation: 
Write code for people (duh)
Pylinting 
> External tool for statically analysing python code
> Can detect errors, warns of potential errors
> Is very strict, can be configured to be more lenient

consider some program: exception1.py, run pylint3 as: 
pylint3 exception1.py
* This will give us a rating out of 10
- pylint is just a bunch of rules, we can configure by 
changing these rules 
We can make it more lenient as: 
> Disable messages via cmd line 
    $ pylint3 --disable=missing-docstring <files>
> If a .pylintrc file is in the current directory it 
 will be used:
    $ pylint3 <options> --generate-rcfile > .pylintrc
--> Put a comment: #pylint disable=no-else-return (eg.)
 

"""

"""
Fixture example: 
"""
import pytest
from auth import auth_register
from channels import channels_create
from message import message_send
from error import InputError

@pytest.fixture # decorator
def get_new_user():
    data = auth_register('hayden.smith@unsw.edu.au', '123!@#asd', 'Hayden', 'Smith')
    return (data['u_id'], data['token'])

def test_message_send(get_new_user):
    u_id, token = get_new_user
    data = channels_create(token, 'my channel', False)
    with pytest.raises(InputError) as e:
        message_send(token, data['channel_id'], 'Hello there' * 1001)

def test_channels_create(get_new_user):
    u_id, token = get_new_user
    data = channels_create(token, 'my channel', False)

"""
Managing data: 
Activity: Use the data in 
https://www.cse.unsw.edu.au/~cs1531/20T1/weatherAUS.csv 
to write a python program to determine the location with 
the most rain over the last years
How? 
> search python csv 

consider sunshine.py: 
> we copied below program from online
> editing it to get some hints 
"""
import csv

with open('./weatherAUS.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    locationInfo = {} 
    for row in csv_reader:

    	line_count += 1
    	if line_count > 1:

	    	location = row[1]
	    	print(location)
	    	# if row[4] == 'NA' i.e exception
	    	try: 
	    		rainfall = float(row[4])

	    	except valueError:
	    		rainfall = 0

	    	if location not in locationInfo:
	    		locationInfo[location] = 0

	    	locationInfo[location] += rainfall 


	    	locationSummary = []
	    	for locationTuple in locationInfo.items():
	    		locationSummary.append(locationTuple)
	    # print out the list
	    for location.rainfall in locationSummary:
	    	print(f '{location}: {round(rainfall)')
	   	print(locationSummary)

"""
4/03/2020 - Verification:
Formal verification: 
- Proving via maths that a piece of software has certain 
  desirable properties
- Treats software, algorithms implemented in software as 
  math object 
- Not something covered in this course 

Unit testing:

- The testing of individual software components
- Blackbox tests: Don't know how functions work, we're
  only caring about input and output. We can write 
  tests before creating actual code

- White box testing example: We dig ino the details of 
  the function and write tests accordingly
  Unit testing IS whitebox testing eg. testing sqrt()
  function, if it has that particular output

- What we are doing right now is Integration testing 
  (checking for any defects in interfaces and interactions
  between components or systems) --> more often blackbox than
  whitebox (method)

- System testing: The process of testing an integrated 
  system to verify that it meets specified requirements.
- How to write good tests:
Coverage : 
- Test coverage: 
  How much feature set is covered with tests
- Code coverage: 
  How much doe is executed in tests
  eg. code below
- Coverage.py:
  - Measure code coverage as a percentage of statements 
   (lines) executed
  - Can give us a good indication how much of our code is 
   executed by the tests
  - and most importantly highlight what has not been executed.
"""

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

from leapyear import is_leap_year

def test_four():
  assert is_leap_year(2020) == True 
  assert is_leap_year(2024) == True 
  assert is_leap_year(2028) == True 
  assert is_leap_year(2032) == True 

# Note: we can also use loops, but that gets complex
"""
Checking code coverage:
   python3-coverage run --source=. -m pytest
View the coverage report:
   python3-coverage report
*You can also generate html to see breakdown: 
   python3-coverage html
--> puts eport in htmlcov/
Note: --source = current folder, -m = run pytest, also
A code coverage tool looks at what pytest checks (pytest
runs the program), 

""" 