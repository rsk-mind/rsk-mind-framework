import argparse, jinja2, os, rsk_mind


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.PackageLoader('rsk_mind', 'conf'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def startapp(project_name):
    top_dir = os.path.join(os.getcwd(), project_name)
    if not os.path.exists(top_dir):
        os.makedirs(top_dir)
    else:
        pass

    tmpls = ['manager.py.jinja2', 'transformer.py.jinja2', 'setting.py.jinja2']
    for tmpl in tmpls:
        content = JINJA_ENVIRONMENT \
            .get_template('project_template/%s' % tmpl).render()

        with open(os.path.join(top_dir, tmpl.replace('.jinja2', '')), 'w') as outfile:
            outfile.write(content)

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
