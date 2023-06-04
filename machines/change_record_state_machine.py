from statemachine import StateMachine, State
from sure_path_models import ChangeRequest

class RaiseChangeStateMachine(StateMachine):
    "a state machine to manage change records, so we can talk to infra"
    waiting_for_change_number = State(initial=True)
    change_created = State(final=True)

    change_number_requested = (waiting_for_change_number.to(change_created, cond="has_change_number")
                             | waiting_for_change_number.to(waiting_for_change_number, unless="has_change_number"))

    def __init__(self):
        self.change_request: ChangeRequest= None
        super().__init__()

    def before_change_number_requested(self, change_request: ChangeRequest=None):
        self.change_request = change_request

    def has_change_number(self):
        return self.change_request is not None and self.change_request.request_number is not None and len(self.change_request.request_number) > 0
