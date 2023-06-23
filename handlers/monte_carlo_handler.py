import random

from functools import partial

from tornado.ioloop import IOLoop
from .tracing_handler import TracedRequestHandler


def monte_carlo_estimate(number_of_points):
    in_circle = 0
    for _ in range(number_of_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            in_circle += 1

    result = 4 * in_circle / number_of_points
    return str(result)


class MonteCarloHandler(TracedRequestHandler):
    def initialize(self, executor) -> None:
        self.executor = executor

    async def get(self):
        input = self.get_argument("query")

        n = int(input)
        result = await self.run_request(n)

        self.render("../html/monte_carlo_pi.html", n=n, result=result)

    async def run_request(self, n):
        result = await IOLoop.current().run_in_executor(
            self.executor, partial(monte_carlo_estimate, n))
        print(result)
        return result
