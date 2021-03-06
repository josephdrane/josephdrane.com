from flask import Flask, render_template, request, redirect, jsonify, url_for, flash

work_history = [
    {
        "jobtitle" : "Edge & Network Services, Network Engineer",
        "company" : "Facebook",
        "description" : "",
        "duration" : "July 2018 - Present"
    },
    {
        "jobtitle" : "Site Reliability Engineering, Systems Architect",
        "company" : "Alkami Technology",
        "description" : "",
        "duration" : "Sep 2017 - May 2018"
    },
    {
        "jobtitle" : "Site Reliability Engineer",
        "company" : "Alkami Technology",
        "description" : "",
        "duration" : "Jan 2017 - Sep 2017"
    },
    {
        "jobtitle" : "Manager, Information Technology",
        "company" : "Alkami Technology",
        "description" : "",
        "duration" : "Jan 2013 - Dec 2016"
    },
    {
        "jobtitle" : "Manager, ETG Client Network Engineering and Implementations",
        "company" : "Fiserv",
        "description" : "",
        "duration" : "Oct 2012 - Jan 2013"
    },
    {
        "jobtitle" : "ETG Network Engineer",
        "company" : "Fiserv",
        "description" : "",
        "duration" : "Oct 2011 - Oct 2012"
    },
    {
        "jobtitle" : "Network Engineer",
        "company" : "MedFusion",
        "description" : "",
        "duration" : "Oct 2009 - Oct 2011"
    }
]


# FLASK WEB APP OBJECT
app = Flask(__name__)


# DEFAULT ROUTE
@app.route('/')
def homePage():
    return render_template('home.html', work_history=work_history)

@app.route('/privacypolicy')
def privacyPolicy():
    return render_template('privacypolicy.html')

if __name__ == '__main__':
    # THIS IS USED FOR DEVELOPMENT ONLY, PROD USES GUNICORN
    import os
    app.secret_key = 'super_secret_key'
    app.debug = True
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
