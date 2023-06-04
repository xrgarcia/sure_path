import datetime

from statemachine import StateMachine, State
from sure_path_models import ChangeRequest
from typing import Any


class ChangeWindowActiveStateMachine(StateMachine):
    "a state machine to manage change records, so we can talk to infra"
    WAITING_FOR_CHANGE_WINDOW = State(initial=True)
    CHANGE_WINDOW_STARTED = State()
    CHANGE_WINDOW_END = State(final=True)

    change_window_open = (WAITING_FOR_CHANGE_WINDOW.to(CHANGE_WINDOW_STARTED, cond="is_within_change_window")
                                 | WAITING_FOR_CHANGE_WINDOW.to(WAITING_FOR_CHANGE_WINDOW,
                                                                  unless="is_within_change_window"))
    change_window_closed = (CHANGE_WINDOW_STARTED.to(CHANGE_WINDOW_STARTED, cond="is_within_change_window")
                                 | CHANGE_WINDOW_STARTED.to(CHANGE_WINDOW_END,
                                                                  unless="is_within_change_window"))

    def __init__(self, change_request: ChangeRequest):
        self.change_request: ChangeRequest = change_request
        super().__init__()

    def is_within_change_window(self):
        ready = (self.change_request is not None and
                 self.change_request.start_time is not None and
                 self.change_request.end_time is not None)

        if ready:
            now = datetime.datetime.now()
            within_window = (now >= self.change_request.start_time and now < self.change_request.end_time)
            return within_window

        return False
