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
    }
}