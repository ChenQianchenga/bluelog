# -*- coding: utf-8 -*-#
# --------------------------------------------------------------------------
# ProjectName：bluelog
# Name:__init__.py.py
# Description:
# Author:ChenQiancheng
# Date:2023/10/3  16:32
# --------------------------------------------------------------------------
import os
import click
from flask import Flask, render_template
from bluelog.blueprints import blog, admin, auth
from bluelog.blueprints.admin import admin_bp
from bluelog.blueprints.auth import auth_bp
from bluelog.blueprints.blog import blog_bp
from bluelog.extensions import bootstrap, db, ckeditor, mail, moment
from bluelog.models import Admin, Category
from bluelog.settings import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask('bluelog')
    # 引入配置
    app.config.from_object(config[config_name])
    # 注册日志处理器
    register_logging(app)
    # 注册扩展（扩展初始化）
    register_extension(app)
    # 注册蓝本
    register_blueprints(app)
    # 注册自定义shell命令
    register_commands(app)
    # 注册错误处理函数
    register_errors(app)
    # 注册shell上下文处理函数
    register_shell_context(app)
    # 注册模板上下文处理函数
    register_template_context(app)
    return app


def register_logging(app):
    pass


def register_extension(app):
    bootstrap.init_app(app)
    db.init_app(app)
    ckeditor.init_app(app)
    mail.init_app(app)
    moment.init_app(app)


def register_blueprints(app):
    app.register_blueprint(blog_bp)
    app.register_blueprint(auth_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/auth')


def register_template_context(app):
    pass


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'), 400


def register_commands(app):
    @app.cli.command()
    @click.option('--category', default=10, help='Quantity of categories, default is 10.')
    @click.option('--post', default=50, help='Quantity of posts, default is 50.')
    @click.option('--comment', default=500, help='Quantity of comments, default is 500.')
    def forge(category, post, comment):
        """Generates the fake categories, posts, and comments."""
        from bluelog.fakes import fake_admin, fake_categories, fake_posts, fake_comments

        db.drop_all()
        db.create_all()

        click.echo('Generating the administrator...')
        fake_admin()

        click.echo('Generating %d categories...' % category)
        fake_categories(category)

        click.echo('Generating %d posts...' % post)
        fake_posts(post)
        click.echo('Generating %d comments...' % comment)
        fake_comments(comment)

        click.echo('Done.')


def register_shell_context(app):
    pass
