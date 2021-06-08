response.menu = []
inicio = URL('default','index')
errorUsuario       = "usuario"
errorEstado        = "estado"
estadoInicial      = "En-linea"
errorUsuInvalido   = "invalido"
def is_session():
    return True if auth.is_logged_in() else False

if is_session():
    idUser               = auth.user.id
    nameUser             = "%s %s" %(auth.user.first_name,auth.user.last_name)
    emailUser            = auth.user.email
    grup                 = auth.user.tipo
    estado               = auth.user.registration_key
    extUser              = auth.user.sal_llamada
    sucursalUsuario      = auth.user.sucursal
    pass

def nombreEmpleado():
    nombre = auth.user.first_name
    return nombre

def datosEmpleado( idUsuario ):
    dbEmpl    = db.empleados
    dbUsuEmpl = db.usuario_empleado 
    tmpData   = db( dbUsuEmpl.usuario_empleado_usuario == idUsuario ).select( dbUsuEmpl.usuario_empleado_empleado ).last()
    if tmpData:
        tmpNom    = db( dbEmpl.id == tmpData.usuario_empleado_empleado ).select( dbEmpl.empleados_nombres ).last()
        if tmpNom:
            dato = tmpNom.empleados_nombres
        else:
            dato = nombreEmpleado()
            pass
    else:
        dato = nombreEmpleado()
        pass
    return dato

def plantilla():
    if grup==['Coordinador']:
        plantilla = 'templateCoorInit.html'
    elif grup==['Director']:
        plantilla = 'templateDirInit.html'
    elif grup==['Asesor']:
        plantilla = 'templateAseInit.html'
    else:
        plantilla = 'templateInit.html'
        pass

    return plantilla


def estadoServicioAsesor():
    multi_users   = db.auth_user
    estadoAsesor  = db(  multi_users.id == idUser ).select().last()['estado_servicio'] 
    return estadoAsesor


def codigoPais():
    paisId      = db( db.empresas.id == empresaUsuario ).select( db.empresas.empresas_pais ).last()['empresas_pais']
    codigoPais  = db( db.paises.id == paisId ).select().last()['paises_codigo']
    return codigoPais



