var tipificacion;
var template = {
    stars: function() {
        this.carga()
    },

    avisoDeLogaut: function() {
        Swal.fire({
            title:'Aviso.!',
            text:'¿Desea cerrar la sesión?',
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
                window.location.href="../default/user/logout";
            }
        });
    },

    carga() {},
    limpiar:function(form,input) {
       $('#'+form+'')[0].reset();
       $('#'+input+'').focus();
    },
    validaCampo(selector,campo){
        Swal.fire({
            title:'Campo '+selector+' vacío',
            icon:'warning',
            confirmButtonText: 'Validar',
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
                $('#'+campo+'').trigger('focus');
            }
        });
    },
    resulError(mensaje){
        Swal.fire('Error',''+mensaje+'','error');
    },
    resulSucces(mensaje,smsBotonOk){
        Swal.fire({
            title:'Felicidades',
            text:mensaje,
            icon:'success',
            showCancelButton: false,
            confirmButtonColor: '#1BC5BD',
            cancelButtonColor: '#d33',
            confirmButtonText: smsBotonOk,
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
                window.location.href=" ";
            }
        });
    },
    showPreloader: function(txt){
        var datosHtml = `
            <p align="center" style="font-size:12px;text-align:center;">
            Un momento por favor <br>`+txt+`
            </p>
            <hr>
            <p align="center">
                <i class="fa fa-spinner fa-spin"  style="font-size:35px;color:#00c600;text-align:center;"></i>
            </p>
        `;
        Swal.fire({
            html: datosHtml,
            allowOutsideClick: false,
            allowEscapeKey: false,
            allowEnterKey: false,
            showDenyButton: false,
            showCancelButton: false,
            showConfirmButton: false,
            showClass: {
                popup: 'animate__animated animate__fadeInLeft'
            },
            hideClass: {
                popup: 'animate__animated animate__fadeOutRight'
            }
        });
    },
    hidePreloader: function(){
        Swal.close();
    },
    number_format:function(amount,decimals) {
	    amount += ''; // por si pasan un numero en vez de un string
	    amount = parseFloat(amount.replace(/[^0-9\.]/g, '')); // elimino cualquier cosa que no sea numero o punto

	    decimals = decimals || 0; // por si la variable no fue fue pasada

	    // si no es un numero o es igual a cero retorno el mismo cero
	    if (isNaN(amount) || amount === 0) 
	        return parseFloat(0).toFixed(decimals);

	    // si es mayor o menor que cero retorno el valor formateado como numero
	    amount = '' + amount.toFixed(decimals);

	    var amount_parts = amount.split('.'),
	        regexp = /(\d+)(\d{3})/;

	    while (regexp.test(amount_parts[0]))
	        amount_parts[0] = amount_parts[0].replace(regexp, '$1' + '.' + '$2');

	    return amount_parts.join('.');
    },
    asigEmpleado: function(usu){
        $('#asignarEmpleado_'+usu).load('empleadosAsig',{usu: usu});    
    },
    asignarEmpleado: function(usu,empl) {
        
        if ( (empl == 0) || (empl == '0')) {
            var texto = 'Este usuario quedara sin un empleado asignado';
            var textoFinal = 'Operación finalizada con éxito';
        } else {
            var texto = "El usuario se le asignara un empleado!";
            var textoFinal = "El empleado se ha asignado Exitosamente.";
        }
        Swal.fire({
            title: texto,   
            text: "Esta seguro de continuar el proceso?",   
            icon: "info",   
            showCancelButton: true,   
            cancelButtonText: "Cancelar",   
            confirmButtonColor: "#007bff",   
            confirmButtonText: "Si, continuar",
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
                
                if(empl==''){
                    Swal.fire("Error!", "Debe seleccionar un empleado!", "error");
                }else{
                    $.post('asignarEmpleado', {empl: empl, usu: usu}, function(data, textStatus, xhr) {
                        if ( (data == '0') || (data == 0)) {
                            Swal.fire("Wirning", "El usuario ya tiene un empleado asignado.", "warning");
                        } else if ( data == 'error' ) {
                            Swal.fire("Error", "No pudimos procesar su solicitud, Intente nuevemente.", "error");
                        }else {
                            $("#asignarEmpleado_"+usu).html(data);
                            Swal.fire("Felicidades", textoFinal, "success");
                        }
                    });
                }
            }
        }); 
    },
    cerrarAsigEmpl: function(usu){
        
        $.post('cerrarAsigEmpl', {usu: usu}, function(data, textStatus, xhr) {
            $("#asignarEmpleado_"+usu).html(data);
        });    
    },
    updateEstado: function(est,usu){
        Swal.fire({
            title: "El estado se modificara!",   
            text: "Esta seguro de continuar el proceso?",   
            icon: "info",   
            showCancelButton: true,   
            cancelButtonText: "Cancelar",   
            confirmButtonColor: "#007bff",   
            confirmButtonText: "Si, continuar",   
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
                $.post('updateEstado', {est: est, usu: usu}, function(data, textStatus, xhr) {
                    $("#div_usu_"+usu).html(data);
                    Swal.fire("Felicidades!", "Estado modificado Exitosamente!", "success");
                });
            }
        });
    },
    updateEstadoEmplado: function(est,empl){
        Swal.fire({
            title: "El estado se modificara!",   
            text: "Esta seguro de continuar el proceso?",   
            icon: "info",   
            showCancelButton: true,   
            cancelButtonText: "Cancelar",   
            confirmButtonColor: "#007bff",   
            confirmButtonText: "Si, continuar",   
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
                console.log('est', est);
                console.log('empl', empl);
                $.post('updateEstadoEmplado', {est: est, empl: empl}, function(data, textStatus, xhr) {
                    // $("#div_empl_"+empl).html(data);
                    Swal.fire("Felicidades!", "Estado modificado Exitosamente!", "success");
                    window.location.href = '';
                });
            }
        });
    },
    updateEstadoEmpresa: function(estado,empresa){
        Swal.fire({
            title: "El estado se modificara!",   
            text: "Esta seguro de continuar el proceso?",   
            icon: "info",   
            showCancelButton: true,   
            cancelButtonText: "Cancelar",   
            confirmButtonColor: "#007bff",   
            confirmButtonText: "Si, continuar",   
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
                console.log('estado', estado);
                console.log('empresa', empresa);
                $.post('updateEstadoEmpresa', {estado: estado, empresa: empresa}, function(data, textStatus, xhr) {
                    $("#div_empresa_"+empresa).html(data);
                    Swal.fire("Felicidades!", "Estado modificado Exitosamente!", "success");
                });
            }
        });
    },
    regresarGnrl:function( hide,show ){
        $('#'+hide+'').hide();
        $('#'+show+'').show();
        $('#subTitleAsesor').html('');
    },
};
template.stars();