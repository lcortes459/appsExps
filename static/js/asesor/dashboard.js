var aseInt = {
    start: function(){ aseInt.ready(); },
    ready: function(){ },
    gestion: function( clienteNombre ){
        var tmp = `
        	<h4 class="modal-title"><b>Cuentanos como te fue con: `+clienteNombre+`</b></h4>
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
        Swal.fire('Felicidades','Gestión guardada con exito','success'); 
    },
};
aseInt.start();