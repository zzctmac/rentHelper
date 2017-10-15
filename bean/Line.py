class Line(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_station(self, station):
        self.station = station

    def __str__(self):
        return "%s" % self.name
