mySelf = {
'name':'My name is Clyde Drexler',
'age':'My age is 25',
'location':'My country of origin is Dubai, UN',
'language':'My favorite language is Python'
}

def print_dictionary_values(dic):
    for some_key, some_value in dic.iteritems():
        print "My" + " " + some_key + " " + "is" + " " + str(some_value)

        # alternate method:
        # concatenating variables to strings commonly done with the .format() method (can be used on any string, or variable that
            # contains a string

        #print "My {} is {}".format(some_key, some_value)
