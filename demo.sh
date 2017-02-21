#!/bin/sh

#set the root path for directory where you will have all these python files
DIR="."

echo "\n Datastore demo app..."
$DIR/demo_users.py
echo
$DIR/demo_catalog.py
echo
$DIR/demo_query_kinds.py
echo
$DIR/demo_checkout.py
echo
$DIR/demo_query_checkout_user.py
echo
$DIR/demo_query_checkout_duedate.py
echo
echo "\n demo complete"
