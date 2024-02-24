# -*- coding:utf-8 -*-
import subprocess
import tempfile
import time
from flask import Blueprint, request, render_template, redirect, json
from app.models import TmpCourse
from app.extensions import db
import os
import random
import datetime

game = Blueprint('course', __name__,url_prefix='/game')

@game.route('/',methods=("GET", "POST"))
def game_parent():
    if request.method == "POST":
        return redirect('/game')

    return render_template('game/parent.html')


@game.route('/child',methods=("GET", "POST"))
def game_child():
    if request.method == "POST":
        return redirect('/game/child')

    return render_template('game/child.html')