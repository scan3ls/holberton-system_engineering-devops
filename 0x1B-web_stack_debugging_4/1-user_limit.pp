# PLD via Jill Rogers(Jilroge7): remove limit for requests
exec { 'comment out limit':
    command => "sed -i 's/ULIMIT=/# ULIMIT=/g' /etc/default/nginx",
    path    => [ '/usr/bin', '/bin', '/usr/sbin', '/sbin' ],
}
exec { 'nginx restart':
    command => 'sudo service nginx restart',
    path    => '/usr/bin',
} ~>
service { 'nginx':
    ensure  => running,
}
