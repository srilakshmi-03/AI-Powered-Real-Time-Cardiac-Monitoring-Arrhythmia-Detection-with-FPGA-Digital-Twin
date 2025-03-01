#define ECG_PIN 35   // AD8232 OUTPUT to GPIO34
#define LO_PLUS 26   // Lead-Off Detection
#define LO_MINUS 27

void setup() {
  Serial.begin(115200);
  pinMode(ECG_PIN, INPUT);
  pinMode(LO_PLUS, INPUT);
  pinMode(LO_MINUS, INPUT);
}

void loop() {
  if (digitalRead(LO_PLUS) == 1 || digitalRead(LO_MINUS) == 1) {
    Serial.println("Leads Off!");  // Display if electrodes are disconnected
  } else {
    int ecgValue = analogRead(ECG_PIN);
    Serial.println(ecgValue);  // Print ECG signal values
  }
  delay(10);
}

