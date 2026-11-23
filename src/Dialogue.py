BEDROOM_DIALOGUES = {
    "bed": {
        "start": {
            "speaker": "Blank",
            "text": "A messy bed. You've never had the energy to make it in the morning",
            "options": [{"text": "Back", "next": None}]
        },
    },
    "flowers": {
        "start": {
            "speaker": "Blank",
            "text": "Fresh lilies. There's a faint scent.",
            "options": [
                        {"text": "Throw them out", "next": "throw out"},    # Index 0
                        {"text": "Leave them alone", "next": "leave"}       # Index 1
                        ]
        },
        "throw out": {
            "speaker": "Maynne",
            "text": "Lilies were never my favourite flower anyways.",
            "options": [{"text": "Back", "next": None}]
        },
        "leave": {
            "speaker": "Maynne",
            "text": "The flowers make the room smell fresh. There would be no reason to remove them.",
            "options": [{"text": "Back", "next": None}]
        }
    },
    "wall decor": {
        "start": {
            "speaker": "Blank",
            "text": "Posters of your favourite band. It would have been nice if you bought tickets when they were on tour",
            "options": [{"text": "Back", "next": None},]
            }
    },
    "lyra": {
        "start": {
            "speaker": "Lyra",
            "text": "Meow!",
            "options": [{"text": "Pet", "next": "pet"},
                        {"text": "Back", "next": None}]
        },
        "pet": {
            "speaker": "Blank",
            "text": "My cat. My absolute favourite part of every morning.",
            "options": [{"text": "Back", "next": None}]
        }
    }
}

KITCHEN_DIALOGUE = {
    "breakfast": {
        "start": {
            "speaker": "Blank",
            "text": "Freshly made pancakes, courtesy of my mother.",
            "options": [
                        {"text": "Eat them", "next": "eat"},    # Index 0
                        {"text": "Leave them there", "next": "leave"}       # Index 1
                        ]
        },
        "eat": {
            "speaker": "Maynne",
            "text": "What a great start to my day. My mother's cooking has never let me down.",
            "options": [{"text": "Back", "next": None}]
        },
        "leave": {
            "speaker": "Maynne",
            "text": "I couldn't bring myself to eat them. My stomach turned at the thought.",
            "options": [{"text": "Back", "next": None}]
        }
    },
    "calendar": {
        "start": {
            "speaker": "Blank",
            "text": "It's the date. Why is it smudged?",
            "options": [{"text": "Back", "next": None}]
        }
    }
}

TIMED_DIALOGUE = {
    "mother breakfast": {
            "start": {
                "speaker": "Mom",
                "text": "Maynne! Breakfast is ready!",
                "options": [
                            {"text": "Coming, Mom!", "next": "respond breakfast"},    # Index 0
                            {"text": "Ignore her", "next": "ignore breakfast"}       # Index 1
                            ]
            },
            "respond breakfast": {
                "speaker": "Maynne",
                "text": "Coming, Mom!",
                "options": [{"text": "Back", "next": None}]
            },
            "ignore breakfast": {
                "speaker": "Maynne",
                "text": "...",
                "options": [{"text": "Back", "next": None}]
            }
    },
    "death_ending": {
        "start": {
            "speaker": "Death",
            "text": "It's not your fault.",
            "options": [{"text": "Next", "next": "maynne_response_1"}]
        },
        "maynne_response_1": {
            "speaker": "Maynne",
            "text": "...What?",
            "options": [{"text": "Next", "next": "death_response_1"}]
        },
        "death_response_1": {
            "speaker": "Death",
            "text": "You did nothing wrong.",
            "options":[{"text": "Next", "next": "maynne_response_2"}]
        },
        "maynne_response_2": {
            "speaker": "Maynne",
            "text": "I didn't say goodbye.",
            "options": [{"text": "Next", "next": "death_response_2"}]
        },
        "death_response_2": {
            "speaker": "Death",
            "text": "People rarely get to.",
            "options": [{"text": "Next", "next": "maynne_response_3"}]
        },
        "maynne_response_3": {
            "speaker": "Maynne",
            "text": "There is so much I should have done differently.",
            "options": [{"text": "Next", "next": "death_response_3"}]
        },
        "death_response_3": {
            "speaker": "Death",
            "text": "Humans are imperfect. Every decision you made would have led to a different regret.",
            "options": [{"text": "Next", "next": "maynne_response_4"}]
        },
        "maynne_response_4": {
            "speaker": "Maynne",
            "text": "It felt so quick... I didn't have enough time to experience life.",
            "options": [{"text": "Next", "next": "death_response_4"}]
        },
        "death_response_4": {
            "speaker": "Death",
            "text": "You lived. You loved. You cared for others and got their care in return.",
            "options": [{"text": "Next", "next": "death_response_4.1"}]
        },
        "death_response_4.1": {
            "speaker": "Death",
            "text": "Although short lived, you got to experience what it means to be human.",
            "options": [{"text": "Next", "next": "death_response_4.2"}]
        },
        "death_response_4.2": {
            "speaker": "Death",
            "text": "If that is not experiencing life, then I'm not sure what is.",
            "options": [{"text": "Next", "next": "maynne_response_5"}]
        },
        "maynne_response_5": {
            "speaker": "Maynne",
            "text": "What do I do now? What can I do?",
            "options": [{"text": "Next", "next": "death_response_5"}]
        },
        "death_response_5": {
            "speaker": "Death",
            "text": "What do you want to do?",
            "options": [{"text": "Next", "next": "maynne_response_6"}]
        },
        "maynne_response_6": {
            "speaker": "Maynne",
            "text": "...",
            "options": [{"text": "Next", "next": None}]
        },
    }
}