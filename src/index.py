#!/usr/bin/python3

import bottle
import pymongo
import dao

@bottle.route('/')
def guestbook_index():
  return bottle.template('index',
                         { 'entries': guestbook.find_entries() })
                         
@bottle.route('/new', method='POST')
def insert_newguest():
  guestbook.insert_entry(bottle.request.params.get('name'),
                         bottle.request.params.get('email'))
  bottle.redirect('/')

@bottle.route('/delete', method='GET')
def delete():
  guestbook.delete_entry(bottle.request.params.get('id'))
  bottle.redirect('/')

@bottle.route('/editform')
def edit_form():
  return bottle.template('edit', 
                         guestbook.find_entry(
                           bottle.request.params.get('id')));

@bottle.route('/edit', method='POST')
def edit():
  guestbook.update_entry(bottle.request.params.get('id'),
                       bottle.request.params.get('name'),
                       bottle.request.params.get('email'))
  bottle.redirect('/')

# This is to setup the connection
connection = pymongo.MongoClient('mongodb://mongo')

# We use the "guestbook" database
database = connection.guestbook
guestbook = dao.dao(database)

import signal
import sys
import os
def signal_handler(_signal, _frame):
  os.kill(os.getpid(), signal.SIGINT)
signal.signal(signal.SIGTERM, signal_handler)

bottle.run(host='0.0.0.0', port=8082)
