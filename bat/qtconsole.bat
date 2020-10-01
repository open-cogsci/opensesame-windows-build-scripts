ECHO Please don't close this window. (Doing so will close QtConsole.)
cd /D %~dp0
SET PATH=%PATH%;%~dp0\Library\bin
SET PATH=%PATH%;%~dp0\Scripts
Scripts\jupyter-qtconsole.exe
