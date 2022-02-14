from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField
from wtforms.widgets import PasswordInput


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Название блюда", validators=[DataRequired()])
    subtitle = StringField("Описание одним предложением так, чтобы захотелось попробовать", validators=[DataRequired()])
    img_url = StringField("Ссылка на фото-подложку. Картинка должна передавать вкус!", validators=[DataRequired(), URL()])
    body = CKEditorField("Рецепт", validators=[DataRequired()])
    submit = SubmitField("Сохранить")


class UserRegisterForm(FlaskForm):
    name = StringField("Имя или кулинарный псевдоним", validators=[DataRequired()])
    password = StringField('Пароль', widget=PasswordInput(hide_value=False))
    email = StringField("Email", validators=[DataRequired(), Email()])
    # about = CKEditorField("Short story about you")
    submit = SubmitField("Регистрация")


class UserLoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField('Пароль', widget=PasswordInput(hide_value=False))
    submit = SubmitField("Войти")

class AddComment(FlaskForm):
    comment = CKEditorField("Ваш комментарий", validators=[DataRequired()])
    submit = SubmitField("Опубликовать")