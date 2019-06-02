import os
import inspect


SCRIPT = ":script:"
NAME = ":name:"
POOL = ":pool:"
TAGS = ":tags:"
POOL_SHORT = ":p:"
CORE_TEXT = ":coretxt:"
ALL_TAG = "All"
NEWCOMMAND_START="\\newcommand{\\" +"%1"+ "}{";
NEWCOMMAND_END="}";
ENDLINE = "\n"

def debug(*message):
    m_str = ""
    for m in message:
        m_str += str(m)
        m_str += " "
    print ("D " + file_name(str(inspect.currentframe().f_back.f_code.co_filename)) + " " + str(inspect.currentframe().f_back.f_lineno).rjust(3) + ": " + m_str.strip())

def file_name(path):
    return path[(path.rfind("/") + 1):]

def file_base(path):
    return path[(path.rfind("/") + 1): (path.rfind("."))]


def find_files(path):
    all_files = []
    for r, d, files in os.walk(path):
        for file in files:
            all_files.append(r + "/" + file)
    return all_files

def read_file(path):
    f = open(path, "r")
    return f.readlines()

def as_newcommand(lines, script = SCRIPT):
    return [NEWCOMMAND_START.replace("%1", script)] + lines + [NEWCOMMAND_END]


class Content:
    def __init__(self, file):
        debug("create " + file)
        self.file = file
        self.template_context = {}
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
        for template_name in self.template_names:
            templateContext = ":" + file_base(template_name).lower() + ":"
            debug(templateContext)
            if not templateContext in self.content:
                self.template_context[template_name] = templateContext
                debug("id:" , self.id)
                debug("file:" , file_name(self.file))
                scriptName = file_base(template_name) + file_name(self.file).replace("_", "").replace(" ", "")
                self.content[templateContext] = [scriptName]
                debug("templateContext:", templateContext)
                debug("script:", scriptName)

    def get(self, context):
        if not context.lower() in self.content:
            return []
        return self.content[context.lower()]

    def template(self):
        return []

    def script(self, target_template):
        debug("target_template:", target_template)
        tmp = ":" + target_template + ":"
        if self.get(tmp):
            return "\\" + self.get(tmp)[0] + "{}"
        return ""

    def templates(self):
        templates = []
        for template_name in self.template_names:
            templates.append(file_base(template_name))
        return templates;

    def template(self):
        template = []
        for template_name in self.template_names:
            debug("tempContext:" ,self.template_context[template_name])
            template += fill_template_lines(as_newcommand(read_file(template_name), self.template_context[template_name]), self.content)
        return template

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
            debug(new_line)
        new_lines.append(new_line)
    return new_lines

def fill_template(template, content):
    lines = read_file(template)
    return fill_template_lines(lines, content)

def write_result_file(contents, tag_script, target_file):
    lines = []
    commands = []
    collectionScripts = {}
    tags = {ALL_TAG: []}
    for content in contents:
        commands.append(ENDLINE.join(content.template()))
        for t in content.templates():
            debug(t)
            if not t in collectionScripts:
                collectionScripts[t] = {}

        for tag in content.get(TAGS):
            if not tag in tags:
                tags[tag] = []
            tags[tag].append(content)
        tags[ALL_TAG].append(content)
    debug("collectionScript")
    for collectionScript in collectionScripts:
        debug(collectionScript)
        for tag, contents in tags.items():
            lines.append(NEWCOMMAND_START.replace("%1", tag + collectionScript))
            debug("for", tag, collectionScript)
            for content in contents:
                debug("ContentName:", content.get(":name:"))
                debug(content.get(":" + collectionScript + ":"))
                lines.append(content.script(collectionScript))
            lines.append(NEWCOMMAND_END)

    for command in commands:
        lines.append(command)

    f = open(target_file, "w")
    f.write(ENDLINE.join(lines))