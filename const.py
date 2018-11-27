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
NW_TERRITORY = {"coords" : (193,154), "color" : GRAY, "troops" : 0, "neighbors" : [ALASKA,ALBERTA,ONTARIO,GREENLAND]}
ALBERTA = {"coords" : (178,223), "color" : GRAY, "troops" : 0, "neighbors" : [ALASKA,NW_TERRITORY,ONTARIO,WESTERN_US]}
GREENLAND = {"coords" : (403,114), "color" : GRAY, "troops" : 0, "neighbors" : [QUEBEC,NW_TERRITORY,ONTARIO]}
QUEBEC = {"coords" : (329,236), "color" : GRAY, "troops" : 0, "neighbors" : []}
ONTARIO = {"coords" : (254,235), "color" : GRAY, "troops" : 0, "neighbors" : []}
EASTERN_US = {"coords" : (276,334), "color" : GRAY, "troops" : 0, "neighbors" : []}
CENTRAL_AMERICA = {"coords" : (201,414), "color" : GRAY, "troops" : 0, "neighbors" : []}

# SOUTH AMERICA
VENEZUELA = {"coords" : (289,469), "color" : GRAY, "troops" : 0, "neighbors" : []}
PERU = {"coords" : (302,572), "color" : GRAY, "troops" : 0, "neighbors" : []}
ARGENTINA = {"coords" : (304,660), "color" : GRAY, "troops" : 0, "neighbors" : []}
BRAZIL = {"coords" : (375,544), "color" : GRAY, "troops" : 0, "neighbors" : []}

# AFRICA
NORTH_AFRICA = {"coords" : (531,517), "color" : GRAY, "troops" : 0, "neighbors" : []}
EGYPT = {"coords" : (620,479), "color" : GRAY, "troops" : 0, "neighbors" : []}
CONGO = {"coords" : (620,605), "color" : GRAY, "troops" : 0, "neighbors" : []}
SOUTH_AFRICA = {"coords" : (624,703), "color" : GRAY, "troops" : 0, "neighbors" : []}
EAST_AFRICA = {"coords" : (670,554), "color" : GRAY, "troops" : 0, "neighbors" : []}
MADAGASCAR = {"coords" : (725,702), "color" : GRAY, "troops" : 0, "neighbors" : []}

# EUROPE
ICELAND = {"coords" : (498,200), "color" : GRAY, "troops" : 0, "neighbors" : []}
BRITAIN = {"coords" : (477,290), "color" : GRAY, "troops" : 0, "neighbors" : []}
SCANDINAVIA = {"coords" : (587,187), "color" : GRAY, "troops" : 0, "neighbors" : []}
NORTHERN_EUROPE = {"coords" : (576,303), "color" : GRAY, "troops" : 0, "neighbors" : []}
SOUTHERN_EUROPE = {"coords" : (593,369), "color" : GRAY, "troops" : 0, "neighbors" : []}
WESTERN_EUROPE = {"coords" : (486,405), "color" : GRAY, "troops" : 0, "neighbors" : []}
EASTERN_EUROPE = {"coords" : (682,254), "color" : GRAY, "troops" : 0, "neighbors" : []}

# ASIA
MIDDLE_EAST = {"coords" : (701,439), "color" : GRAY, "troops" : 0, "neighbors" : []}
KAZAKHSTAN = {"coords" : (775,328), "color" : GRAY, "troops" : 0, "neighbors" : []}
URAL = {"coords" : (796,218), "color" : GRAY, "troops" : 0, "neighbors" : []}
SIBERIA = {"coords" : (852,173), "color" : GRAY, "troops" : 0, "neighbors" : []}
CHINA = {"coords" : (899,378), "color" : GRAY, "troops" : 0, "neighbors" : []}
INDIA = {"coords" : (832,440), "color" : GRAY, "troops" : 0, "neighbors" : []}
SIAM = {"coords" : (917,473), "color" : GRAY, "troops" : 0, "neighbors" : []}
MONGOLIA = {"coords" : (941,309), "color" : GRAY, "troops" : 0, "neighbors" : []}
IRKUSTK = {"coords" : (924,230), "color" : GRAY, "troops" : 0, "neighbors" : []}
YAKUSTK = {"coords" : (938,140), "color" : GRAY, "troops" : 0, "neighbors" : []}
KAMCHATKA = {"coords" : (1028,144), "color" : GRAY, "troops" : 0, "neighbors" : []}
JAPAN = {"coords" : (1052,321), "color" : GRAY, "troops" : 0, "neighbors" : []}
# OCEANIA
INDONESIA = {"coords" : (937,599), "color" : GRAY, "troops" : 0, "neighbors" : []}
PAPUA_NEW_GUINEA = {"coords" : (1035,568), "color" : GRAY, "troops" : 0, "neighbors" : []}
WESTERN_AUSTRALIA = {"coords" : (969,694), "color" : GRAY, "troops" : 0, "neighbors" : []}
EASTERN_AUSTRALIA = {"coords" : (1057,666), "color" : GRAY, "troops" : 0, "neighbors" : []}

NEIGHBORS = [{"territory" : ALASKA, "neighbors" : [NW_TERRITORY,ALBERTA,KAMCHATKA]},
{"territory" : WESTERN_US, "neighbors" : [ALBERTA,ONTARIO,EASTERN_US,CENTRAL_AMERICA]},
{"territory" : WESTERN_US, "neighbors" : [ALASKA,ALBERTA,ONTARIO,GREENLAND]},
{"territory" : WESTERN_US, "neighbors" : [ALASKA,NW_TERRITORY,ONTARIO,WESTERN_US]},
{"territory" : WESTERN_US, "neighbors" : [QUEBEC,NW_TERRITORY,ONTARIO]},
{"territory" : WESTERN_US, "neighbors" : []},]
{"territory" : WESTERN_US, "neighbors" : []},
{"territory" : WESTERN_US, "neighbors" : []},
{"territory" : WESTERN_US, "neighbors" : []},




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
