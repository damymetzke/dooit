from typing import Optional, Callable
from .model import Model


class Topic(Model):
    fields = ["about"]
    nomenclature: str = "Todo"

    def __init__(self, name: str, parent: Optional["Model"] = None) -> None:
        from .todo import Todo

        super().__init__(name, parent)
        self.about = ""
        self.ctype: Callable = Todo

    def commit(self):
        return [child.commit() for child in self.children]

    def from_data(self, data):
        for i in data:
            self.add_child()
            self.children[-1].fill_from_data(i[0])
            if len(i) > 1:
                self.children[-1].from_data(i[1])

    def get_todos(self):
        return self.children