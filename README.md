### tornado-app

A simple tornado based web application to understand the various components that come together

#### Request handler

It has a GET request handler that executes a Monte Carlo simulation to estimate the value of Pi. This is a simple example program with one parameter, number of points "n" that controls how much time it takes to execute - ideal to control the computation time.  

#### Asynchronous

The RequestHandler is a async, to make use to asynchronous functions and handle multiple concurrent requqets. 

#### Multiprocessing

The requests are handled in a ProcessPoolExecutor that runs concurrent requests in different processes, to handle the requets in parallel. 

Python doesn't support multithreading if the bottle-neck is computation, so multiprocessing is suitable for this. 

