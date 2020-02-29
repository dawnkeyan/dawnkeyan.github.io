.. title: centos搭建PHP环境
.. slug: centosda-jian-phphuan-jing
.. date: 2018-11-05 15:07:02 UTC+08:00
.. tags: lnmp
.. category: linux
.. link: 
.. description: 
.. type: tex

操作系统: CentOS 7.4 64位

创建组和账号

groupadd 组名
useradd -g 组名-s /bin/bash 账号
nginx（1.14.0）

https://nginx.org/en/linux_packages.html#stable

vim /etc/yum.repos.d/nginx.repo

[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/7/$basearch/
gpgcheck=0
enabled=1
sudo yum install nginx

站点配置文件位置 /etc/nginx

mysql（5.6.4）

yum install mysql  mysql-devel mysql-server

但是centost 安装mysql-server 会找不到包

办法：官网下载安装mysql-server

wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm

rpm -ivh mysql-community-release-el7-5.noarch.rpm

yum install mysql-community-server

安装好后重启  service mysqld restart

进入mysql mysql -u root

设置root密码

set password for 'root'@'localhost' =password('xxxx');

修改配置文件

vim /etc/my.cnf

进入mysql

创建中小学账号 CREATE USER 'user'@'%' IDENTIFIED BY 'password'; （%可访问IP，%表示全部可访问）

创建数据库 create database 数据库名

授权账号数据库 grant all privileges on 数据库名.* to 账号@'%' identified by '密码';

刷新系统权限表 flush privileges;

可以使用的Navicat传输数据

mongo（3.6.x）

https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/index.html

vim /etc/yum.repos.d/mongodb-org-3.6.repo

[mongodb-org-3.6]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.6/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.6.asc
yum install -y mongodb-org

配置文件位置/etc/mongod.conf

MongoDB默认将数据文件存储在/var/lib/mongo目录，默认日志文件在/var/log/mongodb中。如果要修改, 可以把这两个文件放在空间大的硬盘 ，但是不要修改 /etc/mongod.conf ，我试过无法重启，应该是建软链接。

然后重启mongo

生成软连接

ln -s

相关命令service mongod start|stop|restart

mongo创建账号

use admin

db.createUser(

{

 user: "root",

 pwd: "密码",

 roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]

}

);

创建普通账号

use 数据库

db.createUser(

{

 user: "username",

 pwd: "password",

 roles: [ { role: "readWrite", db: "数据库名" } ]

}

);

修改密码db.changeUserPassword('账号','密码');

还原数据mongorestore -d db 数据库名 数据库文件

卸载yum erase $(rpm -qa | grep mongodb-org)

删除数据库文件和日志文件

PHP（5.6.36）

1.检查当前安装的PHP包

yum list installed | grep php

如果有安装的PHP包，先删除他们

yum remove php.x86_64 php-cli.x86_64 php-common.x86_64 php-gd.x86_64 php-ldap.x86_64 php-mbstring.x86_64 php-mcrypt.x86_64 php-mysql.x86_64 php-pdo.x86_64

2.加载安装包

Centos 5.X

 rpm -Uvh http://mirror.webtatic.com/yum/el5/latest.rpm

CentOs 6.x

 rpm -Uvh http://mirror.webtatic.com/yum/el6/latest.rpm

CentOs 7.X

 rpm -Uvh https://mirror.webtatic.com/yum/el7/epel-release.rpm

 rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm

如果想删除上面安装的包，重新安装

rpm -qa | grep webstatic

rpm -e  上面搜索到的包即可

3.运行yum install

yum install php56w.x86_64 php56w-cli.x86_64 php56w-common.x86_64 php56w-gd.x86_64 php56w-ldap.x86_64 php56w-mbstring.x86_64 php56w-mcrypt.x86_64 php56w-mysql.x86_64 php56w-pdo.x86_64

注：如果想用其他版本。把所有56改成其他的

4.安装php-fpm

yum install php56w-fpm (其他版本对应改掉56)

