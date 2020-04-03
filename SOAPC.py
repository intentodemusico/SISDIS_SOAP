import SOAPpy
server = SOAPpy.SOAPProxy("http://localhost:8080/")
name=raw_input("name: ")
print server.hello(name)
print server.bye(name)
