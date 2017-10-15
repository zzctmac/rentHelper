class Route(object):
    def __init__(self, line, prev, nextS):
        self.line = line
        self.prevStation = prev
        self.nextStation = nextS

    def __str__(self):
        if self.prevStation is None:
            p = "null"
        else:
            p = self.prevStation.name

        if self.nextStation is None:
            n = "null"
        else:
            n = self.nextStation.name
        return "%s,%s,%s" % (self.line.name, p, n)
