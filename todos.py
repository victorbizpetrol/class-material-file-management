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
        if self.path.exists() and not self.path.is_dir():
            raise ValueError('{} path is invalid'.format(base_todos_path))

        if not self.path.exists():
            if not create_dir:
                raise ValueError("{} doesn't exist".format(base_todos_path))
            self.path.mkdir(parents=True)

    def list(self, status=STATUS_ALL, category=CATEGORY_GENERAL):
        todos = {}
        for todo_path in self.path.glob('*.json'):
            with todo_path.open('r') as fp:
                document = json.load(fp)
                if 'category_name' not in document or 'todos' not in document:
                    raise ValueError('Invalid JSON todo format.')

                category_todos = []
                for todo in document['todos']:
                    if status == self.STATUS_ALL or todo['status'] == status:
                        category_todos.append(todo)

                todos[document['category_name']] = category_todos

        return todos

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

        todo_file_name = '{}.json'.format(category)
        path = self.path / todo_file_name

        todos = {
            'category_name': category.title(),
            'todos': []
        }
        if path.exists():
            with path.open('r') as fp:
                todos = json.load(fp)

        todo = {
            'task': task,
            'description': description,
            'due_on': due_on,
            'status': self.STATUS_PENDING
        }

        todos['todos'].append(todo)

        with path.open('w') as fp:
            todos = json.dump(todos, fp, indent=2)
