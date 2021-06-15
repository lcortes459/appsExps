var aseInt = {
    start: function(){ aseInt.ready(); },
    ready: function(){ },
    gestion: function( idRegistro ){
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
        $('#modalTipificacion').modal('hide');
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
                            $('#subTitleAsesor').html('<a href="javascript:aseInt.gestion('+data+');" title="Tipificar gestión"><i class="fa fa-save text-primary" style="font-size:1em;"></i>');
                        });
                    });
                });
            }else {
              template.resulError('No encontramos información para tí');
            }
        });
            
    },
};
aseInt.start();