# creates a file in /tmp
file { '/home/vagrant/.ssh/config':
  ensure  => file,
  source => '/home/vagrant/holberton-system_engineering-devops/0x0B-ssh/2-ssh_config',
}
