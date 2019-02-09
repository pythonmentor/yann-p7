import parser as script

#test if our function send a sentence in lower case
def test_in_lower_case():
	x = "TEST"
	pa = script.SentenceParse(x)
	assert pa.in_lower_case(x) == "test"


