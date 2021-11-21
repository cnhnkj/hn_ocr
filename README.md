# 惠农网开源的离线OCR服务


# 项目介绍
hn_ocr是惠农网基于[cnstd](https://github.com/breezedeus/cnstd) + [cnocr](https://github.com/breezedeus/cnocr) + [tronado](https://github.com/tornadoweb/tornado/tags) 构建的web服务
提供了http的接口，便于微服务体系中其他服务调用
也便于前端页面进行调用


# 特性
* 中文检测(基于cnstd)
* 中文识别(基于cnocr)
* web接口(基于tronado)
* 返回的文字按坐标,从上至下,从左至右
* 返回检测文字的坐标

# 部署说明
## python安装

1. 安装python3.7
    
2. 安装依赖包  
``` shell script
pip install -r requirements.txt
```  

3. 初始化环境
(如果不执行这一步，也是可以运行的， 只是第一次需要下载对应的模型，会导致启动变慢)
``` shell script
python install.py
``` 

4. 运行  
项目默认运行在8898端口  
``` shell script
python server.py
```

4. 配置文件在`settings`目录下面的`config.py`文件

5. 离线非web模式运行
``` shell script
python main.py
```

## docker部署

```shell script
# 从源码编译
# 目前编译的镜像太大，暂时没有上传到dockerhub，希望可以有什么办法可以进行压缩镜像
docker build -t hnocr:v1.0.0 .

# 运行镜像
docker run -itd --rm -p 8898:8898 --name hnocr hnocr:latest 
```

```shell script
# 或者从 dockerhub pull
# 暂时还没有上传
docker pull hnocr:latest

# 运行镜像
docker run -itd --rm -p 8898:8898 --name hnocr hncnb/hnocr:latest 
```




## web服务接口文档

-----------------------------------
### 简要描述 

根据图片url或者图片的base64来进行识别

### 请求url

`/api/ocr/url`

### 请求方式

`POST`

### 请求协议

`application/json; charset=UTF-8`

### 入参说明

|  参数名称   | 是否必须  | 数据类型 | 说明 |
|  ----  | ----  |  ----  | ----  |
| url  | 必须 | string  | 要识别图片的url地址,有该字段则优先这个字段 |
| image  | 必须 | string  | 要识别图片base64数据(不需要头标签) |
| coordinate  | 不必须 | bool  | 是否返回坐标 |

### 具体请求例子

```
curl -XPOST '127.0.0.1:8898/api/ocr/url' -d '{"url":"https://image.cnhnb.com/image/jpg/head/2021/10/31/ebb000315807439cb92bcde5dc9136ce.jpg", "coordinate": true}' -H 'Content-Type: application/json; charset=UTF-8'
```

### 出参说明

|  参数名称   | 是否必须  | 数据类型 | 说明 |
|  ----  | ----  |  ----  | ----  |
| ocr_result  | 必须 | string  | 识别出来的文字 |
| ocr_prob  | 必须 | float  | 文字准确性概率 |
| ocr_box  | 不必须 | float  | 为文字的所占住的矩形的左上角和右下角的坐标 |
| speed_time  | 必须 | float  | 文字识别所用的时间 |


### 返回示例

```json
{
    "code":200,
    "msg":"\u6210\u529f",
    "data":{
        "ocr_res":[
            {
                "ocr_result":"\u4e00\u751f\u7231\u5403\u7684\u6761\u7eb9\u82f9\u679c",
                "ocr_prob":0.9542221426963806,
                "ocr_box":[
                    186.43750000000003,
                    66.5,
                    627.0000000000001,
                    108.0625
                ]
            },
            {
                "ocr_result":"\u7ea2\u5bcc\u58eb\u5929\u751f\u5c31\u662f",
                "ocr_prob":0.9251773357391357,
                "ocr_box":[
                    298.06250000000006,
                    150.8125,
                    518.9375000000001,
                    180.5
                ]
            },
            {
                "ocr_result":"\u81ea\u7136\u6210\u719f\u91c7\u6458,\u4e0d\u6253\u836f\u4e0d\u50ac\u719f,",
                "ocr_prob":0.5450785160064697,
                "ocr_box":[
                    186.43750000000003,
                    186.4375,
                    609.1875000000001,
                    219.6875
                ]
            },
            {
                "ocr_result":"\u7f8e\u5473\u6ee1\u6ee1\u54e6",
                "ocr_prob":0.615333080291748,
                "ocr_box":[
                    313.50000000000006,
                    224.4375,
                    478.5625000000001,
                    254.12499999999997
                ]
            },
            {
                "ocr_result":"\u65b0\u9c9c",
                "ocr_prob":0.9971355199813843,
                "ocr_box":[
                    115.18750000000003,
                    349.125,
                    199.5,
                    395.4375
                ]
            },
            {
                "ocr_result":"\u6ee1\u6ee1",
                "ocr_prob":0.3760497570037842,
                "ocr_box":[
                    115.18750000000003,
                    393.0625,
                    200.68750000000006,
                    439.375
                ]
            }
        ],
        "speed_time":1.1941959857940674
    }
}
```

-----------------------------------

### 简要描述 

根据上传的图片文件来进行识别

### 请求url

`/api/ocr/file`

### 请求方式

`POST`

### 请求协议

`multipart/form-data`

### 入参说明

|  参数名称   | 是否必须  | 数据类型 | 说明 |
|  ----  | ----  |  ----  | ----  |
| file  | 必须 | file  | 要识别图片的文件 |
| coordinate  | 不必须 | bool  | 是否返回坐标 |

### 具体请求例子

```
curl -XPOST '127.0.0.1:8898/api/ocr/file?coordinate=21' -H 'Content-Type: multipart/form-data' -F 'file=@/Users/longzhe/Downloads/apple_001.jpeg'
```

### 出参说明

|  参数名称   | 是否必须  | 数据类型 | 说明 |
|  ----  | ----  |  ----  | ----  |
| ocr_result  | 必须 | string  | 识别出来的文字 |
| ocr_prob  | 必须 | float  | 文字准确性概率 |
| ocr_box  | 不必须 | float  | 为文字的所占住的矩形的左上角和右下角的坐标 |
| speed_time  | 必须 | float  | 文字识别所用的时间 |


### 返回示例

```json
{
    "code":200,
    "msg":"\u6210\u529f",
    "data":{
        "ocr_res":[
            {
                "ocr_result":"\u4e00\u751f\u7231\u5403\u7684\u6761\u7eb9\u82f9\u679c",
                "ocr_prob":0.9542221426963806,
                "ocr_box":[
                    186.43750000000003,
                    66.5,
                    627.0000000000001,
                    108.0625
                ]
            },
            {
                "ocr_result":"\u7ea2\u5bcc\u58eb\u5929\u751f\u5c31\u662f",
                "ocr_prob":0.9251773357391357,
                "ocr_box":[
                    298.06250000000006,
                    150.8125,
                    518.9375000000001,
                    180.5
                ]
            },
            {
                "ocr_result":"\u81ea\u7136\u6210\u719f\u91c7\u6458,\u4e0d\u6253\u836f\u4e0d\u50ac\u719f,",
                "ocr_prob":0.5450785160064697,
                "ocr_box":[
                    186.43750000000003,
                    186.4375,
                    609.1875000000001,
                    219.6875
                ]
            },
            {
                "ocr_result":"\u7f8e\u5473\u6ee1\u6ee1\u54e6",
                "ocr_prob":0.615333080291748,
                "ocr_box":[
                    313.50000000000006,
                    224.4375,
                    478.5625000000001,
                    254.12499999999997
                ]
            },
            {
                "ocr_result":"\u65b0\u9c9c",
                "ocr_prob":0.9971355199813843,
                "ocr_box":[
                    115.18750000000003,
                    349.125,
                    199.5,
                    395.4375
                ]
            },
            {
                "ocr_result":"\u6ee1\u6ee1",
                "ocr_prob":0.3760497570037842,
                "ocr_box":[
                    115.18750000000003,
                    393.0625,
                    200.68750000000006,
                    439.375
                ]
            }
        ],
        "speed_time":1.1941959857940674
    }
}
```


## 更新记录  
* 2021年11月20日  
    基本完成简单的web接口服务

## License  
Apache 2.0

## 鸣谢
* 感谢项目 [cnstd](https://github.com/breezedeus/cnstd)
* 感谢项目 [cnocr](https://github.com/breezedeus/cnocr)
