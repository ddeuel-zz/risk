FPS = 30

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

# NORTH AMERICA
ALASKA = {"coords" : (86,162), "color" : GRAY, "troops" : 0}
WESTERN_US = {"coords" : (185,313), "color" : GRAY, "troops" : 0}
NW_TERRITORY = {"coords" : (193,154), "color" : GRAY, "troops" : 0}
ALBERTA = {"coords" : (178,223), "color" : GRAY, "troops" : 0}
GREENLAND = {"coords" : (403,114), "color" : GRAY, "troops" : 0}
QUEBEC = {"coords" : (329,236), "color" : GRAY, "troops" : 0}
ONTARIO = {"coords" : (254,235), "color" : GRAY, "troops" : 0}
EASTERN_US = {"coords" : (276,334), "color" : GRAY, "troops" : 0}
CENTRAL_AMERICA = {"coords" : (201,414), "color" : GRAY, "troops" : 0}

# SOUTH AMERICA
VENEZUELA = {"coords" : (289,469), "color" : GRAY, "troops" : 0}
PERU = {"coords" : (302,572), "color" : GRAY, "troops" : 0}
ARGENTINA = {"coords" : (304,660), "color" : GRAY, "troops" : 0}
BRAZIL = {"coords" : (375,544), "color" : GRAY, "troops" : 0}

# AFRICA
NORTH_AFRICA = {"coords" : (531,517), "color" : GRAY, "troops" : 0}
EGYPT = {"coords" : (620,479), "color" : GRAY, "troops" : 0}
CONGO = {"coords" : (620,605), "color" : GRAY, "troops" : 0}
SOUTH_AFRICA = {"coords" : (624,703), "color" : GRAY, "troops" : 0}
EAST_AFRICA = {"coords" : (670,554), "color" : GRAY, "troops" : 0}
MADAGASCAR = {"coords" : (725,702), "color" : GRAY, "troops" : 0}

# EUROPE
ICELAND = {"coords" : (498,200), "color" : GRAY, "troops" : 0}
BRITAIN = {"coords" : (477,290), "color" : GRAY, "troops" : 0}
SCANDINAVIA = {"coords" : (587,187), "color" : GRAY, "troops" : 0}
NORTHERN_EUROPE = {"coords" : (576,303), "color" : GRAY, "troops" : 0}
SOUTHERN_EUROPE = {"coords" : (593,369), "color" : GRAY, "troops" : 0}
WESTERN_EUROPE = {"coords" : (486,405), "color" : GRAY, "troops" : 0}
EASTERN_EUROPE = {"coords" : (682,254), "color" : GRAY, "troops" : 0}

# ASIA
MIDDLE_EAST = {"coords" : (701,439), "color" : GRAY, "troops" : 0}
KAZAKHSTAN = {"coords" : (775,328), "color" : GRAY, "troops" : 0}
URAL = {"coords" : (796,218), "color" : GRAY, "troops" : 0}
SIBERIA = {"coords" : (852,173), "color" : GRAY, "troops" : 0}
CHINA = {"coords" : (899,378), "color" : GRAY, "troops" : 0}
INDIA = {"coords" : (832,440), "color" : GRAY, "troops" : 0}
SIAM = {"coords" : (917,473), "color" : GRAY, "troops" : 0}
MONGOLIA = {"coords" : (941,309), "color" : GRAY, "troops" : 0}
IRKUSTK = {"coords" : (924,230), "color" : GRAY, "troops" : 0}
YAKUSTK = {"coords" : (938,140), "color" : GRAY, "troops" : 0}
KAMCHATKA = {"coords" : (1028,144), "color" : GRAY, "troops" : 0}
JAPAN = {"coords" : (1052,321), "color" : GRAY, "troops" : 0}
# OCEANIA
INDONESIA = {"coords" : (937,599), "color" : GRAY, "troops" : 0}
PAPUA_NEW_GUINEA = {"coords" : (1035,568), "color" : GRAY, "troops" : 0}
WESTERN_AUSTRALIA = {"coords" : (969,694), "color" : GRAY, "troops" : 0}
EASTERN_AUSTRALIA = {"coords" : (1057,666), "color" : GRAY, "troops" : 0}

