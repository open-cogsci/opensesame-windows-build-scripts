@ECHO OFF
ECHO Please don't close this window. (Doing so will close OpenSesame.)
cd /D %~dp0
set PATH=%~dp0Scripts;%PATH%
python.exe Lib\site-packages\opensesame.py %*
