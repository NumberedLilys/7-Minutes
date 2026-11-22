from Dialogue import FIRST_EVENT_DIALOGUE
def setup_timed_events(timer, dialogue):

    def first_event():
        dialogue.queue(FIRST_EVENT_DIALOGUE["mother breakfast"])

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