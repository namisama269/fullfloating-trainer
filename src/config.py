
"""
Cube Settings
"""
# Enter orientation colours in the format "ULFRBD".
orientation = "YBRGOW"

# Enter pieces in order of buffers, the first sticker is the buffer sticker
pieces = {
    'c': [
        ['UFR','RUF','FUR'], ['UFL','FUL','LUF'], ['UBL','LUB','BUL'], ['UBR','BUR','RUB'],
        ['DFR','FDR','RDF'], ['DFL','LDF','FDL'], ['DBR','RDB','BDR'], ['DBL','BDL','LDB'],
    ],
    'e': [
        ['UF','FU'], ['UB','BU'], ['UR','RU'], ['UL','LU'], 
        ['DF','FD'], ['DB','BD'], ['FR','RF'], ['FL','LF'],
        ['DR','RD'], ['DL','LD'], ['LB','BL'], ['RB','BR'],
    ]
}

# Piece types to train
pce_types = ['e','c']

# Buffers to train, comment out to not train 
buffers = {
    'c': [
        #'UFR', 
        'UFL', 
        #'UBL', 
        #'UBR', 
        #'DFR', 
        #'DFL',
        ],
    'e': [
        #'UF', 
        'UB', 
        'UR', 
        'UL', 
        #'DF', 
        #'DB', 
        #'FR', 
        #'FL', 
        #'DR', 
        #'DL',
        ],
}

# Enter letter scheme for each piece type.

letter_scheme = {
    # corners
    'UBL': 'A',
    'UBR': 'B',
    'UFL': 'C',
    'UFR': 'D',
    'LUB': 'E',
    'LUF': 'F',
    'LDB': 'G',
    'LDF': 'H',
    'FUL': 'I',
    'FUR': 'J',
    'FDL': 'K',
    'FDR': 'L',
    'RUF': 'M',
    'RUB': 'N',
    'RDF': 'O',
    'RDB': 'P',
    'BUL': 'Q',
    'BUR': 'R',
    'BDL': 'S',
    'BDR': 'T',
    'DBL': 'U',
    'DBR': 'V',
    'DFL': 'W',
    'DFR': 'X',

    # edges
    'UB': 'A',
    'UL': 'B',
    'UR': 'C',
    'UF': 'D',
    'LU': 'E',
    'LB': 'F',
    'LF': 'G',
    'LD': 'H',
    'FU': 'I',
    'FL': 'J',
    'FR': 'K',
    'FD': 'L',
    'RU': 'M',
    'RF': 'N',
    'RB': 'O',
    'RD': 'P',
    'BU': 'Q',
    'BL': 'R',
    'BR': 'S',
    'BD': 'T',
    'DB': 'U',
    'DL': 'V',
    'DR': 'W',
    'DF': 'X',
}


#日本語ナンバーリング
"""
letter_scheme = {
    # corners
    'UBL': 'あ',
    'UBR': 'い',
    'UFL': 'え',
    'UFR': 'う',
    'LUB': 'さ',
    'LUF': 'し',
    'LDB': 'せ',
    'LDF': 'す',
    'FUL': 'か',
    'FUR': 'き',
    'FDL': 'け',
    'FDR': 'く',
    'RUF': 'な',
    'RUB': 'に',
    'RDF': 'ね',
    'RDB': 'ぬ',
    'BUL': 'て',
    'BUR': 'つ',
    'BDL': 'た',
    'BDR': 'ち',
    'DBL': 'へ',
    'DBR': 'ふ',
    'DFL': 'は',
    'DFR': 'ひ',

    # edges
    'UB': 'あ',
    'UL': 'え',
    'UR': 'い',
    'UF': 'う',
    'LU': 'さ',
    'LB': 'せ',
    'LF': 'し',
    'LD': 'す',
    'FU': 'か',
    'FL': 'け',
    'FR': 'き',
    'FD': 'く',
    'RU': 'な',
    'RF': 'ね',
    'RB': 'に',
    'RD': 'ぬ',
    'BU': 'つ',
    'BL': 'て',
    'BR': 'ち',
    'BD': 'た',
    'DB': 'ふ',
    'DL': 'へ',
    'DR': 'ひ',
    'DF': 'は',
}
"""

"""
GUI Settings
"""
# Enter the following colours in (R, G, B) format. 

# Background colour
bg_colour = (255,250,205)#(238,255,204)

# Face colours
face_colours = {
    'W': (255,255,255),
    'Y': (240,255,0),
    'B': (32,85,255),
    'G': (102,255,51),
    'R': (232,18,10),
    'O': (251,140,0),
}

# BLD mode colours
buffer_clr = (255,0,0)
target_clr1 = (204,153,255)
target_clr2 = (153,51,255)
highlight_clr = (245,245,245)
fill_clr = (224,224,224)

# Button colours
button_clr = (255,187,187)#(190,190,190)
hover_clr = (255,221,221)#(211,211,211)

"""
Keybind Settings
"""

keybind_333 = {
    '9': "E'",
    '3': "E",
    '4': "S'",
    '8': "S",
    '5': "M",
    '6': "M",
    'q': "z",
    'w': "B",
    'e': "L'",
    'r': "Lw'",
    't': "x",
    'y': "x",
    'u': "Rw",
    'i': "R",
    'o': "B'",
    'p': "z",
    'a': "y'",
    's': "D",
    'd': "L",
    'f': "U'",
    'g': "F'",
    'h': "F",
    'j': "U",
    'k': "R'",
    'l': "D'",
    ';': "y",
    'z': "Dw",
    'x': "M'",
    'c': "Uw'",
    'v': "Lw",
    'b': "x'",
    'n': "x'",
    'm': "Rw'",
    ',': "Uw",
    '.': "M'",
    '/': "Dw'",
}