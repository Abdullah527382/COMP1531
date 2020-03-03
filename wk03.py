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
	    	print(f"{location}: {round(rainfall}")
	   	print(locationSummary)