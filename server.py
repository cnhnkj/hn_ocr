import tornado.web
import tornado.httpserver
import tornado.ioloop

from settings import config


def make_app():
    from handler import ocr_handler
    import tornado.options

    tornado.options.options.logging = config.logging_settings['log_level']

    tornado.options.options.log_file_prefix = config.logging_settings['log_path']
    tornado.options.options.log_rotate_mode = config.logging_settings['log_rotate_mode']
    tornado.options.options.log_rotate_when = config.logging_settings['log_rotate_when']
    tornado.options.options.log_rotate_interval = config.logging_settings['log_rotate_interval']

    tornado.options.parse_command_line()

    return tornado.web.Application([
        (r"/api/ocr", ocr_handler.OcrRun)
    ])


def main():
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)

    port = config.tornado_settings['port']
    server.bind(port)

    server.start(1)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
