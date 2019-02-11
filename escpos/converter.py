import escpos.constants as const
import json

def json_to_escpos(json_data):
    """
    Convert JSON to escpos code.

    Each line in the array is a line one the recipe.
    """

    data = json.loads(json_data)
    data = json.loads(data['data']) ## XXX: This bug needs to be fixed in mKassa.

    escpos = []
    escpos.append(const.INIT)
    escpos.append(const.BOLD['true'])
    escpos.append(const.ALIGN['center'])
    escpos.append(const.FONT_SIZE['2x'])
    escpos.append(b'WonderLAN')
    escpos.append(const.LINE_BREAK)
    escpos.append(const.FONT_SIZE['1x'])
    escpos.append(const.BOLD['false'])
    escpos.append(str.encode(data['date']))
    escpos.append(const.LINE_BREAK)
    escpos.append(str.encode(data['method']))
    escpos.append(const.LINE_BREAK)
    escpos.append(const.LINE_BREAK)
    escpos.append(const.HORIZONTAL_RULE)
    escpos.append(const.LINE_BREAK)
    for e in products(data['products']):
        escpos.append(e)

    escpos.append(const.LINE_BREAK)
    escpos.append(const.HORIZONTAL_RULE)
    escpos.append(const.ALIGN['right'])
    escpos.append(str.encode(str(data['sum'])))
    escpos.append(b'kr')
    escpos.append(const.LINE_BREAK)
    escpos.append(const.LINE_BREAK)
    escpos.append(b'Org-nummer: 802460-7155')
    escpos.append(const.LINE_BREAK)
    escpos.append(const.LINE_BREAK)
    escpos.append(b"Tack for ditt kop!")
    escpos.append(const.LINE_BREAK)
    escpos.append(const.LINE_BREAK)
    escpos.append(const.LINE_BREAK)
    escpos.append(const.LINE_BREAK)
    escpos.append(const.CUT_PAPER)

    return escpos

def products(products):
    escpos = []
    WIDTH = 42
    for p in products: # TODO: Move string build to its own function
        price = str(p['price']) + ' kr'
        escpos.append(const.ALIGN['left'])
        length = len(price)
        length += len(p['name'])
        space = ' ' * (WIDTH-length)
        string = f'{p["name"]}{space}{price}'
        escpos.append(str.encode(string))
        escpos.append(const.LINE_BREAK)
    return escpos
