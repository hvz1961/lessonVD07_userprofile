from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

class EditProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Save Changes')

@app.route('/', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        # Здесь можно обработать данные, например, сохранить изменения в базе данных
        name = form.name.data
        email = form.email.data
        password = form.password.data

        # Вывести сообщение об успешном изменении
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('edit_profile'))

    return render_template('edit_profile.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
