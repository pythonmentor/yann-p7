"""docs function sentence parsing"""
class SentenceParse:
        
    def in_lower_case(self, sentence):
	    self.sentence = str(sentence)   
	    return(self.sentence.lower())
	    
#METTRE TOUT EN MINUSCULE
#SUPPRIMER LES STOPS WORDS
#RETOURNER PHRASE NETTOYEE