NEIGHBORS = [{"territory" : ALASKA, "neighbors" : [NW_TERRITORY,ALBERTA,KAMCHATKA]},
{"territory" : WESTERN_US, "neighbors" : [ALBERTA,ONTARIO,EASTERN_US,CENTRAL_AMERICA]},
{"territory" : NW_TERRITORY, "neighbors" : [ALASKA,ALBERTA,ONTARIO,GREENLAND]},
{"territory" : ALBERTA, "neighbors" : [ALASKA,NW_TERRITORY,ONTARIO,WESTERN_US]},
{"territory" : GREENLAND, "neighbors" : [QUEBEC,NW_TERRITORY,ONTARIO,ICELAND]},
{"territory" : QUEBEC, "neighbors" : [GREENLAND, ONTARIO, EASTERN_US]},
{"territory" : ONTARIO, "neighbors" : [NW_TERRITORY, ALBERTA, WESTERN_US, EASTERN_US, QUEBEC]},
{"territory" : EASTERN_US, "neighbors" : [QUEBEC,ONTARIO,WESTERN_US,CENTRAL_AMERICA]},
{"territory" : CENTRAL_AMERICA, "neighbors" : [WESTERN_US,EASTERN_US,VENEZUELA]},
{"territory" : VENEZUELA, "neighbors" : [PERU,CENTRAL_AMERICA,BRAZIL]},
{"territory" : PERU, "neighbors" : [BRAZIL,VENEZUELA,ARGENTINA]},
{"territory" : BRAZIL, "neighbors" : [VENEZUELA,PERU,ARGENTINA]},
{"territory" : ARGENTINA, "neighbors" : [PERU,BRAZIL]},
{"territory" : NORTH_AFRICA, "neighbors" : [BRAZIL,EGYPT,WESTERN_EUROPE,CONGO,EAST_AFRICA]},
{"territory" : EGYPT, "neighbors" : [NORTH_AFRICA,SOUTHERN_EUROPE,EAST_AFRICA,MIDDLE_EAST]},
{"territory" : EAST_AFRICA, "neighbors" : [CONGO,MIDDLE_EAST,EGYPT,NORTH_AFRICA,SOUTH_AFRICA,MADAGASCAR]},
{"territory" : CONGO, "neighbors" : [NORTH_AFRICA,EAST_AFRICA,SOUTH_AFRICA]},
{"territory" : SOUTH_AFRICA, "neighbors" : [CONGO,MADAGASCAR,EAST_AFRICA]},
{"territory" : MADAGASCAR, "neighbors" : [SOUTH_AFRICA,EAST_AFRICA]},
{"territory" : ICELAND, "neighbors" : [GREENLAND,BRITAIN,SCANDINAVIA]},
{"territory" : BRITAIN, "neighbors" : [WESTERN_EUROPE,NORTHERN_EUROPE,SCANDINAVIA,ICELAND]},
{"territory" : WESTERN_EUROPE, "neighbors" : [NORTH_AFRICA,BRITAIN,NORTHERN_EUROPE,SOUTHERN_EUROPE]},
{"territory" : SCANDINAVIA, "neighbors" : [EASTERN_EUROPE,BRITAIN,NORTHERN_EUROPE]},
{"territory" : EASTERN_EUROPE, "neighbors" : [URAL,KAZAKHSTAN,MIDDLE_EAST,SOUTHERN_EUROPE,NORTHERN_EUROPE,SCANDINAVIA]},
{"territory" : NORTHERN_EUROPE, "neighbors" : [EASTERN_EUROPE,SOUTHERN_EUROPE,BRITAIN,WESTERN_EUROPE,SCANDINAVIA]},
{"territory" : SOUTHERN_EUROPE, "neighbors" : [NORTHERN_EUROPE,MIDDLE_EAST,WESTERN_EUROPE,EGYPT]},
{"territory" : URAL, "neighbors" : [KAZAKHSTAN,EASTERN_EUROPE,SIBERIA.CHINA]},
{"territory" : KAZAKHSTAN, "neighbors" : [URAL,EASTERN_EUROPE,MIDDLE_EAST,INDIA,CHINA]},
{"territory" : MIDDLE_EAST, "neighbors" : [EGYPT,EAST_AFRICA,KAZAKHSTAN,INDIA,SOUTHERN_EUROPE,EASTERN_EUROPE]},
{"territory" : SIBERIA, "neighbors" : [URAL,CHINA,YAKUSTK,IRKUSTK,MONGOLIA]},
{"territory" : YAKUSTK, "neighbors" : [SIBERIA,IRKUSTK,KAMCHATKA]},
{"territory" : IRKUSTK, "neighbors" : [SIBERIA,YAKUSTK,MONGOLIA,KAMCHATKA]},
{"territory" : MONGOLIA, "neighbors" : [CHINA,JAPAN,KAMCHATKA,IRKUSTK]},
{"territory" : CHINA, "neighbors" : [INDIA,KAZAKHSTAN,MONGOLIA,URAL,SIBERIA,SIAM]},
{"territory" : INDIA, "neighbors" : [MIDDLE_EAST,KAZAKHSTAN,CHINA,SIAM]},
{"territory" : SIAM, "neighbors" : [INDIA,CHINA,INDONESIA]},
{"territory" : KAMCHATKA, "neighbors" : [ALASKA,JAPAN,MONGOLIA,IRKUSTK,YAKUSTK]},
{"territory" : JAPAN, "neighbors" : [MONGOLIA,KAMCHATKA]},
{"territory" : INDONESIA, "neighbors" : [SIAM,WESTERN_AUSTRALIA,PAPUA_NEW_GUINEA]},
{"territory" : WESTERN_AUSTRALIA, "neighbors" : [INDONESIA,PAPUA_NEW_GUINEA,EASTERN_AUSTRALIA]},
{"territory" : EASTERN_AUSTRALIA, "neighbors" : [WESTERN_AUSTRALIA,PAPUA_NEW_GUINEA]},
{"territory" : PAPUA_NEW_GUINEA, "neighbors" : [INDONESIA,WESTERN_AUSTRALIA,EASTERN_AUSTRALIA]},
]




