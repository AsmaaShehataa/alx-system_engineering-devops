# Create a puppet manifest file to install flask package
package { 'flask':
    ensure   => '2.1.1',
    provider => 'pip3'
    }
