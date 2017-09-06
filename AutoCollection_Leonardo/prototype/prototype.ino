#include <Keyboard.h>

void setup() {
  // put your setup code here, to run once: 
  Serial.begin(9600);
  Serial.setTimeout(100);
  Keyboard.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  Keyboard.press(KEY_DOWN_ARROW);
  delay(50);
  Keyboard.press('x');
  delay(60);
  Keyboard.release('x');
  delay(100);
  Keyboard.press('c');
  delay(50);
  Keyboard.release('c');
  delay(100);
  Keyboard.press('d');
  delay(40);
  Keyboard.release('d');
  delay(60);
  Keyboard.releaseAll();
  Serial.println("done.");
  delay(10000) ;
}
