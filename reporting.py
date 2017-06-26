#!/usr/bin/env python2
# coding: utf-8
#
# A reporting tool for web logs in need of a database.

import psycopg2


class Reporting(object):

    def __init__(self, dbname):
        self.db = psycopg2.connect(database=dbname)
        self.cur = self.db.cursor()

    def close(self):
        try:
            self.cur.close()
            self.db.close()
        except AttributeError:
            print "Reporting instance has no attribute 'db'"

    def view_question1(self):
        query = ("create view path_num as "
                 "select path, count(*) as num "
                 "from (select * from log where path!='/') as temp "
                 "group by path "
                 "order by num desc "
                 "limit 3")
        # print query
        self.cur.execute(query)

    def answer_question1(self):
        query = ("select title, num "
                 "from articles right join path_num "
                 "on path_num.path like CONCAT('%', articles.slug, '%')")
        self.cur.execute(query)

    def view_question2(self):
        query = ("create view log_author as " 
                 "select name, path "
                 "from authors, log, articles "
                 "where authors.id=articles.author " 
                 "and log.path like CONCAT('%', articles.slug, '%')")
        self.cur.execute(query)

    def answer_question2(self):
        query = ("select name, count(*) as num "
                 "from log_author "
                 "group by name "
                 "order by num desc")
        self.cur.execute(query)

    def view_question3(self):
        query = ("create view rate_table as "
                 "select date_requests.date, CAST(date_errors.num as FLOAT) / date_requests.num as error_rate "
                 "from date_requests, date_errors "
                 "where date_requests.date=date_errors.date")
        self.cur.execute(query)

    def answer_question3(self):
        query = ("select date, CAST(error_rate as DECIMAL(4,3)) "
                 "from rate_table where error_rate>0.01")
        self.cur.execute(query)

    def create_view(self):
        self.view_question1()
        self.view_question2()
        self.view_question3()
        self.db.commit()
