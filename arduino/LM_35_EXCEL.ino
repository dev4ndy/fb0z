float Temp_C;
int Data_sensor;
int Signal_sensor = 0;

int x,y;

void setup()
{
analogReference(INTERNAL);
Serial.begin(9600);

}

void float2libreoffice(float numero)

{
  int n_int,n_entera,n_decimal1,n_decimal2;
  n_int=numero*100;
   if (n_int<0)
   {
   n_int=-1*n_int;
   Serial.print("-");
   }
  n_entera=n_int/100;
  n_decimal1=(n_int%100)/10;
  n_decimal2=(n_int%100)%10;

  Serial.print(n_entera);Serial.print(",");Serial.print(n_decimal1);Serial.print(n_decimal2);

}

void loop()
{
Data_sensor=analogRead(Signal_sensor);
Temp_C=Data_sensor/9.31;
//Serial.print("'");
float2libreoffice(Temp_C);Serial.println();      
delay(100);
}

