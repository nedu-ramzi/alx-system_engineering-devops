# installs an nginx server and creates a custom http header response

# install nginx
exec { 'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec { 'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

# add custom header
exec { 'add_header':
  provider    => shell,
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$hostname\";/" /etc/nginx/nginx.conf'
  before      => Exec['restart Nginx'],
}

# restart nginx services when the header changes have been made
exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
