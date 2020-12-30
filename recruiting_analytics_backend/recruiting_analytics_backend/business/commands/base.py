from typing import Any

class CommandError(Exception):
    pass

class CommandBase():
    def execute(self):
        raise NotImplementedError()

class CommandResult:
    def __init__(self, is_success: bool, error: str=None, value: Any=None):
        if is_success and error:
            raise ValueError("A result cannot be successful and contain an error")
        if not is_success and not error:
            raise ValueError("A failing result needs to contain an error mesage")

        self.is_success = is_success
        self.error = error
        self.value = value
