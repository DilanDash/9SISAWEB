function cifradoCesar(texto, desplazamiento) {
    let resultado = "";
    for (let i = 0; i < texto.length; i++) {
      let caracter = texto[i];
      if (caracter.match(/[a-z]/i)) {
        let codigo = texto.charCodeAt(i);
        if (codigo >= 65 && codigo <= 90) {
          caracter = String.fromCharCode(((codigo - 65 + desplazamiento) % 26) + 65);
        } else if (codigo >= 97 && codigo <= 122) {
          caracter = String.fromCharCode(((codigo - 97 + desplazamiento) % 26) + 97);
        }
      }
      resultado += caracter;
    }
    return resultado;
  }
  
  function cifrarTexto() {
    let textoOriginal = document.getElementById("texto-original").value;
    let desplazamiento = parseInt(document.getElementById("desplazamiento").value);
    let textoCifrado = cifradoCesar(textoOriginal, desplazamiento);
    document.getElementById("texto-cifrado").value = textoCifrado;
  }
  