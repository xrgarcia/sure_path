from statemachine import StateMachine, State

class NetworkDeviceOsUpgradeStateMachine(StateMachine):
    "A network device os upgrade state machine"
    ready = State(initial=True)
    completed = State()

    next = (
        ready.to(completed)
        | completed.to(ready)

    )

    def before_transition(self, event, state):

        print(f"Before '{event}', on the '{state.id}' state.")

        return "before_transition_return"


    def on_transition(self, event, state):

        print(f"On '{event}', on the '{state.id}' state.")

        return "on_transition_return"


    def on_exit_state(self, event, state):

        print(f"Exiting '{state.id}' state from '{event}' event.")


    def on_enter_state(self, event, state):

        print(f"Entering '{state.id}' state from '{event}' event.")


    def after_transition(self, event, state):

        print(f"After '{event}', on the '{state.id}' state.")