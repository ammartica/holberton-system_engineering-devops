Project: 0x10. HTTPS SSL

This directory contains tasks that explore DNS and web stack debugging:

  0. Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains
  1. Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www.
