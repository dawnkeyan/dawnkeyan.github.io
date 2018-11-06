.. title: php把数据转成csv传到solr
.. slug: phpba-shu-ju-zhuan-cheng-csvchuan-dao-solr
.. date: 2018-11-05 15:10:03 UTC+08:00
.. tags: php,solr,搜索
.. category: 搜索
.. link: 
.. description: 
.. type: text


::

 $field = ['Peter','Griffin','Oslo','Norway','id'];
 $data = [
                   ['Peter'=>43,'Griffin'=>4,'Oslo'=>32,'Norway'=>23,'id'=>1],//主键值必须有，比如这id等于1
                   ['Peter'=>43,'Griffin'=>5,'Oslo'=>32,'Norway'=>23,'id'=>12],
                   ['Peter'=>43,'Oslo'=>32,'Norway'=>23,'id'=>51],
                   ['Peter'=>43,'Griffin'=>6,'Oslo'=>32,'Norway'=>23,'id'=>31],
               ];
 $core = 'test_update';
 $csv_result = [$field];

       //处理数据，给不存在的值赋空值，不然CSV行列不对应
       foreach ($field as $files_value){
           foreach ($data as $data_key=>$data_value){
               $csv_result[$data_key+1][$files_value] = $data_value[$files_value];
           }
       }


       $file_name = time().$core.rand().'.csv';

       $file = fopen($file_name,"w") or exit("Unable to open file!");;

       foreach ($csv_result as $line)
       {
           $line = implode(',',$line);
           fputcsv($file,split(',',$line));
       }
       fclose($file);

       //获取当前的路径
       exec('pwd',$address);

       //上传到solr
       exec('curl http://127.0.0.1:8984/solr/'.$core.'/update?commit=true --data-binary @'.$address[0].'/'.$file_name.' -H \'Content-type:text/csv; charset=utf-8\'',$result);
       //删除生成的文件
       unlink($file_name);
       $result = implode('',$result);

       //上传成功
       if(strpos($result,'<int name="status">0</int>')){
           return ['status'=>true];
       }
       else{//上传失败
           //存日志到mongo
           $MongoModel = new MongoModel('集合', '', 'DB_MONGO');
           $MongoModel->add(['core'=>$core,'msg'=>$result,'field'=>$field,'data'=>$data]);
           return ['status'=>false,'msg'=>$result];
       }在这里书写你的文章。
