.. title: php-fpm
.. slug: php-fpm
.. date: 2018-10-25 15:29:46 UTC+08:00
.. tags: php-fpm
.. category: php
.. link: 
.. description: 
.. type: text

cgi 公共网关接口 是http服务器和其他机器上的程序进行通信的接口，起程序运行在网络服务器上

fastcgi是常驻行的cgi，只要被激活一次，后面就不要每次都去fork一次，把cgi解释器保持在内存获得较高的效率，还支持分布式，可以放在网站服务器以外的主机上执行并且接受来自其他网站服务器的请求

cgi和fastcgi都独立与语言

php-fpm是FastCGI进程管理器

优点：fastcgi独立与服务器，提供了一个比api更安全的环境,sapi把程序的代码和核心web服务器链接在一起，这样一个错误的api会影响其他的应用程序和核心服务器，恶意的挨批应用程序会截取另外的应用程序和核心服务器的密钥，不依赖web服务器

缺点：因为是多进程的，所以比cgi多线程消耗内存（线程之间可共享），

原理：

1.Web服务器启动时，载入FastCGI进程管理器；

2.FastCGI进程管理器初始化，启动多个CGI解释器进程(PHP-CGI)并等待来自Web服务器的连接；

3.当客户端请求到达Web服务器时，FastCGI进程管理器选择并连接到一个CGI解释器，Web服务器将CGI环境变量和标准输入发送到FastCGI子进程PHP-CGI。

4.FastCGI子进程完成处理后将标准输出和错误信息从同一连接返回给Web服务器。当FastCGI子进程关闭连接时，请求便告知处理完成。FastCGI子进程接着等待并处理来自FastCGI进程管理器(运行在Web服务器中)的下一个连接。而在CGI模式中，PHP-CGI在此便退出了。

在上述情况中，可以想象CGI通常有多慢，每一个Web请求PHP都必须重新解析php.ini、重新载入全部扩展，并重初始化全部数据结构。而使用FastCGI，所有这些都只在进程启动时发生一次。另外，数据库持久连接可以工作。

PHP-CGI是PHP自带的FastCGI管理器。

PHP-CGI的不足：

1.php-cgi变更php.ini配置后需重启php-cgi才能让新的php-ini生效，不可以平滑重启。

2.直接杀死php-cgi进程，php就不能运行了(PHP-FPM和Spawn-FCGI就没有这个问题，守护进程会平滑重新生成新的子进程)。

 PHP-FPM的使用非常方便，配置都是在PHP-FPM.ini的文件内，而启动、重启都可以从php/sbin/PHP-FPM中进行。更方便的是修改php.ini后可以直接使用PHP-FPM reload进行加载，无需杀掉进程就可以完成php.ini的修改加载

结果显示使用PHP-FPM可以使php有不小的性能提升。PHP-FPM控制的进程cpu回收的速度比较慢,内存分配的很均匀。

Nginx+PHP配置

1、进程数优化

pm = dynamic

pm.max_children = 300 最大进程数

pm.start_servers = 20 启动时的进程数

pm.min_spare_servers = 5 最小空闲进程数，少于这个会启动新的等待服务

pm.max_spare_servers = 35 最大空闲进程数 超过这个数会杀掉一部分

注：
dynamic - 表示子进程的数量在下面配置的基础上动态设置，还有static和ondemand选项
static - 子进程的数量是固定的（pm.max_children）
ondemand - 进程在有需求时才产生（当请求时，与 dynamic 相反，pm.start_servers 在服务启动时即启动max_children


2、最大请求数优化

pm.max_requests = 10240

NOTE:

这个用来处理因为PHP解析器或引用的第三方库时，造成的内存泄露问题。
一个进程处理的请求数超过这个，就不接受新的请求


3、最长执行时间优化（php.ini）

request_terminate_timeout = 20

NOTE:

这个是用来处理因为PHP执行时间超长而报502错误的解决。

这个时长配置可以在php.ini（max_execution_time）或php-fpm.conf中配置均可，为了不影响全局配置，可在php-fpm.conf中实现。


PHP-FPM设置的脚本最大执行时间已经够长了，但执行耗时PHP脚本时，发现Nginx报错变为504错误。这是因为我们修改的只是PHP的配置，Nginx中也有关于与上游服务器通信超时时间的配置factcgi_connect/read/send_timeout。

查看php进程数 ps aux | grep -c php-fpm
