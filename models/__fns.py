# -*- coding: utf-8 -*-
from datetime import  datetime, date, timedelta, time 

def userGetEstado(r):
    resul  = ''
    if r:
        estado = r.registration_key
        if (estado==None) or (estado==''):
            resul = XML(
                """
                    <div id="div_usu_%s" title='Desactivar usuario'>
                        <a href="javascript:template.updateEstado(0,'%s')" class="btn btn-icon btn-success">
                            <i class="fa fa-check"></i>
                        </a>
                    </div>
                """ %(r.id,r.id))
        else:
            resul = XML(
                """
                    <div id="div_usu_%s" title='Activar usuario'>
                        <a href="javascript:template.updateEstado(1,'%s')" class="btn btn-icon btn-danger">
                            <i class="fa fa-times"></i>
                        </a>
                    </div>
                """ %(r.id,r.id))
            pass
        pass
    return resul

def fecha(par):
    import time
    fecha_actual = request.now
    fecha        = str(fecha_actual)[:16]
    if par == 'all':
        fecha = str(fecha_actual)[:16].replace('-','')
    elif par == 'fecha':
        fecha = str(fecha_actual)[:10].replace('-','')
    elif par == 'hora':
        fecha = str(time.strftime("%H:%M:%S")) #Formato de 24 horas
        if str(fecha)[:2] == '00':
            fecha = fecha.replace('00','24').replace(':','')
        else:
            fecha.replace(':','')
            pass
    elif par == 'fecMeDia':
        from datetime import datetime, timedelta
        fecha = datetime.today()+timedelta(days=-1)
    else:
        fecha = str(fecha_actual)[:19].replace('-','')
        pass
    return int(fecha)

def misAsesores():
    misAsesores  = 0
    misAsesores = db(db.auth_user.tipo == 'Asesor').count()
    return misAsesores

def misEmpleados():
    misEmpleados = 0
    misEmpleados = db(db.empleados.empleados_estado == True).count()
    return misEmpleados

def getFotoZoom(r,ws,hs):
    if 'empleados_foto' in r:
        img = r.empleados_foto
    elif 'logo' in r:
        img = r.logo
    if img:
        resul = XML(""" <img   src="%s"  width="%s" height="%s" > """  %(URL('default','download/%s' %(img)),ws,hs) )
    else:
        ff = """ <img src="%s"  width="%s" height="%s"> """ %(URL('static','images/img/user7-128x128.jpg'),ws,hs)
        fh = """ <img src="%s"  width="%s" height="%s"> """ %(URL('static','images/img/user2-160x160.jpg'),ws,hs)
        if r.empleados_genero:
            if r.empleados_genero[0] == 'Femenino':
                resul = XML(ff)
            else:
                resul = XML(fh)
        else:
            resul = ''
    return resul

def emplGetEstado(r):
    resul  = ''
    if r:
        estado = r.empleados_estado
        if (estado==True) or (estado=='True'):
            resul = XML(
                """
                    <div id="div_empl_%s" title='Desactivar ampleado'>
                        <a href="javascript:template.updateEstadoEmplado(0,'%s')" class="btn btn-icon btn-success">
                            <i class="fa fa-check"></i>
                        </a>
                    </div>
                """ %(r.id,r.id))
        else:
            resul = XML(
                """
                    <div id="div_empl_%s" title='Activar empleado'>
                        <a href="javascript:template.updateEstadoEmplado(1,'%s')" class="btn btn-icon btn-danger">
                            <i class="fa fa-times"></i>
                        </a>
                    </div>
                """ %(r.id,r.id))
            pass
        pass
    return resul

def empresaGetEstado(r):
    resul  = ''
    if r:
        estado = r.empresas_estado
        if (estado==True) or (estado=='True'):
            resul = XML(
                """
                    <div id="div_empresa_%s" title='Desactivar empresa'>
                        <a href="javascript:template.updateEstadoEmpresa(0,'%s')" class="btn btn-icon btn-success">
                            <i class="fa fa-check"></i>
                        </a>
                    </div>
                """ %(r.id,r.id))
        else:
            resul = XML(
                """
                    <div id="div_empresa_%s" title='Activar empresa'>
                        <a href="javascript:template.updateEstadoEmpresa(1,'%s')" class="btn btn-icon btn-danger">
                            <i class="fa fa-times"></i>
                        </a>
                    </div>
                """ %(r.id,r.id))
            pass
        pass
    return resul

def getFotoUsuario(id):
    lastIdEmplado   = db(db.usuario_empleado.usuario_empleado_usuario==id).select(db.usuario_empleado.ALL).last()
    if lastIdEmplado:
        empleado = db.empleados[lastIdEmplado.usuario_empleado_empleado]
        
        if empleado.empleados_foto:
            resul = URL('default','download/%s' %(empleado.empleados_foto))
        else:
            ff = URL('static','images/img/user7-128x128.jpg')
            fh = URL('static','images/img/user2-160x160.jpg')
            if empleado.empleados_genero:
                if empleado.empleados_genero[0] == 'Femenino':
                    resul = ff
                else:
                    resul = fh
            else:
                resul = ''
    else:
        resul = URL('static','images/logoGuardianweb.png')
        pass
    return resul 

