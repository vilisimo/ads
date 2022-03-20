import pytest

from leetcode.easy.ex0020 import Solution


@pytest.mark.parametrize('input', [
	'()',
	'()[]{}',
	'(())',
	'([{}])',
	'([[{[[]]}]])',
])
def test_recognizes_valid_parentheses(input: str):
	assert Solution().isValid(input)


@pytest.mark.parametrize('input', [
	'(]',
	'[)',
	'[}',
	'(({]}))',
	'(])(',
	'][',
	')',
	'[',
	'{{',
	'())',
	'()))',
])
def test_recognizes_invalid_parentheses(input: str):
	assert not Solution().isValid(input)