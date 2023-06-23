from .tracing_handler import TracedRequestHandler


class StartHandler(TracedRequestHandler):
    def get(self):
        self.render("../html/start.html")
