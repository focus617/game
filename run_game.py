from wargame.attackoftheorcs import AttackofTheOrcs
from wargame.gameutils import show_theme_message,  print_dotted_line
from orcrider import OrcRider
from wargame.jumpstrategy import *

show_theme_message()
game = AttackofTheOrcs()
#game.play()

game.setup_game_scenario()

knight = game.player
knight.jump()
knight.jump = can_not_jump
knight.jump()

knight.equip_with_armor( 'ironjacket')
knight.show_details()

print_dotted_line()

orc = OrcRider('Orc战士')
orc.info()
orc.equip_with_armor( 'powersuit')
orc.show_details()
