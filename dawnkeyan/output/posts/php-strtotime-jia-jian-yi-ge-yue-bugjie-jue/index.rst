.. title: PHP strtotime 加减一个月bug解决
.. slug: php-strtotime-jia-jian-yi-ge-yue-bugjie-jue
.. date: 2020-02-29 16:34:55 UTC+08:00
.. tags: php bug
.. category: php
.. link: 
.. description: 
.. type: text

strtotime('-1 month',strtotime('2011-3-31'));
当31好的时候减一个月的时候，就是前一个月的31号，但是有些月份没有31号，就会往后下一个月移，就乱了

old日期可以减一个月或者加一个月的第一天，然后再把old的日期的天拼到新日期，在和新日期的最后一天比较，如果小于拼接的，就取最后一天，否则就取拼接的


::


 if (!function_exists('calculate_month')) {
    /**
     * 对月进行加减
     * @param int $date 时间戳
     * @param string $algorithm 比如 +1 month 或者-1 month
     * @return string
     */
    function calculate_month(int $date, string $algorithm): string
    {
        $day = date('d', $date);
        $newDateFirst = date('Y-m', strtotime('first day of ' . $algorithm, $date));
        $newDate = $newDateFirst . '-' . $day;
        $newDateLast = date('Y-m-d', strtotime('last day of ' . $algorithm, $date));
        return $newDateLast < $newDate ? $newDateLast : $newDate;

    }
 }


::

 var_dump(calculate_month(strtotime('2020-05-31'),'-3 month'));
 var_dump(calculate_month(strtotime('2020-08-31'),'+1 month'));
 var_dump(calculate_month(strtotime('2020-08-15'),'+1 month'));

 string(10) "2017-02-28"
 string(10) "2017-09-30"
 string(10) "2017-09-15"