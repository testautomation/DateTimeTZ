@echo off

for %%i in (%cd%) do set project=%%~ni
set /p version=<VERSION.txt

python setup.py install
python -m robot.libdoc -F html -v %version% %project% %cd%\doc\%project%.html