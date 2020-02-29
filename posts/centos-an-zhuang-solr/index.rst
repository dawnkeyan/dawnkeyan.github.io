.. title: centos 安装solr
.. slug: centos-an-zhuang-solr
.. date: 2018-11-05 14:45:40 UTC+08:00
.. tags: solr
.. category: 搜索
.. link: 
.. description: 
.. type: text

1.安装jdk

下载安装包（也可以使用其他下载文件方式），因为认证问题，不能直接wget, 打开此页面 ，在Java SE Development Kit 8u161勾上Accept License Agreement，然后点击jdk-8u161-linux-x64.rpm,在下载页面获取文件下载地址，比如我本次的是http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jdk-8u161-linux-x64.rpm?AuthParam=1519538436_f233fa0ab4a9cba466bec47d360db37a，然后在/down目录下wget此地址。然后再重命名文件
mv jdk-8u161-linux-x64.rpm\?AuthParam\=1519538436_f233fa0ab4a9cba466bec47d360db37a jdk-8u161-linux-x64.rpm

安装
rpm -ivh jdk-8u161-linux-x64.rpm

配置系统环境变量，在/etc/profile里追加

::

 JAVA_HOME=/usr/java/jdk1.8.0_161
 JRE_HOME=$JAVA_HOME/jre
 CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib
 PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH
 export PATH JAVA_HOME CLASSPATH

生效配置，并检验结果

::

 source /etc/profile
 java -version

2.安装solr

安装前检测rng-tools及lsof是否正确安装(安装成功输入命令后显示版本号)

::

 rpm -qa |grep rng-tools
 rpm -qa |grep lsof

若未安装，设备能够联网的情况下，可使用如下命令安装，否则自行下载安装包安装

::

 yum install rng-tools
 yum install lsof

配置rng-tools

::

 echo 'EXTRAOPTIONS="--rng-device /dev/urandom"' >/etc/sysconfig/rngd
 service rngd start
 chkconfig rngd on

在down目录下创建solr,下载solr安装包,下载apache-tomcat安装包（如果找不到页面，则在浏览器打开https://tomcat.apache.org/download-80.cgi查看有的版本号，然后修改版本号），然后使用tar -zxvf命令解压两个文件

::

 #下载solr安装包
 wget http://mirror.bit.edu.cn/apache/lucene/solr/6.6.2/solr-6.6.2.tgz
 #下载apache-tomcat安装包（如果找不到页面，则在浏览器打开https://tomcat.apache.org/download-80.cgi查看有的版>本号，然后修改版本号）
 wget http://mirror.bit.edu.cn/apache/tomcat/tomcat-8/v8.0.50/bin/apache-tomcat-8.0.50.tar.gz

3.配置solr

使用tar -zxvf命令解压刚刚下载的solr安装包和下载apache-tomcat安装包

::

 tar -zxvf solr-6.6.2.tgz
 tar -zxvf apache-tomcat-8.0.50.tar.gz

在solr-6.6.2目录下拷贝dataimporthandler的jar包

::

 cp dist/solr-dataimporthandler-* server/solr-webapp/webapp/WEB-INF/lib/

在/down/solr目录下载mysql-connector-java-5.1.45安装包

::

 wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.45.tar.gz

解压mysql-connector-java-5.1.45.tar.gz

::

 tar -zxvf mysql-connector-java-5.1.45.tar.gz

拷贝mysql-connector-java

::

 cp mysql-connector-java-5.1.45/mysql-connector-java-5.1.45-bin.jar solr-6.6.2/server/solr-webapp/webapp/WEB-INF/lib/

在/down/solr目录下载ikanalyzer安装包

::

 wget https://github.com/zxiaofan/ik-analyzer-solr6/releases/download/6.6.0/ikanalyzer-6.6.0.jar

解压ikanalyzer

::

 jar -xvf ikanalyzer-6.6.0.jar

拷贝ikanalyzer

::

 cp ikanalyzer-6.6.* solr-6.6.2/server/solr-webapp/webapp/WEB-INF/lib/

在/down/solr目录下载pinyin4j

