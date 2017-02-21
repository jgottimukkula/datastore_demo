#!/usr/bin/env python

import demo_app

app = demo_app.DemoApp()

raw_input("\n Let's query the Checkout kind based on user....\n")

while(True):
    app.query_kind_by_ancestor()
    input = raw_input("\nEnter to continue or - to end: ")
    if input == "-":
        break

