function cargar() {
    let temperaturas = [];

    for (let i = 0; i < 6; i++) {
        let temperatura = parseInt(
            prompt(`Ingrese la temperatura ${i + 1}:`)
        );

        temperaturas.push(temperatura);
    }

    return temperaturas;
}

function extremos(temperaturas) {
    let maximo = temperaturas[0];
    let minimo = temperaturas[1];

    for (let temperatura of temperaturas) {
        if (maximo < temperatura) {
            maximo = temperatura;
        } else if (minimo > temperatura) {
            minimo = temperatura;
        }
    }

    return [maximo, minimo];
}

let temperaturas = cargar();

let [maximo, minimo] = extremos(temperaturas);

console.log(`La temperatura máxima es: ${maximo}`);
console.log(`La temperatura mínima es: ${minimo}`);
