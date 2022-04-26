from subprocess import Popen, PIPE, STDOUT
import sys

def test_flit_help():
    p = Popen([sys.executable, '-m', 'flit', '--help'], stdout=PIPE, stderr=STDOUT)
    out, _ = p.communicate()
    assert 'Build wheel' in out.decode('utf-8', 'replace')

def test_flit_usage():
    p = Popen([sys.executable, '-m', 'flit'], stdout=PIPE, stderr=STDOUT)
    out, _ = p.communicate()
    assert 'Build wheel' in out.decode('utf-8', 'replace')
    assert p.poll() == 1

def test_flit_install_reqs():
    p = Popen([sys.executable, '-m', 'flit', 'install-reqs'], stdout=PIPE, stderr=STDOUT)
    out, _ = p.communicate()
    assert 'pip' in out.decode('utf-8', 'replace')
    assert p.poll() == 0
