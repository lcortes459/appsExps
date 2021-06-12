# -*- coding: utf-8 -*-

@auth.requires_login()
def dashboard():
    response.title    = T("Dashboard")  
    response.subTitle = T("Asi vamos")
    titulo            = T("Dashboard coordinador")
    infoAsignaciones  = []
    return locals()


@auth.requires_login()
def cerrarGestion():
    resul = 1
    return resul
