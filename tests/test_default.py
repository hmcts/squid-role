import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_squid_running_and_enabled(host):
    squid = host.service("squid")
    assert squid.is_running
    assert squid.is_enabled


# Requires netstat or ss to be installed in the container, so doesn't work.
# def test_squid_socket_listening(host):
#     assert host.socket("tcp://8080").is_listening
