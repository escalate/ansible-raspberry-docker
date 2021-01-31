# Ansible Role: Raspberry - Docker

[![CI](https://github.com/escalate/ansible-raspberry-docker/workflows/CI/badge.svg?event=push)](https://github.com/escalate/ansible-raspberry-docker/actions?query=workflow%3ACI)

An Ansible role that manages [Docker CE](https://www.docker.com) on Raspberry Pi OS.

## Install

```
$ ansible-galaxy install escalate.raspberry-docker
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-docker/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: [requirements.yml](https://github.com/escalate/ansible-raspberry-docker/blob/master/requirements.yml)
* Collections: None

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.raspberry-docker
      tags: docker
```

## License

MIT
