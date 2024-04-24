# 安装Python3.11.0 
# https://www.python.org/downloads/release/python-3110/

# 请填入你登录的学工号和校园网密码 Please fill in your student ID and campus network password below.
# 示例 Example :
# user_account = "20001234567"
# user_password = "123456789"
# 请在下面的代码中填入你的学号和密码, 而不是在上面的示例 Please fill in your student ID and password in the code below instead of the example above.

import subprocess
import requests
import threading

user_account = "你的学号"
user_password = "密码"

url = "https://xha.ouc.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account=" + user_account + "&user_password=" + user_password

def is_connected():
    host = 'www.baidu.com'
    try:
        output = subprocess.check_output(['ping', '-n', '1', host], timeout=1)
        if 'TTL=' in output.decode('gbk'):
            print("Already Connected to the Internet")
            return True
        else:
            print("Not connected to the Internet")
            return False
    except subprocess.CalledProcessError as ex:
        print("Not connected to the Internet: "+str(ex))
        return False
    except subprocess.TimeoutExpired as ex:
        print("Not connected to the Internet: "+str(ex))
        return False

def send_request_login():
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("Login successful")
        else:
            print("Login failed")
    except requests.exceptions.RequestException as ex:
        print("Login failed: "+str(ex))

if __name__ == '__main__':
    if is_connected() == False:
        thread = threading.Thread(target=send_request_login)
        thread.start()
