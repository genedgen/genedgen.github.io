"""
Gen-Ed Name Generator
By: Gal Koplewitz, Harvard College '17
May 2017

"""


import random
"""
### Aesthetic and Interpretive Understanding ###
cultural [practices]
[Practice] as [Academic word]
Narratives of []
[]: A [] reading of []
The Evolution of []
How and what [person] learned to read: The Rise of [jargon] Literary culture in the 19th century
[jargon] for [science professions]

poems, poets, poetry. Teeth, dentists, dentistry. 
The ____ Imagination: Visions, Dreams and Prophecies
Back Roads to Far Places: Literature of Journey and Quest


### Culture and Belief ###


Monuments of [Religion] [Silly Practice] (Monuments of Jewish Pedagogy; Monuments of Farsi counterpunct)
[The Contested Bible: The Sacred-Secular Dance]
[Human Being and the Sacred in the History of the West]
Performance, Tradition and Cultural Studies: An Introduction to Folklore and Mythology
Institutional Violence and Public Spectacle: The Case of the Roman Games
Understanding Islam and Contemporary Muslim Societies
Reason and Faith in the West
Pathways through the Andes - Culture, History, and Beliefs in Andean South America
The Ancient Greek Hero
From the Hebrew Bible to Judaism, From the Old Testament to Christianity
[Among the Nations: Jewish History in Pagan, Christian and Muslim Context]
Studying Buddhism, Across Place and Time
Saints, Heretics, and Atheists: An Historical Introduction to the Philosophy of Religion
Communism and the Politics of Culture: Czechoslovakia from World War II to the Velvet Revolution
[The American Evangelical Tradition from Jonathan Edwards to Jerry Falwell]
Sacred and Secular Poetry
Animated Spirituality: Japanese Religion in Anime, Manga, and Film
[Athens, Rome, and Us: Questions of Identity]
Religion in India: Texts and Traditions in a Complex Society
[The Empire Strikes Back: Science Fiction, Religion, and Society]


### US in the World ###
[practices] and Society in America
The Evolution of American []
[Hot Button Topic]: Pros and Cons
[jargon_2] [practice] and [f_father]
American []: A Global History
[The Theory and Practice of Republican [practice]]
Reinventing (and Reimagining) [us_event]: The Changing American [jarg_1] Myth


[American Encounters: Art, Contact, and Conflict, 1560-1860]

Sex and the Citizen: Race, Gender, and Belonging in the United States
Designing the []:

### Societies of the World ###
[practices] without borders
[practices] as Global popular culture
Forbidden [practices] in Modern [Place]
[practice] Between East and West
[jargon] [place]: Past, Present, Future
[place]'s [jarg_1] Samurai [jarg_2]
[place] on Trial: Retribution, Reconciliation, and [practices] Since [year_1]
[[person]'s [place]: Then and Now]
Case Studies in Global [practices]: [jargon_1] Perspectives


"""

# Dictionaries to use
practices = ["Masturbation", "Ineptitude", "Sodomy", "Colonoscopies","Bird Watching", "Hamster Breeding", "Fingering",
				"Dog Walking", "Chocolate-Making", "Dissemination", "Retribution"]
places = ["Ulaanbaatar", "Paris", "Tokyo", "Beijing", "Jerusalem", "Sao Paulo", "Madrid", "China", "France", "Vietnam", "Papua New Guinea",
			"Japan", "Russia", "Moscow", "Korea", "Norway", "Europe", "Cuba", "Mexico", "Czechoslovakia"]
jargon_1 = ["Imperialist", "Freudian", "Marxist", "Feminist", "Hermeneutical", "Capitalist", "Nazi", "Colonial", "Disruptive", "Postcolonial",
				"Postwar", "Revolutionary", "Biosocial", "Socialist", "Contested", "Secular", "Performative", "Non-binary", "Communist"]
jargon_2 = ["Hegemony", "Fiction", "Pedagogy", "Myth", "Hermeneutics", "Diasporas", "Masturbation", "Phenomenology", "Injustice", "Modernities",
				"Othering", "Dissemination", "Justice", "Aspirations", "Poetry", "Landscapes", "Encounters", "Revelations", "Religiosity", "Gender"]
times = ["Primitive", "Ancient", "Modern", "Contemporary", "16th-Century", "17th-Century", "18th-Century", "Medieval"]
religions = ["Christianity", "Judaism", "Buddhism", "Islam", "Paganism", "Hinduism", "Evangelism"]

