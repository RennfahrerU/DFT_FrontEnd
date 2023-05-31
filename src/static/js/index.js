function calcularMagnitud(numeroComplejo) {
  let parteReal = numeroComplejo.real;
  let parteImaginaria = numeroComplejo.imaginary;
  let magnitudes = [];

  // Verificar que los dos arrays tengan la misma longitud
  if (parteReal.length !== parteImaginaria.length) {
    console.error(
      "Error: Los arrays de parte real e imaginaria deben tener la misma longitud"
    );
    return magnitudes;
  }
  //se calcula la magnitud y se agrega al array
  for (let i = 0; i < parteReal.length; i++) {
    let real = parteReal[i];
    let imaginaria = parteImaginaria[i];
    let magnitud = Math.sqrt(Math.pow(real, 2) + Math.pow(imaginaria, 2));
    magnitudes.push(magnitud);
  }
  return magnitudes;
}

fetch("/data.json")
  .then((response) => response.json())
  .then((data) => {
    // Aquí puedes trabajar con los datos JSON
    console.log(data);
    let magnitud = [];
    //console.log(calcularMagnitud(data));

    // Obtén una referencia al elemento canvas
    var canvas = document.getElementById("myChart");

    // Crea un contexto 2D para dibujar en el canvas
    var ctx = canvas.getContext("2d");

    // Definir los datos de la onda
    var frecuenciaMuestreo = 1; // Frecuencia de muestreo en Hz

    var datosMagnitud = calcularMagnitud(data);
    console.log("las magnitudes importadas son: " + datosMagnitud);

    var data = [];
    for (var i = 0; i < datosMagnitud.length; i++) {
      var valorX = i / frecuenciaMuestreo;
      data.push({ x: valorX, y: datosMagnitud[i] });
    }

    // Configura la configuración del gráfico
    var chartConfig = {
      type: "line",
      data: {
        datasets: [
          {
            label: "Onda",
            data: data,
            borderColor: "blue",
            fill: false,
          },
        ],
      },
      options: {
        responsive: true,
        scales: {
          x: {
            type: "linear",
            position: "bottom",
            beginAtZero: true,
          },
          y: {
            beginAtZero: true,
          },
        },
      },
    };

    // Crea el gráfico utilizando Chart.js
    var myChart = new Chart(ctx, chartConfig);
    // ...
  })
  .catch((error) => {
    // Manejo de errores
    console.error("Error:", error);
  });
