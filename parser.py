"""docs function sentence parsing"""
class SentenceParse:
        
    def in_lower_case(self, sentence):
	    self.sentence = str(sentence)   
	    return(self.sentence.lower())


#SUPPRIMER LES STOPS WORDS
#RETOURNER PHRASE NETTOYEE