# people
ancient_people = ["Moses","Maimonides","Julius Caesar", "Jesus", "Genghis Khan", "King David", "Henry VIII", "Dante", "Chaucer", "Moctezuma"]
celebs = ["Boy George", "Guy Fieri", "Tony Danza", "Hillary Clinton", "Bill Murray", "Mike Pence", "Paul Krugman", "Kim Kardashian", "Selena Gomez", "Tupac"]
authors = ["Shakespeare", "J. K. Rowling", "Umberto Eco", "Amos Oz", "Dante"]
harvard_people = ["Harvey Mansfield", "Greg Mankiw", "Homi Bhabha", "Michael Sandel","Drew Faust", "Dean Khurana", "Stephen Greenblatt",
					"Judith Butler", "Alan Dershowitz", "Cornel West", "John Stilgoe", "Harry Lewis", "Amartya Sen"]
mix = ancient_people + celebs + authors + harvard_people

# US Dictionaries
f_fathers = ["Thomas Jefferson", "James Madison", "Alexander Hamilton", "John Quincy Adams", "George Washington", "Benjamin Franklin"]
us_events = ["The Civil War", "World War I", "World War II", "The American Revolution", "The Civil Rights Movement", "The Great Depression", 
				"The Trail of Tears", "The Boston Tea Party", "Seneca Falls", "The Civil Rights Movement", "9/11", "The Gilded Age"]
us_topics = ["Abortion", "Illegal Immigration", "McCarthyism", "Slavery"]

# Culture and Belief Dictionaries
books = ["Bible", "Koran", "New Testament"]
peoples = ["Hebrew", "Christian", "Muslim", "Atheist", "Jedi", "Evangelical"]
terms = ["Sacred", "Secular", "Atheist"]

# Science Dictionaries
technical = ["Machine Learning", "3D Printing", "Gene Editing", "Artificial Intelligence", "Chemical Engineering"]
chemistry = ["Quarks", "Atoms", "Nitrogen", "Oxygen"]
science_professions = ["Spinal Surgeons", "Software Engineers", "Oil Diggers", "Consultants"]
arts_professions = ["Poets","Playwrights"]



# aesthint sentence types
type_1 = ["Narratives of %s", "The Evolution of %s"]
type_2 = ["%s as %s %s"]
type_3 = ["%s %s in the 17th century", "%s %s in the 15th century", "%s %s in the 16th century", "%s %s in the 18th century"]
type_4 = ["%s: From %s to %s"]
type_5 = ["%s: A %s Reading of %s"]
type_6 = ["How and What %s Learned to Read: The Rise of %s Literary Culture"]
type_7 = ["%s for %s"]

# cultbelief sentence types
type_10 = ["%s as Global Popular Culture", "%s Between East and West"]
type_11 = ["A %s Reading of the %s", "The %s %s"]
type_12 = [""]

# us-world sentence types
type_20 = ["%s and Society in America", "The Evolution of American %s", "American %s: A Global History", "The Theory and Practice of Republican %s", "%s in America: A History"]
type_21 = ["%s: from %s to %s"]
type_22 = ["%s: Pros and Cons"]
type_23 = ["%s and Contemporary %s in the United States"]
type_24 = ["%s %s and %s"]
type_25 = ["Reinventing (and Reimagining) %s: The Changing American %s Myth"]

# socworld sentence types
type_30 = ["%s without Borders", "%s Between East and West", "%s as Global Popular Culture", "Russian %s in Global Perspective"]
type_31 = ["Forbidden %s in %s %s"]
type_32 = ["%s %s: Past, Present, Future"]
type_33 = ["%s's %s Samurai %s"]
type_34 = ["%s on Trial: Retribution, Reconciliation and %s Since %s"]
type_35 = ["%s's %s: Then and Now"]
type_36 = ["Case Studies in Global %s: %s Perspectives"]

# sentence lists, for different gen-eds
aesthint_sentence_types = [type_1, type_2, type_3, type_4, type_5, type_1, type_6, type_7]
cultbelief_sentence_types = [type_10, type_11, type_12]
usworld_sentence_types = [type_20, type_20, type_20, type_21, type_22, type_23, type_24, type_25]
socworld_sentence_types = [type_30, type_30, type_31, type_32, type_33, type_34, type_35, type_36]

