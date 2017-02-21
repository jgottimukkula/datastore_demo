#!/usr/bin/env python

import demo_app

app = demo_app.DemoApp()

raw_input("\n Let's create couple of users....") 

for i in xrange(2):
    i += 1
    print "\nCreating user", i
    app.create_user_record()

