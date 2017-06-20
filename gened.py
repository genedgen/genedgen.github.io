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
[jarg_1] [practice] and Public Spectacle: The Case of the Roman Games

poems, poets, poetry. Teeth, dentists, dentistry. 
The ____ Imagination: Visions, Dreams and Prophecies
Back Roads to Far Places: Literature of Journey and Quest


### Culture and Belief ###
Monuments of [Religion] [Silly Practice]
[The [jarg_1] [book]]: A Sacred-Secular Dance
[practice], Tradition and Cultural Studies: An Introduction to [religion]
Understanding [religion] and Contemporary [jarg_1] Societies
[jarg_2] and the Politics of Culture: [Place] from [us_event] to the Velvet Revolution
Animated Spirituality: The [] Manga


Studying Buddhism, Across Place and Time
Saints, Heretics, and Atheists: An Historical Introduction to the Philosophy of Religion
[The American Evangelical Tradition from Jonathan Edwards to Jerry Falwell]
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
practices = ["Ineptitude", "Sodomy", "Colonoscopies","Bird Watching", "Hamster Breeding",
				"Dog Walking", "Chocolate-Making", "Dissemination", "Retribution", "Puberty", "Profanities"]
places = ["Ulaanbaatar", "Paris", "Tokyo", "Beijing", "Jerusalem", "Sao Paulo", "Madrid", "China", "France", "Vietnam", "Papua New Guinea",
			"Japan", "Russia", "Moscow", "Korea", "Norway", "Europe", "Cuba", "Mexico", "Czechoslovakia", "Costa Rica"]
jargon_1 = ["Imperialist", "Freudian", "Marxist", "Feminist", "Hermeneutical", "Capitalist", "Nazi", "Colonial", "Disruptive", "Postcolonial",
				"Postwar", "Revolutionary", "Biosocial", "Socialist", "Contested", "Secular", "Performative", "Non-binary", "Communist", "Neodialectic",
				"Adolescent", "Institutional", "Erotic", "Fascist", "Sensual", "Baudrillardist"]
jargon_2 = ["Hegemony", "Fiction", "Pedagogy", "Myth", "Hermeneutics", "Diasporas", "Phenomenology", "Injustice", "Modernities",
				"Othering", "Dissemination", "Justice", "Aspirations", "Poetry", "Landscapes", "Encounters", "Revelations", "Religiosity", "Gender",
				"Deappropriations"]
times = ["Primitive", "Ancient", "Modern", "Contemporary", "16th-Century", "17th-Century", "18th-Century", "Medieval"]
religions = ["Christianity", "Judaism", "Buddhism", "Islam", "Paganism", "Hinduism", "Evangelism", "Catholicism", "Hinduism", "Atheism", "Agnosticism"]

# people
ancient_people = ["Moses","Maimonides","Julius Caesar", "Jesus", "Genghis Khan", "King David", "Henry VIII", "Dante", "Chaucer", "Moctezuma", "Mussolini"]
celebs = ["Boy George", "Guy Fieri", "Tony Danza", "Hillary Clinton", "Bill Murray", "Mike Pence", "Paul Krugman", "Kim Kardashian", "Selena Gomez", "Tupac",
			"Salman Rushdie", "Quentin Tarantino", "Hayao Miyazaki"]
authors = ["Shakespeare", "J. K. Rowling", "Umberto Eco", "Amos Oz", "Dante", "Joyce"]
harvard_people = ["Harvey Mansfield", "Greg Mankiw", "Homi Bhabha", "Michael Sandel","Drew Faust", "Dean Khurana", "Stephen Greenblatt",
					"Judith Butler", "Alan Dershowitz", "Cornel West", "John Stilgoe", "Harry Lewis", "Amartya Sen"]
mix = ancient_people + celebs + authors + harvard_people

# US Dictionaries
f_fathers = ["Thomas Jefferson", "James Madison", "Alexander Hamilton", "John Quincy Adams", "George Washington", "Benjamin Franklin", "Woodrow Wilson", "Abraham Lincoln"]
us_events = ["The Civil War", "World War I", "World War II", "The American Revolution", "The Civil Rights Movement", "The Great Depression", 
				"The Trail of Tears", "The Boston Tea Party", "Seneca Falls", "The Civil Rights Movement", "9/11", "The Gilded Age"]
