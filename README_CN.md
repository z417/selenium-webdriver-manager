# selenium-webdriver-manager

## 简介

* 在selenium驱动的web自动化中，经常会碰浏览器和driver版本不匹配的状况，本项目提供的功能是自动下载与本地浏览器版本相匹配的driver; 目前在Mac OS, Windows, Linux平台上支持Chrome, Chromium, MS Edge

* 工作原理如下
  
  1. 获取当前指定浏览器的版本
  2. 获取driver的版本(没有则显示0)
  3. 比较版本号, 若不匹配, 则自动下载与浏览器匹配的driver

## 运行环境

* Python >= 3.6.x

## 目录结构

```shell
├── demo                      // Simple example
├── swm
│   ├── __init__.py           // main module
│   ├── Chrome.py             // Chrome manager
│   ├── Chromium.py
│   └── Microsoft.py
├── README.md                 // Main guide
└── setup.py                  // For install
```

## 安/卸指南

### 下载 selenium-webdriver-manager 后运行

```shell
$ python setup.py install
```
### 卸载

```shell
$ pip uninstall selenium-webdriver-manager
```

## 管理Chrome的例子

* 新建配置文件如下 `conf.ini`

  ```ini
  [driver]
  absPath=driver\chromedriver.exe

  # Below 2 urls both work, choose only one at sametime
  ; url=http://npm.taobao.org/mirrors/chromedriver
  url=https://chromedriver.storage.googleapis.com

  # Below are MS Edge's config
  ; absPath=driver\msedgedriver.exe
  ; url=https://msedgedriver.azureedge.net
  ```

* 使用该项目

  ```python
  from swm.Chrome import Chrome

  Chrome('./conf.ini')
  ```

## TODO

* 目前, 只支持 google-chrome, MS Edge, Chromium

* 未来计划支持 Firefox, MS IE, Opera
