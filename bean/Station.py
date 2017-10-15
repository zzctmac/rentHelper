class Station(object):

    def __init__(self, name,  latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.routes = []

    def __str__(self):
        return "%s" % self.name

    def get_name(self):
        return self.name

    def add_routes(self, route):
        self.routes.append(route)
