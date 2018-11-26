import json
from flask import Blueprint, request, render_template
from api import authenticate

show = Blueprint('show', __name__, url_prefix='/show')


@show.route('/kampus-map', methods=['GET'])
def show_kampus_map():
    auth, error = authenticate.get(request)
    if error:
        return json.dumps(auth)
    return render_template('kampus-map.html')
