# Puppet manifest to add a custom HTTP header to Nginx configuration

# Define the custom HTTP header value as the hostname of the server
$hostname = $facts['hostname']

# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}

# Define custom HTTP header in Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'), # Assuming you have a template for Nginx configuration
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create a template for Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

