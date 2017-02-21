#!/usr/bin/env python

import demo_app

app = demo_app.DemoApp()

raw_input()
print "\n Let's query the kinds....\n"

while(True):
    app.query_kind()
    input = raw_input("\nEnter to continue or - to end: ")
    if input == "-":
        break

