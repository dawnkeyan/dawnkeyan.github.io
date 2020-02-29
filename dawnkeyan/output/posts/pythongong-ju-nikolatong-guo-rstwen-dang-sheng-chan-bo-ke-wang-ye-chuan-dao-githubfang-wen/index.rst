.. title: python工具nikola通过rst文档生产博客网页传到github访问
.. slug: pythongong-ju-nikolatong-guo-rstwen-dang-sheng-chan-bo-ke-wang-ye-chuan-dao-githubfang-wen
.. date: 2020-02-29 09:44:05 UTC+08:00
.. tags: 博客
.. category: python
.. link: 
.. description: 
.. type: text

由于mac会有python版本乱套问题，所以直接在python3 docker里安装部署

安装nikola
 pip install "git+https://github.com/getnikola/nikola#egg=Nikola[extras]"

包
 git clone https://github.com/getnikola/nikola

cd nikola

pip install -e ".[extras]"

初始化项目
 nikola init --demo <directory_name>.

生成文章
 nikola new_post -e.

然后编辑文章

构建
 nikola build

启动服务浏览器访问
 nikola serve --browser

可以根据喜好编辑conf.py

然后在github建个项目 git名称.github.io

clone到本地把Nikola项目拷在这 执行nikola build的目录的父目录，再把output里的全部目录拷到git项目的根目录
