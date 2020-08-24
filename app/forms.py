from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class CompoundIntrestForm(FlaskForm):
    initialInvestment = IntegerField('Initial Investment', validators=[DataRequired()]) 
    #addition = StringField('Monthly Addition', validators=[DataRequired()])
    #intrestRate = StringField('Intrest Rate', validators=[DataRequired()])
    #yearsToGrow = StringField('Years to Grow', validators=[DataRequired()])
    submit = SubmitField('Calculate')