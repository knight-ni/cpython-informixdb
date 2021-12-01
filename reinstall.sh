#/bin/sh
rm -rf build/
rm -rf dist/
rm -rf InformixDB.egg-info/
rm -rf __pycache__/
/usr/local/python3/bin/python3.9 setup.py install

