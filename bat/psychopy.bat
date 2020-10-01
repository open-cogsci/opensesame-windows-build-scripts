ECHO Please don't close this window. (Doing so will close PsychoPy.)
cd /D %~dp0
SET PATH=%PATH%;%~dp0\Library\bin
SET PATH=%PATH%;%~dp0\Scripts
python.exe Lib\site-packages\psychopy\app\psychopyApp.py