TERRITORIES = [ALASKA,WESTERN_US,NW_TERRITORY,ALBERTA,GREENLAND,QUEBEC,ONTARIO
,EASTERN_US,CENTRAL_AMERICA,VENEZUELA,PERU,ARGENTINA,BRAZIL,NORTH_AFRICA,EGYPT,
CONGO,SOUTH_AFRICA,EAST_AFRICA,MADAGASCAR,ICELAND,BRITAIN,SCANDINAVIA,NORTHERN_EUROPE,
SOUTHERN_EUROPE,WESTERN_EUROPE,EASTERN_EUROPE,MIDDLE_EAST,KAZAKHSTAN,URAL,SIBERIA,
CHINA,INDIA,SIAM,MONGOLIA,IRKUSTK,YAKUSTK,KAMCHATKA,JAPAN,INDONESIA,PAPUA_NEW_GUINEA,
WESTERN_AUSTRALIA,EASTERN_AUSTRALIA]

NORTH_AMERICA = {"territories" : [ALASKA,WESTERN_US,NW_TERRITORY,ALBERTA,GREENLAND,QUEBEC,ONTARIO
,EASTERN_US], "bonus" : 5}

SOUTH_AMERICA = {"territories" : [CENTRAL_AMERICA,VENEZUELA,PERU,ARGENTINA,
BRAZIL], "bonus" : 2}

AFRICA = {"territories" : [NORTH_AFRICA,EGYPT,
CONGO,SOUTH_AFRICA,EAST_AFRICA,MADAGASCAR], "bonus" : 3}

EUROPE = {"territories" : [ICELAND,BRITAIN,SCANDINAVIA,NORTHERN_EUROPE,
SOUTHERN_EUROPE,WESTERN_EUROPE,EASTERN_EUROPE], "bonus" : 5}

ASIA = {"territories" : [MIDDLE_EAST,KAZAKHSTAN,URAL,SIBERIA,
CHINA,INDIA,SIAM,MONGOLIA,IRKUSTK,YAKUSTK,KAMCHATKA,JAPAN], "bonus" : 7}

OCEANIA = {"territories" : [INDONESIA,PAPUA_NEW_GUINEA,
WESTERN_AUSTRALIA,EASTERN_AUSTRALIA], "bonus" : 2}

CONTINENTS = [NORTH_AMERICA, SOUTH_AMERICA, AFRICA, EUROPE,
ASIA, OCEANIA]

PLAYERS = [{"player" : 1, "color" : BLUE, "troops_to_place" : 3}, {"player" : 2, "color" : RED, "troops_to_place" : 3}]
