#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# an exercise of sqlite database from chapter 21

__author__ = 'victor yu'

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# initial data
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
conn.commit()
cursor.close()
conn.close()

def get_score_in(low, high):

    conn = sqlite3.connect(db_file)
    cursor=conn.cursor()

    #query name from user where score is between low and high,ordered by score
    cursor.execute('SELECT name FROM user WHERE score >= ? AND score <= ? ORDER BY score ASC', (low,high))
    result = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return result
    
    

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')