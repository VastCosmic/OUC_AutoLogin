[TOC]

# OUC_AutoLogin

This is a simple script to automatically login to the OUC network.
It is written in Python and uses the Selenium library to interact with the browser.

### Installation

1. Install Python 3.7 or higher from the [official website](https://www.python.org/downloads/).
2. Install the required libraries by running the following command in the terminal:

```
pip install selenium
```

3. Install ChromeBrowser from the [official website](https://www.google.com/chrome/).(If you have already installed, skip this step)
4. Clone this repository by running the following command in the terminal:

```
git clone https://github.com/VastCosmic/OUC_AutoLogin.git
```

5. Enter your username and password in the `OUC_AutoLogin.py` file.
6. Run the script by running the following command in the terminal:

```
python OUC_AutoLogin.py
```

7. If you use Windows, you can just click on the `run.bat` file to run the script instead of running the command in step 6.
8. You can use the Windows Task Scheduler for `run.bat` to run the script automatically at a specific time. If you don't know how to do this, you can search for it on the internet using the keywords "Windows Task Scheduler" and "bat".
9. Execution principle:
   First, create a subprocess to try to send a ping request. If the ping is not successful within 1s, kill the subprocess. Then, simulate the browser through Selenium, send a GET request to get the login page with username and password and complete the login.

# OUC_AutoLogin (中文)

 (中文文档由GitHub Copilot自动生成)

这是一个简单的脚本，用于自动登录中国海洋大学校园网（OUC校园网）。
它是用Python编写的，并使用Selenium库与浏览器交互。

### 安装

1. 从[官方网站](https://www.python.org/downloads/)安装Python 3.7或更高版本。
2. 在终端中运行以下命令安装所需的库：

```
pip install selenium
```

3. 从[官方网站](https://www.google.com/chrome/)安装Chrome浏览器。（如果你已经安装了，就跳过这一步）
4. 在终端中运行以下命令克隆此仓库：

```
git clone https://github.com/VastCosmic/OUC_AutoLogin.git
```

5. 在 `OUC_AutoLogin.py`文件中输入你的用户名和密码。
6. 通过在终端中运行以下命令来运行脚本：

```
python OUC_AutoLogin.py
```

7. 如果你使用Windows，你可以直接点击 `run.bat`文件来运行脚本，而不是运行第6步中的命令。
8. 你可以使用Windows任务计划程序为 `run.bat`在特定时间自动运行脚本。如果你不知道如何做到这一点，你可以使用关键词“Windows任务计划程序执行bat文件”在互联网上搜索。
9. 执行原理：
   首先创建subprocess，尝试发送ping请求，如果1s内ping不通，则杀死subprocess，然后通过Selenium模拟浏览器，发送GET请求，获取登录页面，然后填写用户名和密码，完成登录。
