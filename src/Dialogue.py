BEDROOM_DIALOGUES = {
    "bookshelf": {
        "start": {
            "speaker": "Blank",
            "text": "A shelf full of books. Some are visually worn out, as though read a lot.",
            "options": [{"text": "Next", "next": None}]
        },
    },
    "bed": {
        "start": {
            "speaker": "Blank",
            "text": "A messy bed. You've never had the energy to make it in the morning.",
            "options": [{"text": "Next", "next": None}]
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
            "options": [{"text": "Next", "next": None}]
        },
        "leave": {
            "speaker": "Maynne",
            "text": "The flowers make the room smell fresh. There would be no reason to remove them.",
            "options": [{"text": "Next", "next": None}]
        }
    },
    "wall decor": {
        "start": {
            "speaker": "Blank",
            "text": "Random notes scattered about. One is listed from last year describing a grocery list.",
            "options": [{"text": "Next", "next": None},]
            }
    },
    "lyra": {
        "start": {
            "speaker": "Lyra",
            "text": "Meow!",
            "options": [{"text": "Pet", "next": "pet"},
                        {"text": "Next", "next": None}]
        },
        "pet": {
            "speaker": "Blank",
            "text": "You pet Lyra. The best part of every morning",
            "options": [{"text": "Next", "next": None}]
        }
    },
    "calendar": {
        "start": {
            "speaker": "Blank",
            "text": "Your calendar. The 26th is circled.",
            "options": [{"text": "Exit", "next": None}]
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
            "options": [{"text": "Next", "next": None}]
        },
        "leave": {
            "speaker": "Maynne",
            "text": "I couldn't bring myself to eat them. My stomach turned at the thought.",
            "options": [{"text": "Next", "next": None}]
        }
    },
    "calendar": {
        "start": {
            "speaker": "Blank",
            "text": "It's the date. Why is it smudged?",
            "options": [{"text": "Next", "next": None}]
        }
    },
    "fridge": {
        "start": {
                "speaker": "Blank",
                "text": "The fridge. Your mother already made food, no need to make anything.",
                "options": [{"text": "Next", "next": None}]
            }
    },
    "bench": {
        "start": {
                "speaker": "Blank",
                "text": "It's a bench. No time to sit down.",
                "options": [{"text": "Next", "next": None}]
            }
    },
    "coat rack": {
        "start": {
                "speaker": "Blank",
                "text": "It's a coat rack.",
                "options": [{"text": "Next", "next": None}]
            }
    }

}

NEIGHBOURHOOD_DIALOGUE = {
    "Audra": {
        "start": {
            "speaker": "Audra",
            "text": "Hi, Maynne. I didn't see you at the study group yesterday.",
            "options": [{"text": "I'm sorry. I've been busy. (Apologize)", "next": "apologize"},
                        {"text": "And what of it? (Defensive)", "next": "defensive"}]
        },
        "apologize": {
            "speaker": "Maynne",
            "text": "I'm sorry, Audra. I haven't had much time lately. I will try to go to the next one.",
            "options": [{"text": "Continue", "next": "okay!"}]
        },
        "defensive": {
            "speaker": "Maynne",
            "text": "Why do you need to know? Get off my case, already. I was busy.",
            "options": [{"text": "Continue", "next": "oh..."}]
        },
        "okay!": {
            "speaker": "Audra",
            "text": "Don't worry about it. I'm just glad to see you doing alright. I'll see you at school!",
            "options": [{"text": "Exit", "next": None}]
        },
        "oh...": {
            "speaker": "Audra",
            "text": "Oh.. I'm sorry for asking, then. I'll see you later...",
            "options": [{"text": "Exit", "next": None}]
        }
    },
    "bus stop": {
            "start": {
                "speaker": "Blank",
                "text": "Taking the bus was typically quicker than walking.",
                "options": [{"text": "Go to school?", "next": "go to school"},
                            {"text": "Wait", "next": None}]
            },
            "go to school": {
                "speaker": "Blank",
                "text": "No reason to stay here.",
                "options": [{"text": "Continue", "next": None}]
            }
        }
}

CAMPUS_DIALOGUE = {
    "classroom": {
        "start": {
            "speaker": "Blank",
            "text": "Class is starting. The study group runs at the same time.",
            "options": [{"text": "Go to class. You will miss the study group if so.", "next": "go to class"},
                        {"text": "Wait", "next": None}]
        },
        "go to class": {
            "speaker": "Maynne",
            "text": "I should attend class.",
            "options": [{"text": "Continue", "next": None}]
        }
    },
    "study group": {
        "start": {
            "speaker": "Blank",
            "text": "The study group is starting. Class runs at the same time.",
            "options": [{"text": "Go to the study group. You will miss class if so.", "next": "go to study group"},
                        {"text": "Wait", "next": None}]
        },
        "go to study group": {
            "speaker": "Maynne",
            "text": "I should go to the study group.",
            "options": [{"text": "Continue", "next": None}]
        }
    },
    "roof": {
        "start": {
            "speaker": "Blank",
            "text": "Go to the roof? You will miss the study group and class.",
            "options": [{"text": "Go to the roof. Class and studying can wait.", "next": "go to roof"},
                        {"text": "Wait", "next": None}]
        },
        "go to roof": {
            "speaker": "Maynne",
            "text": "I will attend class and the study group tomorrow.",
            "options": [{"text": "Continue", "next": None}]
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
                "options": [{"text": "Next", "next": None}]
            },
            "ignore breakfast": {
                "speaker": "Maynne",
                "text": "...",
                "options": [{"text": "Next", "next": None}]
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