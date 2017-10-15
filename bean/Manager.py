# -*-coding:utf-8 -*-
from Line import Line
from Station import Station
from Route import Route
from Step import Step
import sys
import copy

reload(sys)
sys.setdefaultencoding('utf8')


class Manager(object):
    stationMap = {}
    lineList = []

    def add_line(self, name, code, stationList):
        line = Line(name, code)
        self.lineList.append(line)

        prevStation = None
        nextStation = None

        stationObjectList = []
        routeObjectList = []

        for i, v in enumerate(stationList):
            name = v['station']
            if name in self.stationMap:
                station = self.stationMap[name]
            else:
                station = Station(name, 0, 0)
                self.stationMap[name] = station
            route = Route(line, prevStation, nextStation)
            prevStation = station
            stationObjectList.append(station)
            routeObjectList.append(route)

        length = len(stationObjectList)

        for i, route in enumerate(routeObjectList):
            if i != length - 1:
                route.nextStation = stationObjectList[i + 1]
                stationObjectList[i].add_routes(route)

    minStep = 0
    def find_ways(self, station1, station2):
        if station1 not in self.stationMap:
            return []
        if station2 not in self.stationMap:
            return []

        station1Object = self.stationMap[station1]
        station2Object = self.stationMap[station2]
        wayList = []
        self.minStep = 500
        self.find_station_ways(station1Object, station2Object, wayList, None, 0)
        return wayList

    @staticmethod
    def find_station_ways(station1, station2, wayList, way, step):
        if station1 == station2:
            return
        routes = station1.routes
        for i, route in enumerate(routes):
            Manager.handle_route(route, station2, wayList, way, step)

    @staticmethod
    def handle_route(route, station2, wayList, step, way):
        # todo 方向
        if route.prevStation is not None:
            step += 1
            stepO = Step(route.prevStation, route.line)

            if route.prevStation == station2:
                way.appendStep(stepO)
                Manager.minStep = min(step, Manager.minStep)
                wayList.append(way)
                return

            if step >= Manager.minStep:
                return

            newWay = copy.copy(way)
            newWay.appendStep(stepO)
            find


        else :


        if route.nextStation == station2:
            step = Step(route.nextStation, route.line)
            way.appendStep(step)
            return
        if route.prevStation
