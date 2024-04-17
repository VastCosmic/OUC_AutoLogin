@echo off
REM 设置OUC_AutoLogin的路径
set OUC_AutoLogin_PATH=%~dp0OUC_AutoLogin.py

REM 启动OUC_AutoLogin
start pythonw %OUC_AutoLogin_PATH%
