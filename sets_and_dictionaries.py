# Instructions
# we want to perform a (simple) modeling of an information flow aggregator. An information
# feed (for example, an RSS feed) is made up of dispatches published by the media (newspapers,
# news sites, etc.). Here, to simplify the problem, a feed is a list of dispatches and a dispatch
# is a triplet of character strings containing the name of the medium, the category of the dispatch
# and the title of the dispatch. Different feeds may contain the same news (for example, the Google
# feed and the Yahoo! feed).
Stream = List[Tuple[str,str,str]]
Rubrics = Dict[str, List[Tuple[str,str]]]

stream_0 : Stream
stream_0 = [("L’équipe", "Sport", "Rugby: les matches du week-end")]
stream_1 : Stream
stream_1 = [("Le Monde","Sport","Match nul du PSG"),
            ("L’équipe","Sport", "Le PSG tenu en échec"),
            ("Le Monde", "Politique", "Congrès de LR"),
            ("20 minutes", "Politique", "Elections présidentielles"),
            ("20 minutes", "Sport", "La Russie gagne la coupe Davis"),
            ("France Inter", "Economie", "Chute du bitcoin"),
            ("The Conversation", "Economie", "Les monnaies numériques"),
            ("The Conversation", "Culture", "Mr Robot: le hacker et sa toile"),
            ("France Inter", "Sport", "Les jeux paralympiques"),
            ("Le Monde", "Politique", "L’avenir des universités")]
stream_2 : Stream
stream_2 = [("20 minutes", "Culture", "Le dernier Spielberg"),
            ("France Inter", "Culture", "Six bonnes raisons de lire Balzac"),
            ("The Conversation", "Culture", "Mr Robot: le hacker et sa toile")]

# Give a definition of the set_media function which, given a stream, returns the set of media
# contained in this stream.
def set_media(stream: Stream) -> Set[str]:
    """ Preconditions:
    """
    ens: Set[str] = set()
    for (media,_,_) in stream:
        ens.add(media)
    return ens

assert set_media([]) == set()
assert set_media(stream_0) == {'L’équipe'}
assert set_media(stream_1) == {'The Conversation', 'L’équipe', 'France Inter', '20 minutes', 'Le Monde'}
assert set_media(stream_2) == {'The Conversation', '20 minutes', 'France Inter'}

# Instructions:
# Give a definition of the group_media function which, given two streams, returns all the media
# contained in these 2 streams.
def group_media(f_1: Stream, f_2: Stream) -> Set[str]:
    """ Preconditions:
    """
    return set_media(f_1) | set_media(f_2)

assert group_media([],[]) == set()
assert group_media([],stream_2) == set_media(stream_2)
assert group_media(stream_1,stream_1) == set_media(stream_1)
assert group_media(stream_0,stream_1) == {"L’équipe", 'France Inter',
        '20 minutes', 'The Conversation', 'Le Monde'}
assert group_media(stream_0,stream_2) == {'France Inter', '20 minutes',
        'The Conversation', "L’équipe"}

# Instructions:
# Give a definition of the function tous_depeches which, given a media name and a stream, returns
# the list of pairs giving the category and the title of the dispatch of this media which are contained
# in the stream.
def all_dispacthes(media:str, stream: Stream) -> List[Tuple[str, str]]:
    """ Preconditions: -
    returns the list of pairs giving the category and the title of the dispatch of this media
    """
    res: List[Tuple[str, str]] = []
    for (name, category, text) in stream:
        if name == media:
            res.append((category, text))
    return res

assert all_dispacthes("Le Monde",[]) == []
assert all_dispacthes("Le Monde",stream_0) == []
assert all_dispacthes("Le Monde",stream_1) == [('Sport', 'Match nul du PSG'),
('Politique', 'Congrès de LR'), ('Politique', "L’avenir des universités")]

# Instructions:
# Give a definition of the construct_rubrics function which, given a stream, returns the corresponding
# Rubrics dictionary.
def build_rubrics(stream: Stream) -> Rubrics:
    """ Preconditions: -
    """
    dic: Rubrics = dict()
    for (name, category, text) in stream:
        if category in dic:
            dic[category].append((name,text))
        else:
            dic[category]= [(name, text)]
    return dic

