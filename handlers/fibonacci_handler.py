from .tracing_handler import TracedRequestHandler


class FibonacciHandler(TracedRequestHandler):
    def get(self):
        with self._tracer.start_as_current_span("/factorial entry"):
            input = self.get_argument("query")
            n = FibonacciHandler.format_input(input)
            result = ", ".join(map(str, self.fibonacci(n)))

            self.render("../html/fibonacci.html", n=n, result=result)

    def fibonacci(self, n):
        with self._tracer.start_as_current_span("Factorial calculation"):
            fib = [0, 1]
            for i in range(2, n):
                fib.append(fib[i - 1] + fib[i - 2])

            return fib

    @staticmethod
    def format_input(n):
        return int(n)
