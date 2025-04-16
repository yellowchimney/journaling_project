# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.all_tasks = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos

        self.all_tasks.append(todo)

    def list_incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        
        list_of_incompletes = [
            task for task in self.all_tasks if not task.complete
            ]
        return list_of_incompletes 


    def list_complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        
        list_of_completes = [
            task for task in self.all_tasks if task.complete
            ]

        return list_of_completes




