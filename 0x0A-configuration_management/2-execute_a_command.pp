# Puppet manifest to kill a process named "killmenow"

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/bin:/usr/bin',
  refreshonly => true,
}
