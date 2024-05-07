#include <DFRobot_BMX160.h>
#include <TinyGPS.h>

TinyGPS gps; // create gps object
DFRobot_BMX160 bmx160;

float lat,lon;

void setup(){
  Serial.begin(115200);
  delay(100);
  
  //init the hardware bmx160  
  if (bmx160.begin() != true){
    Serial.println("init false");
    while(1);
  }
  delay(100);
}

void loop(){
  sBmx160SensorData_t Omagn, Ogyro, Oaccel;
  lat=19.16018;
  lon=-100.13440;
  /* Get a new sensor event */
  Serial.print(lat,6);
  Serial.print(","); 
  Serial.print(lon,6); 
  Serial.print(",");
  bmx160.getAllData(&Omagn, &Ogyro, &Oaccel);
  Serial.print(Omagn.x); Serial.print(",");
  Serial.print(Omagn.y); Serial.print(",");
  Serial.print(Omagn.z); Serial.print(",");
  Serial.print(Ogyro.x); Serial.print(",");
  Serial.print(Ogyro.y); Serial.print(",");
  Serial.print(Ogyro.z); Serial.print(",");
  Serial.print(Oaccel.x); Serial.print(",");
  Serial.print(Oaccel.y); Serial.print(",");
  Serial.print(Oaccel.z); Serial.print("");

    while(Serial1.available()){ 
    if(gps.encode(Serial1.read()))
    { 
      gps.f_get_position(&lat,&lon); 
      Serial.print(lat,6);
      Serial.print(","); 
      Serial.print(lon,6); 
      Serial.print(",");
    }
  }
    Serial.println("");
  delay(1000);
}
