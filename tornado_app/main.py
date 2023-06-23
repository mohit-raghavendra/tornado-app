import tornado.ioloop
import tornado.web

from concurrent.futures import ProcessPoolExecutor

from handlers.monte_carlo_handler import MonteCarloHandler
from handlers.start_handler import StartHandler

num_workers = 3
executor = ProcessPoolExecutor(num_workers)

def make_app():
    return tornado.web.Application(
        [
            (r"/", StartHandler),
            (r"/pi", MonteCarloHandler, dict(executor=executor))
        ],
        debug=True,
        autoreload=True,
    )


if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    print(f"Server is listening on port {port}")

    tornado.ioloop.IOLoop.current().start()
