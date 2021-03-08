from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RegisterAns(FlaskForm):
    ans_desc = TextAreaField('ans_desc',validators=[DataRequired()])
    submit = SubmitField('Create Ans')
    

class RegisterQues(FlaskForm):
    sub_ques_id = StringField('Sub Question Number',validators=[DataRequired()])
    perv_ans_id = StringField('Previos Ans Id',validators=[DataRequired()])
    next_ans_id = StringField('Next Ans Id',validators=[DataRequired()])
    sub_ques_desc = TextAreaField('Question Description',validators=[DataRequired()])
    submit = SubmitField('Create Question')

class AdminLogin(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')