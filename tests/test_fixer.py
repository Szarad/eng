import pytest

from eng import Fixer


@pytest.mark.parametrize('given, expected', [
    # string literal
    ('"centre"', '"center"'),
    ("'centre'", "'center'"),
    ('"center"', '"center"'),
    ('"center,"', '"center,"'),
    ('".center?"', '".center?"'),
    ('"this is the centre"', '"this is the center"'),
    ('"this is the centre of the world"', '"this is the center of the world"'),
    ('"centre of the world"', '"center of the world"'),

    # triple quotes
    ('"""centre"""', '"""center"""'),
    ("'''centre'''", "'''center'''"),
    ("'''\n this\n centre\n world\n'''", "'''\n this\n center\n world\n'''"),
    ("'''\n this\n centre of the\n world\n'''", "'''\n this\n center of the\n world\n'''"),
    ("'''\n this\n the centre\n world\n'''", "'''\n this\n the center\n world\n'''"),
    ("'''\n this\n the centre of the\n world\n'''", "'''\n this\n the center of the\n world\n'''"),
    ("'''\n this\n   the centre of the\n world\n'''", "'''\n this\n   the center of the\n world\n'''"),
])
def test_fixer(given: str, expected: str):
    fixer = Fixer(content=given)
    assert fixer.apply() == expected
