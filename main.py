from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    id_a = StringField('Id астронавта', validators=[DataRequired()])
    password_a = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_k = StringField('Id капитана', validators=[DataRequired()])
    password_k = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login_main.html', title='Аварийный доступ', form=form)


@app.route('/success')
def success():
    return render_template('success.html', title='Успешно')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
