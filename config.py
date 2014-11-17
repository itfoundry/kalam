#!/usr/bin/python

FAMILY_NAME = 'Kalam'

STYLE_NAMES = [
    'Light',
    'Regular',
    'Bold',
]

UFOIG_ARGS = [
    # '-kern',
    '-mark',
    # '-hint',
    '-flat',
    '-mkmk',
    '-clas',
    '-indi',
]

MATCH_mI_OFFSETS_DICT = {
    'Light':    40,
    'Regular':  54,
    'Bold':     80,
}

MAKEOTF_ARGS = [
    '-r',
    '-shw',
]

OUTPUT_DIR = '/Library/Application Support/Adobe/Fonts'
