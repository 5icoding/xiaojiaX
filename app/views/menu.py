from flask import Blueprint, request, render_template, redirect

menu = Blueprint('menu', __name__, url_prefix="/menu")


@menu.route('/')
def menu_index():
    return render_template('menus/index.html')