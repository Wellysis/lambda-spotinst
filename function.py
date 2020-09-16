# Lambda
# Environment variables: AUTH_TOKEN
# memory: 30s
import os
import json
import enum
import time

import requests


AUTH_TOKEN = os.environ['AUTH_TOKEN']
ACCOUNT_ID = 'act-0ca355fb'
URL = "https://api.spotinst.io/aws/ec2/group/{}/statefulInstance/{}/{}?accountId={}"
SERVER_LIST = ['dev', 'stg', 'alg']


class Mode(enum.Enum):
    PAUSE = 0
    RESUME = 1


def get_url(group, instance, state, account):
    if state == Mode.RESUME:
        return URL.format(group, instance, 'resume', account)
    else:
        return URL.format(group, instance, 'pause', account)


def get_header(auth_token):
    return {'Content-Type': 'application/json; charset=utf-8',
           'Authorization': 'Bearer {}'.format(auth_token)}


def get_instances(server):
    with open('./server_list.json') as json_file:
        json_data = json.load(json_file)
    return json_data[server]


def spotinst_handler(event, context):
    if event['server'] not in SERVER_LIST:
        return {'status': 'fail', 'message': 'server name is not available'}, 400
    for item in get_instances(event['server']):
        url = get_url(item['group_id'], item['instance_id'], Mode(event['mode']), ACCOUNT_ID)
        headers = get_header(AUTH_TOKEN)
        response = requests.put(url, headers=headers)
        print(item['name'], response)
        time.sleep(0.5)

    print(response.json())
    return {'status': 'success'}, 200
