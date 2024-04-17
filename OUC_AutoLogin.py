# 安装Python3.11.0 
# https://www.python.org/downloads/release/python-3110/
#
# 安装Chrome浏览器
# https://www.google.cn/chrome/
#
# 安装selenium库
# pip install selenium

# 请在下面填入你登录的学工号和校园网密码 Please fill in your student ID and campus network password below.
# 例如 Example :
# user_account = "20001234567"
# user_password = "123456789"

user_account = "xxxxxxxxxxx"
user_password = "xxxxxxxxxx"

from selenium import webdriver

url="https://xha.ouc.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account="+user_account+"+&user_password="+user_password
driver = webdriver.Chrome()
driver.get(url)
