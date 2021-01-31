"""Role testing files using testinfra"""


def test_daemon_config(host):
    """Check docker daemon config"""
    f = host.file("/etc/docker/daemon.json")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


def test_cron_job(host):
    """Check cron job"""
    cmd = "docker system prune --volumes --force"
    f = host.file('/var/spool/cron/crontabs/root').content_string
    assert cmd in f


def test_docker_service(host):
    """Check docker service"""
    s = host.service("docker")
    assert s.is_running
    assert s.is_enabled
