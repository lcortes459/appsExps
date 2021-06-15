# -*- coding: utf-8 -*-
from datetime import datetime, time, date
import time
diaMes    = fechaIntergar('dia') 
mesAnio   = fechaIntergar('mes')
anioCurso = fechaIntergar('anio')
fechaIntModels  = int(str(request.now)[:10].replace('-',''))
horaIntTmp   = int(str(time.strftime("%H:%M:%S")).replace(':',''))
if str(horaIntTmp)[:2] == '00':
    horaIntModels = horaIntTmp.replace('00','24')
else:
    horaIntModels = horaIntTmp
    pass

def asivamosSucursales():
    dbSuc           = db.sucursales
    infoSuxcursales = db( dbSuc.sucursales_estado == True ).select()
    return infoSuxcursales



def asivamosAsignaciones():
    infoAsigList     = []
    dbAsig           = db.asignaciones
    dbPisAsig        = db.asignacion_piscina
    infoAsignacones  = db( dbAsig.asignaciones_estado == True ).select( dbAsig.id,dbAsig.asignaciones_nombre )
    valAsignado      = 0
    for x_val in infoAsignacones:
        asignados    = db( dbPisAsig.asignacion_piscina_idAsignacion == x_val.id ).select( dbPisAsig.asignacion_piscina_valor,dbPisAsig.asignacion_piscina_telefono,distinct=True)
        asigCount    = db( dbPisAsig.asignacion_piscina_idAsignacion == x_val.id ).select( dbPisAsig.asignacion_piscina_telefono,distinct=True)
        for x_valor in asignados:
            valAsignado  = float(x_valor.asignacion_piscina_valor) +  valAsignado
            pass
        infoAsigList.append(
            dict(
                idAsignacion  = x_val.id,
                nomAsignacion = x_val.asignaciones_nombre,
                valAsignadoAs = SetMoneda(valAsignado),
                cantAsign     = len(asigCount)
            )
        )
        pass
    return infoAsigList

