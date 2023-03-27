from .tracing_handler import TracedRequestHandler


class FactorialHandler(TracedRequestHandler):
    def get(self):
        with self._tracer.start_as_current_span("/factorial entry") as span:
            input = self.get_argument("query")

            n = FactorialHandler.format_input(input)
            result = self.factorial(n)

            span.set_attribute("factorial.output", result)
            self.render("../html/factorial.html", n=n, result=result)

    def factorial(self, n):
        with self._tracer.start_as_current_span("Factorial calculation"):
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

    @staticmethod
    def format_input(n):
        return int(n)
