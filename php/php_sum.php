PHP学习纪录

代码风格: 考虑兼容性, 使用一般风格<?php   ?>, PHP 中的每个代码行都必须以分号结束

关于php函数:
PHP 的真正威力源自于它的函数
1.在 PHP 中, 提供了超过 1000 个内建的函数
2.自建函数function name () {}

注释: // # 通用

输出函数: echo(), print() 
标准输出函数: printf(), sprintf()
print返回值的: 1 or false
printf返回值的: 字符串长度
sprintf返回值: 为字符串本身

var可写可不写
类中的变量使用var来声明, 变量也可以初始化值
<?php
class phpClass {
  var $var1;
  var $var2 = "constant string";
  function myfunc ($arg1, $arg2) {
     [..]
  }
  [..]
}
?>

PHP的变量必须以$符开始, 然后再加上变量名
关于变量的赋值方式, 传值赋值和引用赋值, 同c++
传值赋值:
$a = 3;
$b = 5;
$b = $a;
引用赋值:
$a=3;
$b=5;
$a=&$b;
题目:
$b=9;
$a=&$b;
unset $b;
echo($a) #9

关于局部和全局变量的作用域和语法:
注意同python的区别
<?php
$x=5; 
function myTest() {
   $y=10;
   echo "<p>在函数内部测试变量: </p>";
   echo "变量 x 是: $x";
   echo "<br>";
   echo "变量 y 是: $y";
}
myTest();  // $x并不能访问到, $y是可以的, python是可以的
echo "<p>在函数之外测试变量: </p>";
echo "变量 x 是: $x"; //不能访问到
echo "<br>";
echo "变量 y 是: $y"; //可以访问到
?>
怎么才能在局部空间访问到全局变量呢? 用global
<?php
$x=5;
$y=10;
function myTest() {
  global $x, $y;
  $y = $x + $y;
}
myTest();
echo $y;
?>

关于静态变量的演示:
定义一个函数来申请一个局部空间, 这个函数内部的普通局部变量每次在函数执行的时候都会刷新, static静态变量会保存
<?php
//普通局部变量
function local() {
    $loc = 0; //如果直接不给初值0是错误的
    ++$loc;
    echo $loc . '<br>';
}
local(); //1
local(); //1
local(); //1
//static静态局部变量
function static_local() {
    static $local = 0 ; //此处可以不赋0值
    $local++;
    echo $local . '<br>';
}
static_local(); //1
static_local(); //2
static_local(); //3
//注意虽然静态变量, 但是它仍然是局部的, 在外不能直接访问的
?>

关于可变变量:
可变变量允许我们动态地改变一个变量的名称, 只需要在变量前边加上$就可以了
$a = 'hello';
$$a = 'world';
echo($a $hello);
一个用法:
<?php
$nameTypes = array("first", "last", "company");
$name_first = "John";
$name_last = "Doe";
$name_company = "PHP.net";
foreach($nameTypes as $type)
 print ${"name_$type"} . "\n";
?>

php的基本的数据类型:
整形, 浮点型, 字符串, 布尔型 
数组, 对象
资源(resourse), 空值, mixed
双引号字符串: 变量用{}括起来, 不同的字符串之间用.相连
php中的数组:  $network = array(1=>”as”,2=>”df”) 
		      $network = array(“a”,”b”,”c”)
php中的对象: 对象就是类的实例, 实例化一个对象用, new
php中的资源: $cn = mysql_connect('local', 'host')
		     $fp = feen(“foo”,”w”)
php中的空值: Null
mixed, 一个可以存放任何类型数据的数据类型
php中的强制类型转化的两种方法

关于变量的几个函数：
判空函数empty($a)
变量检查函数isset($a) 存在返回true
变量销毁函数unset($a)
变量类型获取函数gettype($a)
类型转换函数settype($a, 'float')
变量类型判断函数is_int($a)
var_dump($a)函数, 打印变量的相关信息, 包括变量类型和值, 字符串还会打印长度, dump: 倒垃圾的倒
var_export(), 返回合法的php代码

数组的排序函数：
sort() - 对数组进行升序排列
rsort() - 对数组进行降序排列
asort() - 根据关联数组的值，对数组进行升序排列
ksort() - 根据关联数组的键，对数组进行升序排列
arsort() - 根据关联数组的值，对数组进行降序排列
krsort() - 根据关联数组的键，对数组进行降序排列
eg:
<?php
$cars=array("Volvo", "BMW", "Toyota");
sort($cars);
?>

