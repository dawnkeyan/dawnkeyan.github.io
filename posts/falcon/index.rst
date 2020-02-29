.. title: 安装python框架falcon
.. slug: falcon
.. date: 2018-11-29 13:50:07 UTC+08:00
.. tags: falcon
.. category: python
.. link: 
.. description: 
.. type: text

docker run  -v $PWD/myapp:/usr/src/myapp  -it --rm -p 8000:8000 -w /usr/src/myapp python:3.5 bash
安装python和pip

$ pip install falcon

$ mkdir look
$ cd look

$touch app.py
import falcon
api = application = falcon.API()

$ pip install gunicorn

$ gunicorn -b 0.0.0.0:8000 app（默认是127.0.0.1:8000，这样的话只有主机可以访问）

$ curl localhost:8000 -v

$ pip install --upgrade httpie

$ http localhoost:8000

pip install msgpack-python

$ http GET localhost:8000/images


