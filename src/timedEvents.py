from Dialogue import TIMED_DIALOGUE
def setup_timed_events(timer, dialogue, get_current_room, ending_state):

    def first_event():
        if get_current_room() == "bedroom":
            dialogue.queue(TIMED_DIALOGUE["mother breakfast"])

    def second_event():
        ending_state["image_active"] = True
        dialogue.queue(TIMED_DIALOGUE["death_ending"])

    timer.add_event(
        minutes=0,
        seconds=10,
        callback=first_event
    )

    # timer.add_event(
    #     minutes=7,
    #     seconds=0,
    #     callback=second_event
    # )