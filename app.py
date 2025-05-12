from flask import Flask,render_template
import subprocess
import os
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/resources')
def resources():
    return render_template('resource.html')
@app.route('/contact me')
def contact():
    return render_template('contactme.html')
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')
@app.route('/open_python_file')
def open_python_file():
    print("Hello")
    file_path = os.path.abspath('flaskapp', 'main2.py')
    print(f"Current Working Directory: {os.getcwd()}")
    print(file_path)

    try:
        if os.path.exists(file_path):
            print("exists")
            ##  subprocess.Popen(['explorer',open_python_file])
            subprocess.Popen(r'explorer /select,"'+file_path+'"', shell=True)
            print("abc")
            subprocess.call(['python', file_path])
            return 'project opened successfully'
        else:
            return 'index.html'
    except Exception as e:
        return f'error opening project:{e}'

if __name__=='__main__':
    app.run(debug=True, port=5500,use_reloader=False)