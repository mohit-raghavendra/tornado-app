import time

from .tracing_handler import TracedRequestHandler


class FactorialHandler(TracedRequestHandler):
    def get(self):
        with self._tracer.start_as_current_span("/factorial get call") as span:
            input = self.get_argument("query")

            n = FactorialHandler.format_input(input)
            result = self.factorial(n)

            span.set_attribute("factorial.output", result)
            self.render("../html/factorial.html", n=n, result=result)

    def post(self):
        with self._tracer.start_as_current_span("/factorial post call") as span:
            input = self.get_argument("query", "no data received")

            n = yield FactorialHandler.format_input(input)
            result = yield self.factorial(n)

            span.set_attribute("factorial.output", result)
            self.write(str(result)) 

    async def factorial(self, n):
        with self._tracer.start_as_current_span("Factorial calculation"):
            if n in self.cache:
                result = self.cache[n]
            else:
                result = 1
                for i in range(1, n + 1):
                    result *= i

                self.cache[n] = result
            return result

    @staticmethod
    async def format_input(n):
        return int(n)
