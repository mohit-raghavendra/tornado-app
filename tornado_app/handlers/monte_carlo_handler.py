import random
import tornado

from concurrent.futures import ProcessPoolExecutor
from functools import partial
from tornado.ioloop import IOLoop


def monte_carlo_estimate(number_of_points: int) -> float:
    in_circle = 0
    for _ in range(number_of_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            in_circle += 1

    result = 4 * in_circle / number_of_points
    return result


class MonteCarloHandler(tornado.web.RequestHandler):
    def initialize(self, executor: ProcessPoolExecutor) -> None:
        self.executor = executor

    async def get(self):
        n = int(self.get_argument("query"))

        result = await self.run_request(n)

        self.render("../html/start.html", n=n, result=result)

    async def run_request(self, n: int) -> float:
        result = await IOLoop.current().run_in_executor(
            self.executor, partial(monte_carlo_estimate, n))
        print(result)
        return result
