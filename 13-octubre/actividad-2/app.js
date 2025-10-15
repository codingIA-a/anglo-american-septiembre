let contador = 0;
let numero = document.getElementById("id-numero");
numero.textContent = "texto desde javascript";

function sumar(){
    contador ++;
    document.getElementById("id-numero").innerText = contador;
}

function restar(){
    contador --;
    document.getElementById("id-numero").innerText = contador;
}