def insertEstadoLlamada( idRegistro, identificacion, telefono, extUser, idUser ):
    if ( (telefono != '' ) & ( identificacion != '' ) & ( idRegistro != '' )):
        idRegistro = db.control_llamadas.insert(
            control_llamadas_telefono              = telefono,
            control_llamadas_estado_llamada        = 'Proceso',
            control_llamadas_identificacion        = identificacion,
            control_llamadas_id_registro_historica = idRegistro,
            control_llamadas_asesor_ext            = extUser,
            control_llamadas_asesor_id             = idUser
        )
    else:
        idRegistro = 0
        pass
    return idRegistro

def usuarioEmplado( usuario ):
    empleado = db( db.usuario_empleado.usuario_empleado_usuario == usuario ).select( db.empleados.empleados_nombres,left=( db.empleados.on( db.empleados.id == db.usuario_empleado.usuario_empleado_empleado) ) ).last()
    if empleado:
        return empleado.empleados_nombres
    else:
        return 'No se encontro asesor'
        pass
    
def newTeleCliente( idRegistro, telefono ):
    from datetime import date
    from datetime import datetime
    import time
    t = time.localtime()
    current_timeTmp = time.strftime("%H:%M:%S", t)
    now = datetime.now()
    idRegistroNew = 0
    sqlSelectRegistro = """
        SELECT registros_gestion_historica_id_campana, registros_gestion_historica_telefono, registros_gestion_historica_extension, registros_gestion_historica_intento, registros_gestion_historica_identificacion, registros_gestion_historica_nombre, registros_gestion_historica_name, registros_gestion_historica_surname, registros_gestion_historica_estado, registros_gestion_historica_idresultado, registros_gestion_historica_fecha1, registros_gestion_historica_fecha2, registros_gestion_historica_valor1, registros_gestion_historica_valor2, registros_gestion_historica_asesor, registros_gestion_historica_dias_mora, registros_gestion_historica_email, registros_gestion_historica_direccion, registros_gestion_historica_token, registros_gestion_historica_url, registros_gestion_historica_url_enc, registros_gestion_historica_id_cliente, registros_gestion_historica_id_segmento, registros_gestion_historica_id_asignacion, registros_gestion_historica_placa, registros_gestion_historica_v1, registros_gestion_historica_descripcion_v1, registros_gestion_historica_v2, registros_gestion_historica_descripcion_v2, registros_gestion_historica_v3, registros_gestion_historica_descripcion_v3, registros_gestion_historica_v4, registros_gestion_historica_descripcion_v4, registros_gestion_historica_v5, registros_gestion_historica_descripcion_v5, registros_gestion_historica_v6, registros_gestion_historica_descripcion_v6, registros_gestion_historica_v7, registros_gestion_historica_descripcion_v7, registros_gestion_historica_v8, registros_gestion_historica_descripcion_v8, registros_gestion_historica_v9, registros_gestion_historica_descripcion_v9, registros_gestion_historica_v10, registros_gestion_historica_descripcion_v10, registros_gestion_historica_v11, registros_gestion_historica_descripcion_v11, registros_gestion_historica_v12, registros_gestion_historica_descripcion_v12, registros_gestion_historica_v13, registros_gestion_historica_descripcion_v13, registros_gestion_historica_v14, registros_gestion_historica_descripcion_v14, registros_gestion_historica_v15, registros_gestion_historica_descripcion_v15, registros_gestion_historica_v16, registros_gestion_historica_descripcion_v16, registros_gestion_historica_v17, registros_gestion_historica_descripcion_v17, registros_gestion_historica_v18, registros_gestion_historica_descripcion_v18, registros_gestion_historica_v19, registros_gestion_historica_descripcion_v19, registros_gestion_historica_v20, registros_gestion_historica_descripcion_v20, registros_gestion_historica_v21, registros_gestion_historica_descripcion_v21, registros_gestion_historica_v22, registros_gestion_historica_descripcion_v22, registros_gestion_historica_v23, registros_gestion_historica_descripcion_v23, registros_gestion_historica_v24, registros_gestion_historica_descripcion_v24, registros_gestion_historica_v25, registros_gestion_historica_descripcion_v25, registros_gestion_historica_v26, registros_gestion_historica_descripcion_v26, registros_gestion_historica_v27, registros_gestion_historica_descripcion_v27, registros_gestion_historica_v28, registros_gestion_historica_descripcion_v28, registros_gestion_historica_v29, registros_gestion_historica_descripcion_v29, registros_gestion_historica_v30, registros_gestion_historica_descripcion_v30, registros_gestion_historica_producto1, registros_gestion_historica_saldo_capital1, registros_gestion_historica_empresa, registros_gestion_historica_cliente, registros_gestion_historica_segmento, registros_gestion_historica_id_base, registros_gestion_historica_fecha_creacion, registros_gestion_historica_hora
        FROM asesores.registros_gestion_historica
        WHERE registros_gestion_historica_id  = """+str(idRegistro)+"""
    """
    df = pd.DataFrame()
    df = df.append(pd.read_sql_query(sqlSelectRegistro,engine2))
    if len(df) > 0:
        df['registros_gestion_historica_telefono']       = telefono
        df['registros_gestion_historica_fecha_creacion'] = int( str(request.now)[:10].replace('-','') )
        df['registros_gestion_historica_hora']           = int( str(current_timeTmp).replace(':','') )
        df.to_sql('registros_gestion_historica', con=engine2, chunksize=2000, if_exists='append',index=False)
        idRegistroNew  = 1
    else:
        print('Cero registros')
        pass
    return idRegistroNew
    
