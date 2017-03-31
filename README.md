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
  
