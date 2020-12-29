from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


# @app.route('/<username>/<int:post_id>')
# def hello_world(username= None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def writetofile(data):
    with open('database.txt',mode='a') as database:
        email= data['email']
        subject= data['subject']
        message= data['message']
        file= database.write(f'\n{email}, {subject}, {message}')

def writetocsv(data):
    with open('database.csv',mode='a', newline='') as database2:
        fieldnames = ['email', 'subject', 'message']
        email= data['email']
        subject= data['subject']
        message= data['message']
        csv_writer= csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data= request.form.to_dict()
            writetofile(data)
            writetocsv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Algo salio mal, intente otra vez'

