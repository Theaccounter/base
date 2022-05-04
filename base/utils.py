"""Utils"""

import pytz
from django.conf import settings

ALLOWED_IMAGE_EXTENSIONS = ["jpg", "jpeg", "png"]
ALLOWED_DOC_EXTENSIONS = ["pdf", 'xls', 'xlsx', 'xlsm', 'doc', 'docx']
MAX_ATTACHMENT_FILE_SIZE = 10


def from_utc(moment, tz=None):
    if not tz:
        tz = settings.TIME_ZONE or 'Asia/Dubai'
    utc_moment = moment.replace(tzinfo=pytz.utc)
    return utc_moment.astimezone(pytz.timezone(tz))


def mapped(fun, iter):
    return list(map(fun, iter))
