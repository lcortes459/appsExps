# -*- coding: utf-8 -*-
import pandas as pd
import xlrd,os,subprocess
import numpy as np

def estructuracionBase( idBase ):
    print('idBase', idBase)
    datos    = db( db.bases.id == idBase ).select( db.bases.bases_base,db.bases.bases_asignacion,db.bases.base_segmento ).last()
    if datos:
        #print('datos', datos)
        dest_filename = os.path.join(request.folder, 'uploads', datos.bases_base)
        #print('dest_filename', dest_filename)
        dfOri        = pd.read_excel(dest_filename)
        resul        = 0
        print('dfOri',dfOri.head())
        if datos.base_segmento == 'Libre inversión':
            dfOri.drop_duplicates(subset=['ID_PRINCIPAL','TELEFONO_PRINCIPAL_1'],inplace=True)
        else:
            dfOri.drop_duplicates(subset=['NUM_DOC','TELEFONO_1','TELEFONO_3','TELEFONO_3','CEL_1','CEL_2'],inplace=True)
            pass
        for index, row in dfOri.iterrows():
            #print('row', str(row['2']))
            if datos.base_segmento == 'Libre inversión':
                if 'ID_PRINCIPAL' in row:
                    idRegistro = db.asignacion_piscina.insert(
                        asignacion_piscina_identificacion  = row['ID_PRINCIPAL'],
                        asignacion_piscina_nombres         = row['NOMBRE_PRINCIPAL'],
                        asignacion_piscina_telefono        = row['TELEFONO_PRINCIPAL_1'],
                        asignacion_piscina_valor           = row['CUPO APROBADO'],
                        asignacion_piscina_cuidad          = row['CIUDAD_PRINCIPAL'],
                        asignacion_piscina_interes         = row['TASA'],
                        asignacion_piscina_cuotas          = row['PLAZO'],
                        asignacion_piscina_oficina         = row['ID_PRINCIPAL'],
                        asignacion_piscina_observaciones   = row['OBSERVACIONES'],
                        asignacion_piscina_idBase          = idBase,
                        asignacion_piscina_idAsignacion    = datos.bases_asignacion,
                        asignacion_piscina_idSucursal      = sucursalUsuario
                    )
                    resul = 1
                    print('resul1',resul)
                else:
                    resul = 0
                    pass
            else:
                if 'NUM_DOC' in row:
                    """
                        TIP_DOC	           0
                        NUM_DOC            1
                        NOM_COMPLETO       2
                        TELEFONO_1	       3
                        COD_CIUDAD_1	   4
                        DEPARTAMENTO	   5
                        TELEFONO_2	       6
                        COD_CIUDAD_2	   7
                        DEPARTAMENTO	   8
                        TELEFONO_3	       9
                        COD_CIUDAD_3	   10
                        DEPARTAMENTO	   11
                        CEL_1	           12
                        CEL_2	           13
                        AUTORIZA TTO DATOS (SI/NO) 14	
                        ORIGEN	           15
                        CUPO_APROBADO	   16
                        PLAZO 	           17
                        TASA MV	           18
                        OBSERVACIONES      19
                    """
                    idRegistro = db.asignacion_piscina.insert(
                        asignacion_piscina_tipo_identiifcacion = row['TIP_DOC'],
                        asignacion_piscina_identificacion      = row['NUM_DOC'],
                        asignacion_piscina_nombres             = row['NOM_COMPLETO'],
                        asignacion_piscina_telefono            = row['TELEFONO_1'],
                        asignacion_piscina_valor               = row['CUPO_APROBADO'],
                        asignacion_piscina_cuidad              = '',
                        asignacion_piscina_interes             = row['TASA MV'],
                        asignacion_piscina_cuotas              = row['PLAZO'],
                        asignacion_piscina_oficina             = '',
                        asignacion_piscina_observaciones       = row['OBSERVACIONES'],
                        asignacion_piscina_origen              = row['ORIGEN'],
                        asignacion_piscina_autoriza            = row['AUTORIZA TTO DATOS (SI/NO)'],
                        asignacion_piscina_idBase              = idBase,
                        asignacion_piscina_idAsignacion        = datos.bases_asignacion,
                        asignacion_piscina_idSucursal          = sucursalUsuario
                    )
                    
                    tel1 = cargueTelefonos( idRegistro,row['TELEFONO_1'],row['COD_CIUDAD_1'],row['DEPARTAMENTO'] )
                    tel2 = cargueTelefonos( idRegistro,row['TELEFONO_2'],row['COD_CIUDAD_2'],row['DEPARTAMENTO'] )
                    tel3 = cargueTelefonos( idRegistro,row['TELEFONO_3'],row['COD_CIUDAD_3'],row['DEPARTAMENTO'] )
                    tel4 = cargueTelefonos( idRegistro,row['CEL_1'],0,0 )
                    tel5 = cargueTelefonos( idRegistro,row['CEL_2'],0,0 )
                    resul = 1
                    print('resul1',resul)
                else:
                    print('resul0',resul)
                    pass
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


