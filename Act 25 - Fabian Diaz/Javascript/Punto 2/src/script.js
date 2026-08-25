function cargar() {
    let coordenadas = [];

    for (let i = 0; i < 4; i++) {
        console.log("Cámara " + (i + 1));

        let lat = parseFloat(prompt("Ingrese la latitud:"));
        let lon = parseFloat(prompt("Ingrese la longitud:"));

        coordenadas.push([lat, lon]);
    }

    return coordenadas;
}

function listarPosiciones(coordenadas) {
    console.log("Posiciones de las cámaras:");

    for (let [lat, lon] of coordenadas) {
        console.log("Latitud:", lat, "Longitud:", lon);
    }
}

function filtrarHemisferio(coordenadas) {
    let cantidad = 0;

    for (let [lat, lon] of coordenadas) {
        if (lat > 0) {
            cantidad++;
        }
    }

    console.log(
        "Cantidad de cámaras en el hemisferio norte:",
        cantidad
    );
}

let coordenadas = cargar();
listarPosiciones(coordenadas);
filtrarHemisferio(coordenadas);
