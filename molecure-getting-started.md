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