assert build_rubrics([]) == dict()
assert build_rubrics(stream_0) == {"Sport":[("L’équipe", 'Rugby: les matches du week-end')]}
assert build_rubrics(stream_1) == {'Sport': [('Le Monde', 'Match nul du PSG'),
                                             ("L’équipe", 'Le PSG tenu en échec'),
                                             ('20 minutes', 'La Russie gagne la coupe Davis'),
                                             ('France Inter', 'Les jeux paralympiques')],
                                   'Politique': [('Le Monde', 'Congrès de LR'),
                                                 ('20 minutes', 'Elections présidentielles'),
                                                 ('Le Monde', "L’avenir des universités")],                                                  'Economie': [('France Inter', 'Chute du bitcoin'),
                                                  ('The Conversation', 'Les monnaies numériques')],
                                    'Culture': [('The Conversation', 'Mr Robot: le hacker et sa toile')]}

# Instructions:
# Give a definition of the count_dispatch function which, given a media, a category and a Rubrics
# dictionary, returns the number of dispatches of the considered media for the category.
def count_dispatch(media: str, category: str, dic: Rubrics) -> int:
    """ Preconditions: -
    returns the number of dispatches of the given media and category
    """
    count:int = 0
    if category in dic:
        e: Tuple[str, str]
        for e in dic[category]:
            le_media,_ = e
            if le_media == media:
                count = count + 1
    return count

assert count_dispatch("L’équipe","Economie",dict()) == 0
assert count_dispatch("L’équipe","Economie",build_rubrics(stream_1)) == 0
assert count_dispatch("Le Monde","Sport",build_rubrics(stream_1)) == 1
assert count_dispatch("Le Monde","Politique",build_rubrics(stream_1)) == 2

# Instructions:
# Give a definition of the function merges which, given two Rubrics dictionaries, returns the Rubrics
# dictionary which is the fusion of the 2 dictionaries while avoiding that there are duplicate
# dispatches in the resulting dictionary.
def merge(dic_1:Rubrics, dic_2:Rubrics) -> Rubrics:
    """ Preconditions: -
    returns the union of the two dictionaries
    """
    dic:Rubrics = dict()
    for (key, value) in dic_1.items():
        dic[key] = value
    for (key, value) in dic_2.items():
        if key not in dic:
            dic[key] = value
        else:
            ens_tuples: Set[Tuple[str, str]]= set()
        for e in dic[key]:
            ens_tuples.add(e)
        for v2 in dic_2[key]:
            if v2 not in ens_tuples:
                dic[key].append(v2)
    return dic

assert merge(dict(),dict()) == dict()
assert merge(build_rubrics(stream_1),dict()) == build_rubrics(stream_1)
assert merge(build_rubrics(stream_0), \
            build_rubrics(stream_1)) == {'Sport': [("L’équipe", 'Rugby: les matches du week-end'),
                    ('Le Monde', 'Match nul du PSG'),
                    ("L’équipe", 'Le PSG tenu en échec'),
                    ('20 minutes', 'La Russie gagne la coupe Davis'),
                    ('France Inter', 'Les jeux paralympiques')],
        'Politique': [('Le Monde', 'Congrès de LR'),
                    ('20 minutes', 'Elections présidentielles'),
                    ('Le Monde', 'L’avenir des universités')],
        'Economie': [('France Inter', 'Chute du bitcoin'),
                    ('The Conversation', 'Les monnaies numériques')],
        'Culture': [('The Conversation', 'Mr Robot: le hacker et sa toile')]}
assert merge(build_rubrics(stream_0), \
            build_rubrics(stream_0)) == {'Sport': [("L’équipe",'Rugby: les matches du week-end')]}
assert merge(build_rubrics(stream_1), \
            build_rubrics(stream_2)) == {'Sport': [('Le Monde', 'Match nul du PSG'),
                    ("L’équipe", 'Le PSG tenu en échec'),
                    ('20 minutes', 'La Russie gagne la coupe Davis'),
                    ('France Inter', 'Les jeux paralympiques')],
        'Politique': [('Le Monde', 'Congrès de LR'),
                    ('20 minutes', 'Elections présidentielles'),
                    ('Le Monde', 'L’avenir des universités')],
        'Economie': [('France Inter', 'Chute du bitcoin'),
                    ('The Conversation', 'Les monnaies numériques')],
        'Culture': [('The Conversation', 'Mr Robot: le hacker et sa toile'),
                    ('20 minutes', 'Le dernier Spielberg'),
                    ('France Inter', 'Six bonnes raisons de lire Balzac')]}
