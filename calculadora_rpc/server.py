from xmlrpc.server import SimpleXMLRPCServer

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    return a / b

server = SimpleXMLRPCServer(('localhost', 9000))
print("Listening on port 9000...")

server.register_function(add_numbers, 'add')
server.register_function(subtract_numbers, 'subtract')
server.register_function(multiply_numbers, 'multiply')
server.register_function(divide_numbers, 'divide')

server.serve_forever()