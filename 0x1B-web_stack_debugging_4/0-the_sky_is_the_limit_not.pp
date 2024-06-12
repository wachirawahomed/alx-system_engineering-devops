# This Puppet manifest optimizes Nginx configuration for handling high concurrency.

exec { 'fix--for-nginx':
  command     => '/usr/sbin/nginx -s reload',
  refreshonly => true,
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Exec['fix--for-nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Exec['fix--for-nginx'],
}

class { 'nginx':
  package_ensure => 'present',
  service_ensure => 'running',
  service_enable => true,
}
