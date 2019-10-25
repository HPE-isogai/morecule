## Python 3 Install
$ sudo yum install -y python36 python36-libs python36-devel python36-pip
$ whereis python
python: /usr/bin/python /usr/bin/python2.7 /usr/bin/python2.7-config /usr/bin/python3.6 /usr/bin/python3.6m /usr/lib/python2.7 /usr/lib/python3.6 /usr/lib64/python2.7 /usr/lib64/python3.6 /etc/python /usr/include/python2.7 /usr/include/python3.6m /usr/share/man/man1/python.1.gz
$ python3.6 --version
Python 3.6.8
$ python --version
Python 2.7.5

## Install virtualenv via pip3
$ pip3 --version
pip 9.0.3 from /usr/lib/python3.6/site-packages (python 3.6)
$ pip3 install --user virtualenv
Using base prefix '/usr'
  No LICENSE.txt / LICENSE found in source
New python executable in /home/newgen/molecule_ansible36/bin/python3.6
Also creating executable in /home/newgen/molecule_ansible36/bin/python
Installing setuptools, pip, wheel...
done.

## Set Virtualenv


## Install Molecule and dependencies
$ pip install ansible testinfra molecule docker
