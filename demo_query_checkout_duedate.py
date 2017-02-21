#!/usr/bin/env python

import demo_app

app = demo_app.DemoApp()

print "\n Let's query the Checkout kind based on due date....\n"

while(True):
    app.query_kind_by_date()
    input = raw_input("\nEnter to continue or - to end: ")
    if input == "-":
        break

