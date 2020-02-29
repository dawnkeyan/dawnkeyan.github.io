.. title: mac安装impyla thriftpy失败
.. slug: macan-zhuang-impyla-thriftpyshi-bai
.. date: 2018-11-29 18:45:28 UTC+08:00
.. tags: 大数据
.. category: python
.. link: 
.. description: 
.. type: text

Command "/usr/local/opt/python/bin/python3.7 -u -c "import setuptools, tokenize;__file__='/private/tmp/pip-install-ocg0pik5/thriftpy/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /private/tmp/pip-record-2agxxtar/install-record.txt --single-version-externally-managed --compile" failed with error code 1 in /private/tmp/pip-install-ocg0pik5/thriftpy/

mac python Failed building wheel for thriftpy


解决办法：pip3 install cython thriftpy