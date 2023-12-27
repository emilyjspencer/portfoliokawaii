from flask import Flask, render_template, url_for, request, redirect
import os
import csv

app = Flask(__name__) 
print(__name__) 


@app.route("/")
def my_home():
    return render_template('index.html')


#@app.route("/about.html")
#def about():
    #return render_template('about.html')

#@app.route("/portfolio.html")
#def portfolio():
   # return render_template('portfolio.html')


#@app.route("/contact.html")
#def contact():
    #return render_template('contact.html')

#@app.route("/thankyou.html")
#def thankyou():
    #return render_template('thanks.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect('thanks.html')
        except:
            return 'did not save to the database'
    else:
        return 'something went wrong. try again'

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["subject"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv',newline='', mode='a') as database2:
        email = data["subject"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])