# This Puppet manifest increases the file descriptor limit for the holberton user.

exec { 'increase-file-descriptor-limit':
  command => 'echo "holberton soft nofile 65536" >> /etc/security/limits.conf && echo "holberton hard nofile 65536" >> /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
  unless  => 'grep -q "holberton soft nofile 65536" /etc/security/limits.conf && grep -q "holberton hard nofile 65536" /etc/security/limits.conf',
}

exec { 'increase-pam-limits':
  command => 'echo "session required pam_limits.so" >> /etc/pam.d/common-session && echo "session required pam_limits.so" >> /etc/pam.d/common-session-noninteractive',
  path    => ['/bin', '/usr/bin'],
  unless  => 'grep -q "session required pam_limits.so" /etc/pam.d/common-session && grep -q "session required pam_limits.so" /etc/pam.d/common-session-noninteractive',
}
