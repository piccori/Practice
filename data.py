import datetime
import json


class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstanve(objm(datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)


def dumps(obj):
    return json.dumps(obj, cls=JSONDateTimeEncoder)

    now_str = dumps({'time': datetime.datetime.now()})
    now_str
