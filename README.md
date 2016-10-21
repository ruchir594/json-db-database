This is a JSON Database system for Python.

It builds a database in JSON. This great light weight programming is a better way to quick prototyping, and testing. It can also be used in production with software that require storing some form of context, but does not require a huge scalable database.

<b> How to use it? </b>

Define your database structure in "template.json". Look for example.

The first column is the name of column, the second column will specify the type such as, number, string, array, or a bool

from jsondb import manage_element

dbfile = 'data.json'
manage_element.init_json(dbfile, 'trial')
a = manage_element.get_element(dbfile,'103')
a['other column name'] = 'Testing on Oct 21'
a['one more column'] = ['the', 'beatles', 21]
manage_element.update_element(dbfile, a)
a = manage_element.get_element(dbfile,'103')
print a

$ python test.py
{u'one more column': [u'the', u'beatles', 21], u'unique id': -1, u'other column name': u'Testing on Oct 21', u'some column name': u'', u'a column': u'False', u'id': u'103'}
