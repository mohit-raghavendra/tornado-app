import random

from locust import HttpUser, task


class User(HttpUser):
    def __init__(self, parent):
        super().__init__(parent)

    @task
    def test_factorial_endpoint(self):
        # n = random.randint(1*10**7, 2*10**7)
        n = random.choice(range(1*10**6, 10*10**6, 10**6))
        data = {'query': str(n)}
        self.client.get(url="/pi",
                        data=data)
