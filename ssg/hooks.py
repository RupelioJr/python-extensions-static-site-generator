_callbacks = {}

def register(hook):
    def register_callback(func):
        return func
    return register_callback