[root@zhishu /]# whereis php  （查看安装路径）

php: /usr/bin/php /usr/lib64/php /etc/php.d /etc/php.ini /usr/share/php /usr/share/man/man1/php.1.gz

5.安装

yum install php56w-bcmath

5.安装mongodb扩展

先执行命令php -m 查看是否已有

mkdir /usr/local/php-mongodb

cd usr/local/php-mongodb/

wget http://pecl.php.net/get/mongo-1.6.12.tgz

tar xvzf mongo-1.6.12.tgz

cd mongo-1.6.12

phpize（如果没有php-devel会报错The php-devel package is required for use of this command.  安装php-devel  ：yum install php56w-devel）

./configure --with-php-config=/usr/bin/php-config

make && make install

在php.ini文件中添加extension=mongo.so

extension=mongo.so

重启php-fpm或服务器

systemctl restart php-fpm

修改配置

vim /etc/php-fpm.d/www.conf

svn

https://tecadmin.net/install-svn-1-9-on-centos/

vim /etc/yum.repos.d/wandisco-svn.repo
[WandiscoSVN]
name=Wandisco SVN Repo
baseurl=http://opensource.wandisco.com/centos/$releasever/svn-1.10/RPMS/$basearch/
enabled=1
gpgcheck=0
yum -y install subversion

安装Java

下载安装包（也可以使用其他下载文件方式，拷过来的solr里如果已经有了就不用下载），因为认证问题，不能直接wget, 打开此页面 ，勾上Accept License Agreement，然后点击jdk-8u161-linux-x64.rpm,在下载页面获取文件下载地址，比如我本次的是http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jdk-8u161-linux-x64.rpm?AuthParam=1519538436_f233fa0ab4a9cba466bec47d360db37a，然后在/down目录下wget此地址。然后再重命名文件
mv jdk-8u161-linux-x64.rpm\?AuthParam\=1519538436_f233fa0ab4a9cba466bec47d360db37a jdk-8u161-linux-x64.rpm
安装
rpm -ivh jdk-8u161-linux-x64.rpm
配置系统环境变量，在/etc/profile里追加
JAVA_HOME=/usr/java/jdk1.8.0_161
JRE_HOME=$JAVA_HOME/jre
CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib
PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH
export PATH JAVA_HOME CLASSPATH
生效配置，并检验结果
source /etc/profile
java -version
nodejs (8.x)

https://nodejs.org/en/download/package-manager/#enterprise-linux-and-fedora

curl --silent --location https://rpm.nodesource.com/setup_8.x | sudo bash -
sudo yum -y install nodejs
git (2.x)

通过IUS安装git 最新版

1.安装ius repository

https://ius.io/GettingStarted/

yum install https://centos7.iuscommunity.org/ius-release.rpm

2.安装yum-plugin-replace

https://ius.io/Usage/#installing-ius-packages

yum install yum-plugin-replace

3.安装git2u 替换老的git

yum replace git --replace-with git2u

openvpn(2.4.x)

http://git.dev.backustech.com/apps/wiki/wikis/ubuntu16-%E5%AE%89%E8%A3%85-openvpn-2.4

yum install openvpn

加高效云盘：

1.在阿里云创建云盘，然后挂载云盘

2.登录服务器执行fdisk -l 可以看到刚刚买的硬盘

3.对这块硬盘进行分区 fdisk /dev/vdb（/dev/vdb可能不一样）

4.然后执行fdisk -l 可以看到看到新的分区




5.格式化新分区（使用ext3扩展文件系统）

mkfs.ext3 /dev/vdb1

6.创建挂载目录mkdir data

7.挂载分区到目录

mount /dev/vdb1 /data

8.设置开机自动挂载 vim /etc/fstab

在文件最后加入/dev/vdb1        /data                   ext3  defaults    0 0

9.然后重启reboot（线上不要随便重启服务器，考虑实际情况可不可以重启）

10.用df就可以看到了

安装crontab

yum -y install vixie-cron
