squid3
=========

Ansible role to install and configure squid3 proxy/cache in RedHat/CentOS.

Requirements
------------

No specific requirements.

Role Variables
--------------

This role uses a mix of defaults and `host_vars/group_vars`.     
The defaults are used to set the most common squid3 config, present by default in the package repository.     
The `host_vars/group_vars` are best suited to create custom ACLs and http_access sentences.

### Globals
Variables listed in `defaults/main.yml`

`squid3_localnets`     
List of internal subnets, used to create the default ACL named localnet.

`squid3_sslports`     
List of ports authorized to used the CONNECT methhod, encrypted traffic.

`squid3_safeports`     
List of ports authorized to use HTTP in plain text.

`squid3_port`     
Port that squid3 daemon runs.

`squid3_outgoing_address`     
If specified, tells which IP address to direct the traffic.

`squid3_visible_hostname`
Visible proxy name. Appears in authentication dialog.

`squid3_acls`     
ACLs from default squid.conf. Can be used to create custom ACLs.

`squid3_http_access`     
http_access directives from default squid.conf. Can be used to create custom http_access.

`squid3_refresh_pattern`     
List of refresh_paterrn from defalt squid.conf. Can be used to create custom refresh_pattern.

### Custom
Custom variables. Can be used in `defaults/main.yml`, but it was made to best if in `host_vars` and `group_vars`.

`squid3_custom_localnets`     
Custom localnets.

`squid3_custom_sslports`     
Custom SSL ports.

`squid3_custom_safeports`     
Custom HTTP ports.

`squid3_custom_acls`     
Custom ACLs.

`squid3_custom_http_access`     
Custom http_access directives.

`squid3_custom_refresh_pattern`     
Custom refresh_pattern directives.

Example vars
------------
```
squid3_custom_acls:
  - { name: 'whitelist', type: 'dstdomain', arg: 'google.com' }
  - { name: 'blacklist', type: 'dstdomain', arg: '.facebook.com' }

squid3_localnets:
  - 10.0.0.0/8

squid3_custom_http_access:
  - { perm: 'allow', aclname: 'whitelist' }
  - { perm: 'deny', aclname: 'blacklist' }
```




Dependencies
------------

None.

Example Playbook
----------------
```
---
- hosts: all
  become: yes
  vars_files:
    - vars.yml
  roles:
    - squid-role
```



License
-------

MIT

Author Information
------------------

Jonatas Baldin      
<mailto:jonatas.baldin@gmail.com>      
http://deployeveryday.com
fixes devops@reform
