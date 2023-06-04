from statemachine import StateMachine, State
from sure_path_models import ChangeRequest
from typing import Any


class ChangeApprovalStateMachine(StateMachine):
    "a state machine to manage change records, so we can talk to infra"
    WAITING_FOR_CHANGE_APPROVAL = State(initial=True)
    CHANGE_APPROVED = State(final=True)

    change_approval_requested = (WAITING_FOR_CHANGE_APPROVAL.to(CHANGE_APPROVED, cond="has_change_approval")
                                 | WAITING_FOR_CHANGE_APPROVAL.to(WAITING_FOR_CHANGE_APPROVAL,
                                                                  unless="has_change_approval"))

    def __init__(self):
        self.change_request: ChangeRequest = None
        super().__init__()

    def before_change_approval_requested(self, change_request: ChangeRequest = None):
        self.change_request = change_request

    def has_change_approval(self):
        return self.change_request is not None and self.change_request.status is not None and len(
            self.change_request.status) > 0 and "APPROVED" == self.change_request.status.upper()
