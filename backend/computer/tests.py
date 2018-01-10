from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_you():
    return ('Hello World!')

if __name__=='__main__':
    app.run()



def route(self, rule, **options):
    def decorator(f):
        self.add_url_rule(rule, f.__name__, **options)
        self.view_functions[f.__name__] = f
        return f
    return decorator

def add_url_rule(self, rule, endpoint, **options):
    options['endpoint'] = endpoint
    options.setdefault('methods', ('GET',))
    self.url_map.add(Rule(rule, **options))