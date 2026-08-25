function cargar() {
    let inventario = [];

    for (let i = 0; i < 5; i++) {
        console.log("Componente", i + 1);

        let nombre = prompt("Ingrese el nombre del artículo:");
        let precio = parseFloat(prompt("Ingrese el precio:"));
        let stock = parseInt(prompt("Ingrese el stock:"));

        let articulo = {
            nombre: nombre,
            precio: precio,
            stock: stock
        };

        inventario.push(articulo);
    }

    return inventario;
}

function imprimirListado(inventario) {
    console.log("Listado de artículos:");

    for (let articulo of inventario) {
        console.log("Artículo:", articulo.nombre);
        console.log("Precio:", articulo.precio);
        console.log("Stock:", articulo.stock);
    }
}

function valorInventario(inventario) {
    let total = 0;

    for (let articulo of inventario) {
        total += articulo.precio * articulo.stock;
    }

    console.log("Valor total del inventario:", total);
}

function alertaReposicion(inventario) {
    console.log("Artículos que necesitan reposición:");

    for (let articulo of inventario) {
        if (articulo.stock <= 10) {
            console.log("¡Comprar urgentemente:", articulo.nombre);
        }
    }
}

let inventario = cargar();

imprimirListado(inventario);
valorInventario(inventario);
alertaReposicion(inventario);
