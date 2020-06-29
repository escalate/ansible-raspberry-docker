# Ansible Role: docker

An Ansible role that manages [Docker CE](https://www.docker.com) on Raspberry Pi OS and Debian based systems.

## Install

```
$ ansible-galaxy install escalate.docker
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-docker/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Example Playbook

```
- hosts: all
  roles:
    - escalate.docker
```

## Dependencies

None

## License

MIT
