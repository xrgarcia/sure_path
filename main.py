from machines import NetworkDeviceOsUpgradeStateMachine,RaiseChangeStateMachine
from sure_path_models import ChangeRequest


def run_simulated_create_change():
    # init objs
    change_request_sm = RaiseChangeStateMachine()
    change_request = ChangeRequest()
    print(change_request_sm)

    # pretend to request change to be raised and poll until the right information gets returned
    num_loops = 10
    fake_iteration_where_response_returned = 7

    for i in range(num_loops):
        # pretend to pull new change request from system
        change_request = ChangeRequest()

        # if our current iteration flags us to pretend that a change # has been generated
        if i == fake_iteration_where_response_returned:
            change_request.request_number = "CHG1324512345"
        change_request_sm.change_number_requested(change_request)
        if change_request_sm.current_state == change_request_sm.CHANGE_CREATED:
            print(f"DONE! {change_request_sm.current_state.name}, {change_request_sm}")

            break
        else:
            print(f"waiting {change_request_sm.current_state.id}")


def run_simulated_waiting_for_change_approval():
    pass

if __name__ == "__main__":
    run_simulated_create_change()