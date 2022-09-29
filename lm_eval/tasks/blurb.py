"""
2022.09.25
N. Seelam

This path tests the `bigbio` version of Biosses We generate prompts

"""
from lm_eval.api.task import PromptSourceTask

_CITATION = """"""


class BlurbGeneral(PromptSourceTask):

    DATASET_PATH = "bigscience-biomedical/blurb"
    DATASET_NAME = None

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


class BlurbBC2GM(BlurbGeneral):
    DATASET_NAME = "bc2gm"


class BlurbBC5Chem(BlurbGeneral):
    DATASET_NAME = "bc5chem"


class BlurbBC5Disease(BlurbGeneral):
    DATASET_NAME = "bc5disease"


class BlurbJNLPBA(BlurbGeneral):
    DATASET_NAME = "jnlpba"


class BlurbNCBIDisease(BlurbGeneral):
    DATASET_NAME = "ncbi_disease"
