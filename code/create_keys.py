import os
from common import *


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
KEY_FOLDER = FILE_DIR + "/../Keys"
KEY_TEMPLATE = KEY_FOLDER + "/key_template.tex"
KEY_TARGET_FILE = KEY_FOLDER + "/key_result.tex"
SCRIPT_ALL_KEYS = "AllKeys"
SCRIPT_ID = "key"

class Ability(Content):
    def __init__(self, file):
        Content.__init__(self, file)
        self.template_name = KEY_TEMPLATE
        self.id = SCRIPT_ID

    def template(self):
        return fill_template_lines(as_newcommand(read_file(self.template_name)), self.content)

ability_paths = find_files(KEY_FOLDER)
print(ability_paths)
abilities = []
for ability_path in ability_paths:
    if ability_path != KEY_TEMPLATE and ability_path != KEY_TARGET_FILE:
        abilities.append(Ability(ability_path))

write_result_file(abilities, SCRIPT_ALL_KEYS, KEY_TARGET_FILE)
