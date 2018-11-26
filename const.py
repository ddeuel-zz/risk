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
