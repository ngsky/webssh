# coding=utf-8
import logging
import tornado.web
import tornado.ioloop

from tornado.options import options
from webssh import handler
from webssh.handler import IndexHandler, WsockHandler, NotFoundHandler
from webssh.settings import (
    get_app_settings, get_host_keys_settings, get_policy_setting,
    get_ssl_context, get_server_settings, check_encoding_setting
)


""" 构建处理器  """
def make_handlers(loop, options):
    host_keys_settings = get_host_keys_settings(options)
    policy = get_policy_setting(options, host_keys_settings)

    """ / 开头的是 web处理器: IndexHandler """
    """ /ws 开头的是WebSocket处理器: WsockHandler """
    handlers = [
        (r'/', IndexHandler, dict(loop=loop, policy=policy,
                                  host_keys_settings=host_keys_settings)),
        (r'/ws', WsockHandler, dict(loop=loop))
    ]
    return handlers


def make_app(handlers, settings):
    settings.update(default_handler_class=NotFoundHandler)
    """ 创建一个 WEB 应用程序 """
    return tornado.web.Application(handlers, **settings)


def app_listen(app, port, address, server_settings):
    app.listen(port, address, **server_settings)
    if not server_settings.get('ssl_options'):
        server_type = 'http'
    else:
        server_type = 'https'
        handler.redirecting = True if options.redirect else False
    logging.info(
        'Listening on {}:{} ({})'.format(address, port, server_type)
    )


def main():
    """转换命令行参数，并将转换后的值对应的设置到全局options对象相关属性上。"""
    options.parse_command_line()
    """ 检查字符编码 """
    check_encoding_setting(options.encoding)
    ''' 创建IO循环线程,主事件循环  '''
    loop = tornado.ioloop.IOLoop.current()
    ''' 创建一个 APP 应用 '''
    app = make_app(make_handlers(loop, options), get_app_settings(options))
    """ ssl 配置信息 """
    ssl_ctx = get_ssl_context(options)
    """ 服务器配置信息 """
    server_settings = get_server_settings(options)
    """ 配置监听信息 """
    app_listen(app, options.port, options.address, server_settings)
    if ssl_ctx:
        server_settings.update(ssl_options=ssl_ctx)
        """ 更新完ssl 后重新配置监听 """
        app_listen(app, options.sslport, options.ssladdress, server_settings)
    """ 启动IO 循环服务"""
    loop.start()


if __name__ == '__main__':
    main()
