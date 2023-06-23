from opentelemetry import trace
from tornado.web import RequestHandler


class TracedRequestHandler(RequestHandler):
    cache = {}

    def prepare(self):
        self._tracer = trace.get_tracer(__name__)
        # sys.stdout.write(f'\n\n{"*"*8}\nRequest stack trace\n{"*"*8}\n')
