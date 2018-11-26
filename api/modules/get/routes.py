import datetime
import json

from flask import Blueprint, request
from bson.objectid import ObjectId

from api import mongo, authenticate, status

get = Blueprint('get', __name__, url_prefix='/get')


@get.route('/all-data', methods=['GET'])
def get_all_data():
    auth, error = authenticate.get(request)
    if error:
        return json.dumps(auth)

    menu = mongo.db.menus
    notif = mongo.db.notifications
    weather = mongo.db.weather

    w = weather.find_one({'_id': 'w-latest'})

    ret_json = {
        'all-food-data': {},
        'valid-notifications': {
            'count': 0,
            'notifications': []
        },
        # 'all-news-data': get_news(),
        # 'all-jobs-data': get_jobs(),
        'weather-data': w['weather-data'],
        'status-code': status['STATUS'],
        'api-version': status['VERSION'],
    }
    data = list(menu.find({}, {'_id': 0}))
    for i in data:
        ret_json['all-food-data'][i['menza']] = {'data': i['data'], 'last-update': i['last-update'],
                                                 'last-update-server': i['last-update-server']}

    nots = list(notif.find({}))
    present = datetime.datetime.now()

    # YYYY  DD MM
    for i in nots:
        nid = str(i['_id'])
        date = i['data']['date']
        date = [int(i) for i in date.split('-')]
        dte = datetime.datetime(date[0], date[1], date[2], hour=23, minute=59)
        if dte > present:
            notification = i['data']
            notification['added-on'] = i['added-on']
            ret_json['valid-notifications']['notifications'].append(notification)
            ret_json['valid-notifications']['count'] += 1
        else:
            notif.remove({'_id': ObjectId(nid)})

    return json.dumps(ret_json)


@get.route('/users', methods=['GET'])
def get_users():
    auth, error = authenticate.get(request)
    if error:
        return json.dumps(auth)
    user = mongo.db.users
    data = list(user.find({}, {'_id': 0}))
    return_data = {'users': data, 'count': len(data)}
    return json.dumps(return_data)
