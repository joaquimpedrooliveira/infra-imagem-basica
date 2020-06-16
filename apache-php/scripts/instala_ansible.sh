#!/bin/bash
while [ ! -f /var/lib/cloud/instance/boot-finished ]; do
  echo 'Aguardando finalização do cloud-init...'
  sleep 1
done

apt-get update && apt-get install -y python  python-pip ansible unzip
