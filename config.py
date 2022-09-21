#!/usr/bin/python
# -*- coding: UTF-8 -*-

class MysqlConfig:
    host = ""
    port = 3306
    username = "root"
    password = ""
    schema = "db-create"
    table = "db_test"
    bakTable = "db-bak"
    condition = "date < '2022-04-01'"