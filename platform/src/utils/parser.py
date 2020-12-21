from hashlib import md5
import datetime

def generate_id():
    return md5((str(datetime.datetime.now())).encode('utf-8')).hexdigest()