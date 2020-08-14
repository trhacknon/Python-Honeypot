#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is to be used to store all the queries which are being used
for querying mongodb using pymongo.

Created this file because the queries are repeated over the URI's.
"""
from bson.son import SON
from api.utility import (fix_date,
                         fix_limit,
                         fix_skip)

sort_by_count = {
    "$sort": SON(
        [
            ("count", -1)
        ]
    )
}


def group_by(element_name, element):
    return {
        "$group":
            {
                "_id": {
                    element_name: element
                },
                "count": {
                    "$sum": 1
                }
            }
    }


group_by_elements = {
    "ip": group_by("ip", "$ip_dest"),
    "country": group_by("country", "$country_ip_dest"),
    "port": group_by("port", "$port_dest"),
    "module_name": group_by("module_name", "$module_name"),
    "username": group_by("username", "$username"),
    "password": group_by("password", "$password"),
    "machine_name": group_by("machine_name", "$machine_name")
}

event_types = [
    "all",
    "honeypot",
    "network",
    "credential",
    "file",
    "data"
]


def filter_by_date(date):
    date = fix_date(date)
    return {
        "date": {
            "$gte": date[0],
            "$lte": date[1]
        }
    }


def filter_by_skip(skip):
    return {
        "$skip": fix_skip(skip)
    }


def filter_by_limit(limit):
    return {
        "$limit": fix_limit(limit)
    }


def filter_by_country_ip_dest(country):
    return {
        "country_ip_dest": country
    }


def filter_by_module_name(module_name):
    return {
        'module_name': module_name
    }


# todo: not used?
def filter_by_exclude_unknown_country():
    return {
        "country_ip_dest": {
            "$gt": "-"
        }
    }


def filter_by_match(match_query):
    return {
        "$match": match_query
    }
