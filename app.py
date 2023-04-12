app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
   return "hello world \n"

if __name__ == '__main__':
   app.run(host = '0.0.0.0', port = 8080)
