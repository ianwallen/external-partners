#!/bin/bash
. ./.env
sudo openssl genpkey -algorithm RSA -out ./certs/nginx.key -pkeyopt rsa_keygen_bits:2048
sudo chmod 644 ./certs/nginx.key
sudo openssl req -new -key ./certs/nginx.key -out ./certs/certificate.csr -subj "/C=US/ST=State/L=City/O=Organization/OU=Unit/CN=${BASE_HOSTNAME}-443.app.github.dev"
sudo openssl x509 -req -days 365 -in ./certs/certificate.csr -signkey ./certs/nginx.key -out ./certs/nginx.crt
