import os
from common import *


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
ABILITY_FOLDER = FILE_DIR + "/../Abilities"
#ABILITY_TEMPLATE = ABILITY_FOLDER + "/ability_template.tex"
#ABILITY_NAME_TEMPLATE = ABILITY_FOLDER + "/ability_name_template.tex"
ABILITY_TEMPLATE = ABILITY_FOLDER + "/Ability.tex"
ABILITY_NAME_TEMPLATE = ABILITY_FOLDER + "/AbilityName.tex"
ABILTY_TARGET_FILE = ABILITY_FOLDER + "/.ability_result.tex"
SCRIPT_TAG_ABILITIES ="%1Abilities"
SCRIPT_ID = "ability"

class Ability(Content):
    def __init__(self, file):
        self.template_names = [ABILITY_TEMPLATE, ABILITY_NAME_TEMPLATE]
        self.id = SCRIPT_ID
        Content.__init__(self, file)

ability_paths = find_files(ABILITY_FOLDER)
print(ability_paths)
abilities = []
for ability_path in ability_paths:
    if ability_path != ABILITY_TEMPLATE and \
       ability_path != ABILTY_TARGET_FILE and \
       ability_path != ABILITY_NAME_TEMPLATE:
        abilities.append(Ability(ability_path))
abilities.sort()
write_result_file(abilities , SCRIPT_TAG_ABILITIES, ABILTY_TARGET_FILE)
