length = int(input('Please input the length of the room in meters'))
width =  int(input('Please enter the width of the room in meters'))

totalarea = length*width

cost = int(input('Please input the cost per sq metre for the tile'))

totalcost = cost*totalarea

print('The total cost was {} dollars'.format(totalcost))