::

 wget https://github.com/zxiaofan/ik-analyzer-solr6/releases/download/6.6.0/pinyin4j_IKconfig.zip

复制文件

::

 unzip pinyin4j_IKconfig.zip -d pinyin4j
 cp pinyin4j/pinyin*.jar solr-6.6.2/server/solr-webapp/webapp/WEB-INF/lib/
 mkdir solr-6.6.2/server/solr-webapp/webapp/WEB-INF/classes
 cp pinyin4j/ext.dic solr-6.6.2/server/solr-webapp/webapp/WEB-INF/classes/
 cp pinyin4j/IKAnalyzer.cfg.xml solr-6.6.2/server/solr-webapp/webapp/WEB-INF/classes/
 cp pinyin4j/stopword.dic solr-6.6.2/server/solr-webapp/webapp/WEB-INF/classes/

修改配置solr-6.6.2/server/solr-webapp/webapp/WEB-INF/classes/IKAnalyzer.cfg.xml加入新的内容

::

 <!--词典动态更新时间间隔[首次延时,时间间隔]（格式：正整数，单位：分钟）-->
 <entry key="dic_updateMin">1,1</entry>

 <!--禁用内置主词典main2012.dic（默认false）-->
 <!--<entry key="dicInner_disable">true</entry> -->

修改时区，修改solr-6.6.2/bin/solr.in.sh中的SOLR_TIMEZONE="UTC+8"

4.创建core并配置

进入solr-6.6.2目录，执行创建名称为goods的core,如果无法确定实例端口，加上-p 端口号，如果在root用户下启动solr存在风险，要么换个账号，要么加上 -force

::

 bin/solr create -c goods -p 8983 -force

修改配置：修改server/solr/goods/conf目录下的solrconfig.xml,data-config.xml,managed-schema的文件，没有就新建

::

 #solrconfig.xml添加内容（在</config>之前）
 <requestHandler name="/dataimport" class="org.apache.solr.handler.dataimport.DataImportHandler">
   <lst name="defaults">
       <str name="config">data-config.xml</str>
   </lst>
 </requestHandler>

 #data-config.xml添加内容
 <?xml version="1.0" encoding="UTF-8"?>
 <dataConfig>
   <dataSource
       name="dbSource"
       type="JdbcDataSource"
       driver="com.mysql.jdbc.Driver"
       url="jdbc:mysql://数据库地址:端口号/数据库名称"
       batchSize="-1"
       user="用户名"
       password="密码"
       readOnly="true"
       autoCommit="true"
       netTimeoutForStreamingResults="0"
       />
   <document>
       <entity name="goods" dataSource="dbSource" onError="skip" pk="id" query="select id,address-detail,create_time from lab_model_address"
           deltaImportQuery="select id,address-detail,create_time from lab_model_address where id = '${dih.delta.id}'"
           deltaQuery="select id,address-detail,create_time from lab_model_address where create_time > unix_timestamp('${dataimporter.last_index_time}')">
           <field column="id" name="id" />
           <field column="address-detail" name="address-detail" />
           <field column="create_time" name="create_time" />
       </entity>
   </document>
 </dataConfig>

 #managed-schema添加内容（在<field name="id" ... />之后）
 <field name="address-detail" type="text_ik" indexed="true" stored="true"/>
   <fieldType name="text_pinyin" class="solr.TextField" positionIncrementGap="0">
       <analyzer type="index">
           <tokenizer class="org.wltea.analyzer.lucene.IKTokenizerFactory"/>
           <filter class="solr.SynonymGraphFilterFactory" synonyms="synonyms.txt" ignoreCase="true" expand="true" />
           <filter class="com.shentong.search.analyzers.PinyinTransformTokenFilterFactory" minTermLenght="2" />
           <filter class="com.shentong.search.analyzers.PinyinNGramTokenFilterFactory" minGram="1" maxGram="20" />
       </analyzer>
       <analyzer type="query">
           <tokenizer class="org.wltea.analyzer.lucene.IKTokenizerFactory"/>
           <filter class="solr.SynonymGraphFilterFactory" synonyms="synonyms.txt" ignoreCase="true" expand="true" />
           <filter class="solr.LowerCaseFilterFactory" />
       </analyzer>
   </fieldType>
   <fieldType name="text_ik" class="solr.TextField">
       <analyzer type="index" useSmart="false" isMaxWordLength="false" >
           <tokenizer class="org.wltea.analyzer.lucene.IKTokenizerFactory"/>
           <filter class="solr.SynonymGraphFilterFactory" synonyms="synonyms.txt" ignoreCase="true" expand="true"/>
       </analyzer>
       <analyzer type="query" useSmart="true" isMaxWordLength="true" >
           <tokenizer class="org.wltea.analyzer.lucene.IKTokenizerFactory"/>
           <filter class="solr.SynonymGraphFilterFactory" synonyms="synonyms.txt" ignoreCase="true" expand="true"/>
       </analyzer>
   </fieldType>
   <field name="title_ik" type="text_ik" indexed="true" required="true" stored="true"/>
   <copyField source="address-detail" dest="title_ik"/>
   <field name="create_time" type="int" indexed="true" stored="true"/>
   <field name="pinyin" type="text_pinyin" indexed="true" stored="true"/>
   <copyField source="address-detail" dest="pinyin"/>

