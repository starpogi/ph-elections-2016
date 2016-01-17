import collections
import models.base

base_questions = collections.OrderedDict([
    ('first-time-rocker', models.base.Question({
        "question": "Are you a rocker?",
        "choices": [
            models.base.MultipleChoice({
                "choice": "Yes"
            }),
            models.base.MultipleChoice({
                "choice": "No"
            })
        ]
    })),
    ('question-2', models.base.Question({
        "question": "Are you also?",
        "choices": [
            models.base.MultipleChoice({
                "choice": "Maybe"
            }),
            models.base.MultipleChoice({
                "choice": "No"
            })
        ]
    }))
])
