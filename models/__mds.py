# -*- coding: utf-8 -*-
import time
fechaIntModels  = int(str(request.now)[:10].replace('-',''))
horaIntTmp   = int(str(time.strftime("%H:%M:%S")).replace(':',''))
if str(horaIntTmp)[:2] == '00':
    horaIntModels = horaIntTmp.replace('00','24')
else:
    horaIntModels = horaIntTmp
    pass

def db_tableSucursales():
    db.define_table('sucursales', 
        Field('sucursales_codigo'),
        Field('sucursales_nombre'),
        Field('sucursales_direccion'),
        Field('sucursales_responsable'),
        Field('sucursales_celular'),
        Field('sucursales_email'),
        Field('sucursales_estado',default=True),
        Field('sucursales_tipo_letra',defaul=''),
        Field('sucursales_color_corporativo',defaul=''),
        Field('sucursales_responsable_creacion',defaul=''),
        Field('sucursales_fecha_creacion' , 'integer' ,default=fechaIntModels),
        Field('sucursales_hora_creacion' , 'integer',default=horaIntModels),
        format="%(sucursales_nombre)s"
    )
    db.sucursales.id.readable                        =  db.sucursales.id.writable = False
    db.sucursales.sucursales_estado.readable         =  db.sucursales.sucursales_estado.writable = False
    db.sucursales.sucursales_fecha_creacion.readable =  db.sucursales.sucursales_fecha_creacion.writable = False
    db.sucursales.sucursales_hora_creacion.readable  =  db.sucursales.sucursales_hora_creacion.writable = False
    db.sucursales._enable_record_versioning()
    pass

def db_tableAsiganciones():
    if not hasattr(db,'sucursales'):
        db_tableSucursales()
    db.define_table('asignaciones', 
        Field('asignaciones_sucursal' ,'reference sucursales'),
        Field('asignaciones_codigo', represent= lambda icono, r: creacionCodigo(r.id,r.asignaciones_nombre)),
        Field('asignaciones_nombre'),
        Field('asignaciones_estado',default=True),
        Field('asignaciones_responsable_creacion'),
        Field('asignaciones_fecha_creacion' , 'integer' ,default=fechaIntModels, represent= lambda icono, r: fechaFormato(r.asignaciones_fecha_creacion,'fecha')),
        Field('asignaciones_hora_creacion' , 'integer',default=horaIntModels),
        Field('asignaciones_fecha_inicio' , 'integer',default=fechaIntModels, represent= lambda icono, r: fechaFormato(r.asignaciones_fecha_inicio,'fecha')),
        Field('asignaciones_fecha_cierre' , 'integer',default=0, represent= lambda icono, r: fechaFormato(r.asignaciones_fecha_cierre,'fecha')),
        format="%(asignaciones_nombre)s"
    )
    db.asignaciones.id.readable =  db.asignaciones.id.writable = False
    db.asignaciones.asignaciones_codigo.writable = False
    db.asignaciones.asignaciones_estado.readable =  db.asignaciones.asignaciones_estado.writable = False
    db.asignaciones.asignaciones_fecha_creacion.readable =  db.asignaciones.asignaciones_fecha_creacion.writable = False
    db.asignaciones.asignaciones_hora_creacion.readable =  db.asignaciones.asignaciones_hora_creacion.writable = False
    db.asignaciones._enable_record_versioning()
    pass

def db_tableBaes():
    if not hasattr(db,'asignaciones'):
        db_tableAsiganciones()
    db.define_table('bases', 
        Field('bases_asignacion' ,'reference asignaciones',label='Asignación'),
        Field('bases_base','upload',label='Registros base', represent= lambda bases_base, r: XML("""<div style="text-align: center"> <i class="far fa-file-excel text-success" aria-hidden="true"></i></div>""" )),
        #Field('bases_demo','upload',label='Registros demograficos', represent= lambda bases_demo, r: XML("""<div style="text-align: center"><i class="far fa-file-excel text-success" aria-hidden="true"></i></div>""" )),
        Field('bases_nombre'),
        Field('bases_estado',default='En proceso',label='Estado base', represent= lambda bases_estado, r: XML("""<div style="text-align: center"><span class="right badge badge-primary">"""+str(r.bases_estado)+"""</span></div>""" )),
        Field('bases_responsable_creacion'),
        Field('bases_fecha_creacion' , 'integer' ,default=fechaIntModels),
        Field('bases_hora_creacion' , 'integer',default=horaIntModels),
        format="%(bases_nombre)s"
    )
    db.bases.id.readable =  db.bases.id.writable = False
    #db.bases.bases_estado.writable = False
    #db.bases.bases_estado.readable =  db.bases.bases_fecha_creacion.writable = False
    db.bases.bases_fecha_creacion.readable =  db.bases.bases_fecha_creacion.writable = False
    db.bases.bases_hora_creacion.readable =  db.bases.bases_hora_creacion.writable = False
    db.bases.bases_nombre.readable =  db.bases.bases_nombre.writable = False
    db.bases.bases_responsable_creacion.readable =  db.bases.bases_responsable_creacion.writable = False
    db.bases._enable_record_versioning()
    pass

