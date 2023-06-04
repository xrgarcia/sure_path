from statemachine import StateMachine, State

class RaiseChangeStateMachine(StateMachine):
    "a state machine to manage change records, so we can talk to infra"
    waiting_for_change_number = State(initial=True)
    #change_failed = State(final=True)
    change_created = State(final=True)
    #change_rejected = State(final=True)
    #in_change_window = State(final=True)

    change_number_requested = waiting_for_change_number.to(waiting_for_change_number)
    change_number_received = (waiting_for_change_number.to(change_created, cond="has_change_number")
                             | waiting_for_change_number.to(waiting_for_change_number, unless="has_change_number"))
    change_raised = waiting_for_change_number.to(change_created,cond="has_change_number")


    def __init__(self):
        self.change_number = None
        super().__init__()

    def before_change_number_requested(self, chg_number=None):
        self.change_number = chg_number

    def has_change_number(self):
        return self.change_number is not None and len(self.change_number) > 0
