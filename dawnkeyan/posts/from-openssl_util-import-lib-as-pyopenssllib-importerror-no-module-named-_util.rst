.. title: from OpenSSL._util import lib as pyOpenSSLlib ImportError: No module named _util
.. slug: from-openssl_util-import-lib-as-pyopenssllib-importerror-no-module-named-_util
.. date: 2018-10-25 09:45:33 UTC+08:00
.. tags: python,scrapy,爬虫
.. category: python
.. link: 
.. description: 
.. type: text

* mac 报错   from OpenSSL._util import lib as pyOpenSSLlib ImportError: No module named _util
* 该安装的都安装了，估计是版本的问题
* 因为系统python默认是2.7，所以安装3，而且默认改成3
* 然后重新安装 pip 和scrapy
* 还是不行  默认还是使用2.7
* 用百度  bing 谷歌搜索的方法 试了 还是不行
* 最后  删掉所有python  然后安装python3 重新安装pip和scrapy
* 然后可以了

scrapy爬豆瓣图书例子：https://github.com/dawnkeyan/dawnkeyan.github.io.git
