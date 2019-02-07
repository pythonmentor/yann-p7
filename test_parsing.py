import parser.py as pars

#test if our function send a sentence in lower case
def test_in_lower_case():
	pa = pars.Sentence_pars()
	assert pa.in_lower_case("TEST") == "test"