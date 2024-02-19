# Increase the ULIMIT of the default file

exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
}

# Restart Nginx service
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
  require => Exec['fix--for-nginx'],  # Ensure fix--for-nginx is executed first
}
