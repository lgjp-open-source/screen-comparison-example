::Set PYTHONPATH to Python automation library
set PYTHONPATH=C:\Program Files\LogiGear\TestArchitect\lib\python3\
 
:: switch to where this bat file is stored, and where therefore ta_main.py is
cd /d %0\..
 
::Invoke harness main file.
::Prerequisite:
::- Has Python installed on this machine
python ta_main.py
