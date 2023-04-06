import time

from .tracing_handler import TracedRequestHandler


class FibonacciHandler(TracedRequestHandler):
    def get(self):
        with self._tracer.start_as_current_span("/factorial entry"):
            input = self.get_argument("query")
            n = FibonacciHandler.format_input(input)
            result = ", ".join(map(str, self.fibonacci(n)))

            self.render("../html/fibonacci.html", n=n, result=result)

    def post(self):
        with self._tracer.start_as_current_span("/factorial post request"):
            input = self.get_argument("query", "No data provided")
            n = FibonacciHandler.format_input(input)
            result = ", ".join(map(str, self.fibonacci(n)))

            self.write(str(result))

    def fibonacci(self, n):
        with self._tracer.start_as_current_span("Factorial calculation"):
            if n in self.cache:
                result = self.cache[n]
            else:
                time.sleep(2)
                result = [0, 1]
                for i in range(2, n):
                    result.append(result[i - 1] + result[i - 2])

                self.cache[n] = result

            return result

    @staticmethod
    def format_input(n):
        return int(n)
