#!/usr/bin/pup
# Puppet manifest to install Flask package

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

