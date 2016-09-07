from collections import OrderedDict
yourstring = raw_input("Enter yourstring: ")
print "".join(OrderedDict.fromkeys(yourstring))