def db_tableCampanas():
    if not hasattr(db,'bases'):
        db_tableBaes()
    db.define_table('campanas', 
        Field('campanas_base' ,'reference bases'),
        Field('campanas_codigo'),
        Field('campanas_nombre'),
        Field('campanas_estado',default=True),
        Field('campanas_responsable_creacion'),
        Field('campanas_fecha_creacion' , 'integer' ,default=fechaIntModels),
        Field('campanas_hora_creacion' , 'integer',default=horaIntModels),
        Field('campanas_fecha_inicio' , 'integer' ,default=fechaIntModels),
        Field('campanas_fecha_cierre' , 'integer' ),
        format="%(campanas_nombre)s"
    )
    db.campanas.id.readable =  db.campanas.id.writable = False
    db.campanas.campanas_estado.readable =  db.campanas.campanas_estado.writable = False
    db.campanas.campanas_fecha_creacion.readable =  db.campanas.campanas_fecha_creacion.writable = False
    db.campanas.campanas_hora_creacion.readable =  db.campanas.campanas_hora_creacion.writable = False
    db.campanas._enable_record_versioning()
    pass

def db_tableAsinacionHistory():
    if not hasattr(db,'campanas'):
        db_tableCampanas()
    db.define_table('asignacion_historico', 
        Field('asignacion_historico_identificacion','text'),
        Field('asignacion_historico_nombre','text'),
        Field('asignacion_historico_telefono','text'),
        Field('asignacion_historico_estado',default=True),
        Field('asignacion_historico_fecha_creacion' , 'integer' ,default=fechaIntModels),
        Field('asignacion_historico_hora_creacion' , 'integer',default=horaIntModels),
        Field('asignacion_historico_idBase', 'integer'),
        Field('asignacion_historico_idCampana', 'integer',default=0),
        Field('asignacion_historico_dia','integer',default=fechaIntergar('dia')),
        Field('asignacion_historico_mes','integer',default=fechaIntergar('mes')),
        Field('asignacion_historico_anio','integer',default=fechaIntergar('anio')),
    )
    db.asignacion_historico._enable_record_versioning()
    pass


def db_tableAsinacionPiscina():
    if not hasattr(db,'asignacion_historico'):
        db_tableAsinacionHistory()
    db.define_table('asignacion_piscina', 
        Field('asignacion_piscina_identificacion','text'),
        Field('asignacion_piscina_nombres','text'),
        Field('asignacion_piscina_telefono','text'),
        Field('asignacion_piscina_valor','text'),
        Field('asignacion_piscina_cuidad','text'),
        Field('asignacion_piscina_interes','text'),
        Field('asignacion_piscina_cuotas','text'),
        Field('asignacion_piscina_oficina','text'),
        Field('asignacion_piscina_estado',default=True),
        Field('asignacion_piscina_fecha_creacion' , 'integer' ,default=fechaIntModels),
        Field('asignacion_piscina_hora_creacion' , 'integer',default=horaIntModels),
        Field('asignacion_piscina_idAsignacion', 'integer'),
        Field('asignacion_piscina_idBase', 'integer'),
        Field('asignacion_piscina_idCampana', 'integer',default=0),
        Field('asignacion_piscina_dia','integer',default=fechaIntergar('dia')),
        Field('asignacion_piscina_mes','integer',default=fechaIntergar('mes')),
        Field('asignacion_piscina_anio','integer',default=fechaIntergar('anio')),
        Field('asignacion_piscina_observaciones','text'),
    )
    db.asignacion_piscina._enable_record_versioning()
    pass

def db_tableAgendas():
    if not hasattr(db,'asignacion_piscina'):
        db_tableAsinacionPiscina()
    db.define_table('agendas', 
        Field('agendas_asignacion_historico','reference asignacion_historico'),
        Field('agendas_sucursal','integer'),
        Field('agendas_campana','integer'),
        Field('agendas_base','integer'),
        Field('agendas_hora_agenda'),
        Field('agendas_fecha_agenda'),
        Field('agendas_asesor','integer'),
        Field('agendas_estado',default=True),
        Field('agendas_fecha_creacion','integer' ,default=fechaIntModels),
        Field('agendas_hora_creacion','integer',default=horaIntModels),
        Field('agendas_comentarios','text'),
        Field('agendas_dia','integer',default=fechaIntergar('dia')),
        Field('agendas_mes','integer',default=fechaIntergar('mes')),
        Field('agendas_anio','integer',default=fechaIntergar('anio'))
    )
    db.agendas._enable_record_versioning()
    pass