def cargueTelefonos( idRegistro,telefono,codigoCuidad,codigoDep ):
    resul = 0
    if len(str(telefono).replace(' ','')) == 10:
        tipoTel = 'Celular'
    elif len(str(telefono).replace(' ','')) == 7:
        tipoTel = 'Fijo'
    else:
        tipoTel = 'Desconocido'
        pass
    if telefono:
        idRegTelefono = db.asignPisTelefono.insert(
            asig_pisc_tel_asignacion_piscina             = idRegistro,
            asig_pisc_tel_asignacion_telefono            = telefono,
            asig_pisc_tel_asignacion_codigo_cuidad       = codigoCuidad,
            asig_pisc_tel_asignacion_codigo_departamento = codigoDep,
            asig_pisc_tel_asignacion_tipo_telefono       = tipoTel
        )
        if idRegTelefono:
            resul = idRegTelefono
            pass
        pass
    return resul

def countAsesorPiscina():
    dbPisAsig    = db.asignacion_piscina
    asigCount    = db( ( dbPisAsig.asignacion_piscina_estado == True ) & ( dbPisAsig.asignacion_piscina_idSucursal == sucursalUsuario ) ).select( dbPisAsig.id )
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

def setTelefonos( idRegistro ):
    dbTels     = db.asignPisTelefono
    tels       = db( dbTels.asig_pisc_tel_asignacion_piscina == idRegistro ).select( dbTels.ALL )
    if tels:
        resul = tels
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


def setInteracion(  data ):
    dbIntracc      = db.tipificacion
    dbAsigPisc     = db.asignacion_piscina
    #dbTipTipf     = db.tipo_tipificacion
    #tmpIdTipoTip  = db( ( dbTipTipf.tipo_tipificacion_descripcion == str(data.tipificacion).replace(' ','') ) & ( dbTipTipf.tipo_tipificacion_desc_uno == str(data.tipoContacto).replace(' ','') ) &\
    #( dbTipTipf.tipo_tipificacion_desc_dos == str(data.descripcion).replace(' ','') ) ).select( dbTipTipf.id ).last()
    #print('tmpIdTipoTip',tmpIdTipoTip)
    dataInfo   = db( dbAsigPisc.id == int(data.idRegistroVar) ).select( dbAsigPisc.ALL ).last()
    if dataInfo:
        print(1)
        idRegistro = dbIntracc.insert(
            tipificacion_identificacion_cliente        = dataInfo.asignacion_piscina_identificacion,
            tipificacion_nombre_cliente                = dataInfo.asignacion_piscina_nombres,
            tipificacion_telefono                      = dataInfo.asignacion_piscina_telefono ,
            tipificacion_valor_venta                   = dataInfo.asignacion_piscina_valor,
            tipificacion_valor_oferta                  = dataInfo.asignacion_piscina_valor,
            tipificacion_asignacion                    = dataInfo.asignacion_piscina_idAsignacion,
            tipificacion_campana                       = dataInfo.asignacion_piscina_idCampana,
            tipificacion_base                          = dataInfo.asignacion_piscina_idBase,
            tipificacion_resultado_tipo_tipificacion   = str(data.tipificacion).replace(' ',''),
            tipificacion_resultado_tipo_contacto       = str(data.tipoContacto).replace(' ',''),
            tipificacion_resultado_descripcion         = str(data.descripcion).replace(' ',''),
            tipificacion_resultado_otra_descripcion    = str(data.otraDescripcion).replace(' ',''),
            tipificacion_sucursal                      = sucursalUsuario,
            tipificacion_asignacion_piscina            = data.idRegistroVar,
            tipificacion_asesor_id                     = idUser,
            tipificacion_comentarios                   = data.observaciones
        )
        print('idRegistro', idRegistro)
    else:
        print(0)
        idRegistro = 0
        pass
    return idRegistro



