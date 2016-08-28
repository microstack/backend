import json
import requests


def objects_from_requests(url):
    response = request.get(url)

    if response.status_code != 200:
        '''
        exception required.
        '''
        pass
    
    text = response.text
    objects = json.loads(text)

    return objects


def parse_objects_for_bill_model(objects):
    items = objects['items']
    bill_list = []
    for item in items:
        bill = dict()
        bill['assembly_id'] = item['assembly_id']
        bill['decision_date'] = item['decision_date']
        bill['proposed_date'] = item['proposed_date']
        bill['name'] = item['name']
