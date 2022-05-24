#!/usr/bin/python3
# Convert a QMK Configurator JSON map to a KeyboardLayoutEditor colored one.
# https://config.qmk.fm/#/preonic/rev3_drop/LAYOUT_preonic_1x2uC
# http://www.keyboard-layout-editor.com/#/

import json, sys
#["       tl \n bl \n tr \n br \n\n\n cl \n cr \n tc \n cc \n bc",
LABEL = '{tl}\n{bl}\n{tr}\n{br}\n\n\n{cl}\n{cr}\n{tc}\n{cc}\n{bc}'
REPLACE = {
        'NO': '',
        'UP': '↑',
        'DOWN': '↓',
        'LEFT': '←',
        'RGHT': '→',
        'LSFT': '⇑',
        'SFTENT': '⇪↲',
        'LCPO': 'Ctrl (',
        'RCPC': 'Ctrl )',
        'BSPC': '⌫',
        'DEL': '⌦',
        'PGDN': 'PgUp',
        'PGUP': 'PgDn',
        'RGUI': '◆',
        'LGUI': '◆',
        'HOME': 'Home',
        'END': 'End',
        'LALT': 'Alt',
        'RALT': 'Alt',
        'LAPO': 'Alt (',
        'TAB': '⇥',
        'SPC': ' ',
        'GESC': 'Esc ~',

        'P0': 'N0',
        'P1': 'N1',
        'P2': 'N2',
        'P3': 'N3',
        'P4': 'N4',
        'P5': 'N5',
        'P6': 'N6',
        'P7': 'N7',
        'P8': 'N8',
        'P9': 'N9',
        'PDOT': 'N.',
        'PENT': 'N↲',
        'PEQL': 'N=',
        'PCMM': 'N.',
        'PPLS': 'N+',
        'PMNS': 'N-',
        'PAST': 'N*',
        'PSLS': 'N/',

        'LBRC' : '[',
        'RBRC' : ']',
        'LCBR' : '{',
        'RCBR' : '}',
        'LPRN' : '(',
        'RPRN' : ')',

        'TILD': '~',
        'GRV': '`',
        'PIPE': '|',
        'BSLS': '\\',
        'QUES': '?',
        'SLSH': '/',

        'SCLN': ';:',
        'QUOT': '\'"',
        'DOT': '.>',
        'COMM': ',<',

        # Quantum stuff
        'MS_L': '🖱←',
        'MS_R': '🖱→',
        'MS_U': '🖱↑',
        'WH_U': '🖱↑',
        'MS_D': '🖱↓',
        'WH_D': '🖱↓',
        'BTN1': '🖱',
        'BTN2': '🖱',
        'BTN3': '🖱',
        'BTN4': '🖱',
        'BTN5': '🖱',
        'ANY(ASTG)': 'Autoshift Toggle',
        'ANY(LOCK)': 'Lock',
        'TRNS': '', # transparent. no label.

        # Unique labels
        'LT(2,ENT)': 'RSE↲',
        'LT(1,TAB)': 'LWR⇥',
        'MO(3)': 'Adjust',
        }
data = json.load(open(sys.argv[1]))
print(data)
base = data['layers'][0]
lower = data['layers'][1]
upper = data['layers'][2]
adjust = data['layers'][3]

def getKeycode(text):
    print(text)
    text = text.replace('KC_', '')
    if text in REPLACE:
        return REPLACE[text]
    else:
        return text

output = []
print(len(lower))
for row in range(5):
    row_out = []
    for column in range(12):
        index = 12*row + column
        print(index)
        # Last row has 11 switches.
        if row == 4 and column == 11:
            break
        if base[index] == 'KC_SPC':
            row_out.append({'w': 2})
        # Colors
        if 'LT(1' in base[index]:
            row_out.append({'c': '#004ad4'})
        elif 'LT(2' in base[index]:
            row_out.append({'c': '#bd9700'})
        elif base[index] == 'KC_GESC':
            row_out.append({'c': '#a00000'})
        elif base[index] == 'KC_SFTENT':
            row_out.append({'c': '#a00000'})
        elif row == 4 or column == 0 or column == 11:
            row_out.append({'c': '#999999'})
        else:
            row_out.append({'c': '#cccccc'})

        row_out.append('\n'.join((
            '', # 0
            '', # 1
            '', # 2
            '', # 3
            getKeycode(adjust[index]),
            '', # 5
            '', # 6
            '', # 7
            getKeycode(upper[index]),
            getKeycode(base[index]),
            getKeycode(lower[index]))))
    output.append(row_out)
print(json.dumps(output))
