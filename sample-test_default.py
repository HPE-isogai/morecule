import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_user(host):
    user = host.user("testuser01")

    assert user.name == "testuser01"
    assert user.uid == 9876
    assert user.gid == 9876
    assert user.group == "testgroup01"


def test_group(host):

    assert host.group("testgroup01").exists
    assert host.group("testgroup01").gid == 9876
