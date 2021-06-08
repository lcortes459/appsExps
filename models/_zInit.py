# -*- coding: utf-8 -*-

def iniciales():
    adv_dbSucurs     = db.sucursales
    adv_dbUsuarios   = db.auth_user
    adv_dbemple      = db.empleados
    adv_dbemp_usu    = db.usuario_empleado
    adv_dbesta_ase   = db.estado_tiempos 
    adv_tipInterac   = db.tipo_tipificacion

	
    tipoTipTip  = [
        ['Cliente no desea ser contactado de nuevo','3001'],
        ['No autoriza tratamiento de datos','3002'],
    ]
    estadosAsesor = [  
        'En-linea',
        'Fuera-linea',
        'En-llamada',
        'Almuerzo',
        'Descanso',
        'Reunión',
        'Otro',
    ]
    
    conInt = 1
    for x in tipoTipTip:
        adv_tipInterac.insert(
            tipo_tipificacion_descripcion  = x[0],
            tipo_tipificacion_id_resultado = x[1],
            tipo_tipificacion_orden        = conInt
            )
        conInt = conInt + 1
        pass
    
    
    conEst = 1
    for x in estadosAsesor:
        adv_dbesta_ase.insert(
            estado_tiempos_nombre  = x,
            estado_tiempos_codigo  = conEst
            )
        conEst = conEst + 1
        pass
    
    
    idSucursal      = adv_dbSucurs.insert(
        asignaciones_nombre = 'Principal',
        sucursales_codigo = '102030',
        sucursales_direccion = 'Carrera 7 # 32 13',
        sucursales_responsable = 'Javier Rodriguez',
        sucursales_celular = '1234567890',
        sucursales_email = 'email@email.com',
        sucursales_tipo_letra = '',
        sucursales_color_corporativo = '',
        sucursales_responsable_creacion = None
    )


	#  Usuarios

    idUsuarioDeveloper = adv_dbUsuarios.insert(
        first_name     = 'Developer',
        last_name      = 'FullStack',
        email          = 'developer@appsexps.com',
        password       =  db.auth_user.password.validate('Ab1g3l2@12')[0],
        tipo           = 'Developer',
        sucursal       =  idSucursal
    )
    
    idUsuarioAdministrador = adv_dbUsuarios.insert(
        first_name     = 'Administrador',
        last_name      = 'Full',
        email          = 'admin@appsexps.com',
        password       =  db.auth_user.password.validate('Adm1n2@21=')[0],
        tipo           = 'Administrador',
        sucursal       =  idSucursal
    )

    idCliente          = adv_dbUsuarios.insert(
        first_name     = 'Cliente',
        last_name      = 'General',
        email          = 'cliente@appsexps.com',
        password       =  db.auth_user.password.validate('Cl13nt32@21')[0],
        tipo           = 'Cliente',
        sucursal       =  idSucursal
    )

    idDirector         = adv_dbUsuarios.insert(
        first_name     = 'Director',
        last_name      = 'Operaciones',
        email          = 'director@appsexps.com',
        password       =  db.auth_user.password.validate('D1r3ct0r2@21')[0],
        tipo           = 'Director',
        sucursal       =  idSucursal
    )
    
    
    idCoordinador      = adv_dbUsuarios.insert(
        first_name     = 'Coordinador',
        last_name      = 'Operaciones',
        email          = 'coordinador@appsexps.com',
        password       =  db.auth_user.password.validate('C00rd1nad0r2@21')[0],
        tipo           = 'Coordinador',
        sucursal       =  idSucursal
    )
    
    
    idAsesor           = adv_dbUsuarios.insert(
        first_name     = 'Asesor uno',
        last_name      = 'Operaciones',
        email          = 'asesor_uno@appsexps.com',
        password       =  db.auth_user.password.validate('As3s0rUn02@21')[0],
        tipo           = 'Asesor',
        sucursal       =  idSucursal
    )

	
	#  Empleados
    idEmpleDev    =  adv_dbemple.insert(
        empleados_nombres = 'Luis Cortes',
        empleados_identificacion = '906030',
        empleados_celular =  '1234567890',
        empleados_cliente =  1,
        empleados_proyecto =  1,
        empleados_fecha_ingreso =  '20200101',
        empleados_fecha_nacimiento =  '20200101',
        empleados_contacto_emergancia =  'Kelly Cortes',
        empleados_parentesco_emergancia =  'Hermana',
        empleados_telefono_emergancia =  '1234567890',
        empleados_direccion_recidencia =  'Soacha',
        empleados_email =  'luantrobest@gmail.com',
        empleados_genero =  'Masculino',
        empleados_observaciones =  'Developer',
    )
    
    idEmpleAdm   =  adv_dbemple.insert(
        empleados_nombres = 'Javier Rodriguez',
        empleados_identificacion = '906030',
        empleados_celular =  '1234567890',
        empleados_cliente =  1,
        empleados_proyecto =  1,
        empleados_fecha_ingreso =  '20200101',
        empleados_fecha_nacimiento =  '20200101',
        empleados_contacto_emergancia =  'Wilson Rodriguez',
        empleados_parentesco_emergancia =  'Hermano',
        empleados_telefono_emergancia =  '1234567890',
        empleados_direccion_recidencia =  'Chia',
        empleados_email =  'jrodriguez@email.com',
        empleados_genero =  'Masculino',
        empleados_observaciones =  'Administrador',
    )

    adv_dbemp_usu.insert(
        usuario_empleado_empleado = idUsuarioAdministrador,
        usuario_empleado_usuario = idEmpleAdm,
    )

    adv_dbemp_usu.insert(
        usuario_empleado_empleado = idEmpleDev,
        usuario_empleado_usuario = idUsuarioDeveloper,
    )
    

