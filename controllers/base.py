# -*- coding: utf-8 -*-
def getEmpladoAsigar(id):
	multi_dbEmpleados    = db.usuario_empleado
	if db (multi_dbEmpleados.usuario_empleado_usuario == id).count() > 0:
		empleado    = db( multi_dbEmpleados.usuario_empleado_usuario == id ).select(multi_dbEmpleados.usuario_empleado_empleado).last()
		resul = XML("""<a href="#!" 
						  class="btn btn-primary btn-block"
						  onclick="template.asigEmpleado("""+str(id)+""");" 
					><b>"""+str(db.empleados[empleado.usuario_empleado_empleado].empleados_nombres)+"""</b></span>""")
	else:
		resul = XML("""
			<a 	href="#!" 
				class="btn btn-block btn-danger" 
				onclick="template.asigEmpleado("""+str(id)+""");"
			>Agregar</a>
		""")
		pass
	return resul

def getBasesCargar(id):
	dbBasAsig      = db.bases_asignacion
	cabtBasesAsig  = db( dbBasAsig.bases_asignacion_asignacion == id ).count()
	if cabtBasesAsig > 0:
		resul = XML("""<a href="#!" 
						  class="btn btn-primary btn-block"
						  onclick="template.basesAsignacion("""+str(id)+""");" 
					><b>"""+str(cabtBasesAsig)+"""</b></span>""")
	else:
		resul = XML("""
			<a 	href="#!" 
				class="btn btn-block btn-danger" 
				onclick="template.basesAsignacion("""+str(id)+""");"
			>Agregar</a>
		""")
		pass
	return resul
	
@auth.requires_login()
def allUsuarios():

	response.title       = T("Configuraciones | Usuarios")
	response.subTitle    = T("Mis Usuarios")
	response.icono       = 'user-cog'
	subTitlesubtTile     = T("Usuarios")
	response.botton      = ''
	multi_dbUsuarios     = db.auth_user
	multi_dbUsuarios.id.readable               =  multi_dbUsuarios.id.writable = False
	multi_dbUsuarios.cliente.readable          =  multi_dbUsuarios.cliente.writable = False
	multi_dbUsuarios.proyecto.readable         =  multi_dbUsuarios.proyecto.writable = False
	query                                      = ( multi_dbUsuarios.id > 0 ) 

	links = [
		dict(header='Empleado', body=lambda r: DIV( getEmpladoAsigar(r.id), _id='asignarEmpleado_%s' %r.id ) )
	]

	print('query',query)
	print('grup',grup)

	usuarios             = SQLFORM.grid(
		query,
		deletable        = False,
		details          = False,
		csv              = False,
		maxtextlength    = 150,
		editable         = True,
        paginate         = 100,
        links            = links,
		orderby          = multi_dbUsuarios.id

	) 
	return locals()


@auth.requires_login()
def empleados():
	response.title    = T("Mis empleados")    
	response.subTitle = T("Empleados")
	titulo            = T("Listado Empleados")
	response.botton   = ''
	db_dbEmpleados    = db.empleados
	links = []
	db_dbEmpleados.empleados_sucursal.default   =  auth.user.sucursal
	if grup == ['Gerente']:
		query                                   = ( ( db_dbEmpleados.empleados_estado == True ) & ( db_dbEmpleados.empleados_sucursal == auth.user.sucursal ) )
	else:
		query                                   = ( db_dbEmpleados.empleados_estado == True )
		pass
	empleados            = SQLFORM.grid(
		query,
			deletable        = False,
			details          = False,
			csv              = False,
			maxtextlength    = 50,
			editable         = True,
			paginate         = 100,
			links            = links,
			orderby          = db_dbEmpleados.id
		) 
	return locals()


@auth.requires_login()
def updateEstadoEmplado():
    if str(request.vars.est) == "0":
        estado = False
        db(db.usuario_empleado.usuario_empleado_empleado==request.vars.empl).delete()
    else:
        estado = True
        pass
    db( db.empleados.id == request.vars.empl).update(empleados_estado=estado)
    resul    = 1
    return resul


@auth.requires_login()
def usuarios():

	response.title       = T("Configuraciones | Usuarios")
	response.subTitle    = T("Mis Usuarios")
	titulo               = T("Listado Usuarios")
	response.botton      = ''
	multi_dbUsuarios     = db.auth_user
	multi_dbUsuarios.id.readable               =  multi_dbUsuarios.id.writable = False
	query                                      = ( multi_dbUsuarios.id > 0 ) 

	links = [
		dict(header='Empleado', body=lambda r: DIV( getEmpladoAsigar(r.id), _id='asignarEmpleado_%s' %r.id ) )
	]

	#print('query',query)
	#print('grup',grup)

	usuarios             = SQLFORM.grid(
		query,
		deletable        = False,
		details          = False,
		csv              = False,
		maxtextlength    = 150,
		editable         = True,
        paginate         = 100,
        links            = links,
		orderby          = multi_dbUsuarios.id

	) 
	return locals()


