from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def hello_world():

 orang = {'nama': 'albardani', 'umur':'21thn'}

 return ''' render_template('index.html', title='beranda', orang=orang)

<html>

    <head>

        <title>Beranda - Flask Blog</title>

    </head>

    <body>

        <h1>Hello, ''' + orang['nama'] + ''' Umur Anda, ''' + orang['umur'] + '''!</h1>

    </body>

</html>'''