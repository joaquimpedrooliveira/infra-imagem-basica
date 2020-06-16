def test_base_system(host):
  assert host.system_info.type == 'linux'
  assert host.system_info.distribution == 'ubuntu'
  assert host.system_info.release == '18.04'

def test_mysql_pkg_installed(host):
  mysql = host.package('mysql-server-5.7')
  assert mysql.is_installed
  assert mysql.version.startswith('5.7')

def test_mysql_srv_running_and_enabled(host):
  mysql = host.service('mysql')
  assert mysql.is_running
  assert mysql.is_enabled

def test_mysqld_bind_address(host):
  output = host.check_output("grep bind-address /etc/mysql/mysql.conf.d/mysqld.cnf")
  assert '0.0.0.0' in output
