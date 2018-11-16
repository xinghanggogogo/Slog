# 关于tornado的异步调用:
# 首先必须理解, 同步和异步的概念都是针对单进程的, 也是是针对某一次特定的访问本身, 跟其他访问无关.

# 1.一个简单的同步阻塞的函数, 用的是tornado同步的客户端:
from tornado.httpclient import HTTPClient
class MainHanlder(tornado.web.RequestHandler):
    def get(self):
        url = 'some_api'
        http_client = HTTPClient()
        response = http_client.fetch(url) # 发生阻塞, 必须等待.
        print('以上调用完成后才会打印这条语句.')
        self.write(response)

# 2.同样的函数, 用异步http客户端和回调函数重写的例子:
from tornado.httpclient import AsyncHTTPClient
class MainHanlder(tornado.web.RequestHandler):
    def get(self):
        url = 'some_api'
        http_client = AsyncHTTPClient()
        response = http_client.fetch(url, call_back = self.async_callback) # 异步操作, 无需等待, 继续往下执行. response是一个Future, 即占位符, 异步中使用回调可以不用处理Future, 否则就要参考下面的写法.
        print('不用等待以上调用完成就会打印这条语句.')

    def async_callback(response):
        self.write(response)

# 3.不写回调, 直接干掉Future实现异步的例子:
from tornado.httpclient import AsyncHTTPClient
from tornado.concurrent import Future
class MainHanlder(tornado.web.RequestHandler):
    def get(self):
        url = 'some_api'
        my_future = Future()
        http_client = AsyncHTTPClient()
        response = http_client.fetch(url) # 异步操作, 无需等待, response是一个future.
        print('不用等待以上调用完成就会打印这条语句.')
        response.add_done_callback(
            lambda f: my_future.set_result(f.result()))
        self.write(my_future)

# 4.彻底的避免回调不简洁的写法, 就用gen.croutin这个装饰器:
# 在tornado3发布之后, 强化了coroutine的概念, 在异步编程中, 替代了原来的gen.engine,
# 变成现在的gen.coroutine, 这个装饰器与异步本身没有关系, 异步的具体操作是tornado的AsyncHTTPClinet的实现的, 本质是IOloop()
# 它为了简化在tornado中的异步编程, 避免写回调函数.
# 在 gen.coroutin装饰器中, 调用get, 因为包含yield, 返回值是一个生成器(generator). 需要通过调用 next 或 send 来执行.
from tornado.httpclient import AsyncHTTPClient
class MainHanlder(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        url = 'some_api'
        http_client = AsyncHTTPClient()
        res = yield http_client.fetch(url)
        res = json.loads(res.body.decode())
        return res

# 对于python2而言, 生成器不能return, 所以只能采取这种写法:
from tornado.httpclient import AsyncHTTPClient
from tornado import gen
class MainHanlder(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        url = 'some_api'
        http_client = AsyncHTTPClient()
        res = yield http_client.fetch(url)
        res = json.loads(res.body.decode())
        raise gen.Return(response.body)

# 而对于python3而言, 提供了async和await的异步写法, 更加简洁:
from tornado.httpclient import AsyncHTTPClient
class MainHanlder(tornado.web.RequestHandler):
    async def get(self):
        url = 'some_api'
        http_client = AsyncHTTPClient()
        res = await http_client.fetch(url)
        res = json.loads(res.body.decode())
        return res
