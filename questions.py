import collections
import models
import uuid

base_questions = collections.OrderedDict([
    ('first-time-rocker', models.Question({
        "question": "Are you a rocker?",
        "choices": [
            models.MultipleChoice({
                "choice": "Yes"
            }),
            models.MultipleChoice({
                "choice": "No"
            })
        ]
    })),
    ('question-2', models.Question({
        "question": "Are you also?",
        "choices": [
            models.MultipleChoice({
                "choice": "Maybe"
            }),
            models.MultipleChoice({
                "choice": "No"
            })
        ]
    }))
])
