# -*- coding: utf-8 -*-#
# --------------------------------------------------------------------------
# ProjectName：bluelog
# Name:blog.py.py
# Description:  博客前台
# Author:ChenQiancheng
# Date:2023/10/3  16:07
# --------------------------------------------------------------------------
from flask import render_template, flash, redirect, url_for, Blueprint, request, current_app
from bluelog.models import Post, Category

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/', defaults={'page': 1})
@blog_bp.route('/page/<int:page>')
def index(page):
    """
    获取所有文章分页展示
    :param page: 页码
    :return: 返回当前页码的所有文章
    """
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['BLUELOG_POST_PER_PAGE'])
    posts = pagination.items
    return render_template('blog/index.html', pagination=pagination, posts=posts)


# @blog_bp.route('/post/<slug>')
# def show_post(slug):
#     post = Post.query.filter_by(slug=slug).first_or_404()
#     return render_template('post.html', post=post)


@blog_bp.route('/about')
def about():
    return render_template('blog/about.html')


@blog_bp.route('/category/<int:category_id>')
def show_category(category_id):
    category = Category.query.get_or_404(category_id)
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['BLUELOG_POST_PER_PAGE']
    pagination = Post.query.with_parent(category).order_by(Post.timestamp.desc()).paginate(page, per_page=per_page)
    posts = pagination.items
    return render_template('blog/category.html', category=category, pagination=pagination, posts=posts)


@blog_bp.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog/post.html', post=post)
