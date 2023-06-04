from statemachine import StateMachine, State

class DeviceDeploymentStateMachine(StateMachine):
    "A traffic light machine"
    ready = State(initial=True)
    change_created = State()
    change_approved = State()
    pre_stage_iso_img = State()
    within_change_window = State()
    capture_pre_checks = State()
    upgrade_os = State()
    capture_post_checks = State()
    completed = State()

    next = (
        ready.to(change_created)
        | change_created.to(change_approved)
        | change_approved.to(pre_stage_iso_img)
        | pre_stage_iso_img.to(within_change_window)
        | within_change_window.to(capture_pre_checks)
        | capture_pre_checks.to(upgrade_os)
        | upgrade_os.to(capture_post_checks)
        | capture_post_checks.to(completed)
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