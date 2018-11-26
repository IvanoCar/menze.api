from flask import Blueprint, request
from api import mongo, authenticate
import json
import datetime
from api.modules.utils.notifier import Notify
from api.modules.utils.utility import Utils

port = Blueprint('port', __name__, url_prefix='/port')


@port.route('/weather', methods=['POST'])
def weather():
    try:
        data = json.loads(request.get_data(as_text=True))
    except json.JSONDecodeError:
        return json.dumps({'message': 'Error in JSON.'})

    auth, error = authenticate.weather_post(data)
    if error:
        return json.dumps(auth)

    w = mongo.db.weather
    w.update_one({'_id': 'w-latest'}, {'$set': {'weather-data': data['weather-data']}})
    return json.dumps({'message': 'OK'})


@port.route('/alert', methods=['POST'])
def alert():
    try:
        post_data = json.loads(request.get_data(as_text=True))
    except json.JSONDecodeError:
        return json.dumps({'message': 'Error in JSON.'})

    auth, error = authenticate.notification_post(post_data)
    if error:
        return json.dumps(auth)

    try:
        data = post_data['data']
    except KeyError:
        return json.dumps({'message': 'Invalid JSON sent.'})

    if not '-' in data['date']:
        return json.dumps({'message': 'Invalid date sent.'})

    notif = mongo.db.notifications
    time_added = int((datetime.datetime.utcnow() + datetime.timedelta(hours=2)).timestamp())
    notif.insert({'data': data, 'added-on': Utils.epoch_time_to_human(time_added)})
    Notify.notify(data['title'], data['body'])
    return json.dumps({'message': 'OK'})
