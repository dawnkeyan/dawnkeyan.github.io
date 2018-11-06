.. title: solr删除数据
.. slug: solrshan-chu-shu-ju
.. date: 2018-11-05 15:03:22 UTC+08:00
.. tags: solr,搜索
.. category: 搜索
.. link: 
.. description: 
.. type: text

方法一 在solr页面选择对应的core，然后点击Document然后Document Type选择XML,然后在Document(s)框内填)


::

 <delete><query>*:*</query></delete> #*:*可以改成其他条件
 <commit/>

方法二 post 请求http://ip:端口/solr/core/update?wt=json，<query>id:1</query>里的条件可以修改，post参数

::

 <add commitWithin="1000" overwrite="true">
   <delete>
       <query>id:1</query>
   </delete>
   <commit></commit>
 </add>
