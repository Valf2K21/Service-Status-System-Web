@echo off
cd /d C:\Users\Valfrid\Programming\Projects\PythonProjects\Service Status System - Web
call env\Scripts\activate.bat
start http://127.0.0.1:5000/
python "Service Board System - Web.py"