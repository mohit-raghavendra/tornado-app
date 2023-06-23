import time

import tornado.ioloop
import tornado.web

from concurrent.futures import ProcessPoolExecutor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

from handlers.monte_carlo_handler import MonteCarloHandler
from handlers.start_handler import StartHandler
from utils.span_exporter import PrintSpanExporter

resource = Resource(attributes={
    SERVICE_NAME: "your-service-name"
})

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

num_workers = 3
executor = ProcessPoolExecutor(num_workers)


# def no_op():
#     time.sleep(5) 


# futures = [executor.submit(no_op) for _ in range(num_workers)]
# for future in futures:
#     future.submit()


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
