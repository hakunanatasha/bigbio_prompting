"""
2022.09.25
N. Seelam

This path tests the `bigbio` version of MedNLI;

"""
from lm_eval.api.task import PromptSourceTask

_CITATION = """"""


class MedNLI(PromptSourceTask):

    DATASET_PATH = "bigscience-biomedical/mednli"
    DATASET_NAME = "mednli_bigbio_te"

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
