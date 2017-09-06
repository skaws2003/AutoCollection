#include <Keyboard.h>

void setup() {
  // put your setup code here, to run once: 
  Serial.begin(9600);
  Serial.setTimeout(100);
  Keyboard.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  Keyboard.press(KEY_UP_ARROW);
  delay(10);
  Keyboard.press(' ');
  delay(40);
  Keyboard.release(' ');
  delay(310);
  Keyboard.press('d');
  delay(40);
  Keyboard.release('d');
  delay(95);
  Keyboard.press('t');
  delay(30);
  Keyboard.release('t');
  delay(10);
  Keyboard.releaseAll();
  Serial.println("done.");
  delay(10000) ;
}
