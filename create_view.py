#!/usr/bin/env python2
# coding: utf-8

from reporting import Reporting

DBNAME = 'news'

analyst = Reporting(DBNAME)
analyst.create_view()
analyst.close()
