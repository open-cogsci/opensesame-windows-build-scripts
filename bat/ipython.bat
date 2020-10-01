ECHO Please don't close this window. (Doing so will close IPython.)
cd /D %~dp0
SET PATH=%PATH%;%~dp0\Library\bin
SET PATH=%PATH%;%~dp0\Scripts
Scripts\ipython.exe
