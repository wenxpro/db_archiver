#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import config
import sys
import time
import logging

if __name__ == '__main__':
    # 设置归档时间
    start = time.strftime('%Y-%m-%d %H:%M:%S')
    # 设置日志
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG,format=LOG_FORMAT,filename='log.log')
    logging.info("归档开始："+start)

    server_source = config.MysqlConfig.host
    port_source = config.MysqlConfig.port
    user_source = config.MysqlConfig.username
    password_source = config.MysqlConfig.password
    db_source = config.MysqlConfig.schema
    table_source = config.MysqlConfig.table
    bak_source = config.MysqlConfig.bakTable
    archive_condition = config.MysqlConfig.condition

    # pt-archive 命令
    archive_cmd = "pt-archiver "\
                  "--source h='%s',P='%s',u='%s',p='%s',D='%s',t='%s' "\
                  "--dest h='%s',P='%s',u='%s',p='%s',D='%s',t='%s' "\
                  "--charset=UTF8 --where \"%s\" --progress 50000 --limit 10000 --txn-size 10000 "\
                  "--bulk-insert --bulk-delete --statistics --no-check-charset --purge" % \
                  (server_source, port_source, user_source, password_source, db_source, table_source,
                   server_source, port_source, user_source, password_source, db_source, bak_source,
                   archive_condition)
    # 获取系统输出
    stdout_archive = sys.stdout
    log_file = open('/home/python_script/db_archive_%s_%s.log' % (db_source, table_source), "w")
    # redirect print output to log file
    sys.stdout = log_file
    # archive_cmd = os.popen(pt_archive)
    with os.popen(archive_cmd) as c:
        # with open("db_archive1.log", "r") as c:
        archive_log = c.read()
        print(archive_cmd)
        print(archive_log)

    # close log file
    log_file.close()
    # restore the output to initial pattern
    sys.stdout = stdout_archive

    # 归档结束时间
    end = time.strftime('%Y-%m-%d %H:%M:%S')
    print("执行完成")
    logging.info("归档结束："+end)

