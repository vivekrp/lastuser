#! /usr/bin/env python

from time import sleep
from retask.exceptions import ConnectionError
from requests import post
from lastuserapp import queue
from lastuserapp.models import User, AuthToken


def send(username, notification_uri, message_type):
    """Send Notification to client application
    """
    post(notification_uri,
        data={'message': "%s has updated %s" % (username, message_type)})

try:
    queue.connect()
    while True:
        while queue.length != 0:
            task = queue.dequeue()
            user = User.query.filter_by(userid=task.data['userid']).first()
            auth_tokens = AuthToken.query.filter_by(user=user).all()
            for auth_token in auth_tokens:
                client = auth_token.client
                if client.notification_uri:
                    if task.data['type'] == 'team':
                        if client.team_access:
                            send(user.username, client.notification_uri, task.data['type'])
                    else:
                        send(user.username, client.notification_uri, task.data['type'])
        sleep(1)
except ConnectionError, e:
    print e