# generative functions for each gen-ed category
def aesthint(place, practice, jarg_1, jarg_2, ancient, harvard, time, person, science):
	# Choose specific template at random
	sentence_type = random.choice(aesthint_sentence_types)
	sentence = random.choice(sentence_type)
	prefix = "AESTHINT " + str(random.randint(0,100)) + ": "
	sentence = prefix + sentence
	# Within template, choose word combination at random
	if sentence_type == type_1:
		print(sentence % practice)
	elif sentence_type == type_2:
		print(sentence % (practice, jarg_1, jarg_2))
	elif sentence_type == type_3:
		print(sentence % (jarg_1, practice))
	elif sentence_type == type_4:
		print(sentence % (practice, ancient, harvard))
	elif sentence_type == type_5:
		print(sentence % (practice, jarg_1, harvard))
	elif sentence_type == type_6:
		print(sentence % (person, jarg_1))
	elif sentence_type == type_7:
		print(sentence % (jarg_2, science))
	return None

def cultblf(place, practice, jarg_1, jarg_2, ancient, harvard, time, religion, book):
	# Choose specific template at random
	sentence_type = random.choice(cultbelief_sentence_types)
	sentence = random.choice(sentence_type)
	prefix = "CULTBLF " + str(random.randint(0,100)) + ": "
	sentence = prefix + sentence
	# Within template, choose word combination at random
	if sentence_type == type_10:
		print(sentence % practice)
	if sentence_type == type_11:
		print(sentence % (jarg_1, book))


def usworld(place, practice, jarg_1, jarg_2, ancient, harvard, time, religion, us_event, us_topic, author, celeb, father):
	# Choose specific template at random
	sentence_type = random.choice(usworld_sentence_types)
	sentence = random.choice(sentence_type)
	prefix = "US-WORLD " + str(random.randint(0,100)) + ": "
	sentence = prefix + sentence
	# Within template, choose word combination at random
	if sentence_type == type_20:
		print(sentence % practice)
	elif sentence_type == type_21:
		print(sentence % (us_topic, father, celeb))
	elif sentence_type == type_22:
		print(sentence % us_topic)
	elif sentence_type == type_23:
		print(sentence % (practice, religion))
	elif sentence_type == type_24:
		print(sentence % (jarg_1, practice, father))
	elif sentence_type == type_25:
		print(sentence % (us_event, jarg_1))

def socworld(place, practice, jarg_1, jarg_2, ancient, harvard, time, religion, us_event, us_topic, author, celeb, father,year_1,year_2, person):
	# Choose specific template at random
	sentence_type = random.choice(socworld_sentence_types)
	sentence = random.choice(sentence_type)
	prefix = "SOCWORLD " + str(random.randint(0,100)) + ": "
	sentence = prefix + sentence
	# Within template, choose word combination at random
	if sentence_type == type_30:
		print(sentence % practice)
	elif sentence_type == type_31:
		print(sentence % (practice, time, place))
	elif sentence_type == type_32:
		print(sentence % (jarg_1, place))
	elif sentence_type == type_33:
		print(sentence % (place, jarg_1, jarg_2))
	elif sentence_type == type_34:
		print(sentence % (place, practice, year_1))
	elif sentence_type == type_35:
		print(sentence % (person, place))
	elif sentence_type == type_36:
		print(sentence % (practice, jarg_1))
def generate():
	# generate random word for each slot
	place = random.choice(places)
	practice = random.choice(practices)
	jarg_1 = random.choice(jargon_1)
	jarg_2 = random.choice(jargon_2)
	ancient = random.choice(ancient_people)
	harvard = random.choice(harvard_people)
	time = random.choice(times)
	religion = random.choice(religions)
	person = random.choice(mix)
	science = random.choice(science_professions)
	us_event = random.choice(us_events)
	author = random.choice(authors)
	celeb = random.choice(celebs)
	us_topic = random.choice(us_topics)
	father = random.choice(f_fathers)
	year_1 = random.randint(1400,2015)
	year_2 = str(random.randint(year_1 + 1,2017))
	year_1 = str(year_1)
	book = random.choice(books)
	# choose specific type of Gen Ed at random, and run it
	# choose at random
		# TODO
	#aesthint(place, practice, jarg_1, jarg_2, ancient, harvard, time, person, science)
	# cultblf(place, practice, jarg_1, jarg_2, ancient, harvard, time, religion, book)
	# 
	#print()
	usworld(place, practice, jarg_1, jarg_2, ancient, harvard, time, religion, us_event, us_topic,author, celeb, father)
	# socworld(place, practice, jarg_1, jarg_2, ancient, harvard, time, religion, us_event, us_topic,author, celeb, father,year_1,year_2, person)
# test
for i in range(5):
	generate()
