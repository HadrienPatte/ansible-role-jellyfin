import os

import pytest

import testinfra.utils.ansible_runner

from xml.etree import ElementTree

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    ('apt-transport-https'),
    ('gnupg2'),
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


@pytest.mark.parametrize('port', [
    ('8096'),
    # ('8920'),
    ('80'),
    ('443'),
])
def test_socket(host, port):
    assert host.socket('tcp://0.0.0.0:' + port).is_listening


@pytest.mark.parametrize('option, value', [
    ('PublicPort', '8096'),
    ('PublicHttpsPort', '8920'),
    ('HttpServerPortNumber', '8096'),
    ('HttpsPortNumber', '8920'),
])
def test_configuration(host, option, value):
    configuration = ElementTree.fromstring(
        host.file('/etc/jellyfin/system.xml').content)
    assert configuration.findall(option)[0].text == value
