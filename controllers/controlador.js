let boton=document.getElementById("btnreporte")
boton.addEventListener("click",function(evento){
    evento.preventDefault()

    let conteneder = document.getElementById("contenedor")
    conteneder.classList.remove("d-none")

    let nombreUsuario = document.getElementById("nombre").value
    let mensaje = document.getElementById("mensaje")

    mensaje.textContent=`Apreciado Usario: ${nombreUsuario}, hemos generado su reporte: `
})