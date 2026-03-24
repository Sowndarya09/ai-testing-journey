from deepeval import assert_test
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import GEval

def test_answer_relevancy():
    test_case = LLMTestCase(
        input="What is Playwright?",
        actual_output="Playwright is a testing framework by Microsoft for browser automation.",
    )
    
    correctness_metric = GEval(
        name="Correctness",
        criteria="Check if output mentions Microsoft and browser testing",
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT],
    )
    
    assert_test(test_case, [correctness_metric])