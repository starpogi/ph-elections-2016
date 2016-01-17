import models.extended_types as extended_types
import data.candidates

from schematics import models
from schematics import types
from schematics.types import compound


class Candidate(models.Model):
    name = types.StringType()
    image = types.URLType()
    gender = extended_types.EnumType(data.candidates.Genders)


class MultipleChoice(models.Model):
    id = types.LongType()
    choice = types.StringType()


class Question(models.Model):
    question = types.StringType()
    choices = compound.ListType(compound.ModelType(MultipleChoice), default=[])
    selected_choice = compound.ModelType(MultipleChoice)
