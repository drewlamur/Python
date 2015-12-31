import pdb, sys
from notebook import Notebook, Note


class Menu:
	'''Display a menu and respond to choices when run.'''

	def __init__(self):
		self.notebook = Notebook()
		self.choices  = {
				
			"1" : self.show_notes,
			"2" : self.search_notes,
			"3" : self.add_note,
			"4" : self.modify_note,
			"5" : self.quit

		}

	def display_menu(self):
		print("""
 		
 		Notebook Menu

 		1. Show all notes
 		2. Search notes
 		3. Add notes
 		4. Modify notes
 		5. Quit
        
		""")

	def run(self):
		'''Display the menu and respond to choices.'''
		while True:
			self.display_menu()
			choice = raw_input("Enter an option: ")
			action = self.choices.get(choice)
			if action:
				action()
			else:
				print("{0} is not a valid choice.".format(choice))

	def show_notes(self,notes=None):
		if not notes:
			notes = self.notebook.notes
		for note in notes:
			print("id: {0}\ntags: {1}\nmemo: {2}".format(note.id,note.tags,note.memo))

	def search_notes(self):
		filter = raw_input("Search for: ")
		notes = self.notebook.search(filter)
		self.show_notes(notes)

	def add_note(self):
		memo = raw_input("Enter a memo: ")
		self.notebook.new_note(memo)
		print("Your note has been added.")

	def modify_note(self):
		id = raw_input("Enter a note id: ")
		memo = raw_input("Enter a memo: ")
		tags = raw_input("Enter tags: ")
		if tags:
			self.notebook.modify_memo(id,memo,tags)
		else:
			self.notebook.modify_memo(id,memo)

	def quit(self):
		print("Thank you for using your notebook today.")
		sys.exit(0)

if __name__ == "__main__":
	Menu().run()

# ==> Menu, Note, Notebook class usage
# root@fdc856e8c4dc:/# ls 
# bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var 
# root@fdc856e8c4dc:/# cd var/python_oo_testing/ 
# root@fdc856e8c4dc:/var/python_oo_testing# ls 
# __pycache__  command_option.py  menu.py  notebook.py  notebook.pyc 
# root@fdc856e8c4dc:/var/python_oo_testing# python 
# Python 2.7.10 (v2.7.10:15c95b7d81dc, May 23 2015, 09:33:12) 
# [GCC 4.8.2] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from menu import Menu 
# >>> obj = Menu() 
# >>> obj.run() 
 
                 
#                 Notebook Menu 
 
#                 1. Show all notes 
#                 2. Search notes 
#                 3. Add notes 
#                 4. Modify notes 
#                 5. Quit 
         
                 
# Enter an option: 3 
# Enter a memo: Memo test 1 
# Your note has been added. 
 
                 
#                 Notebook Menu 
 
#                 1. Show all notes 
#                 2. Search notes 
#                 3. Add notes 
#                 4. Modify notes 
#                 5. Quit 
         
                 
# Enter an option: 3 
# Enter a memo: Memo test 2 
# Your note has been added. 
 
                 
#                 Notebook Menu 
 
#                 1. Show all notes 
#                 2. Search notes 
#                 3. Add notes 
#                 4. Modify notes 
#                 5. Quit 
         
                 
# Enter an option: 2 
# Search for: 2 
# id: 2
# tags:  
# memo: Memo test 2 
 
                 
#                 Notebook Menu 
 
#                 1. Show all notes 
#                 2. Search notes 
#                 3. Add notes 
#                 4. Modify notes 
#                 5. Quit 
         
                 
# Enter an option: 4 
# Enter a note id: 2 
# Enter a memo: Memo test 2 - modified 
# Enter tags: test, andy 
 
                 
#                 Notebook Menu 
 
#                 1. Show all notes 
#                 2. Search notes 
#                 3. Add notes 
#                 4. Modify notes 
#                 5. Quit 
         
                 
# Enter an option: 2 
# Search for: 2 
# id: 2 
# tags: test, andy 
# memo: Memo test 2 - modified 
 
                 
#                 Notebook Menu 
 
#                 1. Show all notes 
#                 2. Search notes 
#                 3. Add notes 
#                 4. Modify notes 
#                 5. Quit 
         
                 
# Enter an option: 4 
# Enter a note id: 2         
# Enter a memo: Memo test 2 - modified again 
# Enter tags: test, python, docker 
 
                 
#                 Notebook Menu 
 
#                 1. Show all notes 
#                 2. Search notes
#                 3. Add notes 
#                 4. Modify notes 
#                 5. Quit 
         
                 
# Enter an option: 2 
# Search for: 2 
# id: 2 
# tags: test, python, docker 
# memo: Memo test 2 - modified again 
 
                 
#                 Notebook Menu 
 
#                 1. Show all notes 
#                 2. Search notes 
#                 3. Add notes 
#                 4. Modify notes 
#                 5. Quit 
         
                 
# Enter an option: 5 
# Thank you for using your notebook today. 
# root@fdc856e8c4dc:/var/python_oo_testing#