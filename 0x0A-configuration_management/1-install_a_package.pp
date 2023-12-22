# Create a puppet manifest file to install flask package
package { 'flask':
  ensure   => 'present',
  provider => 'pip3',
  install_options => ['flask==2.1.0'],
}