在 PHP 中, array() 函数用于创建数组
在 PHP 中, 有三种类型的数组
数值数组 - 带有数字 ID 键的数组
关联数组 - 带有指定的键的数组，每个键关联一个值
多维数组 - 包含一个或多个数组的数组
count() 函数用于返回数组的长度（元素的数量）：
遍历关联数组: foreach - 根据数组中每个元素来循环代码块
<?php
$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
foreach($age as $x=>$x_value)
  {
   echo "Key=" . $x . ", Value=" . $x_value;
   echo "<br>";
   }
?>


关于php常量:
自定义php常量: define('CONSTANT” '你好') 注:define(string $name , mixed $value), value是一个mix类型
预定义php常量: 比如PHP_VERSION, PHP_OS
注: 预定义常量广泛存在于各种语言

php的魔术常量
PHP 向它运行的任何脚本提供了大量的预定义常量
不过很多常量都是由不同的扩展库定义的, 只有在加载了这些扩展库时才会出现, 或者动态加载后, 或者在编译安装的时候已经包括进去了
有八个魔术常量它们的值随着它们在代码中的位置改变而改变
1.__LINE__:当前文件中的当前行号
2.__FILE__:当前文件的完整路径和文件名
3.__DIR__:当前文件所在的目录
4.__FUNCTION__:当前所处函数被定义时的名字
5.__CLASS__:当前所处类名
6.__NAMESPACE__:域名空间

PHP中预定义了几个超级全局变量(superglobals), 这意味着它们在一个脚本的全部作用域中都可用. 
你不需要特别说明, 就可以在函数及类中使用
* $GLOBALS: 一个包含了全部变量的全局组合数组, 变量的名字就是数组的键
* $_SERVER: 一个包含了诸如头信息(header), 路径(path), 以及脚本位置(script locations)等等信息的数组, 这个数组中的项目由 Web 服务器创建
* $_REQUEST: 用于收集HTML表单提交的数据。
* $_POST: 被广泛应用于收集表单数据, 在HTML form标签的指定该属性: "method="post"
* $_GET: 同样被广泛应用于收集表单数据, 在HTML form标签的指定该属性: "method="get"
* $_FILES
* $_ENV
* $_COOKIE
* $_SESSION

关于php运算符:
1.算数运算符: +-*/
2.递增递减运算符: ++
3.赋值运算符: +=
4.比较运算符: ==
5.逻辑运算符: and &  or ||
6.位运算符。&|
7.字符串运算符: . 字符串连接符 .=连接赋值运算符
8.数组运算符: + 数组联合运算符
9.错误抑制运算符: 表达式前加@, 可以抑制错误信息的报错
11.三元运算符
12.执行运算符: `dos命令`

在 PHP 中, 只有一个字符串运算符.
并置运算符.用于把两个字符串值连接起来
<?php 
$txt1="Hello world!"; 
$txt2="What a nice day!"; 
echo $txt1 . " " . $txt2; 
?> 

关于_REQUEST:
<html>
<body>
<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
Name: <input type="text" name="fname">
<input type="submit">
</form>
<?php 
$name = $_REQUEST['fname']; 
echo $name; 
?>
</body>
</html>

关于_GET:
<html>
<body>
<a href="test_get.php?subject=PHP&web=runoob.com">Test $GET</a>
</body>
</html>
其中的test_get.php
<html>
<body>
<?php 
echo "Study " . $_GET['subject'] . " at " . $_GET['web'];
?>
</body>
</html>

关于php中的域名空间: PHP 命名空间可以解决以下两类问题:
做项目时 ,一个文件可能会引入多个文件. 如果不使用命名空间, 引入的多个文件中可能存在同名的类, 函数, 常量, 就会报错(重复定义的错误)
问: 如果在一个文件中, 使用不同命名空间下的同名函数呢? 前面加上命名空间即可, 类似于: namespace/func()

php快速排序:
<?php
    seq = array(1, 4, 0, 3, 2)
    function quickSort ($seq) {
        if (count($seq) <= 1) {
            return 
        }
        $left = array()
        $right = array()
        $pivot = $seq[0]
        for ($i=1; $i<count($seq); i++) {
            if ($seq[$i] >= $pivot) {
               $right[] = $seq[$i] 
            }
            else {
               $left[] = $seq[$i] 
            }
        }

        $left = quickSort($left)
        $right = quickSort($right)

        return merge_array($left, array($pivot), $right)
    }
?>


