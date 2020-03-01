.. title: php-fpm和easyswoole性能简单对比
.. slug: php-fpmhe-easyswoolexing-neng-jian-dan-dui-bi
.. date: 2020-03-01 12:41:18 UTC+08:00
.. tags: swoole,laravel
.. category: php
.. link: 
.. description: 
.. type: text

条件说明 自己用的mac开发电脑，电脑还装了很多软件并在运行，但是swoole和php-fpm都在这运行，所以是公平的

swoole使用easyswoole框架

php-fpm 使用laravel框架

php-fpm配置:
max_requests=204800
max_children=100000
start_servers=100
max_spare_servers=1000
min_spare_servers100    

nginx配置：
worker_processes =4
worker_connections=100000

使用Mac自带的ab工工具，请求数10000，并发100

php-fpm结果

::

 wukeyan$ ab -n 15000 -c 100  http://auction.com/api/site/auction/getBeatIng
 This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
 Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
 Licensed to The Apache Software Foundation, http://www.apache.org/

 Benchmarking auction.com (be patient)
 Completed 1500 requests
 Completed 3000 requests
 Completed 4500 requests
 Completed 6000 requests
 Completed 7500 requests
 Completed 9000 requests
 Completed 10500 requests
 Completed 12000 requests
 Completed 13500 requests
 Completed 15000 requests
 Finished 15000 requests


 Server Software:        nginx/1.17.3
 Server Hostname:        auction.com
 Server Port:            80

 Document Path:          /api/site/auction/getBeatIng
 Document Length:        72 bytes

 Concurrency Level:      100
 Time taken for tests:   199.363 seconds
 Complete requests:      15000
 Failed requests:        0
 Total transferred:      4485000 bytes
 HTML transferred:       1080000 bytes
 Requests per second:    75.24 [#/sec] (mean)
 Time per request:       1329.084 [ms] (mean)
 Time per request:       13.291 [ms] (mean, across all concurrent requests)
 Transfer rate:          21.97 [Kbytes/sec] received

 Connection Times (ms)
              min  mean[+/-sd] median   max
 Connect:        0    0   0.4      0      28
 Processing:    98 1327 109.4   1333    1745
 Waiting:       95 1327 109.5   1333    1745
 Total:         98 1327 109.4   1334    1745

 Percentage of the requests served within a certain time (ms)
  50%   1334
  66%   1375
  75%   1399
  80%   1415
  90%   1460
  95%   1493
  98%   1529
  99%   1558
 100%   1745 (longest request)

cpu情况

.. image:: https://dawnkeyan.github.io/images/php-fpm_spu.jpeg



swoole结果

::

 wukeyan$ ab -n 15000 -c 100  http://127.0.0.1:9502/common/test
 This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
 Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
 Licensed to The Apache Software Foundation, http://www.apache.org/

 Benchmarking 127.0.0.1 (be patient)
 Completed 1500 requests
 Completed 3000 requests
 Completed 4500 requests
 Completed 6000 requests
 Completed 7500 requests
 Completed 9000 requests
 Completed 10500 requests
 Completed 12000 requests
 Completed 13500 requests
 Completed 15000 requests
 Finished 15000 requests


 Server Software:        EasySwoole
 Server Hostname:        127.0.0.1
 Server Port:            9502

 Document Path:          /common/test
 Document Length:        14 bytes

 Concurrency Level:      100
 Time taken for tests:   1.029 seconds
 Complete requests:      15000
 Failed requests:        0
 Total transferred:      2310000 bytes
 HTML transferred:       210000 bytes
 Requests per second:    14571.86 [#/sec] (mean)
 Time per request:       6.863 [ms] (mean)
 Time per request:       0.069 [ms] (mean, across all concurrent requests)
 Transfer rate:          2191.47 [Kbytes/sec] received

 Connection Times (ms)
              min  mean[+/-sd] median   max
 Connect:        0    3   0.5      3       6
 Processing:     1    3   0.5      3       6
 Waiting:        0    3   0.5      3       6
 Total:          4    7   0.9      6      11
 WARNING: The median and mean for the total time are not within a normal deviation
        These results are probably not that reliable.

 Percentage of the requests served within a certain time (ms)
  50%      6
  66%      7
  75%      7
  80%      8
  90%      8
  95%      9
  98%      9
  99%     10
 100%     11 (longest request)

cpu情况

.. image:: https://dawnkeyan.github.io/images/swoole_spu.png

swoole100%都是11毫秒内完成，每秒可服务14571个请求，cpu使用接近100%

php-fpm 都是在1秒以上完成的，每秒可服务75个请求，cpu使用平时是10%左右，压测的时候%17左右
