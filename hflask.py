from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Sup!'

@app.route('/admin')
def admin():
    return 'Super Secret Admin Page'

@app.route('/about')
def about():
       user = {'username': 'Valdis'} 
       return '''
            <html>
                <head>
                    <title>Home Page - Microblog</title>
                </head>
                <body>
                    <h1>Hello, ''' + user['username'] + '''!</h1>
                </body>
            </html>'''

@app.route('/hello/')
@app.route('/hello/<name>')
def bighello(name=None):
    return render_template('hello.html', name=name)            

if __name__ == '__main__':
    app.run()