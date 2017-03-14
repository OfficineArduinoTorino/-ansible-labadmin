# ansible-labadmin

Ansible roles to setup a labadmin installation on an debian or ubuntu machine.

## Requirements

The following software must be installed on your machine:

- python2.7
- ansible (>= 2.0)
- sshpass

The following software must be installed on the machine you are provisioning:

- python
- openssh-server

On the provisioned machine there should be an unprivileged user than can use *sudo*.

## Setup

First of all we need to create a playbook, we'll use the shipped *development.yml* as a base so let's
copy that to a file named *playbook.yml*.

Open the file *playbook.yml* and edit the following options:


| Name | Description |
|----- | ------------|
| hosts | the ip of the host you want to provision |
| remote_user | the user we'll use to provision the host |

Then there's the following variables to update, remember to don't reuse the same password:


| Name | Description |
|----- | ------------|
| labadmin_mysql_password | password for the labadmin mysql user |
| labadmin_mysql_root_password | password for the mysql root user |
| labadmin_django_secret_key | random secret string for django, see below on how to generate one |
| labadmin_django_admin_user | admin user for labadmin |
| labadmin_django_admin_password | admin user password |
| labadmin_django_admin_email | admin user email |

You can generate a secret using:

```
# your python interpreter may be called differently e.g. python2.7 or python3
python tools/generatesecret.py
```

Finally we can run ansible with the following command:

```
ansible-playbook -i <ip of your host>, playbook.yml
```

If you authenticate with password you have to pass an additional *--ask-pass* option.
If you need a password to became use you have to pass an additional *--ask-sudo-pass* option.

## Available configurations variables


| Name | Description |
|----- | ------------|
| labadmin_mysql_user | mysql user for labadmin |
| labadmin_mysql_database | mysql database name for labadmin |
| labadmin_mysql_password | password for the labadmin mysql user |
| labadmin_mysql_root_password | password for the mysql root user |
| labadmin_service_user | system user for running labadmin, default: labadmin |
| labadmin_service_group | system group for runing labadmin, default: labadmin |
| labadmin_home | path for labadmin installation, default: /var/www/labadmin |
| labadmin_python_package | labadmin version as understood by pip, default: https://github.com/OfficineArduinoTorino/LabAdmin/archive/master.zip |
| labadmin_django_secret_key | random secret string for django, see tools/generatesecret.py |
| labadmin_django_admin_user | admin user for labadmin |
| labadmin_django_admin_password | admin user password |
| labadmin_django_admin_email | admin user email |
| labadmin_django_language| django installation language, default: it-it |
| labadmin_django_timezone| django installation timezone, default: Europe/Rome |
| labadmin_mqtt_entrance | labadmin mqtt notification, default: False |
