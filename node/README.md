# Connect via Node.js SDK

Mqtt.js 라이브러리를 사용하여 search.raiid.ai 브로커에 연결하고 MQTT 프로토콜을 사용하여 통신하는 방법을 보여주는 MQTT 클라이언트 예제에 대한 간략한 개요를 제공합니다.

## 실행 기준 환경

- node v20.10.0
- mqtt.js v5.3.6

## 사용법

### 1. SDK 설치

```bash
# ./node directory에서 실행
npm install i
```

### 2. example.js 실행

```bash
node example.js
```

## 예시 코드

```javascript
// example.js
const mqtt = require('mqtt');

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
// 웹소켓을 사용하려면 'wss://search.raiid.ai:8084/mqtt'로 변경
const connectUrl = 'mqtts://search.raiid.ai:8883';
const client = mqtt.connect(connectUrl, options);

// 연결이 성공하면 실행되는 이벤트 핸들러
client.on('connect', () => {
  console.log('connected!');

  // 'mqtt/test' 주제를 구독하고 성공 시 메시지를 발행하는 부분
  client.subscribe('mqtt/test', error => {
    if (!error) {
      console.log('send message: Hello mqtt');
      client.publish('mqtt/test', 'Hello mqtt');
      console.log('send message: Hello mqtt');
    }
  });
});

// 재연결 시 실행되는 이벤트 핸들러
client.on('reconnect', error => {
  console.log('reconnecting:', error);
});

// 오류 발생 시 실행되는 이벤트 핸들러
client.on('error', error => {
  console.log('Connection failed:', error);
});

// 메시지 수신 시 실행되는 이벤트 핸들러
client.on('message', (topic, message) => {
  console.log('receive message: ', topic, message.toString());
});
```
