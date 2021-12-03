rm -rf build/*
rm -rf dist/*
rm -rf __pycache__
rm -rf InformixDB.egg-info
/usr/local/python3/bin/python3.9 setup.py sdist
/usr/local/python3/bin/python3.9 setup.py bdist_wheel --universal
/usr/local/python3/bin/python3.9 -m twine upload dist/InformixDB-Knight-*.tar.gz --verbose

