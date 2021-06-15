# -*- coding: utf-8 -*-

@auth.requires_login()
def dashboard():
    response.title    = T("Dashboard")  
    response.subTitle = T("Asi vamos")
    titulo            = T("Dashboard coordinador")
    infoAsignaciones  = asivamosAsignaciones()
    return locals()
