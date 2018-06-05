import math

def distance(origin,destination):

    lat1,lon1 = origin
    lat2,lon2 = destination
    radius = 6371

    dlat = math.radians(lat1-lat2)
    dlon = math.radians(lon1-lon2)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    d = radius*c
    return str(d)

origin2 = (48.1372,11.5756) #Berlin
destination2 = (52.5186,13.4083) #Munich

print('The distance between the two points is ' + distance(origin2,destination2) + ' km')

def takeuserinput():
   

takeuserinput()