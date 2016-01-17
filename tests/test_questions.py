import unittest
import collections

import models.base
import services.questions

class TestQuestions(unittest.TestCase):

    test_questions = collections.OrderedDict([
        ('question-1', models.base.Question({
            "question": "Are you a rocker?",
            "choices": [
                models.base.MultipleChoice({
                    "choice": "Yes"
                }),
                models.base.MultipleChoice({
                    "choice": "No"
                }),
                models.base.MultipleChoice({
                    "choice": "Maybe"
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

    def test_question_keys(self):
        question_list = services.questions.get_questions(
            question_list=self.test_questions
        )
        self.assertListEqual(question_list, ['question-1', 'question-2'])

    def test_get_question(self):
        question_1 = self.test_questions['question-1']

        question = services.questions.get_question(
            'question-1',
            question_list=self.test_questions
        )

        self.assertEqual(question, question_1)

    def test_set_ids(self):
        question = services.questions.get_question(
            'question-1',
            question_list=self.test_questions
        )

        question_with_index = services.questions.set_ids(question)

        for index, choice in enumerate(question_with_index.choices):
            self.assertEqual(index, choice.id)

    def test_set_choice(self):
        chosen_choice = self.test_questions['question-1'].choices[1]

        services.questions.set_choice(
            'question-1',
            chosen_choice,
            question_list=self.test_questions
        )

        self.assertEqual(chosen_choice, self.test_questions['question-1'].selected_choice)

    def test_get_next_question(self):
        self.assertEqual(
            services.questions.get_next_question('question-1', question_list=self.test_questions),
            'question-2'
        )

        with self.assertRaises(IndexError):
            services.questions.get_next_question('question-2', question_list=self.test_questions)

        with self.assertRaises(ValueError):
            services.questions.get_next_question('question-3', question_list=self.test_questions)


    def test_get_index(self):
        self.assertEqual(
            services.questions.get_index('question-1', question_list=self.test_questions),
            0
        )
        self.assertEqual(
            services.questions.get_index('question-2', question_list=self.test_questions),
            1
        )

        with self.assertRaises(ValueError):
            services.questions.get_index('question-3', question_list=self.test_questions)

    def test_get_choice(self):
        chosen_choice = self.test_questions['question-1'].choices[1]

        question = services.questions.set_ids(
            self.test_questions['question-1']
        )

        selected_choice = services.questions.get_selected_choice(
            '1',
            question
        )

        self.assertEqual(chosen_choice, selected_choice)
