import json
from pathlib import Path
from datetime import date


class TodoManager(object):
    STATUS_ALL = 'all'
    STATUS_DONE = 'done'
    STATUS_PENDING = 'pending'
    CATEGORY_GENERAL = 'general'

    def __init__(self, base_todos_path, create_dir=True):
        self.base_todos_path = base_todos_path
        self.path = Path(self.base_todos_path)
        # continue here

    def list(self, status=STATUS_ALL, category=CATEGORY_GENERAL):
        pass

    def new(self, task, category=CATEGORY_GENERAL, description=None,
            due_on=None):

        if due_on:
            if type(due_on) == date:
                due_on = due_on.isoformat()
            elif type(due_on) == str:
                # all good
                pass
            else:
                raise ValueError('Invalid due_on type. Must be date or str')

        # continue here
