#include <SPI.h>

// MCP4921のピン接続
const int CS_PIN = 10;  // Chip Selectピン

void setup() {

  SPI.begin();
  SPI.setClockDivider(SPI_CLOCK_DIV2);
  SPI.setDataMode(SPI_MODE0);
  SPI.setBitOrder(MSBFIRST);

  pinMode(CS_PIN, OUTPUT);
  digitalWrite(CS_PIN, HIGH);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    // シリアルポートからデータを読み取る
    int voltage = Serial.parseInt();
    if (voltage >= 0 && voltage <= 5000) {
      int value = (voltage / 4968.0) * 4095;
      sendToDAC(value);
    }
  }
}
void sendToDAC(int value) {
  uint16_t command = 0x3000 | (value & 0x0FFF);

  digitalWrite(CS_PIN, LOW);

  SPI.transfer(command >> 8);
  SPI.transfer(command & 0xFF);

  digitalWrite(CS_PIN, HIGH);
}
