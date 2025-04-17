#!/bin/bash
. ./.env
sudo mkdir -p /etc/nginx/certs
sudo openssl genpkey -algorithm RSA -out /etc/nginx/certs/private.key -pkeyopt rsa_keygen_bits:2048
sudo openssl req -new -key /etc/nginx/certs/private.key -out /etc/nginx/certs/certificate.csr -subj "/C=US/ST=State/L=City/O=Organization/OU=Unit/CN=${BASE_HOSTNAME}-443.app.github.dev"
sudo openssl x509 -req -days 365 -in /etc/nginx/certs/certificate.csr -signkey ./certs/nginx.key -out ./certs/nginx.crt
