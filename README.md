# selenium-webdriver-manager
## Profile

* In Selenium automation, you often encounter situations where the browser and the driver version don't match. This project provided to automatically download the driver matching the local browser version. Chrome, Chromium and MS Edge are currently supported on Mac OS, Windows and Linux platforms.

* It works as follows
  
  1. Get the current version of the specified browser
  2. Get the version of the driver binary. (zero if there is none)
  3. Compare the versions. The driver that matches the browser will be downloaded automatically if they don't match.

## Environment

* Python >= 3.6.x

## Directory struct

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

## Install/Uninstall guide

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
