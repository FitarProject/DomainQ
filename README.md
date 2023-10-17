# DomainQ
一个批量域名信息查询工具，可查询域名注册人、域名归属、ICP备案号、主域名、变更时间等

使用示例：

```
python3 domain_info.py
```

会读取当前目录下的targets.txt

网站有查询限制，短时间内单个IP至多查询500条，到达限制后请自行更换主机IP



查询结果示例（baidu.com）：

```
{
    "StateCode": 1,
    "Reason": "成功",
    "Result": {
        "Owner": "",
        "CompanyName": "北京百度网讯科技有限公司",
        "CompanyType": "企业",
        "SiteLicense": "京ICP证030173号-1",
        "SiteName": "百度",
        "MainPage": "www.baidu.com",
        "VerifyTime": "2023-01-10 09:43:35",
        "UpdateTime": "2023-03-27 10:17:17"
    }
}
```



