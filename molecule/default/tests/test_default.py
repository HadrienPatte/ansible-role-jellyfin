import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    ('jellyfin'),
    ('nginx'),
])
def test_package_is_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize('name', [
    ('jellyfin'),
    ('nginx'),
])
def test_service_is_running(host, name):
    service = host.service(name)
    assert service.is_running


@pytest.mark.parametrize('name', [
    ('jellyfin'),
    ('nginx'),
])
def test_service_is_enabled(host, name):
    service = host.service(name)
    assert service.is_enabled
