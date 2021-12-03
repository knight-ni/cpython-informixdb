#/bin/sh
rm -rf build/
rm -rf dist/
rm -rf InformixDB.egg-info/
rm -rf __pycache__/
cd ..
/usr/local/python3/bin/pip3.9 uninstall -y InformixDB-Knight
cd informixdb
/usr/local/python3/bin/python3.9 setup.py install

