# WTF_Scan_Fix

This is a fixed version of the original project, mainly fixing the following issues:

1. Update the runtime environment to Python3
2. Fix cms recognition
3. Fix port scanning
4. Fix the original author's shitty code

Why fix it? Because I received a graduation design from a **985 University Cybersecurity student** on an **slavery** platform. He gave me money, so I fixed it.  
I didn't expect a college student to help a top university with his graduation project!

这是个修复版本, 主要修复了以下问题:

1. 更新运行环境为 Python3
2. 修复 cms 识别
3. 修复 端口扫描
4. 修复源作者屎山代码

为什么要修复呢? 因为我在外包平台接到一个 **酒吧舞网络安全学生** 的毕业设计. 他给钱, 我就修复了. 没想到一个文盲大专生也配帮顶级大学做毕设.

一款 WEB 端的在线敏感资产扫描器，扫描网站中的指纹、漏洞及相关敏感信息，针对已经识别的 CMS 指纹，进行二次 0day 扫描利用，一键 GetShell 也不是不可能！！！
![image](https://uploadimages.jianshu.io/upload_images/6661013a5ca96416f635dc1.png)

## 预览界面

![image](https://uploadimages.jianshu.io/upload_images/666101335d11c212e2a941d.png)

## 运行环境

1. PHP > 5.3
2. allow_url_fopen = On

## 使用说明

1. 克隆下载本源码.
2. Deploy the Flask backend. (The Flask backend code is in the wtf directory)
3. 上传到网站空间，直接访问对应目录即可使用.(本质就是使用 PHP 调用后端 Flask 接口) Actually, it is invoke the backend Flask API by the PHP.

## 功能特别说明

1. 支持基本网站基本信息搜集
2. 支持获取 DNS 解析信息
3. 支持获取子域名信息
4. 支持获取网站 CMS 指纹信息
5. 支持逆向穿透国内 CDN 获取网站源 IP 及物理定位地址
6. 支持探测爆破常见端口以及全部 65535 个端口
7. 支持网站敏感目录、文件扫描爆破，字典 6000+匹配
8. 支持 IIS 短文件名漏洞扫描
9. 支持根据扫描结果 CMS 定向 0day 扫描利用（未完成）
10. 支持插件无限扩展

### Tips

最近真的好忙啊~有比赛还有考试复习，大家可以关注我的博客：<https://blog.dyboy.cn> ，日常更新哦~

### 部署

Python3:

```shell
# If you in freedom network, you are not necessary to set proxy.
set HTTPS_PROXY=http://127.0.0.1:10809/
set HTTP_PROXY=http://127.0.0.1:10809/

py m venv ./venv
.\venv\Scripts\Activate.ps1
python.exe m pip install upgrade pip
# same above
pip install r requirements.txt upgrade index_url=https://pypi.org/simple proxy=http://127.0.0.1:10809
python wtf/manage.py
```

Python2 deprecated, use Python3 instead.

```shell
# If you in freedom network, you are not necessary to set proxy.
set HTTPS_PROXY=http://127.0.0.1:10809/
set HTTP_PROXY=http://127.0.0.1:10809/
python m pip install virtualenv
D:\Python27\python.exe V
D:\Python27\python.exe .\getpip.py
# same above
D:\Python27\python.exe m pip install r wtf/requirements.txt proxy=127.0.0.1:10809
D:\Python27\python.exe .\wtf\manage.py
```

### 更新历史

20181221 开源后端代码
