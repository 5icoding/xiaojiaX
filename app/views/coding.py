from flask import Blueprint, request, render_template, redirect

coding = Blueprint('coding', __name__, url_prefix="/coding")

@coding.route('/', methods=['GET', 'POST'])
def read_dev():
    return render_template('coding/index.html')

@coding.route('/sequence', methods=['GET', 'POST'])
def dev_sequence():
    if request.method == 'POST':
        return "post"
    return  render_template('coding/sequence_diagram.html')