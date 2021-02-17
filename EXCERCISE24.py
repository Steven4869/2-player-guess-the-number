#SEARCH ENGINE
"""
TO MAKE A PROGRAM WHERE DIFFERENT SENTENCES ARE THERE, INPUT MUST BE GIVEN AND IT WILL SHOW
ALL THE RELATED SEARCH
FOR EXAMPLE
SENTENCE: "ATTACK ON TITAN IS GOOD","EREN IS GREAT","ARMIN IS HIS BEST FRIEND","EREN LIKES FREEDOM"
INPUT :
PLEASE ENTER THE STRING
EREN
OUTPUT:
2 RESULTS ARE FOUND
"EREN IS GREAT"
"EREN LIKES FREEDOM"
"""
print("WELCOME TO SEARCH")
def matchword(sentence1,sentence2):
    words1=sentence1.split(" ")
    words2=sentence2.split(" ")
    score=0
    for word1 in words1:
        for word2 in words2:
            if word1.lower()==word2.lower():
                score+=1
    return score
if __name__=="__main__":
    sentences=["ATTACK ON TITAN IS GOOD","EREN IS GREAT","ARMIN IS GOOD","EREN LIKES FREEDOM"]
    query=input("please enter your word\n")
    scores=[matchword(query,sentence) for sentence in sentences]
    sortedscore=[sentscore for sentscore in sorted(zip(scores,sentences))]
    print(f"{len(sortedscore)} results found")
    for score,item in sortedscore:
        print(f"\"{item}\": with score of {score}")
