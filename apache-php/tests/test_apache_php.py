def test_base_system(host):
  assert host.system_info.type == 'linux'
  assert host.system_info.distribution == 'ubuntu'
  assert host.system_info.release == '18.04'

def test_pkg_installed(host):
  apache = host.package('apache2')
  assert apache.is_installed
  assert apache.version.startswith('2.4')
  
  php = host.package('php7.2')
  assert php.is_installed

def test_apache_running_and_enabled(host):
  apache = host.service('apache2')
  assert apache.is_running
  assert apache.is_enabled
