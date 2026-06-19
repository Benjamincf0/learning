from . import common

class EventLoop:
    monoid = None

    def __init__(self):
        self.taskQueue: list[Task|None] = []

    def run_loop(self):
        """ Runs until loop is empty """
        while len(self.taskQueue) > 0:
            pass


    def create_task(self, coroutine: Coroutine):
        """ Add task to event loop """
        task = Task(coroutine)
        self._add_task(task)

    def _add_task(self, task: Task):
        self.taskQueue.append(task)
