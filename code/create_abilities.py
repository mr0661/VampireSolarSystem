import os
from common import *


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
ABILITY_FOLDER = FILE_DIR + "/../Abilities"
ABILITY_TEMPLATE = ABILITY_FOLDER + "/ability_template.tex"
ABILTY_TARGET_FILE = ABILITY_FOLDER + "/ability_result.tex"
SCRIPT_ALL_ABILITIES = "AllAbilities"
SCRIPT_ID = "ability"

class Ability(Content):
    def __init__(self, file):
        Content.__init__(self, file)
        self.template_name = ABILITY_TEMPLATE
        self.id = SCRIPT_ID

    def template(self):
        return fill_template_lines(as_newcommand(read_file(self.template_name)), self.content)

ability_paths = find_files(ABILITY_FOLDER)
print(ability_paths)
abilities = []
for ability_path in ability_paths:
    if ability_path != ABILITY_TEMPLATE and ability_path != ABILTY_TARGET_FILE:
        abilities.append(Ability(ability_path))

write_result_file(abilities , SCRIPT_ALL_ABILITIES, ABILTY_TARGET_FILE)
