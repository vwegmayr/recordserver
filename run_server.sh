source venv/bin/activate
sudo /etc/init.d/nginx restart
uwsgi --socket :8000 --module recordserver.wsgi
