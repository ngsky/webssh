# Http 服务: 提交登录信息
URL:http://localhost:8888/
METHOD: POST
Parameters:
---------
hostname: 192.168.230.128
port: 
username: root
password: centos001
passphrase: 
totp: 
term: xterm-256color
_xsrf: 2|1a010715|4beadf6b0c33e43bdd1186e4eddf42ec|1608860408
---------
Response:
----------
{"status": null, "id": "69505672", "encoding": "UTF-8"}
----------

# WebSocket 服务: 操作远程服务器
URL: ws://localhost:8888/ws?id=69505672
METHOD: GET
Parameters:
---------
id=69505672
---------
交互:
---------
1.键入 l
{"data":"l"}	12	
09:58:37.201
Binary Message
2.回车
{"data":"l"}	12	
09:58:37.201
Binary Message	1 B	
09:58:37.208
{"data":"\r"}	13	
09:59:32.782
Binary Message	40 B	
09:59:32.786
Binary Message	3.4 kB	
09:59:33.001
Binary Message	224 B	
09:59:33.004
Binary Message
---------