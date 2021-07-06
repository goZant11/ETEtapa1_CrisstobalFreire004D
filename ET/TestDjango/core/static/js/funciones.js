
// Efectos generales DOM
function CambiarMayusculasContacto()
{
    var a = document.getElementById('nombre');
    a.value = a.value.toUpperCase();
}

function CambiarMayusculasMarca()
{
    var a = document.getElementById('pais');
    a.value = a.value.toUpperCase();
}

function CambiarMayusculas()
{
    var a = document.getElementById('nom');
    a.value = a.value.toUpperCase();
}


// Validación de Sesión

function validacion()
{
    nom= document.getElementById('nom').value;
    email = document.getElementById('ema').value;
    fono = document.getElementById('fono').value;
    pass = document.getElementById('pass').value;
    checkbox = document.getElementById("checkbox1");

    if(nom == null || nom.length<=5 || /^\s+$/.test(nom))
    {
        alert('Debe ingresar un Nombre de Usuario de 5 carácteres mínimo...');
        document.getElementById('nom').value="";
        document.datos.nom.focus();
        return false;
    }

    
    if(email == null || email.length==0 || /^\s+$/.test(email))
    {
        alert('Debe ingresar un Correo...');
        document.getElementById('ema').value="";
        document.datos.ema.focus();
        return false;
    }

    if(!(/^\d{9}$/.test(fono)) )
    {
        alert('Debe ingresar un teléfono de 9 dígitos');
        document.getElementById('fono').value="";
        document.datos.fono.focus();
        return false;
    }   

    if(pass == null || pass.length<8 || /^\s+$/.test(pass))
    {
        alert('Debe ingresar una contraseña de 8 carácteres mínimo...');
        document.getElementById('pass').value="";
        document.datos.pass.focus();
        return false;
    }
    
    if (checkbox.checked){
    }
    else
    {
        alert("Debe aceptar los término y condiciones para poder registrarse...");
        return false;
    }
    return true;      
}


// Validación de aporte
function validacionAporte()
{
    nombre = document.getElementById('nombre').value;
    rut = document.getElementById('rut').value;
    telefono = document.getElementById('telefono').value;
    dir = document.getElementById ('dir').value;
    email = document.getElementById('ema').value;
    pais = document.getElementById('pais').value;
    pass = document.getElementById('pass').value;


    if(rut == null|| nombre.length<=9 ||/^\s+$/.test(rut))
    {
        alert('Debe ingresar un RUT...');
        document.getElementById('rut').value="";
        document.datos.rut.focus();
        return false;
    }

    
    if(nombre == null|| nombre.length==0 ||/^\s+$/.test(nombre))
    {
        alert('Debe ingresar un Nombre...');
        document.getElementById('nombre').value="";
        document.datos.nombre.focus();
        return false;
    }

    

    if(!(/^\d{9}$/.test(telefono)) )
    {
        alert('Debe ingresar un teléfono de 9 dígitos');
        document.getElementById('telefono').value="";
        document.datos.telefono.focus();
        return false;
    }

    if(dir == null|| dir.length==0 ||/^\s+$/.test(dir))
    {
        alert('Debe ingresar una dirección...');
        document.getElementById('dir').value="";
        document.datos.dir.focus();
        return false;
    }

    if(email == null || email.length==0 || /^\s+$/.test(email))
    {
        alert('Debe ingresar un Correo...');
        document.getElementById('ema').value="";
        document.datos.ema.focus();
        return false;
    }

    if(pais == null|| pais.length==0 ||/^\s+$/.test(pais))
    {
        alert('Debe ingresar un Pais...');
        document.getElementById('pais').value="";
        document.datos.pais.focus();
        return false;
    }
    if(pass == null || pass.length<8 || /^\s+$/.test(pass))
    {
        alert('Debe ingresar una contraseña de 8 carácteres mínimo...');
        document.getElementById('pass').value="";
        document.datos.pass.focus();
        return false;
    }
    return true;      
}
