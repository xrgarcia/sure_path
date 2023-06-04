from machines import NetworkDeviceOsUpgradeStateMachine,RaiseChangeStateMachine
from sure_path_models import ChangeRequest

raise_change_sm = RaiseChangeStateMachine()
change_request = ChangeRequest()
print(raise_change_sm)
raise_change_sm.change_number_requested(change_request)
print(raise_change_sm)
raise_change_sm.change_number_requested(change_request)
print(raise_change_sm)
raise_change_sm.change_number_requested(change_request)
print(raise_change_sm)
change_request.request_number = "CHG13452345"
raise_change_sm.change_number_requested(change_request)
raise_change_sm.change_raised()
print(raise_change_sm)