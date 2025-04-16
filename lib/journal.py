from lib.todo_list import TodoList
from lib.diary_entry import DiaryEntry

"""
/// nouns:
diary
diary_entry
todo_list
tasks
contacts

/// verbs:
record
read
read based on how much time I have
keep track of tasks
see list of contacts


class Diary
- has  a list of diary entries (instances)
- has add method for diary entries
- has read method for diary entries 
(how do I want to implement this: return all entries
or 1 entry by title)
- has a find_best_for_reading_time method
- has a method to list all the tasks (ToDo instance)
- has a method to list all phones in all entries 

class DiaryEntry
- has title and contents properties
- has count_words method
- has reading_time method
- has extract_phone_number method 

class ToDo_list
- has a list of tasks
- has a complete and incomplete method to list the relevant taskss

class ToDo:
- has a task title
- has a complete method

"""


class Diary():
    def __init__(self):
        self.entry_list = []
        self.word_counter = 0
        self.todo = TodoList()

    def add(self, entry):
        self.entry_list.append(entry)

    def show_all(self):

        return self.entry_list

    def get_entry_by_title(self, title):
        for entry in self.entry_list:
            if entry.title == title:

                return entry.contents


    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        dict_of_all_suitable_entries = {}
        for entry in self.entry_list:
            reading_time_per_entry = entry.reading_time(wpm)
            if reading_time_per_entry <= minutes:
                dict_of_all_suitable_entries[reading_time_per_entry] = entry
        best_entry = max(dict_of_all_suitable_entries.keys())

        return dict_of_all_suitable_entries[best_entry]

    def get_full_todo_list(self):
        # returns a dictionary of all tasks and their status
        tasks_at_a_glance = {}
        for task in self.todo:
            tasks_at_a_glance[task.task] = task.complete

        return tasks_at_a_glance

    def get_incomplete_tasks(self):
        tasks_to_complete= {}
        for task in self.todo.list_incomplete():
            tasks_to_complete[task.task] = task.complete

    
    def list_contacts(self):
        my_phone_book = []
        for entry in self.entry_list:
            contacts_per_entry = entry.extract_phone_numbers()
            contacts_per_entry.extend(my_phone_book)
        
        return my_phone_book


