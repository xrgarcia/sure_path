from machines import NetworkDeviceOsUpgradeStateMachine,RaiseChangeStateMachine

raise_change_sm = RaiseChangeStateMachine()
print(raise_change_sm)
raise_change_sm.change_number_requested(None)
print(raise_change_sm)
raise_change_sm.change_number_requested(None)
print(raise_change_sm)
raise_change_sm.change_number_requested(None)
print(raise_change_sm)
raise_change_sm.change_number_requested("CHG12341324")
raise_change_sm.change_raised()
print(raise_change_sm)