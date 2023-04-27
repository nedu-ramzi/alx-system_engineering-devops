# install nginx with puppet

class nginx {
   package { 'nginx':
     ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
    }

   file { '/var/www/html/index.html':
     ensure => present,
     content => "Hello World!\n",
   }

   file { '/etc/nginx/sites-available/default':
     ensure => present,
     content => "
       server {
         listen 80 default_server;
	 listen [::]:80 default_server;
	 server_name _;
	 root /var/www/html;
	 index index.html;
	 location /redirect_me {
	   return 301 /;
	   }
	  }
	 "},
	}

   file { '/etc/nginx/sites-enabled/default':
     ensure => 'link',
     target => '/etc/nginx/sites-available/default',
   }

   exec { 'nginx_reload':
     command     => '/usr/sbin/service nginx reload',
     refreshonly => true,
     }
   }

   include nginx

