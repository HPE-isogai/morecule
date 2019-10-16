https://molecule.readthedocs.io/en/stable/installation.html#centos-7

# Prerequite
- Ansible Tower Server
-- RHEL 7.6
-- minimal install


# Procedure
1. install ansible tower
1. install morecule
1.1. yum install `epel` `gcc` `pip` etc  
```
$ sudo yum install -y epel-release
$ sudo yum install -y gcc python-pip python-devel openssl-devel libselinux-python
```
1.1. Install Morecule
```
pip install --
pip install --user molecule
```
1.1. Install Docker
```
