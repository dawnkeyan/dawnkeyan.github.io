.. title: php实现经典算法
.. slug: phpshi-xian-jing-dian-suan-fa
.. date: 2018-10-26 10:29:53 UTC+08:00
.. tags: php,算法
.. category: php
.. link: 
.. description: 
.. type: text


冒泡:
::

  function bub_sort($array){
        $n = count($array);
              for($i=0; $i<$n; $i++){
                      for($j=$i+1; $j<$n; $j++){
                              if($array[$i]>$array[$j]){
                                      $temp = $array[$i];
                                      $array[$i] = $array[$j];
                                      $array[$j] = $temp;
                              }
                      }
              }
              var_dump($array);
      }
      bub_sort([3,2,1,5,7,3]);

直接插入排序:
::

 function ins_sort($array){
              $len = count($array);
              for($i=1;$i<$len;$i++){
                      $temp = $array[$i];
                      for($j=$i-1;$j>=0;$j--){
                              if($temp<$array[$j]){
                                      $array[$j+1] = $array[$j];
                                      $array[$j] = $temp;
                              }
                              else{
                                      break;
                              }
                      }
              }
              var_dump($array);
      }

      ins_sort([3,1,2,5,7,10,9,8]);

直接选择排序:
::

 function sel_sort($array){
              $len = count($array);
              for($i=0;$i<$len-1;$i++){
                      $p = $i;
                      for($j=$i+1;$j<$len;$j++){
                              if($array[$j]>$array[$p]){
                                      $p = $j;
                              }
                      }
                      $temp = $array[$p];
                      $array[$p] = $array[$i];
                      $array[$i] = $temp;
              }
              var_dump($array);
      }

      sel_sort([2,1,3,4,6,9,5,7,1]);

堆排序:
::

      function swap(&$array,$a,$b){
              $temp = $array[$a];
              $array[$a] = $array[$b];
              $array[$b] = $temp;
      }

      function buildMaxHeap(&$array,$len){
              for($i=intval($len/2)-1;$i>=0;$i--){
                      $l = $i*2 + 1;
                      $max = $l;
                      if($len>$l){
                              $r = $l+1;
                              if($len>$r){
                                      if($array[$r]>$array[$l]){
                                              $max = $r;
                                      }
                              }
                              if($array[$max]>$array[$i]){
                                      swap($array,$max,$i);
                              }
                      }
              }
      }

      $array = [3,2,4,5,7,1,8];
      $len = count($array);
      buildMaxHeap($array, $len);
      for($i=$len-1;$i>0;$i--){
              swap($array,$i,0);
              $len--;
              buildMaxHeap($array,$len);
      }

      var_dump($array);

快速排序:
::

 function quick_sort($array){
               $len = count($array);
               if($len<2){
                       return $array;
               }
               $right = $left = [];
               for($i=1;$i<$len;$i++){
                       if($array[$i]<$array[0]){
                               $left[] = $array[$i];
                       }
                       else{
                               $right[] = $array[$i];
                       }
               }
               $left = quick_sort($left);
               $right = quick_sort($right);
               return array_merge($left,[$array[0]],$right);
       }

       var_dump(quick_sort([2,1,2,3,6,5,7]));

归并排序:
::

  $array = [5,4,3,8,8,1,6];
      function merge_sort(&$array){
              $len = count($array);
              if($len<=1){
                      return $array;
              }
              $middle = intval($len/2);
              $left = array_slice($array,0,$middle);
              $right = array_slice($array,$middle);
              merge_sort($left);
              merge_sort($right);
              $array = merge($right,$left);
      }

      function merge($right,$left){
              $merge = [];
              while(count($right) && count($left)){
                      if($right[0]>$left[0]){
                              $merge[] = array_shift($right);
                      }
                      else{
                              $merge[] = array_shift($left);
                      }
              }
              return array_merge($merge,$right,$left);
      }

      merge_sort($array);
      var_dump($array);

基数排序：把每位数分开，高位不存在的补零。从低位开始比较，比到高位完成排序:
::

   function base_sort(&$arr){//前提是数组都是正整数，且不为空

     $bit = 1;

     $len = count($arr);

     for($i=0; $i<$len; $i++){

        $strlen = strlen($arr[$i]);

        $bit = $strlen>$bit ? $strlen : $bit;

     }

     for($i=0; $i<$bit-1; $i++){

        $base = [];

        $divisor = pow(10,$i);

        for($j=0; $j<$len; $j++){

            $remain = $arr[$j]/$divisor%10;

            $base[$remain][] = $arr[$j];

        }

        $arr = [];

        for($k=0; $k<=9; $k++){

           if(isset($base[$k])){

               $arr = array_merge($arr,$base[$k]);

           }

        }

     }

 }

 $arr = [100,1,125,19999,9,808,28];

 base_sort($arr);

 var_dump($arr);



.. figure:: https://img1.doubanio.com/view/note/l/public/p52272377.jpg



二分查找（时间复杂度log2n）:
::

  function bin_sch($array,$start,$end,$value){
              if($start > $end){
                      var_dump('没有找到');
              }
              $mid =  intval(($start + $end) / 2);
              if($array[$mid] == $value){
                      var_dump($mid);
              }
              elseif($array[$mid] > $value){
                      bin_sch($array,$start,$mid-1,$value);
              }
              else{
                      bin_sch($array,$mid+1,$end,$value);
              }
      }

      bin_sch([1,2,3,4,6,8],0,5,6);

顺序查找:
::

  seq_sch([3,2,5,6,1],5,6);
      function seq_sch($array,$n,$value){
              for($i=0; $i<$n; $i++){
                      if($array[$i] == $value){
                              var_dump($i);exit;
                      }
              }
              var_dump('没有找到');
      }

二维数组排序:
::

  function two_array_sort($array,$key,$sort=SORT_ASC,$sort_type=SORT_NUMERIC){
              if(!is_array($array)){
                      return false;
              }
              $array_key = [];
              foreach($array as $value){
                      if(!is_array($value)){
                              return false;
                      }
                      $array_key[] = $value[$key];
              }
              array_multisort($array_key,$sort,$sort_type,$array);
              var_dump($array);
      }

      two_array_sort([['a'=>8,'b'=>2],['a'=>9,'b'=>2],['a'=>5,'b'=>2],['a'=>8,'b'=>2],['a'=>1,'b'=>2]], 'a');

抢红包:
::

 function qhb($num,$money){
               if($money<$num*0.01){
                       return false;//保证每个人能有一分钱
               }
               for($i=1;$i<=$num;$i++){
                       if($i==$num){
                               $hb = $money;
                       }
                       else{
                               $max = round($money-($num-$i)*0.01, 2);//保证每个人能有一分钱
                               $max = round($max/($num-$i), 2);//让每个红包差距不是太大
                               $hb = mt_rand(0.01*100,$max*100)/100;
                               $money -= $hb;
                       }
                       var_dump([$i,$hb]);
               }
       }

       qhb(5,5);
