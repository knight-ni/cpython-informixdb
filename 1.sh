rm -rf build/*
rm -rf dist/*
rm -rf __pycache__
rm -rf InformixDB.egg-info
/usr/local/python3/bin/python3.9 setup.py sdist
/usr/local/python3/bin/python3.9 setup.py bdist_wheel --universal

