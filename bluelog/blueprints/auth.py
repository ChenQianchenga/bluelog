# -*- coding: utf-8 -*-#
# --------------------------------------------------------------------------
# ProjectName：bluelog
# Name:auth.py.py
# Description: 用户认证
# Author:ChenQiancheng
# Date:2023/10/3  16:06
# --------------------------------------------------------------------------
from flask import render_template, flash, redirect, url_for, Blueprint

auth_bp = Blueprint('auth', __name__)