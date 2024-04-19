# Puppet manifest to kill a process named "killmenow"
# Must use 'exec' and 'pkill'

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/bin:/usr/bin',
  refreshonly => true,
}

