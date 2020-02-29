.. title: rand和mt_rand
.. slug: randhe-mt_rand
.. date: 2018-11-04 15:18:52 UTC+08:00
.. tags: 随机
.. category: php
.. link: 
.. description: 
.. type: text

rand默认使用libc生成器，具有一些不确定和未知的弹性而慢；而mt_rand使用Mersener Twister算法生成随机数，速度比rand快4倍。
