const int rele1Pin = 8; // Pin digital para el relé 1
const int rele2Pin = 9; // Pin digital para el relé 2
const int rele3Pin = 10; // Pin digital para el relé 3
const int rele4Pin = 11; // Pin digital para el relé 4

int valorAnterior = 0; // Variable para almacenar el último valor leído
int repeticiones = 0; // Contador de repeticiones

void setup() {
  Serial.begin(9600);
  pinMode(rele1Pin, OUTPUT);
  pinMode(rele2Pin, OUTPUT);
  pinMode(rele3Pin, OUTPUT);
  pinMode(rele4Pin, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char comando = Serial.read();

    if (comando == valorAnterior) {
      repeticiones++;
    } else {
      repeticiones = 0; // Reiniciar el contador si el valor cambia
    }

    if (repeticiones < 3) { // Solo procesar el valor si no se repite 3 veces
      switch (comando) {
        case 'a':
          digitalWrite(rele1Pin, HIGH);
          Serial.println("Rele 1 activado");5
          break;
        case 'b':
          digitalWrite(rele2Pin, HIGH);
          Serial.println("Rele 2 activado");
          break;
        case 'c':
          digitalWrite(rele3Pin, HIGH);
          Serial.println("Rele 3 activado");
          break;
        case 'd':
          digitalWrite(rele4Pin, HIGH);
          Serial.println("Rele 4 activado");
          break;
        case '1':
          digitalWrite(rele1Pin, LOW);
          Serial.println("Rele 1 desactivado");
          break;
        case '2':
          digitalWrite(rele2Pin, LOW);
          Serial.println("Rele 2 desactivado");
          break;
        case '3':
          digitalWrite(rele3Pin, LOW);
          Serial.println("Rele 3 desactivado");
          break;
        case '4':
          digitalWrite(rele4Pin, LOW);
          Serial.println("Rele 4 desactivado");
          break;
        case '5':
          digitalWrite(rele1Pin, LOW);
          digitalWrite(rele2Pin, LOW);
          digitalWrite(rele3Pin, LOW);
          digitalWrite(rele4Pin, LOW);
          Serial.println("Todos los relés apagados");
          break;
        case '0':
          digitalWrite(rele1Pin, HIGH);
          digitalWrite(rele2Pin, HIGH);
          digitalWrite(rele3Pin, HIGH);
          digitalWrite(rele4Pin, HIGH);
          Serial.println("Todos los relés encendidos");
          break;
        default:
          Serial.println("Comando invalido");
      }
    }

    valorAnterior = comando; // Actualizar el valor anterior
  }
}
