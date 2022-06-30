python setup.py sdist
twine upload dist/*
cd dist
pip3 install ./Wdata-1.0.0.tar.gz
cd ../
del  /s /Q dist
del /S /Q Wdata-1.0.0
del /S /Q Wdata.egg-info
rmdir dist
rmdir Wdata-1.0.0
rmdir Wdata.egg-info