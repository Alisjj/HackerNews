import requests
from .models import Item
import datetime
from django.utils.timezone import make_aware
def fetch_items():
    conn = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty')
    res = sorted(conn.json())
    return list(reversed(res))[:5]


def fetch_item_by_id(item):
    int_item = int(item)
    conn = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{int_item}.json?print=pretty')
    res = conn.json()
    print(res['type'])
    return res

def add_kid(kid):
    comment = fetch_item_by_id(kid)
    parent = Item.objects.get(id=comment['parent'])
    if 'deleted'in comment or 'dead' in comment:
        return
    obj = get_obj(comment)
    Item.objects.create(**obj, parent=parent)
    return obj

def get_obj(detail):
    type = detail.get("type")
    id = detail.get("id")
    by = detail.get("by")
    timestamp = datetime.datetime.fromtimestamp(detail.get("time"))
    time = make_aware(timestamp)
    url = detail.get("url")
    title = detail.get("title")
    text = detail.get("text")
    score = detail.get("score", 0)
    obj = {
        "type": type,
        "id": id,
        "by": by,
        "time": time,
        "url": url,
        "title": title,
        "text": text,
        "score": score
    }
    return obj

def add_to_db():
    items = fetch_items()
    for single in items:
        details = fetch_item_by_id(single)
        if details['type'] != 'comment' or 'deleted' not in details or 'dead' not in details:
            if not Item.objects.filter(id=details['id']).exists():
                item_obj = get_obj(details)
                Item.objects.create(**item_obj)
                if 'kids' in details:
                    kids = details['kids']
                    for kid in kids:
                        add_kid(kid)