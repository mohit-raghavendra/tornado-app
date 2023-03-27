import tornado.ioloop
import tornado.web

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor


from handlers.factorial_handler import FactorialHandler
from handlers.fibonacci_handler import FibonacciHandler
from handlers.start_handler import StartHandler

from utils.span_exporter import PrintSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(SimpleSpanProcessor(PrintSpanExporter()))


def make_app():
    return tornado.web.Application(
        [
            (r"/", StartHandler),
            (r"/factorial", FactorialHandler),
            (r"/fibonacci", FibonacciHandler),
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