5.启动，停止,重启solr

::

 bin/solr stop -all
 bin/solr start -force
 bin/solr stop -all; bin/solr start -force

6.导入数据

浏览器中访问http://IP:8983/, 查看CoreAdmin中是否存在创建的core:goods
Core Selector选择新建的core（如goods），选择Dataimport，Command选择full-import，Start, Rows选择合理值，点击Excute执行数据导入

7.验证数据是否导入:接上一步中选择Query，直接点击Execute Query查看结果

8.验证分词是否可用:接上一步中选择Analysis，输入值，类型选择text_ik，查看分词结果（需要分词的数据类型在managed-schema中field的type为text_ik类型。

9.添加批处理任务(apache-solr-dataimporthandler-.jar可以在 我的GitHub下载 )

将apache-solr-dataimporthandler-.jar放到solr-6.6.2/server/solr-webapp/webapp/WEB-INF/lib/
在solr-6.6.2/server/solr-webapp/webapp/WEB-INF/web.xml中的</web-app>之前加入下面代码

::

 <listener>
  <listener-class>org.apache.solr.handler.dataimport.scheduler.ApplicationListener</listener-class>
 </listener>

 在solr-6.6.2/server/solr/conf中新建dataimport.properties，文件夹不存在时新建
 #################################################
 #                                               #
 #       dataimport scheduler properties         #
 #                                               #
 #################################################

 #  to sync or not to sync
 #  1 - active; anything else - inactive
 syncEnabled=1

 #  which cores to schedule
 #  in a multi-core environment you can decide which cores you want syncronized
 #  leave empty or comment it out if using single-core deployment
 syncCores=goods,goods-test

 #  solr server name or IP address
 #  [defaults to localhost if empty]
 server=localhost

 #  solr server port
 #  [defaults to 80 if empty]
 port=8983

 #  application name/context
 #  [defaults to current ServletContextListener's context (app) name]
 webapp=solr

 #  URL params [mandatory]
 #  remainder of URL
 #增量
 params=/dataimport?command=delta-import&clean=false&commit=true&optimize=false&wt=json&indent=true&entity=goods&verbose=false&debug=false

 #  schedule interval
 #  number of minutes between two runs
 #  [defaults to 30 if empty]
 interval=20

 #  重做索引的时间间隔，单位分钟，默认7200，即1天;
 #  为空,为0,或者注释掉:表示永不重做索引
 reBuildIndexInterval=7200

 #  重做索引的参数
 reBuildIndexParams=/dataimport?command=full-import&clean=true&commit=true&optimize=true&wt=json&indent=true&entity=goods&verbose=false&debug=false

 #  重做索引时间间隔的计时开始时间，第一次真正执行的时间=reBuildIndexBeginTime+reBuildIndexInterval*60*1000；
 #  两种格式：2012-04-11 03:10:00 或者  03:10:00，后一种会自动补全日期部分为服务启动时的日期
 reBuildIndexBeginTime=09:00:00

10.重启solr
