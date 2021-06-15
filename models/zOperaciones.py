# -*- coding: utf-8 -*-
import pandas as pd
import xlrd,os,subprocess
import numpy as np

def estructuracionBase( idBase ):
    print('idBase', idBase)
    datos    = db( db.bases.id == idBase ).select( db.bases.bases_base,db.bases.bases_asignacion ).last()
    if datos:
        #print('datos', datos)
        dest_filename = os.path.join(request.folder, 'uploads', datos.bases_base)
        #print('dest_filename', dest_filename)
        dfOri        = pd.read_excel(dest_filename)
        resul        = 0
        for index, row in dfOri.iterrows():
            #print('row', row)
            if 'NOMBRE_PRINCIPAL' in row:
                idRegistro = db.asignacion_piscina.insert(
                    asignacion_piscina_identificacion  = '',
                    asignacion_piscina_nombres         = row['NOMBRE_PRINCIPAL'],
                    asignacion_piscina_telefono        = row['TELEFONO_PRINCIPAL_1'],
                    asignacion_piscina_valor           = row['CUPO APROBADO'],
                    asignacion_piscina_cuidad          = row['CIUDAD_PRINCIPAL'],
                    asignacion_piscina_interes         = row['TASA'],
                    asignacion_piscina_cuotas          = row['PLAZO'],
                    asignacion_piscina_oficina         = row['ID_PRINCIPAL'],
                    asignacion_piscina_idBase          = idBase,
                    asignacion_piscina_idAsignacion    = datos.bases_asignacion
                )
                resul = 1
                print('resul1',resul)
            else:
                print('resul0',resul)
                pass
            pass
        if resul == 0:
            db( db.bases.id == idBase ).update( bases_estado = 'Error columnas' )
        else:
            db( db.bases.id == idBase ).update( bases_estado = 'Finalizada' )
            pass
    else:
        print('Paila idRegistro base no encontrado')
        pass
    resul = 0
    pass



def countAsesorPiscina():
    dbPisAsig    = db.asignacion_piscina
    asigCount    = db( dbPisAsig.asignacion_piscina_estado == True ).select( dbPisAsig.id )
    if asigCount:
        resul = len(asigCount)
    else:
        resul = 0
        pass
    return resul


def getAsesorPiscina():
    dbPisAsig    = db.asignacion_piscina
    asigCount    = db( dbPisAsig.asignacion_piscina_estado == True ).select( dbPisAsig.id).first()
    if asigCount:
        resul = asigCount.id
        db( dbPisAsig.id == asigCount.id ).update( asignacion_piscina_estado = False)
    else:
        resul = 0
        pass
    return resul


def setAsesorPiscina( idRegistro ):
    dbPisAsig    = db.asignacion_piscina
    dbAsePisc    = db.asesor_piscina
    dbAsePisc.insert(
        asesor_piscina_piscina  = idRegistro,
        asesor_piscina_usuario  = idUser
    )
    asigCount    = db( dbPisAsig.id == idRegistro ).select( dbPisAsig.ALL )
    return asigCount



