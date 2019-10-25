## Purpose of this playbook
- add group and user

## Prerequisite
- set virtualenv
- set initial enviromnent in *molecule/default/molecule.yml*
```
---
dependency:
  name: galaxy
driver:
  name: docker
lint:
  name: yamllint
platforms:
  - name: centos7
    image: centos:7
provisioner:
  name: ansible
  lint:
    name: ansible-lint
verifier:
  name: testinfra
  lint:
    name: flake8
```

## Parameter file (*defaults/main.yml*)
```
username: "testuser01"
groupname: "testgroup01"
gid: 9876
uid: 9876
```
## test code (*molecule/default/tests/test_default.py*)
```
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


def test_user_name(host):
    passwd = host.file("/etc/passwd")

    assert passwd.contains("testuser01")


def test_group_name(host):
    group = host.file("/etc/group")

    assert group.contains("testgroup01")
```
## Automation task (role) (*tasks/main.yml*)
```
- name: add group
  group:
    name: "{{ groupname }}"
    gid: "{{ gid }}"

- name: add user
  user:
    name: "{{ username }}"
    uid: "{{ uid }}"
    group: "{{ groupname }}"
```

## Test result
`molecule test`
```
--> Validating schema /home/newgen/user-add/molecule/default/molecule.yml.
Validation completed successfully.
--> Test matrix

└── default
    ├── lint
    ├── dependency
    ├── cleanup
    ├── destroy
    ├── syntax
    ├── create
    ├── prepare
    ├── converge
    ├── idempotence
    ├── side_effect
    ├── verify
    ├── cleanup
    └── destroy

--> Scenario: 'default'
--> Action: 'lint'
--> Executing Yamllint on files found in /home/newgen/user-add/...
Lint completed successfully.
--> Executing Flake8 on files found in /home/newgen/user-add/molecule/default/tests/...
Lint completed successfully.
--> Executing Ansible Lint on /home/newgen/user-add/molecule/default/playbook.yml...
Lint completed successfully.
--> Scenario: 'default'
--> Action: 'dependency'
Skipping, missing the requirements file.
--> Scenario: 'default'
--> Action: 'cleanup'
Skipping, cleanup playbook not configured.
--> Scenario: 'default'
--> Action: 'destroy'
--> Sanity checks: 'docker'

    PLAY [Destroy] *****************************************************************

    TASK [Destroy molecule instance(s)] ********************************************
    changed: [localhost] => (item=centos7)

    TASK [Wait for instance(s) deletion to complete] *******************************
    ok: [localhost] => (item=None)
    ok: [localhost]

    TASK [Delete docker network(s)] ************************************************

    PLAY RECAP *********************************************************************
    localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

--> Scenario: 'default'
--> Action: 'syntax'
--> Sanity checks: 'docker'

    playbook: /home/newgen/user-add/molecule/default/playbook.yml
--> Scenario: 'default'
--> Action: 'create'

    PLAY [Create] ******************************************************************

    TASK [Log into a Docker registry] **********************************************
    skipping: [localhost] => (item=None)

    TASK [Create Dockerfiles from image names] *************************************
    changed: [localhost] => (item=None)
    changed: [localhost]

    TASK [Determine which docker image info module to use] *************************
    ok: [localhost]

    TASK [Discover local Docker images] ********************************************
    ok: [localhost] => (item=None)
    ok: [localhost]

    TASK [Build an Ansible compatible image (new)] *********************************
    ok: [localhost] => (item=molecule_local/centos:7)

    TASK [Build an Ansible compatible image (old)] *********************************
    skipping: [localhost] => (item=molecule_local/centos:7)

    TASK [Create docker network(s)] ************************************************

    TASK [Determine the CMD directives] ********************************************
    ok: [localhost] => (item=None)
    ok: [localhost]

    TASK [Create molecule instance(s)] *********************************************
    changed: [localhost] => (item=centos7)

    TASK [Wait for instance(s) creation to complete] *******************************
    FAILED - RETRYING: Wait for instance(s) creation to complete (300 retries left).
    changed: [localhost] => (item=None)
    changed: [localhost]

    PLAY RECAP *********************************************************************
    localhost                  : ok=7    changed=3    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0

--> Scenario: 'default'
--> Action: 'prepare'
Skipping, prepare playbook not configured.
--> Scenario: 'default'
--> Action: 'converge'

    PLAY [Converge] ****************************************************************

    TASK [Gathering Facts] *********************************************************
    ok: [centos7]

    TASK [user-add : add group] ****************************************************
    changed: [centos7]

    TASK [user-add : add user] *****************************************************
    changed: [centos7]

    PLAY RECAP *********************************************************************
    centos7                    : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

--> Scenario: 'default'
--> Action: 'idempotence'
Idempotence completed successfully.
--> Scenario: 'default'
--> Action: 'side_effect'
Skipping, side effect playbook not configured.
--> Scenario: 'default'
--> Action: 'verify'
--> Executing Testinfra tests found in /home/newgen/user-add/molecule/default/tests/...
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.5, pytest-4.6.6, py-1.8.0, pluggy-0.13.0
    rootdir: /home/newgen/user-add/molecule/default
    plugins: testinfra-3.2.0
collected 3 items

    tests/test_default.py ...                                                [100%]

    =========================== 3 passed in 2.49 seconds ===========================
Verifier completed successfully.
--> Scenario: 'default'
--> Action: 'cleanup'
Skipping, cleanup playbook not configured.
--> Scenario: 'default'
--> Action: 'destroy'

    PLAY [Destroy] *****************************************************************

    TASK [Destroy molecule instance(s)] ********************************************
    changed: [localhost] => (item=centos7)

    TASK [Wait for instance(s) deletion to complete] *******************************
    FAILED - RETRYING: Wait for instance(s) deletion to complete (300 retries left).
    changed: [localhost] => (item=None)
    changed: [localhost]

    TASK [Delete docker network(s)] ************************************************

    PLAY RECAP *********************************************************************
    localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

--> Pruning extra files from scenario ephemeral directory
```

