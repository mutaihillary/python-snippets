"""
Given 50 randomly located drivers, map them to some random number of randomly located jobs such that
total distance to jobs is minimised. With 100 jobs available, map the driver ids and job location ids
and print out the result in a key value pair

This snippet will efficiently work with a specified number of job ids whereby each location is treated as a
location id. I.e. while running on an app, the job locations available as by customer needs will be used to
compute their distances to the closest driver, also given the number of drivers.

driver range = 50
job number = randomly located(generated) for mapping in range 1 - 50

Pseudocode:

first loops through all the driver ids.
A new list is created for all the driver ids where they are stored
Then Generates a random job location id in the range 1-50 for the 50 drivers.
The job location ids are stored in another seperate list
Checks whether the  driver ids and random job locations are in range
A dictionary is then created to map each driver to the closest location and
finally printed out to the console.
"""

from random import randint

for id in range(1,51):
    id_list = []
    id_list.append(id)
    j_location = randint(1,51)
    location_list = []
    location_list.append(j_location)
    #print location_list
    if id >= j_location <=51:
            #item_list.append(id)
            #print item_list
        list = dict(zip(id_list,location_list))
        print list
        #this list contain all list of all drivers and location closest to each other



