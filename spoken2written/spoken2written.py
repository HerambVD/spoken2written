#!python -m spacy download en_core_web_sm
import spacy
import en_core_web_sm
from spacy.matcher import Matcher
from spacy.tokens import Span
#from pprint import pprint
from spacy import displacy
#from collections import Counter
from word2number import w2n



def StringMultiplier(para):
    nlp = spacy.load("en_core_web_sm")
    ans1=para.split()
    doc=nlp(para)
    matcher = Matcher(nlp.vocab)
    pattern = [{'LOWER': 'double', 'POS': 'ADJ'}, {'POS':{'NOT_IN': ['VERB','AUX','ADJ','PRON','ADV']}}]
    pattern1 = [{'LOWER': 'single', 'POS': 'ADJ'}, {'POS':{'NOT_IN': ['VERB','AUX','ADJ','PRON','ADV']}}]
    pattern2 = [{'LOWER': 'triple', 'POS': 'ADJ'}, {'POS':{'NOT_IN': ['VERB','AUX','ADJ','PRON','ADV']}}]
    pattern3 = [{'LOWER': 'quadruple', 'POS': 'ADJ'}, {'POS':{'NOT_IN': ['VERB','AUX','ADJ','PRON','ADV']}}]
    matcher.add("Matching", None, pattern)
    matcher.add("Matching", None, pattern1)
    matcher.add("Matching", None, pattern2)
    matcher.add("Matching", None, pattern3)

    matches = matcher(doc)

    index=[]
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  
        span = doc[start:end]
        #print(match_id, string_id, start, end, span.text)
        index.append([start,end,span.text])
   
    #print(match_id, string_id, start, end, span.text)
    index1=[]    
    for i in range(len(index)):
        index1.append(index[i][0]-i)
        beg=index[i][0]
        last=index[i][1]
        value=str(index[i][2])
        m1=value.split()
        if m1[0]=="double":
            ans1[last-1]=2*ans1[last-1]
        elif m1[0]=="triple":
            ans1[last-1]=3*ans1[last-1]
        elif m1[0]=="quadruple":
            ans1[last-1]=3*ans1[last-1]
        else:
            ans1=ans1
    #print(beg,last,value)

    for z in index1:
        del ans1[z]

    ans1=(' '.join(ans1))
    return ans1






def QuantityMoneyTranslator(para):
    nlp = en_core_web_sm.load()
    #nlp1= spacy.load('en')

    #text='European authorities fined Google a record sixty five million dollars on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices. Furthermore, My weight was thirty five kilograms in 2018. A chocolate costs six dollars.'
    #text1='C M of Maharashtra spent two thousand and fouty two dollars.'
    doc = nlp(para)

    #pprint([(X.text, X.pos_) for X in doc])
    #pprint([(X.text, X.label_) for X in doc.ents])

    #pprint([[X, X.ent_iob_, X.ent_type_] for X in doc])


    currency=["dollars", "dollar", "euro", "euros", "yens", "yen", "rupee", "rupees", "pound", "pounds"]
    quantity=["pounds","kilograms","grams"]

    ls_money=[]
    ls_no=[]
    ls_quan=[]
    for X in doc.ents:
        if X.label_ =='MONEY':
            ls_money.append(str(X))
        
    for X in doc:
        if X.ent_type_ =='CARDINAL':
            ls_no.append(str(X))
        
    for X in doc.ents:
        if X.label_ == X.label_ =='QUANTITY':
            ls_quan.append(str(X))
      
#dollar value conversion
    number=[]
    money=[]
    quan=[]
    for a in ls_money:
        a=a.lower()
        a=a.split()
        b=[word for word in a if word in set(currency)]
        b=' '.join(b)
        if b=="dollars" or b=="dollar":
            symbol="$"
        elif b=="euros" or b=="euro":
            symbol="€"
        elif b=="yens" or b=="yen":
            symbol="¥"
        elif b=="pound" or b=="pounds":
            symbol="£"
        else:
            symbol=""
        a=[word for word in a if word not in set(currency)]
        a=' '.join(a)
        p=symbol+str(w2n.word_to_num(a))
        money.append(p)
    
    for a in ls_no:
        number.append(str(w2n.word_to_num(a)))
    
    for a in ls_quan:
        a=a.lower()
        a=a.split()
        b=[word for word in a if word in set(quantity)]
        b=' '.join(b)
        if b=="pounds":
            symbol=" lbs"
        elif b=="kilograms":
            symbol=" kg"
        elif b=="grams":
            symbol=" gm"
        else:
            symbol=""
        a=[word for word in a if word not in set(quantity)]
        a=' '.join(a)
        quan.append(str(str(w2n.word_to_num(a))+symbol))
    
    
    j=0
    final_str_spacyv1= []
    for Y in doc:
        if Y.ent_iob_ =='B' and Y.ent_type_ =='QUANTITY':
            final_str_spacyv1.append(str(quan[j]))
            j=j+1
        elif Y.ent_iob_ =='I' and Y.ent_type_ =='QUANTITY':
            final_str_spacyv1=final_str_spacyv1
        else:
            final_str_spacyv1.append(str(Y))
        
    ans=' '.join(final_str_spacyv1)

    doc=ans
    doc=nlp(doc)

    k=0
    final_str_spacy=[]
    for Y in doc:
        if Y.ent_iob_ =='B' and Y.ent_type_ =='MONEY':
            final_str_spacy.append(str(money[k]))
            k=k+1
        elif Y.ent_iob_ =='I' and Y.ent_type_ =='MONEY':
            final_str_spacy=final_str_spacy
        else:
            final_str_spacy.append(str(Y))
        
    ans=' '.join(final_str_spacy)
    return ans


def TextTranslator(para):
    return QuantityMoneyTranslator(StringMultiplier(para))

   
#!python -m spacy download en_cire_web_sm