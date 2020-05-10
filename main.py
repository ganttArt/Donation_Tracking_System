import os
import base64
from flask import Flask, render_template, request, redirect, url_for, session
from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def donations():
    donations = Donation.select()
    return render_template('all_donations.jinja2', donations=donations)


@app.route('/donors/', methods=['GET', 'POST'])
def all_donors():
    if request.method == 'POST': 
        donor = Donor.select().where(Donor.name == request.form['donor_name']).get()
        return render_template('donor_info.jinja2', donor=donor)
    else:
        donors = Donor.select()
        return render_template('all_donors.jinja2', donors=donors)


@app.route('/donor')
def donor_info():
    return render_template('donor_info.jinja2')


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

        return redirect(url_for('donations'))

    else:
        return render_template('add_donation.jinja2')


@app.route('/add_donor/', methods=['GET', 'POST'])
def add_donor():
    if request.method == 'POST':
        donor = Donor(name=request.form['name'], email=request.form['email'])

        for _donor in Donor().select():
            if str(_donor.name).lower() == str(donor.name).lower():
                return render_template('add_donation.jinja2')

        donor.save()
        return render_template('add_donation.jinja2')
    else:
        return render_template('add_donor.jinja2')


@app.route('/thank_you/', methods=['GET', 'POST'])
def thank_you():
    if request.method == 'POST':
        donor = Donor.select().where(Donor.name == request.form['name']).get()
        return render_template('personalized_thank_you.jinja2', donor=donor)
    else:
        return render_template('generate_thank_you.jinja2')



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
