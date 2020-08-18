#!/usr/bin/env bash
# Sets up in wen servers for the deployment of web_static
apt-get update
apt-get -y install nginx
service nginx start
mkdir -p /data/ /data/{web_static/,web_static/releases/,web_static/shared/,web_static/releases/test/}
touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '42i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
