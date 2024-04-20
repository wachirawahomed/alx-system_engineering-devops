# Puppet manifest to install Flask package and its dependencies

package { 'python3':
  ensure => '3.8.10',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3'],
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3'],
}

