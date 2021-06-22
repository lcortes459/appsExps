var emailIngreso = '';
var img;
var ing = {
    stars: function() {
        this.carga();
    },
    carga() {
        var local = JSON.parse(localStorage.getItem("datosUsuario"));
        if (local) {
            $('#body').removeClass('class name');
            $('#body').addClass('hold-transition lockscreen');
            $('#divLogin').hide();
            $('#divLockScreen').show();

            if ((local.img === '0') || (local.img === 0)) {
                img = "/PonosCRM/static/template/dist/img/user2-160x160.jpg";
            } else {
                img = "/PonosCRM/" + local.img;
            }
            $('#divImg,#divNombreUsuario').html('');
            $('#divNombreUsuario').html(local.nombres);
            $('#divImg').html("<img src=" + img + " alt='User Image' sty_le='width:20%'>");
        } else {
            $('#btnIngreso').click(function(event) {

                var emailIngreso = $('#emailIngreso').val();
                var passIngreso = $('#passIngreso').val();
                if (emailIngreso == '') {
                    ing.validaCampo(  'Email','emailIngreso' );
                    return false;
                } else if (passIngreso == '') {
                    ing.validaCampo(  'Password','passIngreso' );
                    return false;
                } else {
                    $('#emailIngreso,#passIngreso,#btnIngreso,#olvidePss').attr("disabled", true);
                    $('#btns_ingreso,#olvidePss').hide();
                    $('#validando').show();
                    $.post('../ingresoUsuario', { emailIngreso: emailIngreso, passIngreso: passIngreso }, function(data, textStatus, xhr) {

                        var dat = JSON.parse(data);
                        if (dat.multi_valores == 'usuario') {
                            Swal.fire({
                                title:'Error',
                                text:'Email no encontrtado',
                                icon:'error',
                                showCancelButton: false,
                                confirmButtonColor: '#1BC5BD',
                                cancelButtonColor: '#d33',
                                confirmButtonText: 'Validar',
                                allowOutsideClick: false,
                                allowEscapeKey:false,
                                allowEnterKey:false,
                            }).then((result) => {
                                if (result.value) {
                                    $('#emailIngreso,#passIngreso,#btnIngreso,#olvidePss').attr("disabled", false);
                                    $('#validando').hide();
                                    $('#btns_ingreso,#olvidePss').show();
                                    $('#emailIngreso').focus();
                                }
                            });
                        } else if (dat.multi_valores == 'invalido') {
                            Swal.fire({
                                title:'Error',
                                text:'Password Invalido',
                                icon:'error',
                                showCancelButton: false,
                                confirmButtonColor: '#1BC5BD',
                                cancelButtonColor: '#d33',
                                confirmButtonText: 'Validar',
                                allowOutsideClick: false,
                                allowEscapeKey:false,
                                allowEnterKey:false,
                            }).then((result) => {
                                if (result.value) {
                                    $('#emailIngreso,#passIngreso,#btnIngreso,#olvidePss').attr("disabled", false);
                                    $('#validando').hide();
                                    $('#btns_ingreso,#olvidePss').show();
                                    $('#passIngreso').focus();
                                }
                            });
                        } else if (dat.multi_valores == 'estado') {
                            Swal.fire({
                                title:'Usuario Bloquedo',
                                text:'Comuniquese con su asesor.',
                                icon:'error',
                                showCancelButton: false,
                                confirmButtonColor: '#1BC5BD',
                                cancelButtonColor: '#d33',
                                confirmButtonText: 'Validar',
                                allowOutsideClick: false,
                                allowEscapeKey:false,
                                allowEnterKey:false,
                            }).then((result) => {
                                if (result.value) {
                                    $('#emailIngreso,#passIngreso,#btnIngreso,#olvidePss').attr("disabled", false);
                                    $('#validando').hide();
                                    $('#btns_ingreso,#olvidePss').show();
                                    $('#passIngreso').focus();
                                }
                            });
                        } else {

                            if (typeof(Storage) !== "undefined") {
                                if ($('#inputCheckbox').is(':checked')) {
                                    mi_objeto = {
                                        usuario: emailIngreso,
                                        nombres: dat.multi_valores,
                                        img: dat.img
                                    }
                                    localStorage.setItem("datosUsuario", JSON.stringify(mi_objeto));
                                    var local = JSON.parse(localStorage.getItem("datosUsuario"));
                                    ing.resulSucces();
                                } else {
                                    localStorage.clear();
                                    ing.resulSucces();
                                }
                            } else {
                                Swal.fire({
                                    title:'Advertencia',
                                    text:'El navegador que está utilizando no soporta el recordar datos',
                                    icon:'error',
                                    showCancelButton: false,
                                    confirmButtonColor: '#1BC5BD',
                                    cancelButtonColor: '#d33',
                                    confirmButtonText: 'Entendido',
                                    allowOutsideClick: false,
                                    allowEscapeKey:false,
                                    allowEnterKey:false,
                                }).then((result) => {
                                    if (result.value) {
                                        window.location.href = '../../default/index';
                                    }
                                });
                            }
                        }
                    });
                }
            });
        }
    },
    limpiarSession: function() {
        localStorage.clear();
        location.reload();
    },

    ingresoSession: function() {
        var local = JSON.parse(localStorage.getItem("datosUsuario"));
        emailIngreso = local.usuario;
        var passIngreso = $('#passwordSession').val();
        if (passIngreso == '') {
            ing.validaCampo(  'Password','passIngreso' );
            return false;
        } else {
            $('#FormIngresoSession,#ingOtroUsuario').hide();
            $('#validandoSession').show();
            $.post('../ingresoUsuario', { emailIngreso: emailIngreso, passIngreso: passIngreso }, function(data, textStatus, xhr) {

                var dat = JSON.parse(data);
                if (dat.multi_valores == 'usuario') {
                    toastr.error('Error', 'Email no encontrtado', { timeOut: 3000 }, toastr.options.onHidden = function() { $('#emailIngreso').focus(); });
                    Swal.fire({
                        title:'Error',
                        text:'Email no encontrtado',
                        icon:'error',
                        showCancelButton: false,
                        confirmButtonColor: '#1BC5BD',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'Validar',
                        allowOutsideClick: false,
                        allowEscapeKey:false,
                        allowEnterKey:false,
                    });
                } else if (dat.multi_valores == 'invalido') {
                    Swal.fire({
                        title:'Error',
                        text:'Password Invalido',
                        icon:'error',
                        showCancelButton: false,
                        confirmButtonColor: '#1BC5BD',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'Validar',
                        allowOutsideClick: false,
                        allowEscapeKey:false,
                        allowEnterKey:false,
                    }).then((result) => {
                        if (result.value) {
                            $('#validandoSession').hide();
                            $('#FormIngresoSession,#ingOtroUsuario').show();
                            $('#passwordSession').focus();
                        }
                    });
                }else if (dat.multi_valores == 'estado') {
                    Swal.fire({
                        title:'Usuario Bloquedo',
                        text:'Comuniquese con su asesor.',
                        icon:'error',
                        showCancelButton: false,
                        confirmButtonColor: '#1BC5BD',
                        cancelButtonColor: '#d33',
                        confirmButtonText: 'Validar',
                        allowOutsideClick: false,
                        allowEscapeKey:false,
                        allowEnterKey:false,
                    }).then((result) => {
                        if (result.value) {
                            $('#emailIngreso,#passIngreso,#btnIngreso,#olvidePss').attr("disabled", false);
                            $('#validando').hide();
                            $('#btns_ingreso').show();
                            $('#passIngreso').focus();
                        }
                    });
                } else {

                    if (typeof(Storage) !== "undefined") {
                        if ($('#inputCheckbox').is(':checked')) {
                            mi_objeto = {
                                usuario: emailIngreso,
                                nombres: dat.multi_valores,
                                img: dat.img
                            }
                            localStorage.setItem("datosUsuario", JSON.stringify(mi_objeto));
                            var local = JSON.parse(localStorage.getItem("datosUsuario"));
                            ing.resulSucces();
                        } else {
                            localStorage.clear();
                            ing.resulSucces();
                        }
                    } else {
                        Swal.fire({
                            title:'Advertencia',
                            text:'El navegador que está utilizando no soporta el recordar datos',
                            icon:'error',
                            showCancelButton: false,
                            confirmButtonColor: '#1BC5BD',
                            cancelButtonColor: '#d33',
                            confirmButtonText: 'Entendido',
                            allowOutsideClick: false,
                            allowEscapeKey:false,
                            allowEnterKey:false,
                        }).then((result) => {
                            if (result.value) {
                                window.location.href = '../../default/index';
                            }
                        });

                    }
                }
            });
        }
    },

    mostrarPassword: function(){
        var cambio = document.getElementById("passIngreso");
        
        if(cambio.type == "password"){
            cambio.type = "text";
            $('.icon').removeClass('fa fa-eye-slash').addClass('fa fa-eye');
        }else{
            cambio.type = "password";
            $('.icon').removeClass('fa fa-eye').addClass('fa fa-eye-slash');
        }
    },

    mostrarPasswordAfter: function(){
        var cambio = document.getElementById("passwordSession");
        
        if(cambio.type == "password"){
            cambio.type = "text";
            $('.icon').removeClass('fa fa-eye-slash').addClass('fa fa-eye');
        }else{
            cambio.type = "password";
            $('.icon').removeClass('fa fa-eye').addClass('fa fa-eye-slash');
        }
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
                popup: 'animate__animated animate__fadeInDown'
            },
            hideClass: {
                popup: 'animate__animated animate__fadeOutUp'
            }
         }).then((result) => {
            if (result.value) {
                $('#'+campo+'').trigger('focus');
            }
        });
    },
    resulSucces(){
        
        Swal.fire({
            position: 'top-end',
            icon: 'success',
            title: 'Datos correctos.',
            text: 'En un momento sera redireccionado a PonosCRM',
            showConfirmButton: false,
            timer: 2000
        }).then(() => {
            window.location.href = '../../default/index'
        });
    },
};
ing.stars();