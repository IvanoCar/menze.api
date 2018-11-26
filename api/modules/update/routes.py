from flask import Blueprint, request
from api import mongo, authenticate
import json
import datetime

update = Blueprint('update', __name__, url_prefix='/update')


@update.route('/kampus', methods=['POST'])
def update_kampus():
    try:
        post_data = json.loads(request.get_data(as_text=True))
    except json.JSONDecodeError:
        return json.dumps({'message': 'Error in JSON.'})

    auth, error = authenticate.post(post_data)
    if error:
        return json.dumps(auth)

    try:
        data = post_data['data']
    except KeyError:
        return json.dumps({'message': 'Invalid JSON sent.'})

    menu = mongo.db.menus
    timest = int((datetime.datetime.utcnow() + datetime.timedelta(hours=4)).timestamp())

    # menu.update_one({'menza': 'Kampus'}, {'$set': {'data': data, 'last-update-server': timest}})

    menu.remove({'menza': 'Kampus'})
    menu.insert(
        {'menza': 'Kampus', 'data': data, 'last-update-server': timest, 'last-update': post_data['update-time']})

    return json.dumps({'message': 'OK'})


@update.route('/index', methods=['POST'])
def update_index():
    try:
        post_data = json.loads(request.get_data(as_text=True))
    except json.JSONDecodeError:
        return json.dumps({'message': 'Error in JSON.'})

    auth, error = authenticate.post(post_data)
    if error:
        return json.dumps(auth)

    try:
        data = post_data['data']
    except KeyError:
        return json.dumps({'message': 'Invalid JSON sent.'})

    menu = mongo.db.menus
    timest = int((datetime.datetime.utcnow() + datetime.timedelta(hours=4)).timestamp())
    menu.remove({'menza': 'Index'})
    menu.insert({'menza': 'Index', 'data': data, 'last-update-server': timest, 'last-update': post_data['update-time']})

    # menu.update_one({'menza': 'Index'}, {'$set': {'data': data, 'last-update-server': timest}})

    return json.dumps({'message': 'OK'})


@update.route('/igk', methods=['POST'])
def update_IGK():
    try:
        post_data = json.loads(request.get_data(as_text=True))
    except json.JSONDecodeError:
        return json.dumps({'message': 'Error in JSON.'})

    auth, error = authenticate.post(post_data)
    if error:
        return json.dumps(auth)

    try:
        data = post_data['data']
    except KeyError:
        return json.dumps({'message': 'Invalid JSON sent.'})

    menu = mongo.db.menus
    timest = int((datetime.datetime.utcnow() + datetime.timedelta(hours=4)).timestamp())
    menu.remove({'menza': 'IGK'})
    menu.insert({'menza': 'IGK', 'data': data, 'last-update-server': timest, 'last-update': post_data['update-time']})

    # menu.update_one({'menza': 'IGK'}, {'$set': {'data': data, 'last-update-server': timest}})

    return json.dumps({'message': 'OK'})
