let edad = 31
const nombre = "Adán"
let calificaciones = [5.5, 4.0, 7.0, 6.4, 6.0]
let frutas_favoritas = ["Pera", "Manzana", "Plátano"]

console.log(edad)
console.log(nombre)
console.log(calificaciones)
console.log(frutas_favoritas)

frutas_favoritas.push("Sandía", "Melón")
console.log(frutas_favoritas[0])
console.log(frutas_favoritas)

for(let i = 0; i < frutas_favoritas.length; i++ ){
    console.log(frutas_favoritas[i])
}