_COLOUR_NUMBERS = {
	'black': 0,
	'red': 1,
	'green': 2,
	'yellow': 3,
	'blue': 4,
	'purple': 5,
	'cyan': 6,
	'white': 7,
	'grey': 7
}


_TEXT_STYLES = {
	'normal': 0,
	'bold': 1,
	'underline': 2,
	'negative1': 3,
	'negative2': 5
}

def colour(text, text_colour=0, style=0, background_colour=None):
	if text_colour in _COLOUR_NUMBERS: text_colour = _COLOUR_NUMBERS[text_colour]
	if background_colour in _COLOUR_NUMBERS: background_colour = _COLOUR_NUMBERS[background_colour]
	if style in _TEXT_STYLES: style = _TEXT_STYLES[style]

	if background_colour is None and style == 0:
		return '\033[0;0m'+u"\u001b[38;5;" + str(text_colour % 256) + "m" + text + '\033[0;0m'
	else:
		return '\033[0;0m'+f'\033[{style};{text_colour%8+30};{background_colour%8+40}m{text}' + '\033[0;0m'

