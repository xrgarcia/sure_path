from statemachine import StateMachine, State


class OsUpgradeStateMachine(StateMachine):
    "A traffic light machine"
    ready = State(initial=True)
    change_created = State()
    change_approved = State()
    pre_stage_iso_img = State()
    within_change_window = State()
    capture_pre_checks = State()
    upgrade_os = State()
    capture_post_checks = State()

    cycle = (
        ready.to(change_created)
        | change_created.to(change_approved)
        | change_approved.to(pre_stage_iso_img)
        | pre_stage_iso_img.to(within_change_window)
        | within_change_window.to(capture_pre_checks)
        | capture_pre_checks.to(upgrade_os)
        | upgrade_os.to(capture_post_checks)
        | capture_post_checks.to(ready)
    )

    def before_cycle(self, event: str, source: State, target: State, message: str = ""):
        message = ". " + message if message else ""
        return f"Running {event} from {source.id} to {target.id}{message}"

    def on_enter_ready(self):
        print("I am ready to upgrade a network device!")

    def on_exit_ready(self):
        print("sweet.... now i must have a change")


sm = OsUpgradeStateMachine()
print(f"current state: {sm}")
print("Cycling to next state")
sm.send("cycle")
print(f"current state: {sm}")
print("Cycling to next state")
sm.send("cycle")
print(f"current state: {sm}")
print("Cycling to next state")
sm.send("cycle")
print(f"current state: {sm}")
print("Cycling to next state")
sm.send("cycle")
print(f"current state: {sm}")
print("Cycling to next state")
sm.send("cycle")
print(f"current state: {sm}")
print("Cycling to next state")
sm.send("cycle")
print(f"current state: {sm}")
print("Cycling to next state")
sm.send("cycle")
print(f"current state: {sm}")
print("Cycling to next state")
sm.send("cycle")
print(f"current state: {sm}")

