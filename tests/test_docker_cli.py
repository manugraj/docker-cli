import docker_cli


def test_version():
    assert docker_cli.__version__ == '1.0.0'


def test_docker():
    assert docker_cli.is_docker_set() is True


def test_docker_compose():
    assert docker_cli.is_docker_compose_set() is True


def test_docker_ps():
    assert docker_cli.docker("ps").type == docker_cli.ResponseFormat.JSON.value


def test_docker_swarm():
    assert docker_cli.docker("swarm leave").type == docker_cli.ResponseFormat.JSON.STRING.value