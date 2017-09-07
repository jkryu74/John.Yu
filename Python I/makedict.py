name = ['Le','Fe','Au','Ag','He','Co']
nameList = ['Leo','Fey','Austin','Agatha','Henry','Collin']

def make_dict(x, y):
    new_dict = {}
    for idx in range(len(x)):
        new_dict[x[idx]] = y[idx]
    print new_dict

make_dict(name, nameList)
