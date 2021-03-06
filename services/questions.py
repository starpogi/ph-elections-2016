import data.questions

def get_questions(question_list=data.questions.base_questions):
    """
    Gets all the available question ids

    :return: List of question keys
    :rtype: list
    """
    return list(question_list.keys())

def get_question(qid, question_list=data.questions.base_questions):
    """
    Gets actual question

    :param qid: Question ID in the form of the base_questions key
    :return: Question Model
    :rtype: models.Question
    """
    base_question = question_list.get(qid)
    with_index = set_ids(base_question)

    return with_index

def set_ids(question):
    """
    Sets the choice ids based on index for each choice
    """
    for index, choice in enumerate(question.choices):
        choice.id = index

    return question

def set_choice(qid, selected_choice, question_list=data.questions.base_questions):
    """
    Sets the choice for a question

    :param qid: Question ID in the form of the base_questions key
    :param selected_choice: Choice that is selected
    """
    question_list[qid].selected_choice = selected_choice

def get_next_question(qid, question_list=data.questions.base_questions):
    """
    Gets the next question

    :param qid: Question ID in the form of the base_questions key
    :return: Next Question ID
    :rtype: string
    :raises: IndexError if at the last question
    """
    all_questions = get_questions(question_list=question_list)
    return all_questions[get_index(qid, question_list=question_list) + 1]

def get_index(qid, question_list=data.questions.base_questions):
    """
    Get index of question
    """
    all_questions = get_questions(question_list=question_list)
    qid_index = all_questions.index(qid)
    return qid_index

def get_selected_choice(selected_choice_id, question):
    selected_choice = [
        choice for choice in question.choices
        if choice.id == int(selected_choice_id)
    ]

    if not selected_choice:
        return None

    return selected_choice[-1]
