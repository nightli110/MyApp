# MyApp
application demo for LiuDao

MyApp 是LiuDao应用的一个SDK库，主要分为3个进程:  
1. server进程，基于flask，接受发送消息  
2. infer进程，部署infer模型  
3. watcher进程， 监控程序的一些资源及进行上报(开发中)  

需要环境:  
1. python3
2. flask
3. concurrent_log_handler
4. opencv 

食用方法：
```
python Main.py
```
程序会运行flask和infer两个进程:   
flask进行负责server进程  
infer进程负责推理数据  

flask下接口:  
/online: 应用上线,接受json消息格式:
```json
{
    "loadmodel": true
}
```
/postdata: 请求处理数据,接受消息格式:  
```json 
{
    "input": "image:1",
    "image_1": imagebase64code,
    "uuid": "dadasdsadas"
}
```
其中uuid 为用户名  
input 为输入数据格式: type:n 表示type格式数据n组
json中必须包含type_m key的数据,其中1<m<=n  
若type为image，image需改为base64编码

返回值用户定义(目前)可参考CaffeOpencvApp  

infer进程为推理进程:  
初衷是用户只需修改*App.py文件 i.g.CaffeOpencvApp.py  
定义模型处理，及数据预处理步骤
目前以CaffeopencvApp.py 支持以opencv dnn的形式部署模型，后续会支持更多



中二解释:
六道中的畜生道，能像通灵出各种通灵兽

开发过程的问题可以参考:  http://www.styxhelix.life/categories/MYAPP%E5%BC%80%E5%8F%91/