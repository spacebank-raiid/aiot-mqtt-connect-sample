# Connect via Browser SDK

Mqtt.js 라이브러리를 사용하여 search.raiid.ai 브로커에 연결하고 MQTT 프로토콜을 사용하여 통신하는 방법을 보여주는 MQTT 클라이언트 예제에 대한 간략한 개요를 제공합니다.

## 실행 기준 환경

- Python v3.10.12
- paho-mqtt v2.0.0

## 사용법

`index.html` 파일 실행

## 예시 코드

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>MQTT Example</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        text-align: center;
        margin: 20px;
      }

      label {
        display: block;
        margin-bottom: 5px;
      }

      input {
        width: 200px;
        padding: 8px;
        margin-bottom: 10px;
      }

      button {
        padding: 10px;
        font-size: 16px;
        cursor: pointer;
      }

      #resultConsole {
        text-align: left;
        list-style-type: '\1F680';
      }

      .input-container {
        margin-top: 20px;
        width: 720px;
        text-align: left;
      }
    </style>
    <script src="https://unpkg.com/mqtt/dist/mqtt.min.js"></script>
  </head>
  <body>
    <h1>MQTT Example</h1>

    <div style="display: flex; flex-direction: column; align-items: center">
      <!-- Subscribe Section -->
      <div class="input-container">
        <label for="subscribeTopic">Subscribe Topic:</label>
        <input
          type="text"
          id="subscribeTopic"
          placeholder="Enter subscribe topic"
        />
        <button onclick="subscribeTopic()">Subscribe</button>
      </div>

      <!-- Publish Section -->
      <div class="input-container">
        <label for="publishTopic">Publish Topic:</label>
        <input
          type="text"
          id="publishTopic"
          placeholder="Enter publish topic"
        />
        <label for="publishMessage">Publish Message:</label>
        <input
          type="text"
          id="publishMessage"
          placeholder="Enter publish message"
        />
        <button onclick="publishMessage()">Publish</button>
      </div>
    </div>
    <hr />

    <ul id="resultConsole"></ul>

    <script>
      // 연결 옵션 설정
      const options = {
        clean: true, // 세션 유지
        connectTimeout: 4000, // 타임아웃 기간
        // 인증 정보
        clientId: 'mqtt_test',
        username: 'mqtt_test',
        password: 'mqtt_test',
      };

      // 브로커에 연결할 URL 설정
      const connectUrl = 'wss://search.raiid.ai:8084/mqtt';
      const client = mqtt.connect(connectUrl, options);

      // 연결이 성공하면 실행되는 이벤트 핸들러
      client.on('connect', () => {
        resultConsoleLog('connected!');
      });

      client.on('reconnect', error => {
        resultConsoleLog(`reconnecting: ${error}`);
      });

      client.on('error', error => {
        resultConsoleLog(`connection failed: ${error}`);
      });

      client.on('message', (topic, message) => {
        resultConsoleLog(`receive message: ${topic} ${message.toString()}`);
      });

      // dom에 로깅하기 위한 함수
      function resultConsoleLog(msg) {
        const log = document.createElement('li');
        log.innerHTML = `[${new Date().toLocaleTimeString()}] ${msg}`;
        const resultConsole = document.getElementById('resultConsole');
        if (resultConsole) {
          resultConsole.insertBefore(log, resultConsole.firstChild);
        } else {
          console.error('resultConsole element not found!');
        }
      }
    </script>
    <script>
      // 메시지를 발행하는 함수
      function publishMessage() {
        var topic = document.getElementById('publishTopic').value;
        var message = document.getElementById('publishMessage').value;

        client.publish(topic, message);
        resultConsoleLog(
          `publishing to topic: ${topic} with message: ${message}`,
        );
      }

      // 토픽을 구독하는 함수
      function subscribeTopic() {
        var topic = document.getElementById('subscribeTopic').value;

        client.subscribe(topic, error => {
          if (!error) {
            resultConsoleLog('subscribing to topic: ' + topic);
          }
        });
      }
    </script>
  </body>
</html>
```
