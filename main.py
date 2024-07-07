from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cool_form', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('cool_form.html')
    

app.run(host='0.0.0.0', port=81)

# code from https://stackoverflow.com/questions/27539309/how-do-i-create-a-link-to-another-html-page


#url_for generates urls to routes defined in your application. There are no (or should probably not be any) raw html files being served, especially out of the templates folder. Each template should be something rendered by Jinja. Each location you want to display or post a form to should be handled and generated by a route on your application.

#In this case, you probably want to have one route to both render the form on GET and handle the form submit on POST.