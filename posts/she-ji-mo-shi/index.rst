.. title: 设计模式
.. slug: she-ji-mo-shi
.. date: 2018-10-30 09:13:45 UTC+08:00
.. tags: php,设计模式
.. category:设计模式
.. link: 
.. description: 
.. type: text

===================
创建型
===================
* 简单工厂模式

优点：
        操作者不用管具体实例化哪个对象，工厂类通过参数去决定实例化对象；降低耦合
缺点：
        编译期间就定好了有哪些类，如果有新需求，需要修改工厂类


.. figure:: https://img3.doubanio.com/view/note/l/public/p55239996.jpg
   :alt: uml图



::

 <?php
 /**
 * Created by PhpStorm.
 * User: wky
 * Date: 2018/10/30
 * Time: 10:16
 */
 namespace Simple\Factory;

 /**
 * Class ArchitectureFactory 工厂类
 * @package Simple\Factory
 */
 class ArchitectureFactory{

    protected $typeList;

    public function __construct()
    {
        //需要实例化的对象的数组
        $this->typeList = [
            'officeBuilding'=>__NAMESPACE__.'\OfficeBuilding',//造写字楼
            'school'=>__NAMESPACE__.'\School',//造学校
        ];
    }

    public function getExample($type){
        if(!isset($this->typeList[$type])){
            //todo 提示类不存在
        }
        return new $this->typeList[$type]();
    }
 }

ArchitectureInterFace

::

 <?php
 /**
 * Created by PhpStorm.
 * User: wky
 * Date: 2018/10/30
 * Time: 10:16
 */
 namespace Simple\Factory;

 /**
 * Interface ArchitectureInterFace 造写字楼和学校需要的设计图
 * @package Simple\Factory
 */
 interface ArchitectureInterFace{

    public function designChart();
 }

OfficeBuilding

::

 <?php
 /**
 * Created by PhpStorm.
 * User: wky
 * Date: 2018/10/30
 * Time: 10:16
 */
 namespace Simple\Factory;

 /**
 * Class OfficeBuilding 造写字楼
 * @package Simple\Factory
 */
 class OfficeBuilding implements ArchitectureInterFace{

    public function designChart(){
        return '造写字楼的图纸';
    }
 }

School

::

 <?php
 /**
 * Created by PhpStorm.
 * User: wky
 * Date: 2018/10/30
 * Time: 10:22
 */
 namespace Simple\Factory;

 /**
 * Class School 造学校
 * @package Simple\Factory
 */
 class School implements ArchitectureInterFace{

    public function designChart(){
        return '造学校的图纸';
    }
 }

Test

::

 <?php
 /**
 * Created by PhpStorm.
 * User: wky
 * Date: 2018/10/30
 * Time: 10:24
 */
 namespace Simple\Factory;

 /**
 * Class Test
 * @package Simple\Factory
 */
 class Test{

    public function test(){
        $architecture = ['officeBuilding', 'school'];
        $factory = new ArchitectureFactory();
        foreach ($architecture as $type){
            $factory->getExample($type);
        }
    }
 }


* 工厂方法模式

和简单工厂方法模式的区别是工厂方法实例化在子类

* 抽象工厂模式

和工厂方法模式的区别是抽象工厂一个产品一个实现类，有新需求不用改原来的代码

* 静态工厂模式

和简单工厂的区别是静态工厂是在工厂类中的静态方法实例化对象

* 建造者模式

和抽象工厂的区别就是，建造者模式构建对象由导演类构建，而抽象工厂由工厂类构造；建造者模式更适用于复杂的对象的构建

* 多例模式

需要多个对象，比如各种数据库的链接

* 单例模式

保证整个生命周期只有一个实例对象。比如一种数据库链接、锁定文件等等

* 对象池模式

对象用完归还对象池类，而不是销毁，适用于实例化代价比较大的前景，因为对象放着也是需要消耗内存的

* 原型模式

通过类的克隆方法创建对象，而不是new,但是类的克隆方法是私有的就无法克隆了；使用场景是需要的类不是最初的类，而是运行中某一种状态下的类


===================
结构型
===================
* 适配器模式
* 桥梁模式
* 组合模式
* 数据映射模式
* 装饰模式
* 依赖注入模式
* 门面模式
* 流接口模式
* 代理模式
* 注册模式

===================
行为型
===================
* 责任链模式
* 命令行模式
* 迭代器模式
* 中介者模式
* 备忘录模式
* 空对象模式
* 观察者模式
* 规格模式
* 状态模式
* 策略模式
* 模板方法模式
* 访问者模式

===================
其他
===================
* 委托模式
* 服务定位模式
* 资源模式


参考地址：https://laravelacademy.org/post/2465.html
