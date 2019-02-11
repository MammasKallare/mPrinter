INIT = b'\x1b'

LINE_BREAK = b'\x0A'

HORIZONTAL_RULE = b"------------------------------------------" + LINE_BREAK

CUT_PAPER = b'\x1B\x69'

# String manipulation
BOLD = {
    'true':     b'\x1B\x45\x0D',
    'false':    b'\x1B\x45\x0A'
}

ALIGN = {
    'center':   b'\x1B\x61\x31',
    'left':     b'\x1B\x61\x30',
    'right':    b'\x1B\x61\x32'
}

FONT_SIZE = {
    '1x': b'\x1D\x21\x00',
    '2x': b'\x1D\x21\x11'
}
