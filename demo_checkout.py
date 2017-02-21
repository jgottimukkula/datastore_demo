#!/usr/bin/env python
import demo_app


app = demo_app.DemoApp()

raw_input()
raw_input("\n Let's checkout some books....")

for i in xrange(5):
    i += 1
    print "\nChecking out book", i
    app.create_checkout_record()
