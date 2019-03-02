# Ansible Role: Jellyfin

[![Build Status](https://travis-ci.com/HadrienPatte/ansible-role-jellyfin.svg?branch=master)](https://travis-ci.com/HadrienPatte/ansible-role-jellyfin)

An Ansible Role that installs [Jellyfin](https://github.com/jellyfin/jellyfin) on Debian and Ubuntu.

## Requirements

None.

## Role Variables

* `jellyfin_HTTP_port`: HTTP port Jellyfin should bind to, defaults to `8096`
* `jellyfin_HTTPS_port`: HTTPS port Jellyfin should bind to, defaults to `8920`
* `jellyfin_FQDN`: Fully Qualified Domain Name of the server
* `jellyfin_HTTP_server`: HTTP reverse proxy server, possible values are
  `apache2` and `nginx`, defaults to `nginx`
* `jellyfin_certificate_path`: directory where the TSL/SSL certificate will be
* `jellyfin_generate_self_signed_certificate`: wether to generate a self-signed
  certificate, defaults to `true`. If you set this to `false`, make sure to have
  a certificate and private key in `jellyfin_certificate_path`, otherwise the
  role will fail to start the reverse proxy HTTP server.
* `jellyfin_remove_default`: set this to `true` to remove apache2/nginx default
  site

# Dependencies

* [hadrienpatte.self_signed_certificate](https://galaxy.ansible.com/hadrienpatte/self_signed_certificate)

# Example Playbook

```yaml
- name: Install Jellyfin
  hosts: all
  become: true
  roles:
    - hadrienpatte.jellyfin
```

## License

MIT

## Author Information

Hadrien Patte [![PGP 0xFB500BB0](https://peegeepee.com/badge/orange/FB500BB0.svg)](https://peegeepee.com/FB500BB0)
