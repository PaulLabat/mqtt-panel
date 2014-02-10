#!/usr/bin/env python
# 
# test-messages.py - This script publish a random MQTT messages every 2 s.
#
# Copyright (c) 2013, Fabian Affolter <fabian@affolter-engineering.ch>
# Released under the MIT license. See LICENSE file for details.
#
import random
import time
import mosquitto

timestamp = int(time.time())

broker = '127.0.0.1'
port = 1883
element = 'sensors'
areas = ['front4', 'back5', 'basement3', 'living2', 'DHT221', 'mq47', 'geiger6']
entrances = ['door', 'window']
states = ['true', 'false']

print 'Messages are published on topic %s/#... -> CTRL + C to shutdown' \
    % element

while True:
    area = random.choice(areas)
    if (area in ['basement3', 'living2', 'DHT221']):
        topic = element + '/' + area + '/temp'
        message = random.randrange(0, 30, 1)
    elif area == 'mq47':
        topic = element + '/' + area + '/ppm'
        message = random.randrange(0, 1000, 1)
    elif area == "geiger6":
        topic = element + '/' + area + '/bq'
        message = random.randrange(0,100,1)
    else:
        topic = element + '/' + area + '/' + random.choice(entrances)
        message = random.choice(states)

    client = mosquitto.Mosquitto("mqtt-panel-test")
    client.connect(broker)
    client.publish(topic, message)
    time.sleep(2)
