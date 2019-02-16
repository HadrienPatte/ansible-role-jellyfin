import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package_is_installed(host):
    package = host.package('jellyfin')
    assert package.is_installed


def test_service_is_running(host):
    service = host.service('jellyfin')
    assert service.is_running


def test_service_is_enabled(host):
    service = host.service('jellyfin')
    assert service.is_enabled
