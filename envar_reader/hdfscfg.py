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
DEFAULT_DATA_ROOT="hdfs:///data"

def __parse_port_intv(v):
    try:
        rst = int(v)
    except ValueError:
        return int(DEFAULT_PORT)
    return rst


class HConfig:
    def __init__(self, host, port, data_root):
        self.host = host
        self.port = port
        self.data_root = data_root

def read():
    host = __get_env_var("HADOOP_HOST")
    port = __get_env_var("HADOOP_PORT")
    data_root = __get_env_var("HADOOP_DATA_ROOT")
    if host == "" :
        host =DEFAULT_HOST
    if port == "" :
        port = DEFAULT_PORT
    if data_root == "" :
        data_root = DEFAULT_DATA_ROOT
    return HConfig(host, __parse_port_intv(port), data_root)
