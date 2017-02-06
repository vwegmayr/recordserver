
SERVER_IP="129.132.45.56"

sudo pip install virtualenv
virtualenv venv
source venv/bin/activate

pip install configparser
pip install git+http://github.com/vwegmayr/sumatra
pip install git+https://github.com/vwegmayr/sumatra_server
sudo apt-get install nginx
pip install django-registration
pip install uwsgi

nginx_conf="upstream django {
    server 127.0.0.1:8000;
}

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
        uwsgi_pass 127.0.0.1:8000;
        include cwd/uwsgi_params;
    }
}"

nginx_conf=${nginx_conf//server_ip/$SERVER_IP}
nginx_conf=${nginx_conf//cwd/$(pwd)}
echo "$nginx_conf" > recordserver_nginx.conf

sudo ln -s $(pwd)"/recordserver_nginx.conf" /etc/nginx/sites-enabled/

python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic