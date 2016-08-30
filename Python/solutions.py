#!/usr/bin/python
import json
import datetime
import dateutil.parser


def reverse_string(text):
    reversed_string = ''.join(reversed(text))

    return {
        "string": reversed_string
    }


def find_in_haystack(text):
    data = json.loads(text)
    haystack = data['haystack']
    needle = data['needle']

    index = haystack.index(needle)

    return {
        "needle": index
    }


def find_all_unprefixed(text):
    data = json.loads(text)
    prefix = data['prefix']
    array = data['array']

    new_array = [i for i in array if i.find(prefix) != 0]

    return {
        "array": new_array
    }


def add_seconds_to_date(text):
    date_and_interval = json.loads(text)
    date = date_and_interval['datestamp']
    interval = date_and_interval['interval']

    # Parse date, add interval, convert back to ISO string
    parsed_date = dateutil.parser.parse(date)
    new_date = parsed_date + datetime.timedelta(0, interval)
    iso_new_date = new_date.isoformat()

    # code2040 doesn't accept +00:00 as tz specification,
    # even though it's ISO 8601 compliant
    iso_new_date = iso_new_date.replace('+00:00', 'Z')

    return {
        "datestamp": iso_new_date
    }
