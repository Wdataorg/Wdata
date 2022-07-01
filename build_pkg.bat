C:\Users\S.X.Y\AppData\Local\Programs\Python\Python310\python.exe setup.py sdist
C:\Users\S.X.Y\AppData\Local\Programs\Python\Python310\python.exe -m twine upload dist/*
cd dist
C:\Users\S.X.Y\AppData\Local\Programs\Python\Python310\python.exe -m pip3 install ./Wdata-1.0.0.tar.gz
cd ../
del  /s /Q dist
del /S /Q Wdata-1.0.0
del /S /Q Wdata.egg-info
rmdir dist
rmdir Wdata-1.0.0
rmdir Wdata.egg-info