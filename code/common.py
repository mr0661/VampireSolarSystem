import os

SCRIPT = ":script:"
NAME = ":name:"
POOL = ":pool:"
POOL_SHORT = ":p:"
CORE_TEXT = ":coretxt:"
NEWCOMMAND_START="\\newcommand{\\" + SCRIPT + "}{";
NEWCOMMAND_END="}";
ENDLINE = "\n"

def find_files(path):
    all_files = []
    for r, d, files in os.walk(path):
        for file in files:
            all_files.append(r + "/" + file)
    return all_files

def read_file(path):
    f = open(path, "r")
    return f.readlines()

def as_newcommand(lines):
    return [NEWCOMMAND_START] + lines + [NEWCOMMAND_END]

class Content:
    def __init__(self, file):
        print("create " + file)
        self.file = file
        self.parse()

    def parse(self):
        self.content = {}
        lines = read_file(self.file)
        context = ""
        for line in lines:
            line = line.rstrip()

            if not line:
                continue
            elif line[0] == ":":
                context = line.lower()
                continue
            elif line[0] == "#":
                continue

            if context:
                if context == SCRIPT:
                    self.content[context] = [self.id + line]
                elif context in self.content:
                    self.content[context].append(line)
                else:
                    self.content[context] = [line]

    def get(self, context):
        if not context in self.content:
            return []
        return self.content[context.lower()]

    def template(self):
        return []

    def script(self):
        if self.get(SCRIPT):
            return "\\" + self.get(SCRIPT)[0] + "{}"
        return ""

    def template(self):
        return fill_template_lines(as_newcommand(read_file(self.template_name)), self.content)

def print_ability(content):
    name = content.get(NAME)
    pool = content.get(POOL)
    p = content.get(POOL_SHORT)
    core_txt = content.get(CORE_TEXT)
    if name:
        print(name[0])
    if pool:
        print(pool[0] + "(" + p[0] + ")")
    for txt in core_txt:
        print(txt)

def fill_template_lines(template_lines, content):
    new_lines = []
    for line in template_lines:
        line = line.rstrip()
        new_line = line
        for key, values in content.items():
            if values:
                new_line = new_line.replace(key, " ".join(values))
        if new_line and new_line != line and new_line[0] == "%":
            new_line = new_line[1:]
            print(new_line)
        new_lines.append(new_line)
    return new_lines

def fill_template(template, content):
    lines = read_file(template)
    return fill_template_lines(lines, content)

def write_result_file(contents, all_script, target_file):
    scripts = []
    commands = []
    for content in contents:
        scripts.append(content.script())
        print(content.script())
        commands.append(ENDLINE.join(content.template()))
    lines = [NEWCOMMAND_START.replace(SCRIPT, all_script)]
    for script in scripts:
        lines.append(script)
    lines.append(NEWCOMMAND_END)

    for command in commands:
        lines.append(command)

    f = open(target_file, "w")
    f.write(ENDLINE.join(lines))
