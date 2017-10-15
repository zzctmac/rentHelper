class Station(object):
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return "%s" % self.name


s = Station("111", 112, 56)

print s
