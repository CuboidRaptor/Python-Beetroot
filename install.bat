@ECHO OFF

python setup.py install

RMDIR /S /Q Beetroot.egg-info
RMDIR /S /Q build
RMDIR /S /Q dist

ECHO Done!
pause >nul