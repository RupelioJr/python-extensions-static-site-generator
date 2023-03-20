_callbacks = {}

def register():
    
    def register_callback(func):
        return func
    return register_callback