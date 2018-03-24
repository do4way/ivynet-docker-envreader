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
DEFAULT_PORT="5432"
DEFAULT_USER="docker"
DEFAULT_PASSWORD="d0cker"
DEFAULT_SSLMODE="disable"

def __parse_port_intv(v):
    try:
        rst = int(v)
    except ValueError:
        return int(DEFAULT_PORT)
    return rst

class PgConfig:
    def __init__(self, host, port, user, password, sslmode):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.sslmode = sslmode

def read():
    host = __get_env_var("POSTGRES_HOSTNAME")
    port = __get_env_var("POSTGRES_PORT")
    user = __get_env_var("POSTGRES_USER")
    password = __get_env_var("POSTGRES_PASSWORD")
    sslmode = __get_env_var("POSTGRES_SSLMODE")
    if host == "" :
        host =DEFAULT_HOST
    if port == "" :
        port = DEFAULT_PORT
    if user == "" :
        user = DEFAULT_USER
    if password == "" :
        password = DEFAULT_PASSWORD
    if sslmode == "" :
        sslmode = DEFAULT_SSLMODE
    return PgConfig(host, __parse_port_intv(port), user, password, sslmode)
