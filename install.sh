#!/bin/bash

if which pyenv > /dev/null; then
    eval "$(pyenv init -)"
else
    echo "pyenv is not installed"
fi

shopt -s expand_aliases

if [ ! -d ~/.pyenv/versions/keystone-python ]; then

    if [ ! -d ~/.pyenv/versions/2.7.8 ]; then
        pyenv install 2.7.8
    fi

    pyenv virtualenv 2.7.8 keystone-python
    pyenv shell keystone-python
    pyenv rehash
fi

pyenv shell keystone-python

pip install https://github.com/openstack/keystone/tarball/ed1b10f#egg=keystone
pip install mysql-python

DESTINATION=python/Lib

mkdir -p $DESTINATION

cp -r $(pyenv prefix)/lib/python2.7/site-packages/* $DESTINATION
cp -r keystone_jvm python/Lib

touch $DESTINATION/dogpile/__init__.py
touch $DESTINATION/oslo/__init__.py
touch $DESTINATION/paste/__init__.py
touch $DESTINATION/repoze/__init__.py

sed -i -e '/SET SESSION/d' $DESTINATION/oslo/db/sqlalchemy/session.py
