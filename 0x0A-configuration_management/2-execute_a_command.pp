# kills the process killmenow
exec { 'pkill':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'pkill killmenow',
}
