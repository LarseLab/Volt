// Lendo 10 caracteres da porta serial e armazenando em palavraSerial
void lerSerial(){
  char vetorSerial[12];
  palavraSerial = "";

  for(int i=0; i<10; i++)
  {
    palavraSerial = "";
    vetorSerial[i] = Serial.read();
  }
  for(int i=0; i<9; i++)
  {
     palavraSerial += vetorSerial[i];
  } 
}

// Mudando o valor de pwm para o valor lido na serial
void setPwm(float vel)
{  
  if ((vel > 0) && (vel <=100))
  {
  vel = vel/100.00;
    pwm =  255*vel;
    Serial.print("Pwm: ");
    Serial.println(pwm);
  }
  else
  {
    pwm = 0;
  }
}

// Atribuindo as partes da palavraSerial que correspondem a direcao, velocidade e tempo
void setCmd()
{
  cmd.direcao = palavraSerial.substring(0,1);
  cmd.velocidade = palavraSerial.substring(1,4).toInt();
  cmd.tempo = palavraSerial.substring(4,9).toInt(); 
}
