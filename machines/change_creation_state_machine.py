from statemachine import StateMachine, State
from sure_path_models import ChangeRequest
from typing import Any


class WaitingForChangeNumberState(State):

    def __init__(
            self,
            name: str = "",
            value: Any = None,
            initial: bool = False,
            final: bool = False,
            enter: Any = None,
            exit: Any = None,
    ):
        super().__init__(name, value, initial, final, enter, exit)
        #self.name: str = "chg-creation-1001"


class RaiseChangeStateMachine(StateMachine):
    "a state machine to manage change records, so we can talk to infra"
    WAITING_FOR_CHANGE_NUMBER = WaitingForChangeNumberState(initial=True)
    CHANGE_CREATED = State(final=True)

    change_number_requested = (WAITING_FOR_CHANGE_NUMBER.to(CHANGE_CREATED, cond="has_change_number")
                               | WAITING_FOR_CHANGE_NUMBER.to(WAITING_FOR_CHANGE_NUMBER, unless="has_change_number"))

    def __init__(self):
        self.change_request: ChangeRequest = None
        super().__init__()

    def before_change_number_requested(self, change_request: ChangeRequest = None):
        self.change_request = change_request

    def has_change_number(self):
        return self.change_request is not None and self.change_request.request_number is not None and len(
            self.change_request.request_number) > 0
