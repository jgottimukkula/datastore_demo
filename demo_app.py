#!/usr/bin/env python

import ds_helper
import datetime


class DemoApp():

    def __init__(self):
        self.user_kind = 'User'
        self.catalog_kind = 'Catalog'
        self.checkout_kind = 'Checkout'
        self.ds = ds_helper.DS()

    def create_user_record(self):
        record = dict()
        record['email'] = unicode(raw_input("Enter user email: "))
        record['name'] = unicode(raw_input("Enter user name: "))
        record['address'] = unicode(raw_input("Enter user address: "))

        self.ds.create_default_entity(self.user_kind, record)

    def create_catalog_record(self, record):
        id = int(record.get('id'))
        del record['id']
        self.ds.create_entity_with_id(self.catalog_kind, id, record)

    def create_checkout_record(self):
        record = dict()
        email = raw_input("Enter user email: ")

        record['book_id'] = int(raw_input("Enter book unique id: "))
        num_days = int(raw_input("Enter number of due days: "))
        record['due_date'] = datetime.datetime.now() + datetime.timedelta(days=num_days)
        print record

        self.ds.create_entity_with_ancestor(self.checkout_kind, record, self.user_kind, email)

    def query_kind(self):
        kind = raw_input("Enter the kind to query: ")
        self.ds.query(kind)

    def query_kind_by_ancestor(self):
        email = raw_input("Enter user email: ")
        self.ds.query_by_ancestor(self.checkout_kind, self.user_kind, email)

    def query_kind_by_date(self):
        d = raw_input("Enter due date: ")
        start_date = datetime.datetime.strptime(d, '%Y-%m-%d')
        end_date = start_date + datetime.timedelta(days=1)
        self.ds.query_by_date(self.checkout_kind, start_date, end_date)
