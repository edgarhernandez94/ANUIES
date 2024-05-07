/*
*******************************************************************************
* Copyright (c) 2021 by M5Stack
*                  Equipped with M5StickC-Plus sample source code
*                          配套  M5StickC-Plus 示例源代码
* Visit for more information: https://docs.m5stack.com/en/core/m5stickc_plus
* 获取更多资料请访问: https://docs.m5stack.com/zh_CN/core/m5stickc_plus
*
* Describe: MPU6886.
* Date: 2021/9/14
*******************************************************************************
*/
#include <M5StickCPlus.h>

float accX = 0;
float accY = 0;
float accZ = 0;

float gyroX = 0;
float gyroY = 0;
float gyroZ = 0;

float heartrate = 0;
float gsr = 0;
float spo2 = 0;


/* After M5StickC Plus is started or reset
  the program in the setUp () function will be run, and this part will only be
  run once. 在 M5StickC Plus
  启动或者复位后，即会开始执行setup()函数中的程序，该部分只会执行一次。 */
void setup() {
    Serial.begin(9600);
    M5.begin(9600);                // Init M5StickC Plus.  初始化 M5StickC Plus
    M5.Imu.Init();             // Init IMU.  初始化IMU
    M5.Lcd.setRotation(3);     // Rotate the screen. 将屏幕旋转
    M5.Lcd.setCursor(50, 15);  // set the cursor location.  设置光标位置
    M5.Lcd.println("MPU6886 TEST");
    M5.Lcd.setCursor(30, 30);
    M5.Lcd.println("  X       Y       Z");
}

/* After the program in setup() runs, it runs the program in loop()
The loop() function is an infinite loop in which the program runs repeatedly
在setup()函数中的程序执行完后，会接着执行loop()函数中的程序
loop()函数是一个死循环，其中的程序会不断的重复运行 */
void loop() {
    static float temp = 0;
    M5.Imu.getGyroData(&gyroX, &gyroY, &gyroZ);
    M5.Imu.getAccelData(&accX, &accY, &accZ);
    M5.Imu.getTempData(&temp);

    heartrate = random(50, 120);  // Generar un número aleatorio entre -100 y 100
    gsr = random(20, 40);
    spo2 = random(90, 100);

    M5.Lcd.setCursor(30, 45);
    M5.Lcd.printf("%.2f   %.2f   %.2f      ", gyroX, gyroY, gyroZ);
    M5.Lcd.setCursor(170, 45);
    M5.Lcd.print("o/s");
    M5.Lcd.setCursor(30, 60);
    M5.Lcd.printf("%.2f   %.2f   %.2f      ", accX * 1000, accY * 1000,
                  accZ * 1000);
    M5.Lcd.setCursor(185, 60);
    M5.Lcd.print("mg");
    M5.Lcd.setCursor(30, 75);
    M5.Lcd.printf("Temperature : %.2f C", temp);

    Serial.print(gyroX);
    Serial.print(",");
    Serial.print(gyroY);
    Serial.print(",");
    Serial.print(gyroZ);
    Serial.print(",");
    Serial.print(accX);
    Serial.print(",");
    Serial.print(accY);
    Serial.print(",");
    Serial.print(accZ);
    Serial.print(",");
    Serial.print(heartrate);
    Serial.print(",");
    Serial.print(gsr);
    Serial.print(",");
    Serial.print(temp);
    Serial.print(",");
    Serial.println(spo2);
    delay(100);
}
