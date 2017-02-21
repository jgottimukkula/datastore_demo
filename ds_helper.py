#!/usr/bin/env python

from gcloud import datastore


class DS():

    def __init__(self):
        self.client = datastore.Client("<YOUR PROJECT ID>")

    def create_default_entity(self, kind, record):
        key = self.client.key(kind)
        self.create_entity(key, record)

    def create_entity_with_id(self, kind, id, record):
        key = self.client.key(kind, id)
        self.create_entity(key, record)

    def create_entity_with_ancestor(self, kind, record, ancestor_kind, ancestor_id):
        ancestor_key = self.client.key(ancestor_kind, ancestor_id)
        key = self.client.key(kind, parent=ancestor_key)
        self.create_entity(key, record)

    def create_entity(self, key, record):
        entity = datastore.Entity(key)
        entity.update(record)
        self.client.put(entity)

    def query(self, kind):
        q = self.client.query(kind=kind)
        records = list(q.fetch())
        self.print_query_results(records)

    def query_by_ancestor(self, kind, ancestor_kind, ancestor_id):
        ancestor_key = self.client.key(ancestor_kind, ancestor_id)
        q = self.client.query(kind=kind, ancestor=ancestor_key)
        records = list(q.fetch())
        self.print_query_results(records)

    def get_entity(self, kind, id):
        key = self.client.key(kind, id)
        return self.client.get(key)

    def update_entity(self, record):
        self.client.put(record)

    def create_bulk_regular_entities(self, kind, num_records, record):
        count = 0
        for i in xrange(num_records):
            count += 1
            self.create_default_entity(kind, record)
            print "Record created:", count,
            self.query_bulk_regular_entities(kind)

    def query_bulk_regular_entities(self, kind):
        q = self.client.query(kind=kind)
        record = list(q.fetch())
        print "Record fetched:", len(record)

    def create_ancestor_entity(self, kind, properties, ancestor):
        key = self.client.key(kind, parent=ancestor)
        entity = datastore.Entity(key)
        entity.update(properties)
        self.client.put(entity)

    def create_bulk_ancestor_entities(self, kind, num_records, record, ancestor_kind, ancestor_id):
        ancestor_key = self.client.key(ancestor_kind, ancestor_id)
        print ancestor_key
        count = 0
        for i in xrange(num_records):
            count += 1
            self.create_ancestor_entity(kind, record, ancestor_key)
            print "Record created:", count,
            self.query_bulk_ancestor_entities(kind, ancestor_key)

    def query_bulk_ancestor_entities(self, kind, ancestor):
        q = self.client.query(kind=kind, ancestor=ancestor)
        record = list(q.fetch())
        print "Record fetched:", len(record)

    def create_bulk_entities(self, kind, num_records, record):
        entities = list()
        for i in xrange(num_records):
            entity = datastore.Entity(self.client.key(kind))
            entity.update(record)
            entities.append(entity)
        self.client.put_multi(entities)

    def query_by_date(self, kind, start_date, end_date):
        q = self.client.query(kind=kind)
        q.add_filter('due_date', '>=', start_date)
        q.add_filter('due_date', '<', end_date)
        records = list(q.fetch())
        self.print_query_results(records)

    def print_query_results(self, records):
        print "Query results: "
        if len(records) == 0:
            print "No results from query"
        else:
            for record in records:
                print record
