function cargar() {
    let pilotos = [];

    for (let i = 0; i < 4; i++) {
        let nombre = prompt(`Ingrese el nombre del piloto ${i + 1}:`);

        let tiempo1 = parseFloat(prompt("Ingrese el tiempo de la vuelta 1:"));
        let tiempo2 = parseFloat(prompt("Ingrese el tiempo de la vuelta 2:"));
        let tiempo3 = parseFloat(prompt("Ingrese el tiempo de la vuelta 3:"));

        let tiempos = [tiempo1, tiempo2, tiempo3];

        pilotos.push([nombre, tiempos]);
    }

    return pilotos;
}


function calcularPromedios(pilotos) {
    console.log("Promedios:");

    for (let [nombre, tiempos] of pilotos) {
        let suma = 0;

        for (let tiempo of tiempos) {
            suma += tiempo;
        }

        let promedio = suma / 3;

        console.log(nombre, "-", promedio, "segundos");
    }
}


function mejorVuelta(pilotos) {
    let mejorTiempo = Infinity;
    let mejorPiloto = "";

    for (let [nombre, tiempos] of pilotos) {
        for (let tiempo of tiempos) {
            if (tiempo < mejorTiempo) {
                mejorTiempo = tiempo;
                mejorPiloto = nombre;
            }
        }
    }

    console.log("Mejor vuelta:");
    console.log("Piloto:", mejorPiloto);
    console.log("Tiempo:", mejorTiempo, "segundos");
}


let pilotos = cargar();

calcularPromedios(pilotos);
mejorVuelta(pilotos);
