# This Puppet manifest optimizes Nginx configuration for handling high concurrency.

exec { '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