def db_tableVentas():
    if not hasattr(db,'agendas'):
        db_tableAgendas()  
    db.define_table('ventas', 
        Field('ventas_identificacion'),
        Field('ventas_nombres'),
        Field('ventas_celular'),
        Field('ventas_valor_venta','double', default=0),
        Field('ventas_valor_oferta','double', default=0),
        Field('ventas_estado',default=True),
        Field('ventas_sucursal','integer'),
        Field('ventas_asignacion','integer'),
        Field('ventas_campana','integer'),
        Field('ventas_asignacion_historico','reference asignacion_historico'),
        Field('ventas_fecha_creacion','integer' ,default=fechaIntModels),
        Field('ventas_hora_creacion','integer',default=horaIntModels),
        Field('ventas_comentarios','text'),
        Field('ventas_dia','integer',default=fechaIntergar('dia')),
        Field('ventas_mes','integer',default=fechaIntergar('mes')),
        Field('ventas_anio','integer',default=fechaIntergar('anio')),
        format="%(ventas_nombre)s"
    )
    db.ventas._enable_record_versioning()
    pass

def db_tableTipoTipificacion():
    if not hasattr(db,'ventas'):
        db_tableVentas() 
    db.define_table('tipo_tipificacion', 
        Field('tipo_tipificacion_id_resultado'),
        Field('tipo_tipificacion_orden'),
        Field('tipo_tipificacion_estado',default=True),
        Field('tipo_tipificacion_descripcion'),
        Field('tipo_tipificacion_fecha_creacion','integer' ,default=fechaIntModels),
        Field('tipo_tipificacion_hora_creacion','integer',default=horaIntModels),
    )
    db.tipo_tipificacion._enable_record_versioning()
    pass
    
def db_tableTipificaciones():
    if not hasattr(db,'tipo_tipificacion'):
        db_tableTipoTipificacion()  
    db.define_table('tipificacion', 
        Field('tipificacion_identificacion_cliente'),
        Field('tipificacion_nombre_cliente'),
        Field('tipificacion_telefono'),
        Field('tipificacion_resultado','reference tipo_tipificacion'),
        Field('tipificacion_descripcion_resultado','text'),
        Field('tipificacion_numero_producto','text'),
        Field('tipificacion_valor_venta','double', default=0),
        Field('tipificacion_valor_oferta','double', default=0),
        Field('tipificacion_sucursal','integer'),
        Field('tipificacion_asignacion','integer'),
        Field('tipificacion_campana','integer'),
        Field('tipificacion_base','integer'),
        Field('tipificacion_asignacion_historico','reference asignacion_historico'),
        Field('tipificacion_asesor_id','integer'),
        Field('tipificacion_fecha_creacion','integer' ,default=fechaIntModels),
        Field('tipificacion_hora_creacion','integer',default=horaIntModels),
        Field('tipificacion_comentarios','text'),
        Field('tipificacion_dia','integer',default=fechaIntergar('dia')),
        Field('tipificacion_mes','integer',default=fechaIntergar('mes')),
        Field('tipificacion_anio','integer',default=fechaIntergar('anio'))
    )
    db.tipificacion._enable_record_versioning()
    pass

def db_tableBasesAsignacion():
    if not hasattr(db,'tipificacion'):
        db_tableTipificaciones()  
    db.define_table('bases_asignacion', 
        Field('bases_asignacion_asignacion','reference asignaciones'),
        Field('bases_asignacion_base','upload'),
        Field('bases_asignacion_demo','upload'),
        Field('bases_asignacion_creador','integer'),
        Field('bases_asignacion_fecha_creacion','integer' ,default=fechaIntModels),
        Field('bases_asignacion_hora_creacion','integer',default=horaIntModels),
        Field('bases_asignacion_dia','integer',default=fechaIntergar('dia')),
        Field('bases_asignacion_mes','integer',default=fechaIntergar('mes')),
        Field('bases_asignacion_anio','integer',default=fechaIntergar('anio'))
    )
    db.bases_asignacion._enable_record_versioning()
    pass
   
def funciones_tables():
    db_tableBasesAsignacion()
    pass