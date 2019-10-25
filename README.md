# Spoken English to Written English translator

There exits a difference between how we write and how we speak. e.g While speaking we say "I paid twenty thousand dollars to xyz organization". But, we don't write above example as it is, instead we write it as "I paid $20000 to xyz organization."
This is a python module is to translates such spoken english language to its written form.

e.g. It will translate: "I watched movie named triple H ." to "I watched movie named HHH"
                        "My weight is fifty five kilograms ." to "My weight is 55 kg"
                        "I paid twenty thousand dollars to xyz organization ." to "I paid $20000 to xyz organization ."
                        
<h1>Installation guide</h1>

Run this command in terminal:
```
pip install spoken2written
```
The dependencies spaCy,word2number will also be installed after installing the package.
It is better to have english language dependency requirement of spacy which is en_core_web_sm

To install this en_core_web_sm, run following command in terminal
```
python -m spacy download en_core_web_sm
```
<h1>Usage</h1>

First you have to import the module using the below code.
```
import spoken2written
```
If it shows error during importing then spacy english dependency package is not installed in your device. In this case,
install en_core_web_sm library using the command mentioned above.

After importing the package use TextTraslator method to translate spoken English to written form.

Example script:
```
>>>from spoken2written import TextTranslator
...test= "My life is triple B . European authorities fined Google a record sixty five thousand dollars on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices . Furthermore , My T - Shirt size is double X in 2019 and it costs six dollars . My weight is fifty kilograms ."
...result=TextTranslator(test)
...print(result)
```
Output:
```
My life is BBB . European authorities fined Google a record $65000 on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices . Furthermore , My T - Shirt size is XX in 2019 and it costs $6 . My weight is 50 kg .
```

<h1>Features Used to Develop this package</h1>

1. Name Entity Recognition technique is used to detect entities from given input. Name Entity Recognition is done using the library named 'spaCy'. Entities such as QUANTITY (E.g weight: fifty kilograms), MONEY(e.g. amount: thousand dollars), PROPER NOUNS are detected using this technique.

2. The package word2number is used to convert numbers written as 'two thousand' to '2000'. Furthermore, few lines of logical code adds suffix/prefix as $/kg,etc. depending upon type of entity.

3. In some texts entity such as"double X" may occur. In this case, the word double acts as adjective followed by X as noun. To detect such texts along with their corresponding parts of speech spacy Token Matcher is used. Again, after detection of entity few lines of logical code will translate "double X" to "XX".

<b>The logical code for all functions in this package could be found in file spoken2written/spoken2written/spoken2written.py of this repository</b>

<h1>Bugs/ Errors</h1>
Please ensure that you have installed dependency en_core_web_sm of spacy before importing package written2spoken. If you find any bugs/errors in the usage of above code, please raise an issue through <a href="https://github.com/HerambVD/spoken2written">GitHub</a>. Else, send an email to <a href="mailto:heramb1711@gmail.com">heramb1711@gmail.com</a>.
