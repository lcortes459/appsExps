# -*- coding: utf-8 -*-

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
    resul = 1
    return resul
