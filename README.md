# AngularFlask

### How to Get Started

1. fork this repo

2. clone your own version
> git clone git@github.com:YOUR_GITHUB_USERNAME/angular-flask.git && cd angular-flask

3. install all the necessary packages (best done inside of a virtual environment)
> pip install -r requirements.txt

4. run the app
> python runserver.py

5. create and seed the db (the server must still be running, so open a new terminal window first)
> python manage.py create_db && python manage.py seed_db --seedfile 'data/db_items.json'

6. check out your blog
> http://localhost:5000/blog

### Running with Apache (and mod_wsgi)

These instructions are for Fedora, for other Linux flavors modify the httpd parts accordingly

1. Make sure httpd and mod_wsgi are installed

> yum install httpd mod_wsgi

2. In /etc/httpd/conf/httpd.conf file add:
```
    <VirtualHost _default_:80>
    DocumentRoot /path/to/application

    WSGIDaemonProcess sandbox user=<username> group=<groupname> threads=15 maximum-requests=10000 python-path=/path/to/application/path/to/python/site-packages
    WSGIScriptAlias / /path/to/application/apache/angularflask.wsgi
    WSGIProcessGroup <name_of_application>

    CustomLog "|/usr/sbin/rotatelogs /path/to/application/apache/logs/access.log.%Y%m%d-%H%M%S 5M" combined
    ErrorLog "|/usr/sbin/rotatelogs /path/to/application/apache/logs/error.log.%Y%m%d-%H%M%S 5M"
    LogLevel warn

    <Directory /path/to/application>
        Order deny,allow
        Allow from all
    </Directory>

    </VirtualHost>
```
3. Uncomment "NameVirtualHost *:80" in httpd.conf file

4. Make sure you create the /path/to/application/apache/logs folder

5. Make sure that in WSGIDaemonProcess, the python-path=/path/to/application/path/to/python/site-packages points to the virtualenv that you created with "pip install -r requirements.txt"


