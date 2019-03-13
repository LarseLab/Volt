
/*MOTORES - OLHANDO O ROBO DE TRAS
 * 
 * Motor Direito: IN1 (frente) e IN2 (volta)
 * Motor Esquerdo: IN3 (volta) e IN4 (frente)
 */
 
/*Pinagem do arduino*/
//motor A
int IN1 = 2; //Laranja - verde
int IN2 = 4; //Roxo - verde
int velocidadeA = 3;
 
//motor B
int IN3 = 6; //Marnrom - marrom
int IN4 = 7; //Cinza - cinza
int velocidadeB = 5;
//int pwmCurva = 50;

//variavel auxiliar
int velocidade = 100;

void setup()
{
  pinMode(IN1,OUTPUT); 
  pinMode(IN2,OUTPUT); 
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  pinMode(velocidadeA,OUTPUT);
  pinMode(velocidadeB,OUTPUT);
  Serial.begin(115200);
}

void loop(){

/*Exemplo de velocidades no motor A*/

//Sentido 2
  ir_para_frente();
  delay(5000);
  parar();
  delay(200);
  ir_para_tras();
  delay(5000);
  girar_para_direita();
  delay(2000);
  girar_para_esquerda();
  delay(2000);
  parar();
  delay(200);


}
void ir_para_frente()
{
  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  //analogWrite(velocidadeA,120);
  //analogWrite(velocidadeB,120);
  
  //velocidade de 0 a 230(maximo)- FRENTE
  while (velocidade < 230){
  analogWrite(velocidadeB,velocidade);
  analogWrite(velocidadeA,velocidade);
  velocidade = velocidade + 5;
  delay(50);
  }
  delay(1);
}

void ir_para_tras()
{
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,HIGH);
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  //analogWrite(velocidadeA,120);
  //analogWrite(velocidadeB,120);
  
  //velocidade de 0 a 230(maximo)- TRAS
  while (velocidade < 230){
  analogWrite(velocidadeB,velocidade);
  analogWrite(velocidadeA,velocidade);
  velocidade = velocidade + 5;
  delay(50);
  }
  delay(1);
}

void girar_para_direita()
{
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,HIGH);
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  //analogWrite(velocidadeA,120);
  //analogWrite(velocidadeB,120);
  
  //velocidade de 230 a 120(minimo)- DIREITA
  while (velocidade > 120){
  analogWrite(velocidadeB,velocidade);
  analogWrite(velocidadeA,velocidade);
  velocidade = velocidade - 5;
  delay(50);
  }
  delay(1);
}

void girar_para_esquerda()
{
  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  //analogWrite(velocidadeA,120);
  //analogWrite(velocidadeB,120);
  
  //velocidade de 230 a 120(minimo)- ESQUERDA
  while (velocidade > 120){
  analogWrite(velocidadeB,velocidade);
  analogWrite(velocidadeA,velocidade);
  velocidade = velocidade - 5;
  delay(50);
  }
  delay(1);
}

void parar()
{
  analogWrite(IN1, LOW);
  analogWrite(IN4, LOW);
  analogWrite(IN3, LOW);
  analogWrite(IN2, LOW);
  //analogWrite(velocidadeA,0);
  //analogWrite(velocidadeB,0);
  
  //velocidade de 230 a 0 - PARAR
  while (velocidade > 0){
  analogWrite(velocidadeB,velocidade);
  analogWrite(velocidadeA,velocidade);
  velocidade = velocidade - 5;
  delay(50);
  }
  delay(1);
}





