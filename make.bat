@echo off

for %%i in (%cd%) do set project=%%~ni
set /p version=<VERSION.txt

python -m robot.libdoc -F html -v %version% %cd%\_doc\%project% %cd%\doc\%project%.html
python setup.py sdist
python setup.py install