# Puppet manifest to install Flask package and its dependencies

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3'],
}

