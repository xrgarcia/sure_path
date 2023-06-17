from statemachine import StateMachine, State
from sure_path_models import ChangeRequest
import datetime


class NetworkDeviceOsUpgradeStateMachine(StateMachine):
    READY = State(initial=True)
    WAITING_FOR_CHANGE_NUMBER = State()
    CHANGE_CREATED = State(final=True)
    WAITING_FOR_CHANGE_APPROVAL = State(initial=True)
    CHANGE_APPROVED = State(final=True)
    WAITING_FOR_CHANGE_WINDOW = State(initial=True)
    CHANGE_WINDOW_STARTED = State()
    ISO_IMG_PRE_STAGE_STARTED = State()
    ISO_IMG_PRE_STAGE_COMPLETED = State()
    PRE_HEALTH_CHECKS_STARTED = State()
    PRE_HEALTH_CHECKS_COMPLETED = State()
    OS_UPGRADE_STARTED = State()
    DEVICE_REBOOT_STARTED = State()
    DEVICE_REBOOT_COMPLETE = State()
    OS_UPGRADE_COMPLETE = State()
    POST_HEALTH_CHECKS_STARTED = State()
    POST_HEALTH_CHECKS_COMPLETE = State()
    SUCCESS = State()
    CHANGE_WINDOW_END = State(final=True)

    step = (
            WAITING_FOR_CHANGE_NUMBER.to(CHANGE_CREATED, cond="has_change_number")
            | WAITING_FOR_CHANGE_NUMBER.to(WAITING_FOR_CHANGE_NUMBER, unless="has_change_number")
            | WAITING_FOR_CHANGE_APPROVAL.to(CHANGE_APPROVED, cond="has_change_approval")
            | WAITING_FOR_CHANGE_APPROVAL.to(WAITING_FOR_CHANGE_APPROVAL,
                                             unless="has_change_approval")
            | WAITING_FOR_CHANGE_WINDOW.to(CHANGE_WINDOW_STARTED, cond="is_within_change_window")
            | WAITING_FOR_CHANGE_WINDOW.to(WAITING_FOR_CHANGE_WINDOW,
                                           unless="is_within_change_window")
            | CHANGE_WINDOW_STARTED.to(CHANGE_WINDOW_STARTED, cond="is_within_change_window")
            | CHANGE_WINDOW_STARTED.to(CHANGE_WINDOW_END,
                                       unless="is_within_change_window")
    )

    def __init__(self, change_request: ChangeRequest = None):
        self.change_request = change_request
        super().__init__()

    def has_change_approval(self):
        return self.change_request is not None and self.change_request.status is not None and len(
            self.change_request.status) > 0 and "APPROVED" == self.change_request.status.upper()

    def before_step(self, change_request: ChangeRequest = None):
        self.change_request = change_request

    def has_change_number(self):
        return self.change_request is not None and self.change_request.request_number is not None and len(
            self.change_request.request_number) > 0

    def is_within_change_window(self):
        ready = (self.change_request is not None and
                 self.change_request.start_time is not None and
                 self.change_request.end_time is not None)

        if ready:
            now = datetime.datetime.now()
            within_window = (self.change_request.start_time <= now < self.change_request.end_time)
            return within_window

        return False
