virtualenv --no-setuptools .
mkdir -p buildout-cache/downloads
$(which echo) -e "[buildout]\nextends = buildout.d/travis.cfg" > buildout.cfg
./bin/python bootstrap.py -v 1.6.3
./bin/buildout
./bin/develop up -f
# Xvfb :99 -a &
