from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        name=request.form['name']
        age=request.form['age']
        ninja=request.form['ninja']
        if not (name =='Name' and age =='Age' and ninja=='Ninja'):
            return render_template('profile.html', name=name, age=age)

        else:
            return render_template('error.html')

if __name__ == '__main__':
    app.run()
