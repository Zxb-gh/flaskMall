from flask_wtf import FlaskForm
from wtforms import StringField


class LoginForm(FlaskForm):
    """用户登录"""
    username = StringField(label='用户名')