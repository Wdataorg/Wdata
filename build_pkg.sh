python setup.py sdist 
twine upload dist/*
pip3 install dist/*
rm -rf dist
rm -rf Wdata-1.0.0
rm -rf Wdata.egg-info