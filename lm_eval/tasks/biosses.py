"""
2022.09.25
N. Seelam

This path tests the `bigbio` version of Biosses We generate prompts

"""
from lm_eval.api.task import PromptSourceTask

_CITATION = """"""


class Biosses(PromptSourceTask):

    DATASET_PATH = "bigscience-biomedical/biosses"
    DATASET_NAME = "biosses_bigbio_pairs"

    def has_training_docs(self):
        return True

    def has_validation_docs(self):
        return True

    def has_test_docs(self):
        return True

    def training_docs(self):
        if self.has_training_docs():
            return self.dataset["train"]

    def validation_docs(self):
        if self.has_validation_docs():
            return self.dataset["validation"]

    def test_docs(self):
        if self.has_test_docs():
            return self.dataset["test"]
