from machines import NetworkDeviceOsUpgradeStateMachine

sm = NetworkDeviceOsUpgradeStateMachine()
print(f"-----------{sm.current_state.name}--------")
print(f"current state: {sm}")

sm.next()
print(f"\n\n-----------{sm.current_state.name}--------")
print(f"current state: {sm}")

sm.next()
print(f"\n\n-----------{sm.current_state.name}--------")
print(f"current state: {sm}")
sm.next()
print(f"\n\n-----------{sm.current_state.name}--------")
print(f"current state: {sm}")

sm.next()
print(f"\n\n-----------{sm.current_state.name}--------")
print(f"current state: {sm}")

sm.next()
print(f"\n\n-----------{sm.current_state.name}--------")
print(f"current state: {sm}")

sm.next()
print(f"\n\n-----------{sm.current_state.name}--------")
print(f"current state: {sm}")

sm.next()
print(f"\n\n-----------{sm.current_state.name}--------")
print(f"current state: {sm}")

sm.next()
print(f"\n\n-----------{sm.current_state.name}--------")
print(f"current state: {sm}")

sm.next()
print(f"\n\n-----------{sm.current_state.name}--------")
print(f"current state: {sm}")

is_back_to_ready = (sm.current_state == NetworkDeviceOsUpgradeStateMachine.ready)
print(f"back to ready: {is_back_to_ready}")
print(f"ready state is active: {sm.ready.is_active}")

print("---------ALL STATES -------")
for state in sm.states:
    print(state.id)

print("--------ALL Events---------")
for event in sm.events:
    print(event.name)
