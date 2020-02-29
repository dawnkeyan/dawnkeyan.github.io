.. title: ssl
.. slug: ssl
.. date: 2018-11-04 20:48:32 UTC+08:00
.. tags: ssl
.. category: http
.. link: 
.. description: 
.. type: text

http传输是明文的，可以拦截进行修改等等的操作，及其不安全。ssl对http进行包裹，让别人不容易拦截偷窥，组合成https

在进行数据传输前，进行相关的验证生成相应的密钥，验证后面的相互请求是否可靠。

密钥使用的算法有对称加密和非对称加密，对称加密更快，非对称加密更复杂且更慢

https因为在http上做了一层ssl操作，所以要慢一点。
