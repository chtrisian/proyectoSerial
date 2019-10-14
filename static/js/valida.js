$("#formulario").validate(
    {
        rules:{
            "txtEmail":{
                required:true,
                email:true
            },
            "txtNombre":{
                required:true,
                minlength:4
            },
            "txtTelefono":{
                required:true,
                maxlength:9,
                minlength:9,
                number:true
            },
            "txtFechaNacimiento":{
                required:true                
            }
        },
        messages:{
            "txtEmail":{
                required:"Es necesario su eMail para el registro",
                email:"No tiene el formato eMail"
            },
            "txtNombre":{
                required:"Es necesario el nombre en el registro",
                minlength:"Mínimo 4 carácteres"
            },
            "txtTelefono":{
                required:"Es necesario su número de teléfono para el registro",
                maxlength:"Deben ser 9 dígitos en su número de contacto",
                minlength:"Deben ser 9 dígitos en su número de contacto"
            },
            "txtFechaNacimiento":{
                required:"La fecha de nacimiento es obligatoria para el registro"
            }            
        }
    }
)