def SetMoneda(num, simbolo="", n_decimales=2):
    """Convierte el numero en un string en formato moneda
    SetMoneda(45924.457, 'RD$', 2) --> 'RD$ 45,924.46'     
    """
    #num = float(num)
    #con abs, nos aseguramos que los dec. sea un positivo.
    n_decimales = abs(n_decimales)
    #se redondea a los decimales idicados.
    num = round(num, n_decimales)
    #se divide el entero del decimal y obtenemos los string
    num, dec = str(num).split(".")
    #si el num tiene menos decimales que los que se quieren mostrar,
    #se completan los faltantes con ceros.
    dec += "0" * (n_decimales - len(dec))
    #se invierte el num, para facilitar la adicion de comas.
    num = num[::-1]
    #se crea una lista con las cifras de miles como elementos.
    l = [num[pos:pos+3][::-1] for pos in range(0,50,3) if (num[pos:pos+3])]
    l.reverse()
    #se pasa la lista a string, uniendo sus elementos con comas.
    num = str.join(".", l)
    #si el numero es negativo, se quita una coma sobrante.
    try:
        if num[0:2] == "-,":
            num = "-%s" % num[2:]
    except IndexError:
        pass
    #si no se especifican decimales, se retorna un numero entero.
    if not n_decimales:
        return "%s %s" % (simbolo, num)
    return "%s %s" % (simbolo, num)

def fechaFormato(valor,opc):
    if opc == 'fecha':
        anio = str(valor)[:4]
        mes  = str(valor)[4:-2]
        dia  = str(valor)[6:]
        formato = anio+'-'+str(mes)+'-'+str(dia)
    else:
        hora  = str(valor)[:2]
        minu  = str(valor)[2:4]
        segun = str(valor)[4:6]
        if hora == '24':
            hora = hora.replace('24','00')
            pass
        formato = hora+':'+str(minu)+':'+str(segun)
        pass
    return formato

def fechaIntergar( opc ):
    fecha_actual = request.now
    if opc == 'dia':
        resul = fecha_actual.day
    elif opc == 'mes':
        resul = fecha_actual.month
    else:
        resul = fecha_actual.year
        pass
    return resul

def mesCurso(mes):
    mesNumero = int(mes)
    if mesNumero == 1:
        mes = 'enero'
    elif mesNumero == 2:
        mes = 'febrero'
    elif mesNumero == 3:
        mes = 'marzo'
    elif mesNumero == 4:
        mes = 'abril'
    elif mesNumero == 5:
        mes = 'mayo'
    elif mesNumero == 6:
        mes = 'junio'
    elif mesNumero == 7:
        mes = 'julio'
    elif mesNumero == 8:
        mes = 'agosto'
    elif mesNumero == 9:
        mes = 'septiembre'
    elif mesNumero == 10:
        mes = 'octubre'
    elif mesNumero == 11:
        mes = 'noviembre'
    else:
        mes = 'diciembre'
        pass
    return str(mes).capitalize()
    
def creacionCodigo(idAsig,nombreAsig):
    if idAsig:
        codRet = str(nombreAsig).replace(' ','')+'-'+str(idAsig)
    else:
        codRet = 'Cod-00'
        pass
    return codRet
    
    
def SetMonedaValores(num, simbolo="", n_decimales=2):   
    """Convierte el numero en un string en formato moneda
    SetMoneda(45924.457, 'RD$', 2) --> 'RD$ 45,924.46'     
    """
    #num = float(num)
    #con abs, nos aseguramos que los dec. sea un positivo.
    n_decimales = abs(n_decimales)
    #se redondea a los decimales idicados.
    num = round(num, n_decimales)
    #se divide el entero del decimal y obtenemos los string
    num, dec = str(num).split(".")
    #si el num tiene menos decimales que los que se quieren mostrar,
    #se completan los faltantes con ceros.
    dec += "0" * (n_decimales - len(dec))
    #se invierte el num, para facilitar la adicion de comas.
    num = num[::-1]
    #se crea una lista con las cifras de miles como elementos.
    l = [num[pos:pos+3][::-1] for pos in range(0,50,3) if (num[pos:pos+3])]
    l.reverse()
    #se pasa la lista a string, uniendo sus elementos con comas.
    num = str.join(".", l)
    #si el numero es negativo, se quita una coma sobrante.
    try:
        if num[0:2] == "-,":
            num = "-%s" % num[2:]
    except IndexError:
        pass
    #si no se especifican decimales, se resulrna un numero entero.
    if not n_decimales:
        return "%s%s" % (simbolo, num)
    return "%s%s" % (simbolo, num)