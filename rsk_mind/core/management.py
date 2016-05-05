import argparse, jinja2, os, rsk_mind


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.PackageLoader('rsk_mind', 'conf'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def startapp(project_name):
    tmpls = ['manager.jinja2', 'transformer.jinja2', 'setting.jinja2']
    for tmpl in tmpls:
        template = JINJA_ENVIRONMENT.get_template('project_template/%s' % tmpl)

        print template.render()

def execute_from_command_line(argv):
    argv = argv[1:]

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('command', help='Command to execute!')
    parser.add_argument('project_name', help='')
    params = parser.parse_args(argv)

    if params.command == 'startapp':
        startapp(params.project_name)
    else:
        pass
