# -*- coding: utf-8 -*-
import gluon.contrib.simplejson

@auth.requires_login()
def dashboard():
    response.title    = T("Dashboard")  
    response.subTitle = T("Asi vamos")
    titulo            = T("Dashboard asesor")
    infoAsignaciones  = countAsesorPiscina()
    return locals()


@auth.requires_login()
def buscarRegisto():
    resul = getAsesorPiscina()
    return resul

@auth.requires_login()
def infoRegistro():
    varsData          = request.vars
    infoReg           = setAsesorPiscina( varsData.idRegistro )
    return locals()


@auth.requires_login()
def cerrarGestion():
    varData  = request.vars
    print('varData',varData)
    resul = setInteracion( varData )
    return str(resul)

@auth.requires_login()
def consultarTipoContacto():
    tipificacion = request.vars.tipoTipe
    data = db( db.tipo_tipificacion.tipo_tipificacion_descripcion == tipificacion ).select( db.tipo_tipificacion.tipo_tipificacion_desc_uno,distinct=True)
    return gluon.contrib.simplejson.dumps(data.as_list())

@auth.requires_login()
def consultarDescripciones():
    tipoContacto = request.vars.tipoContacto
    data = db( db.tipo_tipificacion.tipo_tipificacion_desc_uno == tipoContacto ).select( db.tipo_tipificacion.tipo_tipificacion_desc_dos,distinct=True)
    return gluon.contrib.simplejson.dumps(data.as_list())

@auth.requires_login()
def consultarOtrsDescripciones():
    descripcion = request.vars.descripcion
    data = db( db.tipo_tipificacion.tipo_tipificacion_desc_dos == descripcion ).select( db.tipo_tipificacion.tipo_tipificacion_desc_tres,distinct=True)
    return gluon.contrib.simplejson.dumps(data.as_list())
