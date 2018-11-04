.. title: php处理大文件
.. slug: phpchu-li-da-wen-jian
.. date: 2018-11-04 16:12:59 UTC+08:00
.. tags: php
.. category: php
.. link:
.. description: 
.. type: text

普通的处理文件是要全部吧文件内容读入内存，但是有内存和时间限制，可以修改php.ini,但是还和电脑的内存大小有关系；

::

 <?php
    ini_set('memory_limit', '-1');
    $file = 'access.log';
    $data = file($file);
    $line = $data[count($data) - 1];
    echo $line;
 ?>

还有一个方法就是使用fseek读取，通过指针操作，不用一次性全部读入内存，可以一行一行的读取。

::

 <?php
   $fp = fopen($file, "r");
   $line = 10;
   $pos = -2;
   $t = " ";
   $data = "";
   while ($line > 0)
   {
       while ($t != "\n")
       {
           fseek($fp, $pos, SEEK_END);
           $t = fgetc($fp);
           $pos--;
       }
       $t = " ";
       $data .= fgets($fp);
       $line--;
   }
   fclose($fp);
   echo $data
   ?>

或者一段一段的读取

::

 <?php
   $fp = fopen($file, "r");
   $num = 10;
   $chunk = 4096;
   $fs = sprintf("%u", filesize($file));
   $max = (intval($fs) == PHP_INT_MAX) ? PHP_INT_MAX : filesize($file);
   for ($len = 0; $len < $max; $len += $chunk)
   {
       $seekSize = ($max - $len > $chunk) ? $chunk : $max - $len;
       fseek($fp, ($len + $seekSize) * -1, SEEK_END);
       $readData = fread($fp, $seekSize) . $readData;
       if (substr_count($readData, "\n") >= $num + 1)
       {
           preg_match("!(.*?\n){" . ($num) . "}$!", $readData, $match);
           $data = $match[0];
           break;
       }
   }
   fclose($fp);
   echo $data;
   ?>

平时统计相关文件比如nginx的accesslog,可以使用系统命令awk或者grep或者tail等等，效率是很快的

统计每小时的请求数,top100的时间点(精确到小时)

::

 awk '{print $4}' access.log |cut -c 14-15|sort|uniq -c|sort -nr|head -n 100

统计蜘蛛抓取次数

::

 grep 'Baiduspider' access.log |wc -l

tail

::

 <?php
    $file = 'access.log';
    $file = escapeshellarg($file); // 对命令行参数进行安全转义
    $line = `tail -n 1 $file`;
    echo $line;
 ?>
