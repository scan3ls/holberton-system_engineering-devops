# Use puppet to fix a typo
exec { 'typo_fixer':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
}