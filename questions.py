"""
Types:
memory - Guess the answer
multi - Multiple choice
true - True or False
number - Answer as a number

Topics:
literature - Books, writing
geography - geography
history - history, mythology
entertainment - tv, music, films, art
science - science and nature
leisure - sports, food, games
technology - technology, programming
"""

# Thank you VulcanWM for supplying some questions for this project: https://github.com/VulcanWM/Quiz-API - https://replit.com/@VulcanWM

questions = {
    1: {
        'type': 'memory',
        "topic": "literature",
        "question": "Who wrote Twilight series of novels?",
        "answer": "Stephenie Meyer",
    },
    2: {
        'type': 'multi',
        "topic": "literature",
        "question":
        "Which of these letters is not usually written without taking the pen off of the paper?",
        "option1": 'P',
        "option2": 'K',
        "option3": 'W',
        "answer": "K",
    },
    3: {
        'type': 'memory',
        "topic": "literature",
        "question": "What is the only anagram of the word 'english'?",
        "answer": "Shingles",
    },
    4: {
        'type': 'memory',
        "topic": "science",
        "question":
        "Gala, Jonagold and Pink Lady are varieties of which fruit?",
        "answer": "Apple",
    },
    5: {
        'type': 'memory',
        "topic": "geography",
        "question": "On which side of the road do people drive in Japan?",
        "answer": "Left",
    },
    6: {
        'type': 'memory',
        "topic": "geography",
        "question": "Fort Knox lies in which American state?",
        "answer": "Kentucky",
    },
    7: {
        'type': 'memory',
        "topic": "history",
        "question": "Who was Queen for just nine days in 1553?",
        "answer": "Lady Jane Grey",
    },
    8: {
        'type': 'memory',
        "topic": "history",
        "question":
        "Which American war hero during the Revolutionary War swapped sides to join the British and become a spy?",
        "answer": "Benedict Arnold",
    },
    9: {
        'type': 'memory',
        "topic": "history",
        "question": "Who was the first US Secretary of War?",
        "answer": "Henry Knox",
    },
    10: {
        'type': 'memory',
        "topic": "history",
        "question":
        "Andrew Jackson co-founded the American Democratic Party with who?",
        "answer": "Martin Van Buren",
    },
    11: {
        'type': 'memory',
        "topic": "history",
        "question":
        "Who is most often regarded as the worst American president?",
        "answer": "James Buchanan",
    },
    12: {
        'type': 'memory',
        "topic": "history",
        "question":
        "What battle did the British surrender at in the Revolutionary War? Name the location",
        "answer": "Yorktown",
    },
    13: {
        'type': 'memory',
        "topic": "history",
        "question":
        "France took the America's side in the Revolutionary War with what other country?",
        "answer": "Spain",
    },
    14: {
        'type': 'memory',
        "topic": "history",
        "question":
        "Who caused the French and Indian war, or the Seven Years War?",
        "answer": "George Washington",
    },
    15: {
        'type': 'memory',
        "topic": "history",
        "question": "Who established the First Lady position in the U.S.?",
        "answer": "Dolley Madison",
    },
    16: {
        'type': 'memory',
        "topic": "entertainment",
        "question": "What is the 5th song in the musical Hamilton?",
        "answer": "The Schuyler Sisters",
    },
    17: {
        'type': 'memory',
        "topic": "entertainment",
        "question":
        "Which Beatle led the way across the zebra crossing on the Abbey Road album cover?",
        "answer": "John Lennon",
    },
    18: {
        'type': 'number',
        "topic": "science",
        "question": "How many wings does a bee have?",
        "answer": "4",
    },
    19: {
        'type': 'number',
        "topic": "science",
        "question":
        "Which Apollo moon mission was the first to carry a lunar rover vehicle?",
        "answer": "15",
    },
    20: {
        'type': 'memory',
        "topic": "leisure",
        "question": "Who won the 2009 Rugby World Sevens Cup?",
        "answer": "Wales",
    },
    21: {
        'type': 'number',
        "topic": "leisure",
        "question": "How many rounds are there in an Olympic boxing match?",
        "answer": "4",
    },
    22: {
        'type': 'memory',
        "topic": "literature",
        "question":
        "What is the true name of the titular character in Throne of Gass?",
        "answer": "Aelin Ashryver Whitethorn Galathynius",
    },
    23: {
        'type': 'memory',
        'topic': 'technology',
        'question':
        'A programming language has the icon of a snake. Name the language.',
        'answer': 'Python'
    },
    24: {
        'type': 'memory',
        'topic': 'technology',
        'question': 'What programming language is used to style websites?',
        'answer': 'CSS'
    },
    25: {
        'type': 'memory',
        'topic': 'technology',
        'question': 'What markup language is used to create websites?',
        'answer': 'HTML'
    },
    26: {
        'type': 'number',
        'topic': 'leisure',
        'question':
        'In a men\'s singles Grand Slam tennis match, how many sets do you have to win to win the match? (Answer as a number)',
        'answer': '3'
    },
    27: {
        'type': 'memory',
        'topic': 'literature',
        'question':
        'What is the name of the lion in C. S. Lewis\'s novel: The Lion, the Witch and the Warrdrobe?',
        'answer': 'Aslan'
    },
    28: {
        'type': 'memory',
        'topic': 'leisure',
        'question':
        'In a tennis game, what is the term used when two players are tied at 40 points each?',
        'answer': 'Deuce'
    },
    29: {
        'type': 'memory',
        'topic': 'history',
        'question':
        'What is the name of the volcano that destroyed the Roman city of Pompeii?',
        'answer': 'Vesuvius'
    },
    30: {
        'type': 'true',
        'topic': 'science',
        'question':
        'A human has the same number of bones in its neck as a giraffe does.',
        'answer': 'True'
    },
    31: {
        'type': 'memory',
        'topic': 'technology',
        'question': 'What programming language has a coffee cup for a logo?',
        'answer': 'Java'
    },
    32: {
        'type': 'multi',
        'topic': 'leisure',
        'question': 'Which of these doesn\'t use a ball?',
        'option1': 'Snooker',
        'option2': 'Ice hockey',
        'option3': 'Tennis',
        'answer': 'Ice hockey'
    },
    33: {
        'type': 'memory',
        'topic': 'history',
        'question':
        'In what modern-day country were the first Olympic Games held?',
        'answer': 'Greece'
    },
    34: {
        'type': 'multi',
        'topic': 'leisure',
        'question':
        'What form of martial arts involves throwing an opponent on to the floor and holding them there?',
        'option1': 'Judo',
        'option2': 'Karate',
        'option3': 'Taekwondo',
        'answer': 'Judo'
    },
    35: {
        'type': 'memory',
        'topic': 'geography',
        'question': 'Which South American country is named after the Equator?',
        'answer': 'Ecuador'
    },
    36: {
        'type': 'multi',
        'topic': 'history',
        'question': 'For whom was Valhalla the home of dead warriors?',
        'option1': 'Romans',
        'option2': 'Vikings',
        'option3': 'Incas',
        'answer': 'Vikings'
    },
    37: {
        'type': 'true',
        'topic': 'entertainment',
        'question': 'The Mona Lisa has no eyebrows.',
        'answer': 'True'
    },
    38: {
        'type': 'multi',
        'topic': 'What is the largest country with only one timezone?',
        'option1': 'Russia',
        'option2': 'Turkey',
        'option3': 'China',
        'answer': 'China'
    },
    39: {
        'type': 'memory',
        'topic': 'entertainment',
        'question':
        'What make of car serves as Marty McFly\'s time machine in Back to the Future?',
        'answer': 'DeLorean'
    },
    40: {
        'type': 'memory',
        'topic': 'science',
        'question':
        'On which planet is Olympius Mons, the tallest mountain in the solar system?',
        'answer': 'Mars'
    },
    41: {
        'type': 'memory',
        'topic': 'leisure',
        'question': 'Which video game has a grass block as a logo?',
        'answer': 'Minecraft'
    },
    42: {
        'type': 'true',
        'topic': 'entertainment',
        'question': 'The birthname of Superman is Kal-El.',
        'answer': 'True'
    },
    43: {
        'type': 'multi',
        'topic': 'leisure',
        'question':
        'Michael Phelps broke an Olympic world record in the 2008 Beijing Olympics. How many gold medals did he win?',
        'option1': '4',
        'option2': '8',
        'option3': '10',
        'answer': '8'
    },
    44: {
        'type': 'memory',
        'topic': 'history',
        'question': 'The Statue of Liberty was a gift given by what country?',
        'answer': 'France',
    },
    45: {
        'type': 'memory',
        'topic': 'literature',
        'question':
        'The view of which Italian city is referred to in E. M. Forster\'s novel A Room with a View?',
        'answer': 'Florence',
    },
    46: {
        'type': 'number',
        'topic': 'science',
        'question': 'How many chromosomes are there in a normal human cel?',
        'answer': '46'
    },
    47: {
        'type': 'true',
        'topic': 'history',
        'question':
        'Ireland was the RMS Titanic\'s last port of call before she sank.',
        'answer': 'True'
    },
    48: {
        'type': 'memory',
        'topic': 'technology',
        'question': 'What is the common name for a tiny picture element?',
        'answer': 'Pixel'
    },
    49: {
        'type': 'true',
        'topic': 'science',
        'question': 'A sea-monkey is a pygmy chimpanzee.',
        'answer': 'False'
    },
    50: {
        'type': 'memory',
        'topic': 'leisure',
        'question': 'Nori, the traditional sushi wrapping, is made from what?',
        'answer': 'Seaweed'
    },
    51: {
        'type': 'multi',
        'topic': 'science',
        'question':
        'Which island is the only place in the world where the big-nosed proboscis monkey can be found in the wild?',
        'option1': 'Borneo',
        'option2': 'Palau',
        'option3': 'Samoa',
        'answer': 'Borneo'
    },
    52: {
        'type': 'true',
        'topic': 'technology',
        'question': 'Hotmail took its name from a web page markup language.',
        'answer': 'True'
    },
    53: {
        'type': 'true',
        'topic': 'geography',
        'question': 'Maine is the only US state that has a monosyllabic name.',
        'answer': 'True'
    },
    54: {
        'type': 'multi',
        'topic': 'science',
        'question': 'Which of these is a member of the bear family?',
        'option1': 'Giant panda',
        'option2': 'Red panda',
        'option3': 'Koala',
        'answer': 'Giant panda'
    },
    55: {
        'type': 'multi',
        'topic': 'lesiure',
        'question':
        'Which of these sports was removed from the Olympics after 2008?',
        'option1': 'Softball',
        'option2': 'Netball',
        'option3': 'Handball',
        'answer': 'Softball'
    },
    56: {
        'type': 'memory',
        'topic': 'history',
        'question':
        'Which figure of Greek mythology is often depicted supporting the Earth on his shoulders?',
        'answer': 'Atlas'
    },
    57: {
        'type': 'multi',
        'topic': 'entertainment',
        'question': 'Who wrote the 1995 autobiography "Long Walk to Freedom"?',
        'option1': 'Boris Johnson',
        'option2': 'Barrack Obama',
        'option3': 'Nelson Mandela',
        'answer': 'Nelson Mandela'
    },
    58: {
        'type': 'true',
        'topic': 'entertainment',
        'question':
        'Leonardo DaVinci painted the ceiling of the Sistine Chapel.',
        'answer': 'False'
    },
    59: {
        'type': 'multi',
        'topic': 'science',
        'question': 'What does NASA stand for?',
        'option1': 'National Aeronautics and Space Administration',
        'option2': 'Neutron Astronauts and Space Aeronautics',
        'option3': 'National Administration and Space Astronauts',
        'answer': 'National Aeronautics and Space Administration'
    },
    60: {
        'type': 'memory',
        'topic': 'geography',
        'question':
        'What country has the westernmost point of mainland Europe?',
        'answer': 'Portugal'
    },
    61: {
        'type': 'memory',
        'topic': 'entertainment',
        'question':
        'In the Star Wars films what colour was Mace Windu\'s lightsaber?',
        'answer': 'Purple'
    },
    62: {
        'type': 'number',
        'topic': 'literature',
        'question': 'How many Harry Potter books are there?',
        'answer': '7'
    },
    63: {
        'type': 'number',
        'topic': 'entertainment',
        'question': 'How many Harry Potter movies are there?',
        'answer': '8'
    },
    64: {
        'type': 'multi',
        'topic': 'literature',
        'question':
        'Silky, Moonface and the Saucepan Man are characters in who\'s books?',
        'option1': 'Enid Blyton',
        'option2': 'Roald Dahl',
        'option3': 'Jill Murphy',
        'answer': 'Enid Blyton'
    },
    65: {
        'type': 'true',
        'topic': 'leisure',
        'question': 'McDonalds Hong Kong offers on-site wedding packages.',
        'answer': 'True'
    },
    66: {
        'type': 'memory',
        'topic': 'entertainment',
        'question':
        'In which musical does the cast sing about 525,600 minutes?',
        'answer': 'Rent'
    },
    67: {
        'type': 'multi',
        'topic': 'history',
        'question': 'Which era began first?',
        'option1': 'Mesozoic',
        'option2': 'Palaeozoic',
        'option3': 'Cenozoic',
        'answer': 'Palaeozoic'
    },
    68: {
        'type': 'multi',
        'topic': 'literature',
        'question': 'Pupaphobia is the fear of what?',
        'option1': 'Balloons',
        'option2': 'Puppets',
        'option3': 'Moths',
        'answer': 'Puppets'
    },
    69: {
        'type': 'memory',
        'topic': 'science',
        'question':
        'The flowers of which kind of fruit are referred to as sakura?',
        'answer': 'Cherry'
    },
    70: {
        'type': 'true',
        'topic': 'geography',
        'question': 'If you live in Tahiti then you are a citizen of France.',
        'answer': 'True'
    },
    71: {
        'type': 'memory',
        'topic': 'history',
        'question':
        'Which Roman god has two heads and is the god of beginnings and transitions?',
        'answer': 'Janus'
    },
    72: {
        'type': 'multi',
        'topic': 'entertainment',
        'question':
        'For what kind of artwork is the French town of Lascaux famous?',
        'option1': 'Sculptures',
        'option2': 'Street art',
        'option3': 'Cave paintings',
        'answer': 'Cave paintings'
    },
    73: {
        'type': 'memory',
        'topic': 'science',
        'question':
        'What Greek philosopher is known for his paradoxes including one about a race between Achilles and a tortoise.',
        'answer': 'Zeno'
    },
    74: {
        'type': 'multi',
        'topic': 'leisure',
        'question': 'Where would you wear an ascot?',
        'option1': 'On your head',
        'option2': 'Around your waist',
        'option3': 'Around your neck',
        'answer': 'Around your neck'
    },
    75: {
        'type': 'true',
        'topic': 'history',
        'question':
        'Peterhouse was the first college to be founded at Oxford University',
        'answer': 'False'
    },
    76: {
        'type': 'multi',
        'topic': 'literature',
        'question':
        'What name is given to a poem that is 14 lines long and often ends with a rhyming couplet?',
        'option1': 'Limerick',
        'option2': 'Sonnet',
        'option3': 'Ode',
        'answer': 'Sonnet'
    },
    77: {
        'type': 'true',
        'topic': 'entertainment',
        'question': 'David Guetta is Spanish',
        'answer': 'False'
    },
    78: {
        'type': 'true',
        'topic': 'science',
        'question': 'A solar system is larger than a galaxy.',
        'answer': 'False'
    },
    79: {
        'type': 'multi',
        'topic': 'leisure',
        'question': 'Which of these foods would a pescetarian not eat?',
        'option1': 'Salmon',
        'option2': 'Chicken',
        'option3': 'Peanuts',
        'answer': 'Chicken'
    },
    80: {
        'type': 'multi',
        'topic': 'science',
        'question': 'What rocks are the product of erosion?',
        'option1': 'Igneous',
        'option2': 'Metamorphic',
        'option3': 'Sedimentary',
        'answer': 'Sedimentary'
    },
    81: {
        'type': 'multi',
        'topic': 'science',
        'question': 'What was the maiden name of Buzz Aldrin\'s mother?',
        'option1': 'Moon',
        'option2': 'Mars',
        'option3': 'Neil',
        'answer': 'Moon'
    },
    82: {
        'type': 'multi',
        'topic': 'leisure',
        'question': 'Which cooking method requires liquid?',
        'option1': 'Baking',
        'option2': 'Braising',
        'option3': 'Grilling',
        'answer': 'Braising'
    },
    83: {
        'type': 'multi',
        'topic': 'history',
        'question': 'Which of these countries was not once part of the Soviet Union?',
        'option1': 'Armenia',
        'option2': 'Georgia',
        'option3': 'Macedonia',
        'answer': 'Macedonia'
    },
    84: {
        'type': 'true',
        'topic': 'geography',
        'question': 'The People\'s Liberation Army of China is the world\'s largest employer.',
        'answer': 'True'
    },
    85: {
        'type': 'memory',
        'topic': 'literature',
        'question': 'Who wrote The Tale of Peter Rabbit?',
        'answer': 'Beatrix Potter'
    },
    86: {
        'type': 'memory',
        'topic': 'leisure',
        'question': 'What is the surname of the European football manager that referred to himself as "the special one"?',
        'answer': 'Mourinho'
    },
    87: {
        'type': 'multi',
        'topic': 'science',
        'question': 'Where would you find the pyramids of Malpighi?',
        'option1': 'Banks of the Nile',
        'option2': 'Human body',
        'option3': 'Steam engine',
        'answer': 'Human body'
    },
    88: {
        'type': 'memory',
        'topic': 'leisure',
        'question': 'Which terrier dog breed and type of pudding are named after a county in England?',
        'answer': 'Yorkshire'
    },
    89: {
        'type': 'multi',
        'topic': 'geography',
        'question': 'In which German city does BMW have its headquarters?',
        'option1': 'Munich',
        'option2': 'Hamburg',
        'option3': 'Berlin',
        'answer': 'Munich'
    },
    90: {
        'type': 'memory',
        'topic': 'history',
        'question': 'What was the name for Britain leaving the European Union?',
        'answer': 'Brexit',
    },
    91: {
        'type': 'true',
        'topic': 'history',
        'question': 'Theresa May was the first female Prime Minister of the UK.',
        'answer': 'False'
    },
    92: {
        'type': 'true',
        'topic': 'geography',
        'question': 'Kruger National Park is located in Singapore.',
        'answer': 'False'
    },
    93: {
        'type': 'memory',
        'topic': 'science',
        'question': 'As of 2005, what was the smallest planet in the solar system?',
        'answer': 'Pluto'
    },
    94: {
        'type': 'memory',
        'topic': 'science',
        'question': 'As of 2008, what was the smallest planet in the solar system?',
        'answer': 'Mercury'
    },
    95: {
        'type': 'multi',
        'topic': 'leisure',
        'question': 'Which of these landmarks does the London Marathon not pass?',
        'option1': 'Elizabethan Tower',
        'option2': 'Tower Bridge',
        'option3': 'Trafalgar Square',
        'answer': 'Trafalgar Square'
    },
    96: {
        'type': 'memory',
        'topic': 'entertainment',
        'question': 'Which British rock group released a debut album named Parachutes?',
        'answer': 'Coldplay'
    },
    97: {
        'type': 'memory',
        'topic': 'history',
        'question': 'What board game was introduced during America\'s Great Depression in the 1930\'s and became wildly popular due to its promise of fame and fortune?',
        'answer': 'Monopoly'
    },
    98: {
        'type': 'multi',
        'topic': 'history',
        'question': 'What was the first opera performed at the Sydney Opera House?',
        'option1': 'War and Peace',
        'option2': 'Madame Butterfly',
        'option3': 'Porgy and the Bess',
        'answer': 'War and Peace'
    },
    99: {
        'type': 'memory',
        'topic': 'leisure',
        'question': 'What do the five Olympic rings represent?',
        'answer': 'Continents'
    },
    100: {
        'type': 'memory',
        'topic': 'entertainment',
        'question': 'In what country was the Lord of the Rings film trilogy shot?',
        'answer': 'New Zealand'
    },
    101: {
        'type': 'multi',
        'topic': 'science',
        'question': 'What is a peanut?',
        'option1': 'a nut',
        'option2': 'a legume',
        'option3': 'a drupe',
        'answer': 'a legume'
    },
    102: {
        'type': 'memory',
        'topic': 'leisure',
        'question': 'What is the world\'s most popular colour according to yougov.co.uk?',
        'option1': 'Green',
        'option2': 'Blue',
        'option3': 'Red',
        'answer': 'Blue'
    },
    103: {
        'type': 'memory',
        'topic': 'entertainment',
        'question': 'What colour is Vine Street in Monopoly?',
        'answer': 'Orange'
    },
    104: {
        'type': 'memory',
        'topic': 'science',
        'question': 'What colour is a baby swan?',
        'answer': 'Grey'
    },
    105: {
        'type': 'memory',
        'topic': 'science',
        'question': 'What colour are the largest stars?',
        'answer': 'Blue'
    },
    106: {
        'type': 'memory',
        'topic': 'science',
        'question': 'There are two species of tuna that have colours in their names. One of them is yellowfin. Name the other.',
        'answer': 'Bluefin'
    },
    107: {
        'type': 'memory',
        'topic': 'leisure',
        'question': 'What is the most popular colour of highlighter?',
        'answer': 'Yellow'
    },
    108: {
        'type': 'memory',
        'topic': 'entertainment',
        'question': 'What was the colour in the name of Strauss\' most famous waltz?',
        'answer': 'Blue'
    },
    109: {
        'type': 'memory',
        'topic': 'entertainment',
        'question': 'What colour is Stitch\'s fur from Lilo and Stitch?',
        'answer': 'Blue'
    },
    110: {
        'type': 'memory',
        'topic': 'entertainment',
        'question': 'Nina sang about 99 balloons. What colour were they?',
        'answer': 'Red'
    },
    111: {
        'type': 'memory',
        'topic': 'geography',
        'question': 'What is the colour of mourning in China?',
        'answer': 'White'
    },
    112: {
        'type': 'multi',
        'topic': 'history',
        'question': 'Which Queen of England died in 1901?',
        'option1': 'Queen Victoria',
        'option2': 'Queen Elizabeth',
        'option3': 'Lady Jane Grey',
        'answer': 'Queen Victoria'
    },
    113: {
        'type': 'true',
        'topic': 'literature',
        'question': 'The Lion, the Witch and the Wardrobe is the first book in the Chronicles of Narnia.',
        'answer': 'False'
    },
    114: {
        'type': 'true',
        'topic': 'geography',
        'question': 'French is the official language of Suriname.',
        'answer': 'False'
    },
    115: {
        'type': 'true',
        'topic': 'entertainment',
        'question': 'John Torode has presented both Masterchef and Junior Masterchef.',
        'answer': 'True'
    },
    116: {
        'type': 'multi',
        'topic': 'history',
        'question': 'Which of tthese US presidents didn\'t have a moustache while in office?',
        'option1': 'Abraham Lincoln',
        'option2': 'Ulysses Grant',
        'option3': 'James Garfield',
        'answer': 'Abraham Lincoln'
    },
    117: {
        'type': 'memory',
        'topic': 'entertainment',
        'question': 'Who sculpted the statue of David and the Pietà?',
        'answer': 'Michaelangelo'
    },
    118: {
        'type': 'memory',
        'topic': 'science',
        'question': 'What aquatic mammal makes its home in a holt?',
        'answer': 'Otter'
    },
    119: {
        'type': 'multi',
        'topic': 'leisure',
        'question': 'Which of these sauces does not contain eggs?',
        'option1': 'Hollandaise',
        'option2': 'Vinaigrette',
        'option3': 'Tartare sauce',
        'answer': 'Vinaigrette'
    },
    120: {
        'type': 'memory',
        'topic': 'history',
        'question': 'What was Nelson\'s flagship called during the Battle of Trafalgar?',
        'answer': 'HMS Victory'
    }
}
