ubuntu 1
{
    "taskdb": "mysql+taskdb://root:098f6bcd4621d373cade4e832627b4f6@10.9.138.23:3306/taskdb",
    "projectdb": "mysql+projectdb://root:098f6bcd4621d373cade4e832627b4f6@10.9.138.23:3306/projectdb",
    "resultdb": "mysql+resultdb://root:098f6bcd4621d373cade4e832627b4f6@10.9.138.23:3306/resultdb",
    "message_queue": "redis://127.0.0.1:6379/db",
    "phantomjs-proxy": "127.0.0.1:25555",
    "scheduler" : {
        "xmlrpc-host": "0.0.0.0",
        "delete-time": 3600
    },
    "webui": {
        "username": "thunder",
        "password": "xinghang186//",
        "need-auth": true,
        "port": 5055
     }
 }

# 注意ip地址的一致
centos 1
{
    "taskdb": "mysql+taskdb://pyspider:pyspider-pass@192.168.1.3:3306/taskdb",
    "projectdb": "mysql+projectdb://pyspider:pyspider-pass@192.168.1.3:3306/projectdb",
    "resultdb": "mysql+resultdb://pyspider:pyspider-pass@192.168.1.3:3306/resultdb",
    "message_queue": "redis://192.168.1.3:6379/db",
    "phantomjs-proxy": "127.0.0.1:25555",
    "fetcher": {
        "xmlrpc-host": "192.168.1.3"
    }
}
