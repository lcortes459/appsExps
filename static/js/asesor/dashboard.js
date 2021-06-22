var idRegistroVar    = 0; 
var observaciones    = ''; 
var tipificacionFin  = ''; 
var tipoContacto     = ''; 
var descripcion      = ''; 
var otraDescripcion  = '';
var aseInt = {
    start: function(){ aseInt.ready(); },
    ready: function(){ },
    gestion: function( idRegistro ){
        idRegistroVar = idRegistro;
        var tmp = `
        	<h4 class="modal-title"><b>Cuentanos como te fue en la gestión</b></h4>
	      	<button type="button" class="close" data-dismiss="modal" aria-label="Close">
		      <span aria-hidden="true">&times;</span>
	      	</button>
        `;
        $('#infoProyectoSubirArchivo').html('Asignacion 1');
		$('#idHeaderModal').html(tmp);
		$('#modalTipificacion').modal('show');
    },
    guardarGestion: function(){
        tipoContacto    = $('#tipoContacto').val();
        descripcion     = $('#descripcionSel').val();
        otraDescripcion = $('#otroDescriptcion').val();
        observaciones   = $('#observaciones').val();
        console.log('tipificacion',tipificacionFin);
        console.log('tipoContacto',tipoContacto);
        console.log('descripcion',descripcion);
        console.log('otraDescripcion',otraDescripcion);
        console.log('observaciones',observaciones);
        if ( parseInt(tipificacionFin) === ' ' ) {
            template.validaCampo('tipoTipificacion','Tipo de tipificación');
            return false;
        } else if ( parseInt(tipoContacto) === ' ' ) {
            template.validaCampo('tipoTipificacion','Tipo de contacto');
            return false;
        } else if ( parseInt(descripcion) === ' ' ) {
            template.validaCampo('tipoTipificacion','Descripción de tipificación');
            return false;
        } else if ( parseInt(observaciones) === ' ' ) {
            template.validaCampo('tipoTipificacion','Observaciones');
            return false;
        } else {
            $('#modalTipificacion').modal('hide');
            template.showPreloader('Un momento mas estamos guardando tu gestión ');
            $.ajax({
                url: 'cerrarGestion',
                type: 'GET',
                dataType: 'json',
                data: {
                    idRegistroVar:idRegistroVar,
                    tipoContacto:tipoContacto,
                    tipificacion: tipificacionFin,
                    descripcion:descripcion,
                    otraDescripcion:otraDescripcion,
                    observaciones:observaciones
                },

            }).done(function( data ) {
                console.log('data', data);
                if ( parseInt(data) > 0 ) {
                    Swal.fire({
                        title:'Felicidades',
                        title:'Gestión guardada con exito',
                        icon:'success',
                        allowOutsideClick: false,
                        allowEscapeKey:false,
                        allowEnterKey:false,
                        showCancelButton: false,
                        confirmButtonColor: '#3085d6',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'Continuar',
                        showClass: {
                          popup: 'animate__animated animate__fadeInLeft'
                        },
                        hideClass: {
                          popup: 'animate__animated animate__fadeOutRight'
                        }
                    }).then((result) => {
                        if (result.value) {
                            window.location.href="";
                        }
                    });
                } else {
                    Swal.fire('No eres tu somos nosotros','No pudimo sguardar tu gestión.\nIntentra nuevamnete','error');
                }
            }); 
        }

    },
    siguienteRegistro: function() {
        
        template.showPreloader('Estamos buscando........');
        $.ajax({
          url: 'buscarRegisto',
          type: 'GET',
          dataType: 'json',
        }).done(function( data ) {
            console.log("success", data);
            template.hidePreloader();
            if (parseInt(data) > 0) {
                template.showPreloader('Encontramos un registro para tí');
                $('#infoPrincipal').hide(function() {
                    $('#infoRegistro').load('infoRegistro',{idRegistro:data},function() {
                        $('#infoRegistro').show(function() {
                            template.hidePreloader();
                            // $('#subTitleAsesor').html('<a href="javascript:aseInt.gestion('+data+');" title="Tipificar gestión"><i class="fa fa-save text-primary" style="font-size:1em;"></i>');
                        });
                    });
                });
            }else {
              template.resulError('No encontramos información para tí');
            }
        });
            
    },
    cargaTipoContacto : function( idSelect ) {
        tipificacion = (idSelect.vidSelectlue || idSelect.options[idSelect.selectedIndex].value);
        if ( parseInt(tipificacion) > 0 ) {

            aseInt.consultarTipoContacto( parseInt(tipificacion) );
        }else{
            $('#tipoContacto').html('<option value="0">Seleccione un opcion</option>');
            $('#tipoContacto').prop("disabled", true);
            $('#btnGuardarGestion').addClass('disabled');  
        }
    },
    consultarTipoContacto : function( tipificacion ) {
        if ( tipificacion === 1 ) {
            var tmp = 'CONTACTO';
        } else {
            var tmp = 'NO CONTACTO';
        }
        tipificacionFin = tmp;
        console.log('Tmp', tmp);
        $.ajax({
            url: 'consultarTipoContacto',
            type: 'GET',
            dataType: 'json',
            data: {tipoTipe: tmp},
        })
        .done(function( data ) {
            $('#tipoContacto').prop("disabled", false);

            if ( data.length > 0 ) {
                var dataHtml = new Array();
                $('#tipoContacto').html('');
                var conteo = 0;
                $.each(data, function(index, val) {
                    if ( conteo === 0 ) {

                        dataHtml.push(

                            `
                                <option value="0">Seleccione un opcion</option>
                                <option value="`+val.tipo_tipificacion_desc_uno+`">`+val.tipo_tipificacion_desc_uno+`</option>
                            `
                        );

                    }else{

                        dataHtml.push(
                            `
                                <option value="`+val.tipo_tipificacion_desc_uno+`">`+val.tipo_tipificacion_desc_uno+`</option>

                            `
                        );
                    }

                    conteo = conteo + 1;    
                });

                $('#tipoContacto').html(dataHtml);
            }else {

                $('#tipoContacto').html('<option value="0">Este tipo de tipificación  no tiene tipos de contactos</option>');
            }
        });
    },
    cargaDescripciones : function( idSelect ) {
        tipoContacto = (idSelect.vidSelectlue || idSelect.options[idSelect.selectedIndex].value);
        if ( tipoContacto != 0 ) {
            aseInt.consultarDescripciones( tipoContacto );
        }else{
            $('#descripcionSel').html('<option value="0">Seleccione un opcion</option>');
            $('#descripcionSel').prop("disabled", true);
            $('#btnGuardarGestion').addClass('disabled');
        }
    },
    consultarDescripciones : function( tipoContacto ) {
        
        $.ajax({
            url: 'consultarDescripciones',
            type: 'GET',
            dataType: 'json',
            data: {tipoContacto: tipoContacto},
        })
        .done(function( data ) {
            $('#descripcionSel').prop("disabled", false);
            if ( data.length > 0 ) {
                var dataHtml = new Array();
                $('#descripcionSel').html('');
                var conteo = 0;
                $.each(data, function(index, val) {
                    if ( conteo === 0 ) {

                        dataHtml.push(

                            `
                                <option value="0">Seleccione un opcion</option>
                                <option value="`+val.tipo_tipificacion_desc_dos+`">`+val.tipo_tipificacion_desc_dos+`</option>
                            `
                        );

                    }else{

                        dataHtml.push(
                            `
                                <option value="`+val.tipo_tipificacion_desc_dos+`">`+val.tipo_tipificacion_desc_dos+`</option>

                            `
                        );
                    }

                    conteo = conteo + 1;    
                });

                $('#descripcionSel').html(dataHtml);
            }else {

                $('#descripcionSel').html('<option value="0">Este tipo de contacto no tiene descripciones</option>');
            }
        });
    },
    cargaOtrasDescripciones : function( idSelect ) {
        descripcion = (idSelect.vidSelectlue || idSelect.options[idSelect.selectedIndex].value);
        if ( descripcion != 0 ) {
            aseInt.consultarOtrsDescripciones( descripcion );
            $('#btnGuardarGestion').removeClass('disabled');
        }else{
            $('#otroDescriptcion').html('<option value="0">Seleccione un opcion</option>');
            $('#otroDescriptcion').prop("disabled", true); 
            $('#btnGuardarGestion').addClass('disabled'); 
        }
    },
    consultarOtrsDescripciones : function( descripcion ) {
            
        $.ajax({
            url: 'consultarOtrsDescripciones',
            type: 'GET',
            dataType: 'json',
            data: {descripcion: descripcion},
        })
        .done(function( data ) {
            $('#otroDescriptcion').prop("disabled", false);
            if ( data.length > 0 ) {
                var dataHtml = new Array();
                $('#otroDescriptcion').html('');
                var conteo = 0;
                $.each(data, function(index, val) {
                    if ( conteo === 0 ) {

                        dataHtml.push(

                            `
                                <option value="0">Seleccione un opcion</option>
                                <option value="`+val.tipo_tipificacion_desc_tres+`">`+val.tipo_tipificacion_desc_tres+`</option>
                            `
                        );

                    }else{

                        dataHtml.push(
                            `
                                <option value="`+val.tipo_tipificacion_desc_tres+`">`+val.tipo_tipificacion_desc_tres+`</option>

                            `
                        );
                    }
                    conteo = conteo + 1;    
                });
                $('#otroDescriptcion').html(dataHtml);
            }else {

                $('#otroDescriptcion').html('<option value="0">Este tipo de contacto no tiene otras descripciones</option>');
            }
        });
    },
};
aseInt.start();