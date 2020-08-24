from app import app
from flask import render_template, flash, redirect
from app.forms import CompoundIntrestForm
from app.dpEngine import DPEngine
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/compoundintrest', methods=['GET', 'POST'])
def compoundintrest():
    form = CompoundIntrestForm()
    print(str(form.validate_on_submit()))
    engine = DPEngine()
    print(engine.calculateCompIntBalance(1,1,1,1,1,1))

    if form.validate_on_submit():
        flash('The number {} has been submitted'.format(form.initialInvestment.data))
        return redirect('/index')
    return render_template('compoundintrest.html', form=form)
