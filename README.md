### tornado-app

A simple tornado based web application to understand the various components that come together

#### Request handlers

The two request handlers ```handlers/fibonacci_handler.py``` and ```handlers/factorial_handler.py``` handle two type of requests. 
They handle requests to /fibonacci and /factorial respectively. 

#### Tracing 

The request paths are traced using opentelemetry tracing across different methods that are used to return the response

#### Caching

A rudimentary cache is used to store previously computed results for quick responses. This is a very barebones verison and ideally should have 
a flushing mechanism and TTL.

#### Asynchronous

The FactorialHandler is a async, to make use to asynchronous functions and handle multiple concurrent requqets. 

