#!/usr/bin/env python
# -*- : coding: utf-8 -*-

import os

def __get_env_var(name) :
    try :
        v = os.environ[name]
    except KeyError:
        return ""
    return v

DEFAULT_HOST="localhost"
DEFAULT_PORT="9000"
DEFAULT_USER="docker"
DEFAULT_PASSWORD="d0cker"

def __parse_port_intv(v):
    try:
        rst = int(v)
    except ValueError:
        return int(DEFAULT_PORT)
    return rst

class PgConfig:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

def read():
    host = __get_env_var("POSTGRES_HOSTNAME")
    port = __get_env_var("POSTGRES_PORT")
    user = __get_env_var("POSTGRES_USER")
    password = __get_env_var("POSTGRES_PASSWORD")
    if host == "" :
        host =DEFAULT_HOST
    if port == "" :
        port = DEFAULT_PORT
    if user == "" :
        user = DEFAULT_USER
    if password == "" :
        password = DEFAULT_PASSWORD
    return PgConfig(host, __parse_port_intv(port), user, password)
