# JinRiTouTiao

目标：
    爬取今日头条文章，并根据不同的模块制作词云图

思路：
    今日头条为动态页面，采用爬虫框架为scrapy+splash（splahs为轻量级js渲染引擎）
   
工具：
    Mac, 阿里云服务器A，B，C
    3台服务器分别部署了splash引擎，mac请求指向服务器A的nginx负载均衡端口80，轮询到A,B,C的splash进程端口
    爬取的数据写入服务器A的mongodb
    
    SPLASH_URL = 'http://server:port' #此处填写的是部署了nginx负载均衡的服务器及端口号，通过负载均衡将请求分发到各个splash服务器
    MONGO_DB_URI = "mongodb://server:27017" #mongodb服务器
    MONGO_DB_NAME = "toutiao"
    
生成词云图：
    
    

