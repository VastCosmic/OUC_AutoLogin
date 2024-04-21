# 安装Python3.11.0 
# https://www.python.org/downloads/release/python-3110/
#
# 安装Chrome浏览器
# https://www.google.cn/chrome/
#
# 安装selenium库
# pip install selenium

# 请填入你登录的学工号和校园网密码 Please fill in your student ID and campus network password below.
# 示例 Example :
# user_account = "20001234567"
# user_password = "123456789"
# 请在下面的代码中填入你的学号和密码, 而不是在上面的示例 Please fill in your student ID and password in the code below instead of the example above.

import subprocess
import time

def is_connected():
    process = subprocess.Popen("ping -n 1 baidu.com > nul 2>&1", shell=True)
    time.sleep(1)

    if process.poll() is None:
        print("Ping command did not complete within 1 second")
        process.terminate()
        return False
    else:
        return True


if is_connected():
    print("Connected to the Internet")
else:
    user_account = "你的学号/工号"
    user_password = "你的校园网密码"

    from selenium import webdriver

    url="https://xha.ouc.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account="+user_account+"&user_password="+user_password
    driver = webdriver.Chrome()
    driver.get(url)