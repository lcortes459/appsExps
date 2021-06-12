var bsa = {
	start: function() {
		
		this.ready();
	},

	ready: function() {
		$('#idListadoProyectosCarguesTable').DataTable({
			"order": [[ 0, "asc" ]]
		});

		$("#formuploadProyectoFile").submit(function(e) {
            e.preventDefault();
                 
            var data = new FormData();
            if($('#formuploadProyectoFile input[type=file]').val()==''){

                Swal.fire('Error..!','No se ha adjuntado ningun archivo','error');                 
                return false
            }                                                                                                                                                                                    

            jQuery.each($('#formuploadProyectoFile input[type=file]')[0].files, function(i, file) {
                data.append('file', file);
            });

            $('#modalCargueArchivo').modal('hide');
            
            $('#showResutado').modal('show');


            $.ajax({
                url: 'cargueBase',
                type: 'post',               
                contentType: false,
                processData: false,                
                data: data,
                dataType: 'json',
            })
            .done(function(data) {
            	console.log('data',data);
                console.log('data', data[0].estado);
                
                if(data.estado=='error'){
                    Swal.fire('Error!!!','El sistema no puede reconocer el archivo indicado, verifica e intenta nuevamente','error');                                          
                 	$('#showResutado').modal('hide');
                }else{
                	var resultados = `
                        <tr class="headeTable">
                            <td>Concepto</td><td>Creados</td><td>Asignados</td>
                        </tr>
                		<tr>
                			<td>Parqueaderos</td><td>`+data[0].parqueaderos+`</td><td>En proceso...</td>
                		</tr>
                		<tr>
                			<td>Bodegas</td><td>`+data[0].bodegas+`</td><td>En proceso...</td>
                		</tr>
                		<tr>
                			<td>Inmuebles</td><td>`+data[0].inmuebles+`</td><td>En proceso...</td>
                		</tr>
                		<tr>
                			<td>Propietarios</td><td>`+data[0].propietarios+`</td><td>En proceso...</td>
                		</tr>
                		<tr>
                			<td>Residentes</td><td>`+data[0].residentes+`</td><td>En proceso...</td>
                		</tr>
                        <tr>
                            <td>Mascotas</td><td>`+data[0].mascotas+`</td><td>En proceso...</td>
                        </tr>
                        <tr>
                            <td>Vehiculos</td><td>`+data[0].vehiculos+`</td><td>En proceso...</td>
                        </tr>
                        <tr>
                            <td>Colaboradores</td><td>`+data[0].colaboradores+`</td><td>En proceso...</td>
                        </tr>

                	`;
                	$("#tituloResultado").html('Resultado carga de configuración');

                    $('#tableSucces').html(resultados);
                    $('#tableError').html(resultados);
                    $("#closeModalUpload").hide();
                    Swal.fire('','Subida de archivo finalizada, verifica el resultado del proceso ','success');               
                    $("#infoLoad").hide();
                    $("#msgREsultado").show()
                }                                                            
            })
            .fail(function(){
               	Swal.fire('Error!!!','Se ha presentado un error al momento de procesar el archivo, por favor intenta nuevamente; si el error persiste comunicate con el administrador','error');                                           
                $('#showResutado').modal('hide');

            })
            ;
        });
	},

	cargarFormato: function( idProyec, nombreProyec ) {

		bsa.idProyecto     = idProyec;
		bsa.nombreProyecto = nombreProyec;
        var tmp = `
        	<h4 class="modal-title"><b>`+bsa.nombreProyecto+`</b></h4>
	      	<button type="button" class="close" data-dismiss="modal" aria-label="Close">
		      <span aria-hidden="true">&times;</span>
	      	</button>
        `;
        $('#infoProyectoSubirArchivo').html(bsa.nombreProyecto);
		$('#idHeaderModal').html(tmp);
		$('#modalCargueArchivo').modal('show');
	},
};

bsa.start();