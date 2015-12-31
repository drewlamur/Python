import datetime, pdb

# Store the next available id for all new notes
last_id = 0

class Note:
	'''Represent a note in the notebook. Match against a string in searches and store tags for each note.'''

	def __init__(self,memo,tags=''):
		'''initialize a note with memo and optional space-separated tags. Automatically set the note's creation date and a unique id.'''
		self.memo = memo
		self.tags = tags
		self.creation_date = datetime.date.today()
		global last_id
		last_id += 1
		self.id = str(last_id)

	def match(self,str):
		'''Determine if this note matches the filter text. Return True if it matches, False otherwise. Search is case sensitive and matches both text and tags.
		   return firlter in self.memo or filter in self.tags'''

		return str in self.memo or str in self.tags


class Notebook:
	'''Represent a collection of notes that can be tagged, modified and searched.'''

	def __init__(self):
		'''initialize a notebook with an empty list.'''
		self.notes = []

	def new_note(self,memo,tags=''):
		'''Create a new note and add it to the list.'''
		self.notes.append(Note(memo,tags))

	# def modify_memo(self,note_id,memo):
	# 	'''Find the note with the given id and change its memo to the values passed in.'''
	# 	for note in self.notes:    # loop collection of notes 
	# 		if note.id == note_id: # id object eqls what is passed
	# 			note.memo = memo   # memo object eqls what is passed
	# 			break

	# def modify_tags(self,note_id,tags):	
	# 	'''Find the note with the given id and change its tags to the values passed in.'''
	# 	for note in self.notes:
	# 		if note.id == note_id:
	# 			note.tags = tags
	# 			break

	def _find_note(self,note_id):
		'''Locate the note with the given id.'''
		for note in self.notes:    # loop collection of notes 
			if note.id == note_id: # object id eqls what is passed
				return note        # return note
		return None

	def modify_memo(self,note_id,memo,tags=''):
		'''Find the note with the given id and change its memo to the given value.'''
		self._find_note(note_id).memo = memo
		self._find_note(note_id).tags = tags

	def search(self,str):
		'''Find all notes that match the given filter string.'''
		return [note for note in self.notes if note.match(str)]						


# ==> Note class usage
# root@fdc856e8c4dc:/# ls
# bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
# root@fdc856e8c4dc:/# cd var/python_oo_testing/
# root@fdc856e8c4dc:/var/python_oo_testing# ls
# command_option.py  menu.py  notebook.py  notebook.pyc
# root@fdc856e8c4dc:/var/python_oo_testing# source ~/.profile 
# root@fdc856e8c4dc:/var/python_oo_testing# python
# Python 2.7.10 (v2.7.10:15c95b7d81dc, May 23 2015, 09:33:12) 
# [GCC 4.8.2] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import subprocess
# >>> subprocess.call(['ls','l'],shell=True)
# command_option.py  menu.py  notebook.py  notebook.pyc
# 0
# >>> from notebook import Note
# >>> n1 = Note("hello world")
# >>> n2 = Note("hello again")
# >>> n1.id
# 1
# >>> n2.id
# 2
# >>> n1.match('hello')
# True
# >>> n1.match('again')
# False
# >>> n2.match('again')
# True

# ==> Note, Notebook class usage
# root@fdc856e8c4dc:/var/python_oo_testing# python
# Python 2.7.10 (v2.7.10:15c95b7d81dc, May 23 2015, 09:33:12) 
# [GCC 4.8.2] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import subprocess
# >>> subprocess.call(['ls','l'],shell=True)
# __pycache__  command_option.py	menu.py  notebook.py  notebook.pyc
# 0
# >>> from notebook import Note, Notebook
# >>> n = Notebook()
# >>> n.notes
# []
# >>> n.new_note("hello world")
# >>> n.new_note("hello again")
# >>> n
# <notebook.Notebook object at 0x7f92ea0fe6a0>
# >>> n.notes
# [<notebook.Note object at 0x7f92e8883860>, <notebook.Note object at 0x7f92ea112b00>]
# >>> n.notes[0].id
# 1
# >>> n.notes[1].id
# 2
# >>> n.notes[0].memo
# 'hello world'
# >>> n.notes[1].memo
# 'hello again'
# >>> n.search("hello")
# [<notebook.Note object at 0x7f92e8883860>, <notebook.Note object at 0x7f92ea112b00>]
# >>> n.search("world")
# [<notebook.Note object at 0x7f92e8883860>]
# >>> n.modify_memo(1,"hi world")
# >>> n.notes[0].memo
# 'hi world'

# ==> Note, Notebook class usage after function changes
# root@fdc856e8c4dc:/var/python_oo_testing# python
# Python 2.7.10 (v2.7.10:15c95b7d81dc, May 23 2015, 09:33:12) 
# [GCC 4.8.2] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from notebook import Note, Notebook
# >>> n = Notebook()
# >>> n.new_note("hello world")
# >>> n.new_note("hello again")
# >>> n.notes
# [<notebook.Note object at 0x7f11267c9710>, <notebook.Note object at 0x7f11267c97f0>]
# >>> n.search("hello")
# [<notebook.Note object at 0x7f11267c9710>, <notebook.Note object at 0x7f11267c97f0>]
# >>> n.search("world")
# [<notebook.Note object at 0x7f11267c9710>]
# >>> n.search("again")
# [<notebook.Note object at 0x7f11267c97f0>]
# >>> n._find_note(n.notes[0].id)
# <notebook.Note object at 0x7f11267c9710>
# >>> n._find_note(n.notes[1].id)
# <notebook.Note object at 0x7f11267c97f0>
# >>> n.modify_memo(n.notes[1].id,"hi again mr.")
# >>> n.notes
# [<notebook.Note object at 0x7f11267c9710>, <notebook.Note object at 0x7f11267c97f0>]
# >>> n.notes[0].memo
# 'hello world'
# >>> n.notes[1].memo
# 'hi again mr.'