# client configuration file with puppet


file { '/etc/ssh/ssh_config':
   ensure  => file,
   mode    => '0600',
   content => "Host *
   IdentityFile ~/.ssh/school
   PasswordAuthentication no\n",
}
