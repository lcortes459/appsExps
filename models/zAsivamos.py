# -*- coding: utf-8 -*-

def asivamosSucursales():
    dbSuc           = db.sucursales
    infoSuxcursales = db( dbSuc.sucursales_estado == True ).select()
    return infoSuxcursales