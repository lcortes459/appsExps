# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth
import time
fechaIntModels  = int(str(request.now)[:10].replace('-',''))
horaIntTmp   = int(str(time.strftime("%H:%M:%S")).replace(':',''))
if str(horaIntTmp)[:2] == '00':
    horaIntModels = horaIntTmp.replace('00','24')
else:
    horaIntModels = horaIntTmp
    pass
# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(configuration.get('db.uri'),
             pool_size=configuration.get('db.pool_size'),
             migrate_enabled=configuration.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = [] 
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=configuration.get('host.names'))

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
#auth.settings.extra_fields['auth_user'] = []
funciones_tables()
auth.settings.extra_fields['auth_user'] = [
    Field('tipo', 'list:string', widget=SQLFORM.widgets.radio.widget),
    Field('sucursal' ,'reference sucursales'),
    Field('sal_llamada','integer',default=0),
    ]
auth.define_tables(username=False, signature=False)
db.auth_user.tipo.requires = [
    IS_IN_SET(('Developer','Administrador','Coordinador','Asesor','Cliente','Director')),
    IS_NOT_EMPTY(error_message='Debe seleccionar un tipo de usuario'),
    ]
db.auth_user.first_name.label           = 'Usuario'
db.auth_user.last_name.readable         =  db.auth_user.last_name.writable = False
db.auth_user.registration_key.writable  = False
db.auth_user.registration_key.readable  = True
db.auth_user.registration_key.label     ='Estado'
db.auth_user.registration_key.represent = lambda id, r: userGetEstado(r)
db.auth_user._enable_record_versioning()


db.define_table('empleados', 
    Field('empleados_nombres', label='Nombres Apellidos'),
    Field('empleados_identificacion', label='Identificación'),
    Field('empleados_celular', label='Celular'),
    Field('empleados_fecha_ingreso', label='Fecha Ingreso'),
    Field('empleados_fecha_nacimiento', label='Fecha Nacimiento'),
    Field('empleados_contacto_emergancia', label='Contacto Emergencia'),
    Field('empleados_parentesco_emergancia', label='Parentezco Contacto'),
    Field('empleados_telefono_emergancia', label='Celular Contacto'),
    Field('empleados_direccion_recidencia', label='Dirección Domicilio'),
    Field('empleados_email', label='Email'),
    Field('empleados_genero' , 'list:string', widget=SQLFORM.widgets.radio.widget, label='Genero'),
    Field('empleados_observaciones', 'text',label='Observaciones'),
    Field('empleados_estado',default=True , label="Estado"),
    Field('empleados_fecha_creacion' , 'integer',default=fechaIntModels),
    Field('empleados_hora_creacion' , 'integer',default=horaIntModels),
    Field('empleados_foto','upload'),
    Field('empleados_sucursal','integer',default=0)
)
    
db.empleados.id.readable                        =  db.empleados.id.writable = False
db.empleados.empleados_foto.readable            =  False
db.empleados.empleados_estado.writable          =  False
db.empleados.empleados_fecha_creacion.readable  =  db.empleados.empleados_fecha_creacion.writable = False
db.empleados.empleados_hora_creacion.readable   =  db.empleados.empleados_hora_creacion.writable = False
db.empleados.empleados_observaciones.readable   =  db.empleados.empleados_observaciones.writable = False
db.empleados.empleados_sucursal.readable        =  db.empleados.empleados_sucursal.writable = False

db.empleados.empleados_email.readable        =  db.empleados.empleados_email.writable = False
db.empleados.empleados_direccion_recidencia.readable        =  db.empleados.empleados_direccion_recidencia.writable = False
db.empleados.empleados_telefono_emergancia.readable        =  db.empleados.empleados_telefono_emergancia.writable = False
db.empleados.empleados_contacto_emergancia.readable        =  db.empleados.empleados_contacto_emergancia.writable = False
db.empleados.empleados_fecha_nacimiento.readable        =  db.empleados.empleados_fecha_nacimiento.writable = False
db.empleados.empleados_fecha_ingreso.readable        =  db.empleados.empleados_fecha_ingreso.writable = False
db.empleados.empleados_observaciones.readable        =  db.empleados.empleados_observaciones.writable = False
db.empleados.empleados_parentesco_emergancia.readable        =  db.empleados.empleados_parentesco_emergancia.writable = False

db.empleados.empleados_fecha_ingreso.readable = False
db.empleados.empleados_fecha_nacimiento.readable = False
db.empleados.empleados_parentesco_emergancia.readable = False
db.empleados.empleados_genero.readable = False

db.empleados.empleados_nombres.requires = IS_NOT_EMPTY(error_message='Debe ingresar un nombre y un apellido')
db.empleados.empleados_identificacion.requires = IS_NOT_EMPTY(error_message='Debe ingresar una identificación')
db.empleados.empleados_genero.requires = [
    IS_IN_SET(('Femenino', 'Masculino')),
    IS_NOT_EMPTY(error_message='Debe ingresar un genero'),
]
db.empleados.empleados_foto.represent = lambda empleados_foto, r : getFotoZoom(r,35,35)
db.empleados.empleados_estado.represent = lambda id, r: emplGetEstado(r)
db.empleados._enable_record_versioning()

db.define_table('usuario_empleado',
    Field('usuario_empleado_empleado','reference empleados'),
    Field('usuario_empleado_usuario','reference auth_user'),
)
db.usuario_empleado._enable_record_versioning()


db.define_table('estado_tiempos',
    Field('estado_tiempos_codigo'),
    Field('estado_tiempos_nombre','text'),
    Field('estado_tiempos_estado', default=True),
    Field('estado_tiempos_fecha_creacion' , 'integer',default=fechaIntModels),
    Field('estado_tiempos_hora_creacion' , 'integer',default=horaIntModels),
)
db.estado_tiempos._enable_record_versioning()

db.define_table('usuarios_estado',
    Field('usuarios_estado_usuario','reference auth_user'),
    Field('usuarios_estado_tiempo','reference estado_tiempos'),
    Field('usuarios_estado_estado',defautl=True),
    Field('usuarios_estado_fecha_creacion' , 'integer',default=fechaIntModels),
    Field('usuarios_estado_hora_creacion' , 'integer',default=horaIntModels),
)
db.usuarios_estado._enable_record_versioning()


db.define_table('asesor_piscina',
    Field('asesor_piscina_usuario','reference auth_user'),
    Field('asesor_piscina_piscina','reference asignacion_piscina'),
    Field('asesor_piscina_estado',defautl=True),
    Field('asesor_piscina_fecha_creacion' , 'integer',default=fechaIntModels),
    Field('asesor_piscina_hora_creacion' , 'integer',default=horaIntModels),
)
db.asesor_piscina._enable_record_versioning()



# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else configuration.get('smtp.server')
mail.settings.sender = configuration.get('smtp.sender')
mail.settings.login = configuration.get('smtp.login')
mail.settings.tls = configuration.get('smtp.tls') or False
mail.settings.ssl = configuration.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------  
# read more at http://dev.w3.org/html5/markup/meta.name.html               
# -------------------------------------------------------------------------
response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')
response.show_toolbar = configuration.get('app.toolbar')

# -------------------------------------------------------------------------
# your http://google.com/analytics id                                      
# -------------------------------------------------------------------------
response.google_analytics_id = configuration.get('google.analytics_id')

# -------------------------------------------------------------------------
# maybe use the scheduler
# -------------------------------------------------------------------------
if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configuration.get('scheduler.heartbeat'))

