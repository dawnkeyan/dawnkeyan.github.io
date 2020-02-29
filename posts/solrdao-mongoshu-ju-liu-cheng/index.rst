.. title: solr导mongo数据流程
.. slug: solrdao-mongoshu-ju-liu-cheng
.. date: 2018-11-05 15:01:05 UTC+08:00
.. tags: solr
.. category: 搜索
.. link: 
.. description: 
.. type: text

1.进入/home/solr/solr-6.6.2（solr安装路径）创建core，比如创建lab_cloud_periodical bin/solr create -c core名 -p 端口号 -force（root用户需要加）

2.导出mongodb csv 比如导出lab，-f是需要放在solr的且此集合有的字段 mongoexport --username 用户名 --password 密码 --type=csv -f _id,title -d 数据库 -c 集合 -o /home/文件名.csv

3.把数据传到solrcurl http://ip:端口号/solr/core/update?commit=true --data-binary @/home/文件名.csv -H 'Content-type:text/csv; charset=utf-8'

问题： 可能执行着会报错，那是solr会给字段定义类型，但你的某些值有不是那个类型，比如给你定义了int,然后你传的值是字符串。解决办法就是去把int改成string，位置在vim /home/solr/solr-6.6.2/server/solr/lab（写core名）/conf/managed-schema,比如这的tid(有些是默认给你设置了时间，但你传入的不是时间格式)，这是我遇到的问题，有些配置想改都可以改的。然后重新导入数据，还有就是主键可以重新设置，修改<uniqueKey>id</uniqueKey>

4.如果需要删除数据参考：http://blog.csdn.net/lbf5210/article/details/51207043

5.查询，页面参数解释：http://blog.csdn.net/zhufenglonglove/article/details/51518846 浏览器进入http://ip:端口号/solr

6.目前能弄的mongo实时更新是一个core记录整个库，一个集合一个core不知道咋弄。
