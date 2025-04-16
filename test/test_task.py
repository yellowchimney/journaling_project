from lib.task import Todo

def test_complete_is_initially_set_to_false():
    todo = Todo("do something")

    assert todo.complete == False

def test_mark_complete_changes_initial_setting_to_true():
    todo = Todo("do something")
    todo.mark_complete()

    assert todo.complete == True
