![NOKIA](https://raw.githubusercontent.com/nokia/nsp-workflow/master/logo.png)
# Ansible Collection - nokia.sros

***

This [collection](https://galaxy.ansible.com/nokia/sros) is to provide automation for Nokia SR OS devices using Ansible by RedHat.

## Installation
Distribution is via [ansible-galaxy](https://galaxy.ansible.com/).
To install this collection, please use the following command:
```bash
ansible-galaxy collection install nokia.sros
```

## Requirements
* Ansible 2.9+

## Supported Nokia SR OS versions
Tested with SR OS 19.5, 19.7 and 19.10

## Playbooks
### Classic CLI
* [sros_classic_cli_command_demo.yml](https://raw.githubusercontent.com/nokia/sros-ansible/master/playbooks/sros_classic_cli_command_demo.yml)
* [sros_classic_cli_config_demo.yml](https://raw.githubusercontent.com/nokia/sros-ansible/master/playbooks/sros_classic_cli_config_demo.yml)
* [sros_classic_cli_backup_restore_demo.yml](https://raw.githubusercontent.com/nokia/sros-ansible/master/playbooks/sros_classic_cli_backup_restore_demo.yml)
### MD-CLI
* [sros_mdcli_command_demo.yml](https://raw.githubusercontent.com/nokia/sros-ansible/master/playbooks/sros_mdcli_command_demo.yml)
* [sros_mdcli_config_demo.yml](https://raw.githubusercontent.com/nokia/sros-ansible/master/playbooks/sros_mdcli_config_demo.yml)
* [sros_mdcli_backup_restore_demo.yml](https://raw.githubusercontent.com/nokia/sros-ansible/master/playbooks/sros_mdcli_backup_restore_demo.yml)
### NETCONF
* [sros_nc_state_demo.yml](https://raw.githubusercontent.com/nokia/sros-ansible/master/playbooks/sros_nc_state_demo.yml)

## Modules
None

## Roles
None

## Plugins
|     Network OS     | terminal | cliconf | netconf |
|--------------------|:--------:|:-------:|:-------:|
| nokia.sros.md      |     Y    |    Y    |    Y    |
| nokia.sros.classic |     Y    |    Y    |    -    |

## Usage
To use this collection make sure to set `ansible_network_os=nokia.sros.{mode}` in your host inventory.
Nodes managed in classic-mode must have rollbacks configured. Example to enable rollback can be found in
[sros_classic_cli_commission.yml](https://raw.githubusercontent.com/nokia/sros-ansible/master/playbooks/sros_classic_cli_commission.yml).
NETCONF plugin currently does not work, due to issue [#65655](https://github.com/ansible/ansible/issues/65655) in Ansible. 
