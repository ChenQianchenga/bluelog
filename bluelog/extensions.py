# -*- coding: utf-8 -*-#
# --------------------------------------------------------------------------
# ProjectName：bluelog
# Name:extensions.py
# Description: 存储扩展实例化等操作
# Author:ChenQiancheng
# Date:2023/10/3  16:05
# --------------------------------------------------------------------------
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_ckeditor import CKEditor
from flask_moment import Moment
from flask_login import LoginManager

bootstrap = Bootstrap4()
db = SQLAlchemy()
moment = Moment()
ckeditor = CKEditor()
mail = Mail()
login_manager = LoginManager()

login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'Warning'
login_manager.login_message = u'请先登录！'


@login_manager.user_loader
def load_user(user_id):
    from bluelog.models import Admin
    user = Admin.query.get(int(user_id))
    return user
