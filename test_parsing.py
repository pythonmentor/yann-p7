import parser as script

#test if our function send a sentence in lower case
def test_in_lower_case():
	pa = script.SentenceParse()
	assert pa.in_lower_case("TEST") == "test"