# Puppet manifest to install and configure Nginx web server

# Ensure Nginx package is installed
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
  content => template('nginx/default.erb'), # Assuming you have a template for Nginx configuration
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure custom 404 page is configured
file { '/usr/share/nginx/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

# Ensure Nginx returns 200 when querying /
file { '/usr/share/nginx/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx returns a 301 redirect for /redirect_me
nginx::resource::vhost { 'redirect_me':
  www_root     => '/usr/share/nginx/html',
  ensure       => present,
  listen_port  => 80,
  server_name  => 'localhost',
  location_cfg => {
    'return' => '301 https://www.youtube.com/watch?v=QH2-TGUlwu4;',
  },
  require => Package['nginx'],
}
