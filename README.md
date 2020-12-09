# selenium-webdriver-manager

* 中文版指南: todo

## Profile

* This project aims to automatically download the webdriver.

* It works as follows
  
  1. Get the browser version.
  2. Get the webdriver version.
  3. Download the matched webdriver if they are not matched after comparing the 2 versions.

* It supports Windows, MacOS, Linux/Unix platform

## Environment

* Python >= 3.6.x

## Directory struct

```shell
├── demo                      // Simple example
├── swm
│   ├── __init__.py           // main module
│   └── Chrome.py             // Chrome manager
├── README.md                 // Main guide
└── setup.py                  // For install
```

## Install guide

### Download selenium-webdriver-manager and run

```shell
$ python setup.py install
```
### Uninstall

```shell
$ pip uninstall selenium-webdriver-manager
```

## Chrome demo

* touch a file like `conf.ini`

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

* code in python

  ```python
  from swm.Chrome import Chrome

  Chrome('./conf.ini')
  ```

## TODO

* Currently, it only includes google-chrome, MS Edge, Chromium

* More browser like Firefox, MS IE, Opera
