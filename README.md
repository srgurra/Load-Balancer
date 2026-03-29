# load-balancer
configuration of nginx as a load balancer

Load Balancer is a server that distribute traffic to different servers. It can also act as reverse proxy to redirect different apis to different servers

Implemented for nginx server on local machine to act as load balancer

install nginx and start on machine

modify nginx.conf

nginx run on some port and is made it public. so it listens on 0.0.0.0 i.e., all calls over internet

once it receives a https call it redirects to servers mentioned in location block

It can also redirect based on path like /orders to one server and /users to another etc.,

This load blancer is made secure using SSL
for SSL
need to install certbot (brew install certbot)

generate certificate certbot --nginx

