from machines import RaiseChangeStateMachine, ChangeApprovalStateMachine, ChangeWindowActiveStateMachine
from sure_path_models import ChangeRequest
from datetime import datetime, timedelta
import time

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
        if i >= fake_iteration_where_response_returned:
            change_request.request_number = "CHG1324512345"
        change_request_sm.change_number_requested(change_request)
        if change_request_sm.current_state == change_request_sm.CHANGE_CREATED:
            print("\n\n--------------DONE--------------")
            print(f"{change_request_sm.current_state.name}, {change_request_sm}")

            break
        else:
            print(f"waiting {change_request_sm.current_state.id}")

def run_simulated_waiting_for_change_window():
    # init objs
    change_request = ChangeRequest()
    change_request.request_number = "CHG1234512345"
    change_request.status = "APPROVED"
    change_request.start_time = datetime.now() + timedelta(minutes=1) # starts 1 min from now
    change_request.end_time = change_request.start_time + timedelta(minutes=1) # only open for 1 min
    change_window_sm = ChangeWindowActiveStateMachine(change_request)
    print(change_request.json())

    # pretend to request change to be raised and poll until the right information gets returned
    while True:
        print(f"Checking Change Window: {datetime.now()}, {change_request.json()}")
        if change_window_sm.current_state == change_window_sm.WAITING_FOR_CHANGE_WINDOW:
            change_window_sm.cycle()
            print("Waiting for change window to start: sleeping 10 secs")
            time.sleep(10)
        elif change_window_sm.current_state == change_window_sm.CHANGE_WINDOW_STARTED:
            print(f"---------------change window started----------------")
            print(f"current time {datetime.now()}")
            print(f"{change_request}")
            change_window_sm.cycle()
            print("Hurry UP! Do your job! You only have a min of the change window!")
            time.sleep(10)
        elif change_window_sm.current_state == change_window_sm.CHANGE_WINDOW_END:
            print("Change window is over")
            break


def run_simulated_waiting_for_change_approval():
    # init objs
    change_approval_sm = ChangeApprovalStateMachine()
    change_request = ChangeRequest()
    print(change_approval_sm)

    # pretend to request change to be raised and poll until the right information gets returned
    num_loops = 10
    fake_iteration_where_response_returned = 7

    for i in range(1, num_loops):
        # pretend to pull new change request from system
        change_request = ChangeRequest()
        change_request.request_number = "CHG1234523456"

        # if our current iteration flags us to pretend that a change # has been generated
        if i >= fake_iteration_where_response_returned:
            change_request.status = "APPROVED"
        else:
            change_request.status = "CREATED"
        change_approval_sm.change_approval_requested(change_request)
        if change_approval_sm.current_state == change_approval_sm.CHANGE_APPROVED:
            print("\n\n--------------DONE--------------")
            print(f"{change_approval_sm.current_state.id}, {change_request.json()}")
            break
        else:
            print(f"waiting {change_approval_sm.current_state.id}, {change_request.json()}")

if __name__ == "__main__":
    run_simulated_waiting_for_change_window()