@ECHO OFF

python3 setup.py install
python setup.py install

RMDIR /S /Q Beet.egg-info
RMDIR /S /Q build
RMDIR /S /Q dist

ECHO Done!
pause >nul