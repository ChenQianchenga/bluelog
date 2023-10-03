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

bootstrap = Bootstrap4()
db = SQLAlchemy()
moment = Moment()
ckeditor = CKEditor()
mail = Mail()
