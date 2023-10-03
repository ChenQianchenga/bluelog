# -*- coding: utf-8 -*-#
# --------------------------------------------------------------------------
# ProjectName：bluelog
# Name:blog.py.py
# Description:  博客前台
# Author:ChenQiancheng
# Date:2023/10/3  16:07
# --------------------------------------------------------------------------
from flask import render_template, flash, redirect, url_for, Blueprint

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def index():
    return "hello world"
