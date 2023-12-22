# create a puppet manifest file to kill a running process
exec{ 'pkill':
    command  => 'pkill -f killmenow',
    provider => 'shell',
    }
