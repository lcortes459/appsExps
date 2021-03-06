# -*- coding: utf-8 -*-

@auth.requires_login()
def gestion():
    response.title          = T("Gestiones")  
    response.subTitle       = T("Asi vamos")
    titulo                  = T("Gestiones piscina")
    #infoAsignaciones       = asivamosAsignaciones()
    dbIntracc               = db.tipificacion
    links = []
    query                   = ( dbIntracc.id > 0 )
    #estructuracionBase(21)
    gestiones               = SQLFORM.grid(
        query,
            deletable        = False,
            details          = False,
            csv              = True,
            maxtextlength    = 50,
            editable         = True,
            paginate         = 1000,
            links            = links,
            orderby          = dbIntracc.id,
            create           = False
        ) 
    return locals()


@auth.requires_login()
def piscina():
    response.title          = T("Dashboard")  
    response.subTitle       = T("Asi vamos")
    titulo                  = T("Listado piscina")
    #infoAsignaciones       = asivamosAsignaciones()
    dbPisc                  = db.asignacion_piscina
    links = []
    query                   = ( dbPisc.id > 0 )
    #estructuracionBase(21)
    piscina                  = SQLFORM.grid(
        query,
            deletable        = True,
            details          = False,
            csv              = True,
            maxtextlength    = 50,
            editable         = True,
            paginate         = 100,
            links            = links,
            orderby          = dbPisc.id,
            create           = False
        ) 
    return locals()
