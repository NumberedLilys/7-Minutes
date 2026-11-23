from Dialogue import TIMED_DIALOGUE
def setup_timed_events(timer, dialogue, get_current_room):

    def first_event():
        if get_current_room() == "bedroom":
            dialogue.queue(TIMED_DIALOGUE["mother breakfast"])

    # def second_event():
    #     dialogue.queue(SECOND_EVENT_DIALOGUE)

    timer.add_event(
        minutes=0,
        seconds=10,
        callback=first_event
    )

    # timer.add_event(
    #     minutes=3,
    #     seconds=0,
    #     callback=second_event
    # )