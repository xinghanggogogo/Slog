# 类成员可以分为三类:
# 1. 字段: 静态字段, 普通字段
# 2. 属性: 普通属性
# 3. 方法: 静态方法, 类方法, 普通方法
# 所有成员中, 只有普通字段的内容保存对象中, 即: 根据此类创建了多少对象，在内存中就有多少个普通字段。
# 而其他的成员，则都是保存在类中，即：无论对象的多少，在内存中只创建一份

# 关于字段:
class Province():
    # 静态字段
    country = 'china'
    def __init__(self, name):
        # 普通字段, 保存在对象中
        self.name = name

obj = Province('beijing')
print Province.country
print obj.country
print obj.name

# 关于方法(全部存储在类中):
# 普通方法: 由对象调用, 至少一个self参数, 执行普通方法时, 自动将调用该方法的对象赋值给self
# 类方法: 由类调用, 至少一个cls参数, 执行类方法时, 自动将调用该方法的类复制给cls
# 静态方法: 由类调用, 无默认参数
class Foo:
    def __init__(self, name):
        self.name = name
    # 普通方法
    def ord_func(self):
        print self.name
    # 类方法
    @classmethod
    def class_func(cls):
        print '类方法'
    # 静态方法
    @staticmethod
    def static_func():
        print '静态方法'

# 调用普通方法
f = Foo('xinghang')
f.ord_func()
# 调用类方法
Foo.class_func()
f.class_func()
# 调用静态方法
Foo.static_func()
f.static_func()

# 关于属性:
# Python中的属性其实是普通方法的变种
# 属性存在意义是: 访问属性时可以制造出和访问字段完全相同的假象
# 1.属性的基本使用
class Foo:
    def func(self):
        pass
    # 定义属性
    @property
    def prop(self):
        return 'some_prop'

f = Foo()
f.func()
f.prop
# 2.属性的基本定义方法
