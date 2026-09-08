/*1. Confeccionar una página que muestre dos objetos de la clase RADIO solicitando que
seleccione si es mayor de 18 años o no. Al presionar un botón mostrar un alert
indicando si puede ingresar al sitio o no.*/

function verificar(){
    let radio1 = document.getElementById("radio1").checked
    let radio2 = document.getElementById("radio2").checked

    if(radio1){
        alert("Usted puede ingresar al sitio")
    }
    if(radio2){
        alert("Usted no puede ingresar al sitio")
    }
}