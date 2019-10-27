# Requirements
- OS: RHEL 7.6
- Set Subscription
- yum update

## Python 3 Install
$ sudo yum-config-manager --enable rhel-server-rhscl-7-rpms
$ sudo yum-config-manager --enable rhel-server-rhscl-beta-7-rpms

$ sudo yum install rh-python36

$ whereis python
python: /usr/bin/python /usr/bin/python2.7 /usr/bin/python2.7-config /usr/bin/python3.6 /usr/bin/python3.6m /usr/lib/python2.7 /usr/lib/python3.6 /usr/lib64/python2.7 /usr/lib64/python3.6 /etc/python /usr/include/python2.7 /usr/include/python3.6m /opt/rh/rh-python36/root/usr/bin/python /opt/rh/rh-python36/root/usr/bin/python3.6 /opt/rh/rh-python36/root/usr/bin/python3.6m /opt/rh/rh-python36/root/usr/bin/python3.6-config /opt/rh/rh-python36/root/usr/bin/python3.6m-config /opt/rh/rh-python36/root/usr/bin/python3.6m-x86_64-config /usr/share/man/man1/python.1.gz

$ sudo yum list rh-python36\*
$ sudo yum list rh-python36\*
読み込んだプラグイン:product-id, subscription-manager
インストール済みパッケージ
rh-python36.x86_64                           2.0-1.el7           @rhel-server-rhscl-7-rpms
rh-python36-python.x86_64                    3.6.3-7.el7         @rhel-server-rhscl-7-rpms
rh-python36-python-devel.x86_64              3.6.3-7.el7         @rhel-server-rhscl-7-rpms
rh-python36-python-libs.x86_64               3.6.3-7.el7         @rhel-server-rhscl-7-rpms
rh-python36-python-pip.noarch                9.0.1-2.el7         @rhel-server-rhscl-7-rpms
rh-python36-python-setuptools.noarch         36.5.0-1.el7        @rhel-server-rhscl-7-rpms
rh-python36-python-virtualenv.noarch         15.1.0-2.el7        @rhel-server-rhscl-7-rpms
rh-python36-runtime.x86_64                   2.0-1.el7           @rhel-server-rhscl-7-rpms
rh-python36-scldevel.x86_64                  2.0-1.el7           @rhel-server-rhscl-7-rpms
利用可能なパッケージ
rh-python36-PyYAML.x86_64                    3.12-1.el7          rhel-server-rhscl-7-rpms
rh-python36-babel.noarch                     2.5.1-1.el7         rhel-server-rhscl-7-rpms
rh-python36-mod_wsgi.x86_64                  4.5.18-1.el7        rhel-server-rhscl-7-rpms
rh-python36-numpy.x86_64                     1:1.13.1-1.el7      rhel-server-rhscl-7-rpms
rh-python36-numpy-f2py.x86_64                1:1.13.1-1.el7      rhel-server-rhscl-7-rpms
rh-python36-python-PyMySQL.noarch            0.7.11-1.el7        rhel-server-rhscl-7-rpms
rh-python36-python-babel.noarch              2.5.1-1.el7         rhel-server-rhscl-7-rpms
rh-python36-python-bson.x86_64               3.5.1-1.el7         rhel-server-rhscl-7-rpms
rh-python36-python-coverage.x86_64           4.4.1-2.el7         rhel-server-rhscl-7-rpms
rh-python36-python-debug.x86_64              3.6.3-7.el7         rhel-server-rhscl-7-rpms
rh-python36-python-docutils.noarch           0.14-1.el7          rhel-server-rhscl-7-rpms
rh-python36-python-jinja2.noarch             2.9.6-3.el7         rhel-server-rhscl-7-rpms
rh-python36-python-markupsafe.x86_64         1.0-1.el7           rhel-server-rhscl-7-rpms
rh-python36-python-nose.noarch               1.3.7-3.el7         rhel-server-rhscl-7-rpms
rh-python36-python-nose-docs.noarch          1.3.7-3.el7         rhel-server-rhscl-7-rpms
rh-python36-python-psycopg2.x86_64           2.7.3-1.el7         rhel-server-rhscl-7-rpms
rh-python36-python-psycopg2-doc.x86_64       2.7.3-1.el7         rhel-server-rhscl-7-rpms
rh-python36-python-pygments.noarch           2.2.0-1.el7         rhel-server-rhscl-7-rpms
rh-python36-python-pymongo.x86_64            3.5.1-1.el7         rhel-server-rhscl-7-rpms
rh-python36-python-pymongo-doc.x86_64        3.5.1-1.el7         rhel-server-rhscl-7-rpms
rh-python36-python-pymongo-gridfs.x86_64     3.5.1-1.el7         rhel-server-rhscl-7-rpms
rh-python36-python-simplejson.x86_64         3.11.1-1.el7        rhel-server-rhscl-7-rpms
rh-python36-python-six.noarch                1.11.0-1.el7        rhel-server-rhscl-7-rpms
rh-python36-python-sphinx.noarch             1.2.3-3.el7         rhel-server-rhscl-7-rpms
rh-python36-python-sphinx-doc.noarch         1.2.3-3.el7         rhel-server-rhscl-7-rpms
rh-python36-python-sqlalchemy.x86_64         1.1.14-1.el7        rhel-server-rhscl-7-rpms
rh-python36-python-test.x86_64               3.6.3-7.el7         rhel-server-rhscl-7-rpms
rh-python36-python-tkinter.x86_64            3.6.3-7.el7         rhel-server-rhscl-7-rpms
rh-python36-python-tools.x86_64              3.6.3-7.el7         rhel-server-rhscl-7-rpms
rh-python36-python-wheel.noarch              0.30.0a0-1.el7      rhel-server-rhscl-7-rpms
rh-python36-scipy.x86_64                     0.19.1-2.el7        rhel-server-rhscl-7-rpms


## Set Virtualenv
python3.6 -m virtualenv molecule_ansible36
$ source ~/molecule_ansible36/bin/activate
$ pip --version
pip 19.3.1 from /home/newgen/molecule_ansible36/lib/python3.6/site-packages/pip (python 3.6)

## Install Molecule and dependencies
$ pip install psutil
$ pip install ansible testinfra molecule docker
