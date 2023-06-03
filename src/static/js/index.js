/**
 * Función para calcular la magnitud 
 * @param {Datos en formato JSON} Son los datos procesados en parte real e imaginaria  
 * @returns La magnitud de los datos recibidos en el JSON
 */
function calcularMagnitud(numeroComplejo) {
  // Se declaran las variables real e imaginaria
  let parteReal = numeroComplejo.real;
  let parteImaginaria = numeroComplejo.imaginary;
  // Se declara el array vacío para almacenar la magnitud
  let magnitudes = [];

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
  // Hace una solicitud HTTP al archivo JSON guardado por Flask
  .then((response) => response.json())

  // Se le pasa el argumento data a .then
  .then((data) => {

    // Referencia el elemento canvas en el HTML
    var canvas = document.getElementById("myChart");

    // Crea un contexto 2D para dibujar en el canvas
    var ctx = canvas.getContext("2d");

    // Se define la frecuencia de muestreo en HZ
    var frecuenciaMuestreo = 1;

    // Guarda en una variable los resultados de pasar los datos del JSON a la función para obtener la magnitud
    var datosMagnitud = calcularMagnitud(data);

    // Se definen los datos de la onda a través de un ciclo for
    var data = [];
    for (var i = 0; i < datosMagnitud.length; i++) {
      var valorX = i / frecuenciaMuestreo;
      data.push({ x: valorX, y: datosMagnitud[i] });
    }

    // Se define la configuración del gráfico
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

    // Se crea el gráfico utilizando Chart.js
    var myChart = new Chart(ctx, chartConfig);
    // ...
  })
  .catch((error) => {
    // Manejo de errores
    console.error("Error:", error);
  });

// Se obtiene una referencia al botón de reinicio por su ID
var reiniciarBtn = document.getElementById('reiniciar-btn');

// Se agrega un evento de clic al botón de reinicio
reiniciarBtn.addEventListener('click', function () {
  // Redirecciona a la página inicial
  window.location.href = '/';
});
