https://molecule.readthedocs.io/en/stable/installation.html#centos-7
https://redhatnordicssa.github.io/how-we-test-our-roles

# Prerequite
- Ansible Tower Server  
-- RHEL 7.6  
-- minimal install  
-- install ansible tower  
-- yum update 
-- yum install gcc openssl-devel

# install Procedure
1. install ansible tower
1. install morecule
1.1. yum install `epel` `gcc` `pip` etc  
```
$ sudo yum install -y epel-release
$ sudo yum install -y gcc python-pip python-devel openssl-devel libselinux-python
```
1.1. Install Docker
```
sudo yum remove docker docker-common docker-selinux docker-engine-selinux docker-engine docker-ce
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yum config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce
gpasswd -a <username> docker
```
1.1. Install Morecule
## install using `virtualenv` is recommended.
```
sudo yum install python-virtualenv.noarch
cd ~
python2.7 -m virtualenv molecule_ansible27 # directory created
source ~/molecule_ansible27/bin/activate   # after that, virtualenv activated (molecule_ansible27)
pip install psutil
pip install --user ansible testinfra molecule docker
deactivate # exit virtualenv
```


