# This shows an error - it
# complains that greeting is static.
# However, removing greeting just changes the error.

class Greeter:
    greeting = ""
    def __init__(self, message):
        self.greeting = message
    def greet(self):
        return "Hello, " + self.greeting

greeter = Greeter("world")

def on_forever():
    pass
basic.forever(on_forever)
