import os
from common import *


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
SECRET_FOLDER = FILE_DIR + "/../Secrets"
SECRET_TEMPLATE = SECRET_FOLDER + "/Secret.tex"
SECRET_NAME_TEMPLATE = SECRET_FOLDER + "/SecretName.tex"
SECRET_TARGET_FILE = SECRET_FOLDER + "/.secret_result.tex"
SCRIPT_TAG_SECRETS = "%1Secrets"
SCRIPT_ID = "secret"

class Ability(Content):
    def __init__(self, file):
        self.template_names = [SECRET_TEMPLATE, SECRET_NAME_TEMPLATE]
        self.id = SCRIPT_ID
        Content.__init__(self, file)

ability_paths = find_files(SECRET_FOLDER)
print(ability_paths)
abilities = []
for ability_path in ability_paths:
    if ability_path != SECRET_TEMPLATE and ability_path != SECRET_TARGET_FILE and ability_path != SECRET_NAME_TEMPLATE:
        abilities.append(Ability(ability_path))

write_result_file(abilities, SCRIPT_TAG_SECRETS, SECRET_TARGET_FILE)
