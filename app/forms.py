from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired
from wtforms import TextField, TextAreaField 



class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired('A description is required!')])
    photo = FileField('Photo', validators=[
    FileRequired(),FileAllowed(['jpg', 'png','jpeg','gif', 'Images only!'])
    ])
    