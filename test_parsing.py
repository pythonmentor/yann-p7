import parser as script




#test if our function send a sentence in lower case
def test_in_lower_case():
	x = "TEST"
	pa = script.SentenceParse()
	assert pa.in_lower_case(x) == "test"



def test_deleting_stop_words():
    useless_sentence = "afin ailleurss test"
    pa = script.SentenceParse()
    assert pa.deleting_stop_words(useless_sentence) == "test"



