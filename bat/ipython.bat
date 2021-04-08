ECHO Please don't close this window. (Doing so will close IPython.)
cd /D %~dp0
SET PATH=%~dp0\Library\bin;%PATH%
SET PATH=%~dp0\Scripts;%PATH%
Scripts\ipython.exe
