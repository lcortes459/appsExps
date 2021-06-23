# -*- coding: utf-8 -*-

@auth.requires_login()
def dashboard():
    response.title          = T("Dashboard")  
    response.subTitle       = T("Asi vamos")
    titulo                  = T("Dashboard coordinador")
    #infoAsignaciones       = asivamosAsignaciones()
    dbIntracc               = db.tipificacion
    links = []
    query                   = ( dbIntracc.tipificacion_sucursal == sucursalUsuario )
    #estructuracionBase(21)
    gestiones               = SQLFORM.grid(
        query,
            deletable        = False,
            details          = False,
            csv              = True,
            maxtextlength    = 50,
            editable         = False,
            paginate         = 100,
            links            = links,
            orderby          = dbIntracc.id,
            create           = False
        ) 
    return locals()
