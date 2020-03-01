.. title: php有些加法和乘法会变无限循环小数
.. slug: phpyou-xie-jia-fa-he-cheng-fa-hui-bian-wu-xian-xun-huan-xiao-shu
.. date: 2020-02-29 19:31:52 UTC+08:00
.. tags: php_bug
.. category: php
.. link: 
.. description: 
.. type: text


因为系统的二进制在存储某些数据的时候，二进制可能是无限的，所以就导致加减法和乘法会变无限循环小数的问题

::

 //实验在php 7.2下进行
 var_dump(0.58 * 100);//这种情况不会有问题
 var_dump(json_encode(['a' => 0.58 * 100]));

 float(58)
 string(23) "{"a":57.99999999999999}"

解决办法是使用更高精度的函数

::

 var_dump(json_encode(['a' => bcmul(0.58, 100)]));
 string(10) "{"a":"58"}"


bcadd — 将两个高精度数字相加

bccomp — 比较两个高精度数字，返回-1, 0, 1

bcdiv — 将两个高精度数字相除

bcmod — 求高精度数字余数

bcmul — 将两个高精度数字相乘

bcpow — 求高精度数字乘方

bcpowmod — 求高精度数字乘方求模，数论里非常常用

bcscale — 配置默认小数点位数，相当于就是Linux bc中的”scale=”

bcsqrt — 求高精度数字平方根

bcsub — 将两个高精度数字相减
