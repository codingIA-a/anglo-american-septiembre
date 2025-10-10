let contador = 0
let evento = true

while (evento === true){
    contador ++;
    console.log(contador)
    if (contador === 10){
        evento = false
    }
}