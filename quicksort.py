import json
from pprint import pprint
#import data from json file(Student.json)
with open('student.json') as Tosort_file:
    data = json.load(Tosort_file)
#print out data
pprint(data)
#sort the imported, i have sorted using reversed but still i can revert.
for k in reversed(sorted(data)):
    #print the first_name in reverse
    print k["first_name"]


