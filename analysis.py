#!/usr/bin/env python2
# coding: utf-8

from reporting import Reporting

DBNAME = 'news'

analyst = Reporting(DBNAME)
analyst.answer_question1()
result1 = analyst.cur.fetchall()
print 'Finish Question 1'
analyst.answer_question2()
result2 = analyst.cur.fetchall()
print 'Finish Question 2'
analyst.answer_question3()
result3 = analyst.cur.fetchall()
print 'Finish Question 3'
analyst.close()

with open('result.txt', 'w') as a_file:
    a_file.write('The page views for 3 most popular articles\n\n')
    for row in result1:
        a_file.write(row[0] + ': ' + str(row[1]) + '\n')
    a_file.write('\nThe page views for most popular authors\n\n')
    for row in result2:
        a_file.write(row[0] + ': ' + str(row[1]) + '\n')
    a_file.write('\nThe days on which the error rate is more than 1%\n\n')
    for row in result3:
        a_file.write(str(row[0])[0:10] + ': ' + str(row[1]) + '\n')
