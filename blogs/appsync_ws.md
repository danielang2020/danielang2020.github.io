1. 实时推送地址：wss://byrui3dndbbzngtql4wkmft3bq.appsync-realtime-api.us-east-1.amazonaws.com/graphql
2. 连接时header参数。
   - header需要添加参数。
   Sec-WebSocket-Protocol=graphql-ws

3. 连接时params参数。
   - header
     json字符串进行base64编码。
```json
{
  "host": "byrui3dndbbzngtql4wkmft3bq.appsync-api.us-east-1.amazonaws.com",
  "x-api-key": "da2-xz2im6wg7japhd6f2tt64jthxu"
}
```
   - payload
     {}进行base64编码。
`{}`


`wss://byrui3dndbbzngtql4wkmft3bq.appsync-realtime-api.us-east-1.amazonaws.com/graphql?header=eyJob3N0IjoiYnlydWkzZG5kYmJ6bmd0cWw0d2ttZnQzYnEuYXBwc3luYy1hcGkudXMtZWFzdC0xLmFtYXpvbmF3cy5jb20iLCJ4LWFwaS1rZXkiOiJkYTIteHoyaW02d2c3amFwaGQ2ZjJ0dDY0anRoeHUifQ==&payload=e30=`
   
4. 连接成功后，需要发送固定初始化消息。      
```json
    { "type": "connection_init" }
```
5. 初始化消息发送后，服务端后返回2个消息。
   - 保活消息超时消息（connectionTimeoutMs）。单位毫秒，如果在区间时间内，没有收到服务器推送的保活消息，则需要断开连接后，重新建立新连接。
   
   - 保活消息。
   
6. 发送信号订阅消息。      
```json
{
  "id": "e1149ef0-cf23-4cb8-9fcb-152ae4fd1e69", // 客户端创建的唯一连接ID
  "payload": {
    "data": "{\"query\":\"subscription MySub { onCreateQuotapIndicator { id sc sy i si pe t a pr } }\",\"variables\":{}}",
    "extensions": {
      "authorization": {
        "host": "byrui3dndbbzngtql4wkmft3bq.appsync-api.us-east-1.amazonaws.com",
        "x-api-key": "da2-xz2im6wg7japhd6f2tt64jthxu"
      }
    }
  },
  "type": "start"
}
```
   
7. 订阅后，服务端会发返回订阅确认消息。
   
8. 信号实时订阅流程结束，等待服务器推送最新信号信息。       
```json
{
    "id": "e1149ef0-cf23-4cb8-9fcb-152ae4fd1e69", // 客户端创建的唯一连接ID
    "type": "data", // 固定值
    "payload": {
        "data": {
            "onCreateQuotapIndicator": {
                "id": "EURUSD_CCI_1673601781", // 信号ID
                "sc": "FX", // 产品分类
                "sy": "EURUSD", // 产品
                "i": "CCI", // 指标
                "si": "ccidv2", // 信号
                "pe": "1m", // 周期
                "t": "2023-01-12T09:23:01Z", // 触发时间
                "a": "sell", // 建议买卖
                "pr": "1.07589", // 触发价格
                "et": 1673601781 // 过期时间（前端可以忽略此字段）
                }
            }
        }
    }
```
9. 主动断开连接，送消息。  
```json
    {
      "type":"stop",
      "id":"e1149ef0-cf23-4cb8-9fcb-152ae4fd1e69" // 客户端创建的唯一连接ID
    }
```