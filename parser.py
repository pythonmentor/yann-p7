"""docs function sentence parsing"""
class SentenceParse:
        
    def in_lower_case(self, sentence):
        self.sentence = str(sentence)   
        return(self.sentence.lower())
        




def main():
    parse= SentenceParse()
    x= "JE ne suis pas beau"
    parse.in_lower_case(x)
    for word in parse.sentence:
        print(word)
main()
    
    

#SUPPRIMER LES STOPS WORDS
#RETOURNER PHRASE NETTOYEE
