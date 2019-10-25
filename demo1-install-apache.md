1. Set virtualenv
1. Create role
1. Construction of molecule role  
```
~ cd <dir>
tree
```
```
$ tree
.
├── AUTHORS
├── LICENSE
├── README.md
├── defaults
│   └── main.yml
├── files
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── molecule
│   ├── docker
│   │   ├── Dockerfile.j2
│   │   ├── create.yml
│   │   ├── destroy.yml
│   │   └── molecule.yml
│   ├── kvm
│   │   └── molecule.yml
│   └── shared
│       ├── playbook.yml
│       ├── prepare.yml
│       └── tests
│           └── test_default.py
├── tasks
│   └── main.yml
├── templates
├── tests
│   └── yamllint.yml
└── vars
    └── main.yml

13 directories, 17 files
```
1. Write test code
`cat molecule/shared/tests/test_default.py`
1. set parameter
`cat defaults/main.yml`
1. Write task
`cat tasks/main.yml`
1. Write handlers
`cat handlers/main.yml`

## Execute test
`molecule test -s docker`
