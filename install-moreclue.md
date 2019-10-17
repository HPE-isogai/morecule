https://molecule.readthedocs.io/en/stable/installation.html#centos-7

# Prerequite
- Ansible Tower Server
-- RHEL 7.6
-- minimal install
-- install ansible tower
-- yum update

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
pip install --upgrade setuptools
pip install --user molecule
```
1.1. Install Docker
```
sudo yum remove docker docker-common docker-selinux docker-engine-selinux docker-engine docker-ce
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yumconfig-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce
```
1.1 install python dependency
```
pip install docker-py
```

post install
```
sudo systemctl enable docker.service
sudo systemctl restart docker
```
confirmation
```
docker --version
sudo docker run hello-world
```
