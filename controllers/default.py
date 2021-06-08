# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
import gluon.contrib.simplejson
@auth.requires_login()
def index():
    import time
    response.title    = T("Dashboard")  
    response.subTitle = T("Asi vamos")
    titulo            = T("Dashboard sucursales")
    response.botton   = ''
    if grup[0]=='Coordinador':
        redirect(URL('coordinador','dashboard'))
    elif grup[0]=='Asesor':
        redirect(URL('asesores','dashboard'))
    else:
        infoSucurs = asivamosSucursales()
        pass
    return locals()


def ingresoUsuario():
    multi_emailIngreso    = request.vars.emailIngreso
    multi_passIngreso     = request.vars.passIngreso
    multi_users           = db.auth_user
    multi_consul          = db( multi_users.email==multi_emailIngreso ).count()
    multi_consulEsta      = db( ( multi_users.registration_key ) & ( multi_users.email==multi_emailIngreso ) ).count()
    if multi_consul       == 0:
        multi_valores     = dict(multi_valores=errorUsuario)
    elif multi_consulEsta == 1:
        multi_valores     = dict(multi_valores=errorEstado)
    else:
        multi_Autentic    = auth.login_bare(multi_emailIngreso,multi_passIngreso)
        if multi_Autentic:
            multi_valores = str(session.auth.user.first_name)+' '+str(session.auth.user.last_name)
            img           = 0
            multi_valores = dict(multi_valores=multi_valores,img=img)
            if session.auth.user.tipo == ['Asesor']:
                #db( multi_users.id == session.auth.user.id  ).update(estado_servicio=estadoInicial)
                #print('Hay session')
                #tmpCambioEstado = estadoEmpresaAsesor( 'En-linea',session.auth.user.empresa,session.auth.user.id )
                #print('tmpCambioEstado', tmpCambioEstado)
                #sms = "rTime.noti_ingresoAsesor('"+str(str(session.auth.user.first_name)+' '+str(session.auth.user.last_name))+"');" 
                #setRtime(sms,'gerente_'+str(session.auth.user.empresa)+'_'+str(session.auth.user.cliente)+'_'+str(session.auth.user.sucursal))
                pass
        else:
            multi_valores = dict(multi_valores=errorUsuInvalido)
            pass
        pass
    return gluon.contrib.simplejson.dumps(multi_valores)

def start():
    iniciales()
    pass
# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    #print('auth', auth())
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
