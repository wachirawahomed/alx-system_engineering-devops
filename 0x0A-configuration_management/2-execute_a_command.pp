# Puppet manifest to kill a process named "killmenow"
# Must use 'exec' and 'pkill'

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}

