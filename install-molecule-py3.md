** This steps are not completed **


## Python 3 Install
$ sudo yum install -y python36 python36-libs python36-pip
$ whereis python
python: /usr/bin/python /usr/bin/python2.7 /usr/bin/python2.7-config /usr/bin/python3.6 /usr/bin/python3.6m /usr/lib/python2.7 /usr/lib/python3.6 /usr/lib64/python2.7 /usr/lib64/python3.6 /etc/python /usr/include/python2.7 /usr/include/python3.6m /usr/share/man/man1/python.1.gz
$ python3.6 --version
Python 3.6.8
$ python --version
Python 2.7.5

## python3 depended package install
#doesn't work!! #$ sudo yum install -y rh-python36-python-devel.x86_64
$ sudo yum install https://centos7.iuscommunity.org/ius-release.rpm
$ 

## Set Virtualenv
python3.6 -m virtualenv molecule_ansible36
$ source ~/molecule_ansible36/bin/activate

## Install virtualenv via pip3
$ pip3 --version
pip 9.0.3 from /usr/lib/python3.6/site-packages (python 3.6)


$ pip --version
pip **19.3.1** from /home/newgen/molecule_ansible36/lib/python3.6/site-packages/pip (python 3.6)

## Install Molecule and dependencies
$ pip install psutil
$ pip install ansible testinfra molecule docker
