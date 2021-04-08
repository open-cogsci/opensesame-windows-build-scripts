ECHO Please don't close this window. (Doing so will close PsychoPy.)
cd /D %~dp0
SET PATH=%~dp0\Library\bin;%PATH%
SET PATH=%~dp0\Scripts;%PATH%
python.exe Lib\site-packages\psychopy\app\psychopyApp.py
