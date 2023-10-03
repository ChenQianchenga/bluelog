# -*- coding: utf-8 -*-#
# --------------------------------------------------------------------------
# ProjectName：bluelog
# Name:admin.py
# Description:  博客后台
# Author:ChenQiancheng
# Date:2023/10/3  16:07
# --------------------------------------------------------------------------
from flask import render_template, flash, redirect, url_for, Blueprint

admin_bp = Blueprint('admin', __name__)