@auth.requires_login()
def tipificaciones():
	response.title    = T("Tipificaciones")    
	response.subTitle = T("Tipificaciones")
	subTitlesubtTile  = T("Listado")
	response.botton   = ''
	dbTTip       = db.tipo_interaccion
	#multi_dbEmpleados.empleados_cliente.default  = empresa
	#query                = ( multi_dbEmpleados.empleados_cliente==empresa )
	links = []
	tipificaciones           = SQLFORM.grid(
		dbTTip,
			deletable        = False,
			details          = False,
			csv              = False,
			maxtextlength    = 50,
			editable         = True,
			paginate         = 100,
			links            = links,
			orderby          = dbTTip.id
		)
	return locals()

@auth.requires_login()
def sucursales():
	response.title           = T("Sucursales")    
	response.subTitle        = T("Sucursales")
	titulo                   = T("Listado Sucursales")
	dbSucur                  = db.sucursales
	links                    = []
	query                    = ( dbSucur.id > 0 )
	sucursales              = SQLFORM.grid(
		dbSucur,
			deletable        = False,
			details          = False,
			csv              = False,
			maxtextlength    = 50,
			editable         = True,
			paginate         = 100,
			links            = links,
			orderby          = dbSucur.id
		) 
	return locals()

@auth.requires_login()
def asignaciones():
	response.title           = T("Asignaciones")    
	response.subTitle        = T("Asignaciones")
	titulo                   = T("Listado Asignaciones")
	dbasignac                = db.asignaciones
	links = [
		dict(header='Bases', body=lambda r: DIV( getBasesCargar(r.id), _id='agregarBases_%s' %r.id ) )
	]
	if grup==['Coordinador']:
		dbasignac.asignaciones_responsable_creacion.default  = idUser
		dbasignac.asignaciones_sucursal.default              = sucursalUsuario
		dbasignac.asignaciones_responsable_creacion.readable =  dbasignac.asignaciones_responsable_creacion.writable = False
		dbasignac.asignaciones_sucursal.readable             =  dbasignac.asignaciones_sucursal.writable = False
		query                    = ( dbasignac.asignaciones_responsable_creacion == idUser )
	else:
		query                    = ( dbasignac.id > 0 )
		pass

	asignaciones             = SQLFORM.grid(
		dbasignac,
			deletable        = False,
			details          = False,
			csv              = False,
			maxtextlength    = 50,
			editable         = True,
			paginate         = 100,
			links            = links,
			orderby          = dbasignac.id
		) 
	return locals()

@auth.requires_login()
def basesAsignacion():
	titulo                   = T("Listado Bases x asignación")
	varDatos           = request.vars
	dbBasAsig          = db.bases_asignacion
	links = [
		dict(header='Proceso', body=lambda r: DIV( getBasesCargar(r.id), _id='aprocesoBases_%s' %r.id ) )
	]
	dbasignac               = (  dbBasAsig.bases_asignacion_asignacion == varDatos.idAsignacion ) 
	basesCarg               =  SQLFORM.grid(
		dbasignac,
			deletable        = False,
			details          = False,
			csv              = False,
			maxtextlength    = 50,
			editable         = True,
			paginate         = 100,
			links            = links,
			orderby          = ~dbBasAsig.id
		) 
	return locals()


@auth.requires_login()
def bases():
    response.title    = T("bases")    
    titulo            = T("Listado bases")
    links             = []
    dbBases           = db.bases
    links = [
		dict(header='Empleado', body=lambda r: DIV( getEmpladoAsigar(r.id), _id='asignarEmpleado_%s' %r.id ) )
	]
    dbCBasesSql       = ( dbBases.id > 0 )
    bast              = SQLFORM.grid(
        dbCBasesSql,
            deletable        = False,
            details          = False,
            csv              = False,
            maxtextlength    = 50,
            editable         = True,
            paginate         = 100,
            links            = links,
            orderby          = dbBases.id
        )
    return locals()

@auth.requires_login()
def campanas():
    response.title    = T("Campañas")    
    titulo            = T("Listado Campañas")
    links             = []
    dbCamp            = db.campanas
    dbCampSql         = ( dbCamp.id < 0 )
    camapnas          = SQLFORM.grid(
        dbCampSql,
            deletable        = False,
            details          = False,
            csv              = False,
            maxtextlength    = 50,
            editable         = True,
            paginate         = 100,
            links            = links,
            orderby          = dbCamp.id
        ) 
    return locals()
