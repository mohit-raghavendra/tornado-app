### tornado-app

A simple tornado based web application to understand the various components that come together

#### Request handler

It has a GET request handler that executes a Monte Carlo simulation to estimate the value of Pi. This is a simple example program with one parameter, number of points "n" that controls how much time it takes to execute - ideal to control the computation time.  

#### Asynchronous

The RequestHandler is async, to handle multiple concurrent requests. 

#### Multiprocessing

The requests are handled in a ProcessPoolExecutor that runs concurrent requests in different processes
Thus concurrent requests are handled in parallel. 

Python doesn't support multithreading if the bottle-neck is computation, so multiprocessing is suitable for this. 


### How to run

1. Install requirements with ```pip install -r requirements.txt```
2. Run the tornado server with `python3 tornado_app/main.py`
3. Navigate to localhost:8888 or execute `python3 make_requests.py`
