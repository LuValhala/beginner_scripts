# -*- coding: utf-8 -*-
#základné operácie s vektormi 

import math

class cVec3:
    def __init__(self, inx, iny, inz = None):
        if inz == None and (inx <= 90. and inx >= -90. and -180. <= iny and 180. >= iny):
            self._fi = math.radians(inx)
            self._lbd = math.radians(iny)
            self._ro = 1.0
            self._x = math.cos(self._fi) * math.cos(self._lbd)
            self._y = math.cos(self._fi) * math.sin(self._lbd)
            self._z = math.sin(self._fi)
        else:
            self._x, self._y, self._z = float(inx), float(iny), float(inz)
            self._ro = math.sqrt(inx ** 2 + iny ** 2 + inz ** 2)
            if self._ro > 0:
                self._fi = math.asin(self._z / self._ro)
                if self._y < 0:
                    self._lbd = -math.acos(self._x / (math.cos(self._fi) * self._ro))
                else:
                    self._lbd = math.acos(self._x / (math.cos(self._fi) * self._ro))
    # normovanie vektora
    def norm(self):
        self._x = math.cos(self._fi) * math.cos(self._lbd)
        self._y = math.cos(self._fi) * math.sin(self._lbd)
        self._z = math.sin(self._fi)
        self._ro = 1.
    # súčet vektorov
    def __add__(self, azr): 
        return(cVec3(self._x + azr._x, self._y + azr._y, self._z + azr._z))
    # rozdiel vektorov
    def __sub__(self, azr): 
        return(cVec3(self._x - azr._x, self._y - azr._y, self._z - azr._z))
    # opačný vektor
    def __neg__(self): 
        return(cVec3(-self._x, -self._y, -self._z))
    # skalárny súčin
    def skalSuc(self, azr):
        return(self._x * azr._x + self._y * azr._y + self._z * azr._z)
    # súčin s číslom, vektorom
    def __mul__(self, azr):
        if isinstance(azr, float):
            return(cVec3(self._x * azr, self._y * azr, self._z * azr))
        elif isinstance(azr, int):
            return(cVec3(self._x * float(azr), self._y * float(azr), self._z * float(azr)))
        return(cVec3(self._y * azr._z - self._z * azr._y,\
                     self._z * azr._x - self._x * azr._z,\
                     self._x * azr._y - self._y * azr._x))
    def setFormat(self, b):
        cVec3._euklid = bool(b)
        
    # prevod na reťazec
    def __str__(self):
        if self._euklid:
            return('({:.5f}, {:.5f}, {:.5f})'.format(self._x, self._y, self._z))
        else:
            return('({:.5f}°, {:.5f}°, {:.5f})'.format(math.degrees(self._fi), math.degrees(self._lbd), self._ro))
    def __abs__(self):
        return(math.sqrt(self._x ** 2 + self._y ** 2 + self._z ** 2))
