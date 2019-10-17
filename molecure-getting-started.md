https://molecule.readthedocs.io/en/stable/getting-started.html

```
molecule init role -r my-new-role
```
You can find a new directory
```
ls ~/my-new-role/molecule/default
```

- molecure.yml
```
$ cat molecule.yml
---
dependency:
  name: galaxy
driver:
  name: docker
lint:
  name: yamllint
platforms:
  - name: instance
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

- task create
```
cd ~/my-new-role
molecure create
```
result
```
$ molecule create
--> Validating schema /home/newgen/my-new-role/molecule/default/molecule.yml.
Validation completed successfully.
--> Test matrix

└── default
    ├── dependency
    ├── create
    └── prepare

--> Scenario: 'default'
--> Action: 'dependency'
Skipping, missing the requirements file.
--> Scenario: 'default'
--> Action: 'create'
--> Sanity checks: 'docker'

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
    FAILED - RETRYING: Build an Ansible compatible image (new) (3 retries left).
    changed: [localhost] => (item=molecule_local/centos:7)

    TASK [Build an Ansible compatible image (old)] *********************************
    skipping: [localhost] => (item=molecule_local/centos:7)

    TASK [Create docker network(s)] ************************************************

    TASK [Determine the CMD directives] ********************************************
    ok: [localhost] => (item=None)
    ok: [localhost]

    TASK [Create molecule instance(s)] *********************************************
    changed: [localhost] => (item=instance)

    TASK [Wait for instance(s) creation to complete] *******************************
    FAILED - RETRYING: Wait for instance(s) creation to complete (300 retries left).
    changed: [localhost] => (item=None)
    changed: [localhost]

    PLAY RECAP *********************************************************************
    localhost                  : ok=7    changed=4    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0

--> Scenario: 'default'
--> Action: 'prepare'
Skipping, prepare playbook not configured.
```

- confirm
`molecure list`  
```
$ molecule list
--> Validating schema /home/newgen/my-new-role/molecule/default/molecule.yml.
Validation completed successfully.
Instance Name    Driver Name    Provisioner Name    Scenario Name    Created    Converged
---------------  -------------  ------------------  ---------------  ---------  -----------
instance         docker         ansible             default          true       false
```

- create task
`vi tasks/main.yml`  
```
tasks/main.yml
---
- name: Molecule Hello World!
  debug:
    msg: Hello, World!
---

`molecule converge`

```
--> Validating schema /home/newgen/my-new-role/molecule/default/molecule.yml.
Validation completed successfully.
--> Test matrix

└── default
    ├── dependency
    ├── create
    ├── prepare
    └── converge

--> Scenario: 'default'
--> Action: 'dependency'
Skipping, missing the requirements file.
--> Scenario: 'default'
--> Action: 'create'
Skipping, instances already created.
--> Scenario: 'default'
--> Action: 'prepare'
Skipping, prepare playbook not configured.
--> Scenario: 'default'
--> Action: 'converge'

    PLAY [Converge] ****************************************************************

    TASK [Gathering Facts] *********************************************************
    ok: [instance]

    TASK [my-new-role : Molecule Hello World!] *************************************
    ok: [instance] => {
        "msg": "Hello, World!"
    }

    PLAY RECAP *********************************************************************
    instance                   : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

[newgen@ansibletower01 my-new-role]$ molecule login
--> Validating schema /home/newgen/my-new-role/molecule/default/molecule.yml.
Validation completed successfully.
```
