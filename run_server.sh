source venv/bin/activate
sudo /etc/init.d/nginx restart
uwsgi --socket :8080 --module recordserver.wsgi
