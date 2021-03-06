#!/usr/bin/python3
# -*- coding: Utf-8 -*
import requests

# -tc- éviter la forme d'import: from module import *
from config import *

import wikipediaapi

"""docs function sentence parsing"""
class SentenceParse:

    def __init__(self):
        "we initialize the attribute stop words"
        # -tc- mieux de mettre cette longue liste dans un fichier séparé
        self.stop_words = ["a","abord","absolument","afin","ah","ai","aie","ailleurs","ainsi","ait","allaient","allo","allons","allô","alors","anterieur","anterieure","anterieures","apres","après","as","assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","aupres","auquel","aura","auraient","aurait","auront","aussi","autre","autrefois","autrement","autres","autrui","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avoir","avons","ayant","b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","boum","bravo","brrr","c","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chacune","chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","comparable","comparables","compris","concernant","contre","couic","crac","d","da","dans","de","debout","dedans","dehors","deja","delà","depuis","dernier","derniere","derriere","derrière","des","desormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","different","differentes","differents","différent","différente","différentes","différents","dire","directe","directement","dit","dite","dits","divers","diverse","diverses","dix","dix-huit","dix-neuf","dix-sept","dixième","doit","doivent","donc","dont","douze","douzième","dring","du","duquel","durant","dès","désormais","e","effet","egale","egalement","egales","eh","elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre","envers","environ","es","est","et","etant","etc","etre","eu","euh","eux","eux-mêmes","exactement","excepté","extenso","exterieur","f","fais","faisaient","faisant","fait","façon","feront","fi","flac","floc","font","g","gens","h","ha","hein","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","hé","hélas","i","il","ils","importe","j","je","jusqu","jusque","juste","k","l","la","laisser","laquelle","las","le","lequel","les","lesquelles","lesquels","leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même","là","lès","m","ma","maint","maintenant","mais","malgre","malgré","maximale","me","meme","memes","merci","mes","mien","mienne","miennes","miens","mille","mince","minimale","moi","moi-meme","moi-même","moindres","moins","mon","moyennant","multiple","multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins","necessaire","necessairement","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notamment","notre","nous","nous-mêmes","nouveau","nul","néanmoins","nôtre","nôtres","o","oh","ohé","ollé","olé","on","ont","onze","onzième","ore","ou","ouf","ouias","oust","ouste","outre","ouvert","ouverte","ouverts","o|","où","p","paf","pan","par","parce","parfois","parle","parlent","parler","parmi","parseme","partant","particulier","particulière","particulièrement","pas","passé","pendant","pense","permet","personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","pire","plein","plouf","plus","plusieurs","plutôt","possessif","possessifs","possible","possibles","pouah","pour","pourquoi","pourrais","pourrait","pouvait","prealable","precisement","premier","première","premièrement","pres","probable","probante","procedant","proche","près","psitt","pu","puis","puisque","pur","pure","q","qu","quand","quant","quant-à-soi","quanta","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelqu'un","quelque","quelques","quels","qui","quiconque","quinze","quoi","quoique","r","rare","rarement","rares","relative","relativement","remarquable","rend","rendre","restant","reste","restent","restrictif","retour","revoici","revoilà","rien","s","sa","sacrebleu","sait","sans","sapristi","sauf","se","sein","seize","selon","semblable","semblaient","semble","semblent","sent","sept","septième","sera","seraient","serait","seront","ses","seul","seule","seulement","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous","souvent","specifique","specifiques","speculatif","stop","strictement","subtiles","suffisant","suffisante","suffit","suis","suit","suivant","suivante","suivantes","suivants","suivre","superpose","sur","surtout","t","ta","tac","tant","tardive","te","tel","telle","tellement","telles","tels","tenant","tend","tenir","tente","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutefois","toutes","treize","trente","tres","trois","troisième","troisièmement","trop","très","tsoin","tsouin","tu","té","u","un","une","unes","uniformement","unique","uniques","uns","v","va","vais","vas","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vous","vous-mêmes","vu","vé","vôtre","vôtres","w","x","y","z","zut","à","â","ça","ès","étaient","étais","était","étant","été","être","ô"]

        
    def in_lower_case(self, sentence):  
        "function that put the strings in lower case"
        self.sentence =str(sentence)
        self.sentence = self.sentence.lower() 
        return self.sentence
        
    def deleting_stop_words(self,sentence):
        "function that deletes the stop words"
        self.uncleaned_sentence = []
        self.sentence = str(sentence)
        for word in self.sentence.split():
            if word in self.stop_words:
                pass
            elif word == " ":
                pass
            else:
                self.uncleaned_sentence.append(word)
        self.new_sentence = " ".join(self.uncleaned_sentence)
        return(self.new_sentence)

    

    def deleting_special(self, sentence):
        "function that deletes the special character"
        self.sentence = str(sentence)
        intab = ",:?;.-"
        outtab ="      "
        trantab = str.maketrans(intab, outtab)
        self.sentence = self.sentence.translate(trantab)
        return self.sentence
     
        
    def deleting_several_spaces(self, sentence):
        "function that deletes spaces in case of double spaces"
        # -tc- et les triples espaces?
        self.sentence = str(sentence)
        self.sentence = self.sentence.replace("  ", " ")
        return(self.sentence)

    def returning_cleaned_sentence(self, sentence):
        "fucntion that return the sentence cleaned"
        self.sentence = str(sentence)
        self.sentence = self.in_lower_case(self.sentence)
        self.sentence = self.deleting_special(self.sentence)
        self.sentence = self.deleting_stop_words(self.sentence)
        self.sentence = self.deleting_several_spaces(self.sentence)
        return(self.sentence)
    
    def sending_to_api(self, sentence):
        "function that sends the sentence to google api"
        self.sentence = str(sentence)    
        self.url= "https://maps.googleapis.com/maps/api/geocode/json?address="+ self.sentence + "&key=" + KEY_API
        self.response = requests.get(self.url)
        self.response_json = self.response.json()
        # -tc- Attention: il y sura une erreur si google ne trouve rien
        self.address = (self.response_json["results"][0]["formatted_address"])
        self.lat = (self.response_json["results"][0]["geometry"]["location"]["lat"])
        self.lng = (self.response_json["results"][0]["geometry"]["location"]["lng"])
        self.search_around(self.lat, self.lng)
    
    def search_around(self, lat,lng):
        "search article around gps coordinates"
        self.lat = str(lat)
        self.lng = str(lng)
        self.url_geo = "https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=1000&gscoord=" + self.lat + "|" + self.lng +"&setformat=json&formatversion=2&format=json"
        self.resp = requests.get(self.url_geo)
        self.respo_json = self.resp.json()
        # -tc- quelle diff entre title et dist?
        self.title = (self.respo_json["query"]["geosearch"][0]["title"])
        self.dist = (self.respo_json["query"]["geosearch"][0]["title"])
        self.search_mediawiki(self.title, self.dist)

    # -tc- si de toute manière tu utilises un client python pour wikipedia
    # -tc- pourquoi ne pas en utiliser un qui fait directement le geosearch
    # -tc- également? exemple pymediawiki
    def search_mediawiki(self, title, dist):
        "function that looks up for article on wikipedia"
        self.title = str(title)
        wiki_wiki = wikipediaapi.Wikipedia('fr')
        self.page_py = wiki_wiki.page(self.title)
        self.result = self.page_py.summary
        ligne = self.result.split(".")
        i = 0
        for l in ligne:
            self.info = l
            i = i+1
            if i == 1:
                break
        if self.dist == 0:
            print("Mon petit loup t'ai je dèja raconté ce que ètait ce lieu?"" "+l+".")
        else:
            print("Mon petit loup sais tu que ce lieu est situé à coté d'un lieu très spécial:\n" + l + ".")



        




        


    
def main():
    pa = SentenceParse()
    text= "Courbevoie"
    pa.sending_to_api(text)
    print(pa.title)
main()
