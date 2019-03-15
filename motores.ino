
/*MOTORES - OLHANDO O ROBO DE TRAS
 * 
 * Motor Direito: IN1 (frente) e IN2 (volta)
 * Motor Esquerdo: IN3 (volta) e IN4 (frente)
 */
 
/*Pinagem do arduino*/
// Variavel global pwm
int pwm = 150;

// Variavel que armazena a palavra de 10 caracteres lida na porta serial
String palavraSerial = "";

struct comandosDaPortaSerial
{
  String direcao;
  int velocidade;
  int tempo;
}cmd;


//motor A
int IN1 = 2; //Laranja - verde
int IN2 = 4; //Roxo - verde
int velocidadeA = 3;
 
//motor B
int IN3 = 7; //Marnrom - marrom
int IN4 = 6; //Cinza - cinza
int velocidadeB = 5;
//int pwmCurva = 50;

//variavel auxiliar
int velocidade = 150;

void setup()
{
  Serial.begin(115200);
  delay(1000);
  Serial.println("APTO");
  
  pinMode(IN1,OUTPUT); 
  pinMode(IN2,OUTPUT); 
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  pinMode(velocidadeA,OUTPUT);
  pinMode(velocidadeB,OUTPUT);

}

void loop(){
  lerSerial();
  setCmd();
  delay(50);
  setPwm(cmd.velocidade);
  mover();
}


//Função principal para controle de movimento

void mover()
{ 
  if (cmd.direcao == "F")
  {
    frente();
    delay(cmd.tempo);
    parar();
    Serial.print("Tempo de execucao: ");
    Serial.println(cmd.tempo);
  }
    
  else if (cmd.direcao == "D")
  {
    direita();
    delay(cmd.tempo);
    parar();
    Serial.print("Tempo de execucao: ");
    Serial.println(cmd.tempo);

  }    
  
  else if (cmd.direcao == "T")
  {
    tras();
    delay(cmd.tempo);
    parar();
    Serial.print("Tempo de execucao: ");
    Serial.println(cmd.tempo);
  }
      
  else if (cmd.direcao == "E")
  {
    esquerda();
    delay(cmd.tempo);
    parar();
    Serial.print("Tempo de execucao: ");
    Serial.println(cmd.tempo);

  }
      
  else if (cmd.direcao == "P")
  {
    parar();
    Serial.print("Tempo de execucao: ");
    Serial.println(cmd.tempo);
    delay(cmd.tempo);
  }
}




void frente()
{
  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  analogWrite(velocidadeA,120);
  analogWrite(velocidadeB,120);
  
//  //velocidade de 0 a 230(maximo)- FRENTE
//  while (velocidade < 230){
//  analogWrite(velocidadeB,velocidade);
//  analogWrite(velocidadeA,velocidade);
//  velocidade = velocidade + 5;
//  delay(50);
//  }
  delay(1);
  
}


void tras()
{
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,HIGH);
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  analogWrite(velocidadeA,120);
  analogWrite(velocidadeB,120);
  
//  //velocidade de 0 a 230(maximo)- TRAS
//  while (velocidade < 230){
//  analogWrite(velocidadeB,velocidade);
//  analogWrite(velocidadeA,velocidade);
//  velocidade = velocidade + 5;
//  delay(50);
//  }
  delay(1);
}

void direita()
{
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,HIGH);
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  analogWrite(velocidadeA,120);
  analogWrite(velocidadeB,120);
  
  //velocidade de 230 a 120(minimo)- DIREITA
//  while (velocidade > 120){
//  analogWrite(velocidadeB,velocidade);
//  analogWrite(velocidadeA,velocidade);
//  velocidade = velocidade - 5;
//  delay(50);
//  }
  delay(1);
}

void esquerda()
{
  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  analogWrite(velocidadeA,120);
  analogWrite(velocidadeB,120);
  
//  //velocidade de 230 a 120(minimo)- ESQUERDA
//  while (velocidade > 120){
//  analogWrite(velocidadeB,velocidade);
//  analogWrite(velocidadeA,velocidade);
//  velocidade = velocidade - 5;
//  delay(50);
//  }
  delay(1);
}


void parar()
{
  analogWrite(IN1, LOW);
  analogWrite(IN4, LOW);
  analogWrite(IN3, LOW);
  analogWrite(IN2, LOW);
  analogWrite(velocidadeA,0);
  analogWrite(velocidadeB,0);
  
  //velocidade de 230 a 0 - PARAR
  delay(1);
}
