#include <ESP8266WiFi.h>

const char* ssid = "vivo V23e 5G";
const char* password = "12345678";

WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  server.begin();
  Serial.println("Server started");
}

void loop() {
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
  Serial.println("New client connected");
  while (client.connected()) {
    if (client.available()) {
      //char data = client.read();
      //Serial.write(data);
      String incoming_data="";
      while(client.available()){
        incoming_data+=(char)client.read();
      }
      Serial.println("Received: "+incoming_data);
    }
  }
  // incoming_string=incoming_data.decode()
  // Serial.println("Received: "+ incoming_string)
  client.stop();
  Serial.println("Client disconnected");
}