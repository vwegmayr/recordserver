
SERVER_IP="192.168.0.59"

sudo pip install virtualenv
virtualenv venv
source venv/bin/activate

pip install configparser
pip install pyaml
pip install gitpython
pip install git+http://github.com/vwegmayr/sumatra
pip install git+https://github.com/vwegmayr/sumatra_server
sudo apt-get install nginx
pip install django-registration
pip install uwsgi

nginx_conf="
server {
    listen 8080;
    server_name server_ip;
    charset utf-8;
    client_max_body_size 75M;

    location /media  {
        alias cwd/media;
    }

    location /static {
        alias cwd/static;
    }

    location / {
        include cwd/uwsgi_params;
        uwsgi_pass 127.0.0.1:8000;
    }
}
"

nginx_conf=${nginx_conf//server_ip/$SERVER_IP}
nginx_conf=${nginx_conf//cwd/$(pwd)}
echo "$nginx_conf" > recordserver_nginx.conf

sudo rm /etc/nginx/sites-enabled/recordserver_nginx.conf
sudo ln -s $(pwd)"/recordserver_nginx.conf" /etc/nginx/sites-enabled/

./manage.py migrate
./manage.py createsuperuser --username vwegmayr --email vwegmayr@inf.ethz.ch
./manage.py collectstatic --noinput
