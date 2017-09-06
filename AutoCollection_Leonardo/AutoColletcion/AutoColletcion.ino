#include <Keyboard.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
  Keyboard.begin();
}

void loop() {
  char temp[145];
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
    
    String str = Serial.readString();
    str.toCharArray(temp,144);
    char *ptr = strtok(temp,":");
    while(ptr != NULL) {
      char temp_parsing1[8];
      char temp_parsing2[8];
      char temp_parsing3[8];
      char current;
      int i=0;
      //duration parsing
      while(true){
        if(ptr[i] == ',') break;
        else temp_parsing1[i] = ptr[i];
        i++;
      }
      i++;
      int duration = atoi(temp_parsing1);
      //keyval parsing
      while(true){
        if(ptr[i] == ',') break;
        else temp_parsing2[i] = ptr[i];
        i++;
      }
      i++;
      //operation parsing
      int keyval = atoi(temp_parsing2);
      int op = atoi(ptr[i]);
      //-------------------------keystroke----------------------
      if(op == 0) {
        Keyboard.release(keyval);
        delay(duration);
      } else if(op == 1) {
        Keyboard.press(keyval);
        delay(duration);
      }
      else {
        Keyboard.releaseAll();
        delay(duration);
      }
      ptr = strtok(NULL,":");
    }
    Serial.flush();
  }
  else delay(100);
}
