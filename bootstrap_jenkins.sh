virtualenv --no-setuptools .
mkdir -p buildout-cache/downloads
./bin/python bootstrap.py -v 1.6.3
./bin/buildout -N -t 3 -c jenkins.cfg
./bin/develop up -f
# Xvfb :99 -a &
