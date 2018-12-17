from wargame.attackoftheorcs import AttackofTheOrcs
from wargame.gameutils import show_theme_message,  process_args
from wargame.orcrider import OrcRider
from wargame.jumpstrategy import *


show_theme_message()
setting = process_args()
hutnum = setting['hutnumber']
game = AttackofTheOrcs(hutnum)

# game.setup_game_scenario()

# knight = game.player
# knight.jump()
# knight.jump = can_not_jump
# knight.jump()
#
# knight.equip_with_accessory( 'ironjacket')
# knight.equip_with_accessory( 'superlocket')
# knight.show_details()
#
# print_dotted_line()
#
# orc = OrcRider('Orc战士')
# orc.info()
# orc.equip_with_accessory( 'powersuit')
# orc.equip_with_accessory( 'magiclocket')
# orc.show_details()

game.play()