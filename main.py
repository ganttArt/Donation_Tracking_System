import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def donations():
    donations = Donation.select()
    return render_template('all_donations.jinja2', donations=donations)

@app.route('/add_donation', methods=['GET', 'POST'])
def add_donation():
    if request.method == 'POST':
        
        temp_list = []

        for donor in Donor().select():
            temp_list.append(donor.name)

        if request.form['name'] not in temp_list:
            donor = Donor(name=request.form['name'])
            donor.save()

        donation = Donation(value=request.form['amount'],
                            donor=Donor.select().where(Donor.name == request.form['name']).get())
        donation.save() 

        return redirect(url_for('all'))

    else:
        return render_template('add_donation.jinja2')

@app.route('/donors/')
def all_donors():
    return render_template('all_donors.jinja2')

@app.route('/thank_you/')
def thank_you():
    return render_template('thank_you.jinja2')

@app.route('/add_donor/')
def add_donor():
    return render_template('add_donor.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
