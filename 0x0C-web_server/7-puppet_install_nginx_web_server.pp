# Puppet manifest to install and configure Nginx web server

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

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure custom 404 page is configured
file { '/var/www/html/404.html':
  ensure  => file,
  content => "<html><body>Ceci n'est pas une page</body></html>",
}

# Configure redirection for /redirect_me
nginx::resource::vhost { 'redirect_me':
  www_root     => '/var/www/html',
  ensure       => present,
  listen_port  => 80,
  server_name  => 'localhost',
  location_cfg => {
    'return' => '301 https://www.youtube.com/watch?v=QH2-TGUlwu4;',
  },
  require => Package['nginx'],
}