us_topics = ["Abortion", "Illegal Immigration", "McCarthyism", "Bill Clinton", "Childhood Obesity"]

# Culture and Belief Dictionaries
books = ["Bible", "Koran", "New Testament", "Bhagavad Gita", "Dead Dea Scrolls", "Tibetan Book of the Dead", "Summa Theologica", "Tao Te Ching"]
peoples = ["Hebrew", "Christian", "Muslim", "Atheist", "Jedi", "Evangelical", "Presbyterian", "Anglican", "Agnostic", "Hindu"]
terms = ["Sacred", "Secular", "Atheist", "Spiritual"]
bible_rhymes = ["Bridal", "Bridle", "Dreidel", "Spinal", "Libel"]

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
type_10 = ["Monuments of %s %s"]
type_11 = ["A %s Reading of the %s", "The %s %s"]
type_12 = ["%s's %s"]
type_13 = ["The %s %s: A %s-%s Dance"]
type_14 = ["The Hebrew %s"]
type_15 = ["%s, Tradition, and %s: An Introduction to %s"]
type_16 = ["%s and the Politics of Culture: %s from %s to the Velvet Revolution"]
type_17 = ["Understanding %s and Contemporary %s Societies"]
type_18 = ["%s %s and Public Spectacle: The Case of the Roman Games"]
type_19 = ["Animated Spirituality: The %s as Manga"]

# us-world sentence types
type_20 = ["%s and Society in America", "The Evolution of American %s", "American %s: A Global History", "The Theory and Practice of Republican %s", "%s in America: A History"]
type_21 = ["%s: from %s to %s"]
type_22 = ["%s: Pros and Cons"]
type_23 = ["%s and Contemporary %s in the United States"]
type_24 = ["%s %s and %s"]
type_25 = ["Reinventing (and Reimagining) %s in %s: The Changing American %s Myth"]

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
cultbelief_sentence_types = [type_10, type_11, type_12, type_13, type_10, type_11, type_12, type_13, type_14, type_15, type_16, type_17, type_18, type_19, type_15, type_16, type_17, type_18, type_19]
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

def cultblf(place, practice, jarg_1, jarg_1b, jarg_2, ancient, harvard, time, religion, book, person, religion_2, term, bible, us_event):
	# Choose specific template at random
	sentence_type = random.choice(cultbelief_sentence_types)
	sentence = random.choice(sentence_type)
	prefix = "CULTBLF " + str(random.randint(0,100)) + ": "
	sentence = prefix + sentence
	# Within template, choose word combination at random
	if sentence_type == type_10:
		s = random.choice([(religion_2, practice), (jarg_1,religion)])
		print(sentence % s)
	elif sentence_type == type_11:
		print(sentence % (jarg_1, book))
	elif sentence_type == type_12:
		print(sentence % (harvard, book))
	elif sentence_type == type_13:
		print(sentence % (jarg_1, book, jarg_1b, term))
	elif sentence_type == type_14:
		print(sentence % bible)
	elif sentence_type == type_15:
		print(sentence % (practice, jarg_2, religion))
	elif sentence_type == type_16:
		print(sentence % (jarg_2, place, us_event))
	elif sentence_type == type_17:
		print(sentence % (religion,jarg_1))
	elif sentence_type == type_18:
		print(sentence % (jarg_1, practice))
	elif sentence_type == type_19:
		print(sentence % book)

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
		print(sentence % (practice, us_event, jarg_1))

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
	jarg_1b = random.choice(jargon_1)
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
	religion_2 = random.choice(peoples)
	term = random.choice(terms)
	bible = random.choice(bible_rhymes)
	
	subject = random.choice([aesthint,cultblf,usworld,socworld])
	# generate gen-ed
	if subject == aesthint:
		aesthint(place, practice, jarg_1, jarg_2, ancient, harvard, time, person, science)
	elif subject == cultblf:
		cultblf(place, practice, jarg_1,jarg_1b, jarg_2, ancient, harvard, time, religion, book, person, religion_2, term, bible, us_event)
	elif subject == usworld:
		usworld(place, practice, jarg_1, jarg_2, ancient, harvard, time, religion, us_event, us_topic,author, celeb, father)
	elif subject == socworld:
		socworld(place, practice, jarg_1, jarg_2, ancient, harvard, time, religion, us_event, us_topic,author, celeb, father,year_1,year_2, person)
# test
generate()
