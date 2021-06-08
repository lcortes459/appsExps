var rTime = {
    start: function() {
        this.carga()
    },
    carga() {},
    noti_pantalla: function(title,body,time,cantidadDia, cantidadMes){
        // showWebNotification(title,body,null,null, time);
        $('#divCantidadInteresadoGerentesDia').html(cantidadDia);
		$('#divCantidadInteresadoGerentesMes').html(cantidadMes);
    },
    noti_ingresoAsesor: function( asesor,cantidadAsesores ){
        template.resulSucces('Acaba de ingresar '+asesor+'','Entendido');
		$('#divCantidadAsesoresConectados').html(cantidadAsesores);
    },
    newInfoResulLlamadaAsesor: function( resultado ){
        Swal.fire({
            title:'Aviso.!',
            text:'El resultado de la llamada anterior es: '+resultado+'',
            icon:'success',
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Volver a llamar >>',
            cancelButtonText: 'No',
            allowOutsideClick: false,
            allowEscapeKey:false,
            allowEnterKey:false,
            showClass: {
                popup: 'animate__animated animate__fadeInLeft'
            },
            hideClass: {
            popup: 'animate__animated animate__fadeOutRight'
            }
        }).then((result) => {
            if (result.value) {
                Swal.close();
            }
        });
    },
    noti_descargaArchivo: function( archivo,opcDescarga ){
        Swal.fire({
            title:'Aviso.!',
            text:'Ya tenemos tu archivo de la gestión del '+opcDescarga+'.\nHaz click en descargar',
            icon:'success',
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Descargar >>',
            cancelButtonText: 'No',
            allowOutsideClick: false,
            allowEscapeKey:false,
            allowEnterKey:false,
            showClass: {
                popup: 'animate__animated animate__fadeInLeft'
            },
            hideClass: {
            popup: 'animate__animated animate__fadeOutRight'
            }
        }).then((result) => {
            if (result.value) {
                window.location.href="http://advisers.intelibpo.com/init/static/archivosDescarga/"+archivo+"";
            }
        });
    },
	newTrasferenciaAsesor: function( cliente,asesor,idRegistro,identificacion ){
        console.log('Que putas pasa');
        Swal.fire({
            title: "Nueva transferencia!!!",   
            html: "<b>En segundos recibirás una transferencia con el cliente: "+cliente+"\n</b>",   
            icon: "info",   
            showCancelButton: false,   
            cancelButtonText: "Cancelar",   
            confirmButtonColor: "#007bff",   
            confirmButtonText: "Ver información",   
            allowOutsideClick: false,
            allowEscapeKey: false,
            allowEnterKey:false,
            showClass: {
              popup: 'animate__animated animate__fadeInLeft'
            },
            hideClass: {
              popup: 'animate__animated animate__fadeOutRight'
            }
        }).then((result) => {
            if (result.value) {
				$('#buscarListaCliente').hide();
                $('#informacionClienteTransferencia').load('informacionClienteTransferencia',{idRegistro: idRegistro},function(){});
            }
        });
    },
    newLeads( fechaCreacion, cliente, identificacion, segmento, cantRegistrosLeads, campana ) {
        $('#trId_'+identificacion+'_Segmento_'+segmento+'_campana_'+campana+'').remove();
		$('#tbodyIdLeasAsesores').append(`
			<tr id="trId_`+identificacion+`_Segmento_`+segmento+`_campana_`+campana+`">
				<td>`+fechaCreacion+`</td>
				<td>`+cliente+`</td>
				<td>`+identificacion+`</td>
				<td>`+segmento+`</td>
                <td>`+campana+`</td>
				<td>
					<span class="label label-lg font-weight-bold label-light-success label-inline cursor" data-toggle="tooltip" title="Trazabilidad de `+cliente+`" onclick="opr.trazabilidadLanding('`+identificacion+`','`+cliente+`');">`+cantRegistrosLeads+`</span>
				</td>
				<td nowrap="nowrap">
					<a href="javascript:opr.llamarAclienteLanding('1','Luis Cortes','VENTAS_ASESOR');" cla_ss="btn btn-sm btn-light btn-shadow mr-2" class="pulse pulse-primary btn btn-sm btn-light btn-shadow btn-icon mr-2" data-toggle="tooltip" title="Llamar a `+cliente+`">
					<span class="svg-icon svg-icon-primary svg-icon-2x">
						<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24px" height="24px" viewBox="0 0 24 24" version="1.1">
						<g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
							<rect x="0" y="0" width="24" height="24"/>
							<path d="M7.5,4 L7.5,19 L16.5,19 L16.5,4 L7.5,4 Z M7.71428571,2 L16.2857143,2 C17.2324881,2 18,2.8954305 18,4 L18,20 C18,21.1045695 17.2324881,22 16.2857143,22 L7.71428571,22 C6.76751186,22 6,21.1045695 6,20 L6,4 C6,2.8954305 6.76751186,2 7.71428571,2 Z" fill="#000000" fill-rule="nonzero"/>
							<polygon fill="#000000" opacity="0.3" points="7.5 4 7.5 19 16.5 19 16.5 4"/>
						</g>
						</svg>
					</span>
					<span class="pulse-ring"></span>
					</a>
				</td>
			</tr>
        `);
	},
	sacarLlamadaTransferencia: function( idRegistro, identificacion, telefono, cliente ) {
		Swal.fire({
            html:'<p><b>Aviso.!<b><hr>¿Desea llamar a: '+cliente+' </hr>',
            icon:'info',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si',
            cancelButtonText: 'No',
            allowOutsideClick: false,
            allowEscapeKey:false,
            allowEnterKey:false,
            showClass: {
                popup: 'animate__animated animate__fadeInLeft'
            },
            hideClass: {
            popup: 'animate__animated animate__fadeOutRight'
            }
        }).then((result) => {
            if (result.value) {
				template.showPreloader('Estamos contactando a <br><br>'+cliente+'</br>');
				$.ajax({
					url: 'sacarLlamadaTransferencia',
					type: 'GET',
					dataType: 'json',
					data: {
						idRegistro     : idRegistro,
						identificacion : identificacion,
						telefono       : telefono
					},
				})
				.done(function( data ) {
					if ( parseInt(data) === 0 ) { 
						Swal.close();
						$('#subTituloSubheader').html('Asesor')
						$('#tituloSubheader').html('<a class="btn btn-outline-success pulse pulse-success" style="cursor:none;">Llamado...</a>');
						$('#idTr_'+telefono+'').addClass('table-primary');
					} else {
						template.resulError('No fue posible realizar la llamada.\ Intenta nuevamente.');
					}
				});
            }
        });
	},
    conRt: function( url ){
        rTime.websocket(url, function(e){eval(e.data)});
    },
    websocket:function(url, onmessage, onopen, onclose) {
        console.log(url);
        if("WebSocket" in window) {
            var ws = new WebSocket(url);
            ws.onopen = onopen ? onopen : (function() {});
            ws.onmessage = onmessage;
            ws.onclose = onclose ? onclose : (function() {});
            return true; /* supported */
        } else return false; /* not supported */
    },
};
rTime.start();
