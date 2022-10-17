void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue1 = analogRead(A0);
  int sensorValue2 = analogRead(A1);

  int valueCorrected1 = abs(sensorValue1 - 208);
  int valueCorrected2 = abs(sensorValue2 - 208);

  if (valueCorrected1 <= 6) {
    valueCorrected1 = 0;
  }

  if (valueCorrected2 <= 10) {
    valueCorrected2 = 0;
  }

  // Serial.print("Sensor1 Value: ");
  // Serial.println(valueCorrected1);
  // Serial.print("Sensor2 Value: ");
  Serial.println(valueCorrected2);
}

