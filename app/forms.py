from random import choice
from wsgiref.validate import validator
from xml.dom import VALIDATION_ERR
from xmlrpc.client import Boolean

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, BooleanField, SelectField
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from .models.user import User


class RegistrationForm(FlaskForm):
    name = StringField('ФИО', validators=[DataRequired(), Length(min=2, max=100)])
    login = StringField('Логин', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите Пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')
    avatar = FileField('Загрузите фото', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])

    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError(f"Имя пользователя {login.data} занято. Пожалуйста, выберите другое.")

class LoginForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить Меня')
    submit = SubmitField('Войти')

class TeacherForm(FlaskForm):
    teacher = SelectField('teacher', choice=[], render_kw={'class':'form-control'})

class Upload_file(FlaskForm):
    pass