import SOAPpy
def hello(name):
    hi="Hello "+name
    return hi
def bye(name):
    bye="Bye "+name
    return bye
server = SOAPpy.SOAPServer(("localhost", 8080))
server.registerFunction(hello)
server.registerFunction(bye)
print("corriendo")
server.serve_forever()
