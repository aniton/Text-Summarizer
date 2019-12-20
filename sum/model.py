# -*- coding: utf-8 -*-
import spacy
import textacy.extract
from collections import Counter as co


# Load the large English NLP app
nlp = spacy.load('en_core_web_lg')

string = """ Moscow (/ˈmɒskoʊ/, in US mainly: /ˈmɒskaʊ/;[10][11] Russian: Москва, tr. Moskvá, IPA: [mɐˈskva] (About this soundlisten)) is the capital and most populous city of Russia, with approximately 15.1 million residents within the city limits,[12] 17 million within the urban area[13] and 20 million within the metropolitan area[14][15]. Moscow is one of Russia's federal cities.

Moscow is a major political, economic, cultural, and scientific center of Russia and Eastern Europe, as well as the largest city (by area) on the European continent. By broader definitions, Moscow is among the world's largest cities, being the 14th largest metro area, the 18th largest agglomeration, the 14th largest urban area, and the 11th largest by population within city limits worldwide. According to Forbes 2013,[16] Moscow has been ranked as the ninth most expensive city in the world by Mercer and has one of the world's largest urban economies, being ranked as an alpha global city according to the Globalization and World Cities Research Network, and is also one of the fastest growing tourist destinations in the world according to the MasterCard Global Destination Cities Index.

Moscow is the northernmost and coldest megacity on Earth. It is home to the Ostankino Tower, the tallest free standing structure in Europe; the Federation Tower, the second-tallest skyscraper in Europe; and the Moscow International Business Center. By its territorial expansion on July 1, 2012 southwest into the Moscow Oblast, the area of the capital more than doubled, going from 1,091 to 2,511 square kilometers (421 to 970 sq mi), resulting in Moscow becoming the largest city on the European continent by area; it also gained an additional population of 233,000 people.[17][18]

Moscow is situated on the Moskva River in the Central Federal District of European Russia, making it Europe's most populated inland city. The city is well known for its architecture, particularly its historic buildings such as Saint Basil's Cathedral in Russian architectural style with a richly decorated and multicolored facade.[19][20] With over 40 percent of its territory covered by greenery, it is one of the greenest capitals and major cities in Europe and the world, having the largest forest in an urban area within its borders—more than any other major city—even before its expansion in 2012. The city has served as the capital of a progression of states, from the medieval Grand Duchy of Moscow and the subsequent Tsardom of Russia to the Russian Empire (for the short period of time taking that title from Saint Petersburg in 1728–1730) to the Soviet Union and the contemporary Russian Federation.

Moscow is a seat of power of the Government of Russia, being the site of the Moscow Kremlin, a medieval city-fortress that is today the residence for work of the President of Russia. The Moscow Kremlin and Red Square are also one of several World Heritage Sites in the city. Both chambers of the Russian parliament (the State Duma and the Federation Council) also sit in the city. Moscow is considered the center of Russian culture, having served as the home of Russian artists, scientists, and sports figures and because of the presence of museums, academic and political institutions and theatres.

The city is served by a transit network, which includes four international airports,[21] nine railway terminals, numerous trams, a monorail system and one of the deepest underground rapid transit systems in the world, the Moscow Metro, the fourth-largest in the world and largest outside Asia in terms of passenger numbers, and the busiest in Europe. It is recognized as one of the city's landmarks due to the rich architecture of its 222 stations.[22][citation needed]

Moscow has acquired a number of epithets, most referring to its size and preeminent status within the nation: The Third Rome (Третий Рим), the Whitestone One (Белокаменная), the First Throne (Первопрестольная), the Forty Soroks (Сорок Сороков) ("sorok" meaning both "forty, a great many" and "a district or parish" in Old Russian).

Moscow is also one of the twelve Hero Cities. The demonym for a Moscow resident is "москвич" (moskvich) for male or "москвичка" (moskvichka) for female, rendered in English as Muscovite.

The name "Moscow" is abbreviated "MSK" (МСК in Russian).

Although the Volga River was a place for adventurers and pirates in earlier times and became a destination for them, mainstream in Western Europe only had vague ideas about Moscow and other parts of today's European Russia until the first half of the second century and partly even beyond this time.[23][24]"""
topic = "Moscow"
def summarize(text, topic):
    # Parse the document with spaCy
    #doc = textacy.make_spacy_doc(text)
    doc = nlp(str(text))

    # Extract semi-structured statements
    entities = textacy.extract.entities(doc)


    summary = []
    ent = []
    accuracy = 100


    for entity in entities:
        ent.append(entity)

    split_it = str(ent).split()

    Counter = co(split_it)

    most_occur = Counter.most_common(1)[0][0].replace(',', '')
    if topic:
        statements = textacy.extract.semistructured_statements(doc, topic)
    else:
        statements = textacy.extract.semistructured_statements(doc, most_occur)

    print(most_occur)
    for statement in statements:
        summary.append(statement)

    return str(summary), accuracy
