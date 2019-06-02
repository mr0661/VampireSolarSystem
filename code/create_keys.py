import os
from common import *


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
KEY_FOLDER = FILE_DIR + "/../Keys"
KEY_TEMPLATE = KEY_FOLDER + "/Key.tex"
KEY_NAME_TEMPLATE = KEY_FOLDER + "/KeyName.tex"
KEY_TARGET_FILE = KEY_FOLDER + "/.key_result.tex"
SCRIPT_TAG_KEYS = "%1Keys"
SCRIPT_ID = "key"

class Ability(Content):
    def __init__(self, file):
        self.template_names = [KEY_TEMPLATE, KEY_NAME_TEMPLATE]
        self.id = SCRIPT_ID
        Content.__init__(self, file)

ability_paths = find_files(KEY_FOLDER)
print(ability_paths)
abilities = []
for ability_path in ability_paths:
    if ability_path != KEY_TEMPLATE and ability_path != KEY_TARGET_FILE and ability_path != KEY_NAME_TEMPLATE:
        abilities.append(Ability(ability_path))

write_result_file(abilities, SCRIPT_TAG_KEYS, KEY_TARGET_FILE)
