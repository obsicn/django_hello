# django_hello
Django hello world application running on cloud

1. Install apache httpd server

[root@vm10-0-0-21 ~]# yum install httpd.x86_64 httpd-devel.x86_64

[root@vm10-0-0-21 ~]# apachectl -v
Server version: Apache/2.4.6 (CentOS)
Server built:   Nov 14 2016 18:04:44

2. Install Python 3.6.1
Because the default python from the yum repository is 3.4, python 3.6.1 should been installed from source file.
  
  2.1. Install wget
  [root@vm10-0-0-21 ~]# yum install wget
  [root@vm10-0-0-21 ~]# wget -V
  GNU Wget 1.14 built on linux-gnu.
  
  2.2 Get the latest python version and uncompress

   #wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz

   #tar zxvf Python-3.6.1.tgz 
  2.3 Install the package required by build Python

  # yum install zlib-devel openssl-devel tcl-devel tk-devel sqlite-devel  readline-devel gdbm-devel xz-devel, bzip2-devel  

  2.4. run configure to generate the makefile 
  #./configure --prefix=/opt/python3 --enable-shared CFLAGS=-fPIC

  --prefix: the installation directory
  --enable-shared: generated python shared library which will be loaded by Apache httpd server
  --fPIC: for below error message

relocation R_X86_64_32S against `_Py_NotImplementedStruct' can not be used when making a shared object; recompile with -fPIC /opt/python3/lib/libpython3.6m.a: could not read symbols: Bad value
  2.5. make and install
  #make; make install
  2.6. Modify the .bash_profile for PATH and LD_LIBRARY_PATH environment variables
PATH=/opt/python3/bin:$PATH:$HOME/bin
export LD_LIBRARY_PATH=/opt/python3/lib

otherwise, will face following error when run python3:
/opt/python3/bin/python3.6: error while loading shared libraries: libpython3.6m.so.1.0: cannot open shared object file: No such file or directory

3. Configure the mod_wsgi environment

 3.1 create python virtual environment
  #python3 -m venv django_env

 3.2. Install mod_wsgi module
  #source django_env/bin/activate
  #pip install mod_wsgi
 3.3 Verity the mod_wsgi installation
(django_env) [myang@vm10-0-0-21 ~]$ pip list --format=columns
Package    Version
---------- -------
mod-wsgi   4.5.15 
pip        9.0.1  
setuptools 28.8.0 

will add executable file: mod_wsgi-express in virtual environment binary directory

(django_env) [myang@vm10-0-0-21 bin]$ ./mod_wsgi-express start-server
Server URL         : http://localhost:8000/
Server Root        : /tmp/mod_wsgi-localhost:8000:1000
Server Conf        : /tmp/mod_wsgi-localhost:8000:1000/httpd.conf
Error Log File     : /tmp/mod_wsgi-localhost:8000:1000/error_log (warn)
Request Capacity   : 5 (1 process * 5 threads)
Request Timeout    : 60 (seconds)
Startup Timeout    : 15 (seconds)
Queue Backlog      : 100 (connections)
Queue Timeout      : 45 (seconds)
Server Capacity    : 20 (event/worker), 20 (prefork)
Server Backlog     : 500 (connections)
Locale Setting     : en_US.UTF-8

(django_env) [myang@vm10-0-0-21 django_hello]$ ps -ef|grep http
myang    22319 21490  0 17:36 pts/1    00:00:00 httpd (mod_wsgi-express)   -f /tmp/mod_wsgi-localhost:8000:1000/httpd.conf -DMOD_WSGI_MPM_ENABLE_EVENT_MODULE -DMOD_WSGI_MPM_EXISTS_EVENT_MODULE -DMOD_WSGI_MPM_EXISTS_WORKER_MODULE -DMOD_WSGI_MPM_EXISTS_PREFORK_MODULE -k start -DFOREGROUND
myang    22321 22319  0 17:36 pts/1    00:00:00 (wsgi:localhost:8000:1000) -f /tmp/mod_wsgi-localhost:8000:1000/httpd.conf -DMOD_WSGI_MPM_ENABLE_EVENT_MODULE -DMOD_WSGI_MPM_EXISTS_EVENT_MODULE -DMOD_WSGI_MPM_EXISTS_WORKER_MODULE -DMOD_WSGI_MPM_EXISTS_PREFORK_MODULE -k start -DFOREGROUND
myang    22322 22319  0 17:36 pts/1    00:00:00 httpd (mod_wsgi-express)   -f /tmp/mod_wsgi-localhost:8000:1000/httpd.conf -DMOD_WSGI_MPM_ENABLE_EVENT_MODULE -DMOD_WSGI_MPM_EXISTS_EVENT_MODULE -DMOD_WSGI_MPM_EXISTS_WORKER_MODULE -DMOD_WSGI_MPM_EXISTS_PREFORK_MODULE -k start -DFOREGROUND
myang    22392 22319  0 17:37 pts/1    00:00:00 httpd (mod_wsgi-express)   -f /tmp/mod_wsgi-localhost:8000:1000/httpd.conf -DMOD_WSGI_MPM_ENABLE_EVENT_MODULE -DMOD_WSGI_MPM_EXISTS_EVENT_MODULE -DMOD_WSGI_MPM_EXISTS_WORKER_MODULE -DMOD_WSGI_MPM_EXISTS_PREFORK_MODULE -k start -DFOREGROUND
myang    22457 29269  0 17:38 pts/0    00:00:00 grep --color=auto http

stop http server
#/tmp/mod_wsgi-localhost:8000:1000/apachectl -k stop


4. Configure the integration between Django application with mod_wsgi application
add 'mod_wsgi.server' application in the settings.py file of Django project

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mod_wsgi.server',
)

#start the server with following command
#manage.py runmodwsgi
