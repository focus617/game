from wargame.attackoftheorcs import AttackofTheOrcs
from wargame.gameutils import show_theme_message,  process_args, print_dotted_line
from wargame.orcrider import OrcRider
from wargame.jumpstrategy import *


setting = process_args()
function = setting['function']

if function == 'playgame':
    show_theme_message()
    hutnum = setting['hutnumber']
    game = AttackofTheOrcs(hutnum)
    game.play()
elif function == 'test':
    show_theme_message()
    game = AttackofTheOrcs()
    game.test()

