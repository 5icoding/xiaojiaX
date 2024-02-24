from flask import Blueprint, request, render_template, redirect

pert = Blueprint('pert', __name__, url_prefix="/pert")


@pert.route('/')
def pert_index():
    return render_template('pert/pert.html')