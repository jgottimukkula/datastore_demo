#!/usr/bin/env python

import demo_app


app = demo_app.DemoApp()
raw_input()
raw_input("\n Let's create few books for our catelog....")

records = {
    1 : ["The Fountainhead", "Ayn Rand"],
    2 : ["Great Expectations", "Charles Dickens"],
    3 : ["Kane and Abel", "Jeffrey Archer"],
    4 : ["The Alchemist", "Paulo Coelho"],
    5 : ["The Jungle Book", "Rudyard Kipling"]
}

for i in xrange(5):
    i += 1
    print "\nCreating book", i, 
    r = records.get(i)
    record = { 'id': i, 'name': unicode(r[0]), 'author': unicode(r[1])}
    raw_input(record)
    app.create_catalog_record(record)
