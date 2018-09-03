import docs
import sh
import os
import sys
from colorama import Fore
from jinja2 import Environment, PackageLoader

class Templater:

    def __init__(self, dest,doc_type,doc_args, project_name):
        env = Environment(loader=PackageLoader('docs','templates'))
        self.template = env.get_template(doc_type)
        self.dest = dest
        self.project_name = project_name
        self.doc = getattr(docs,doc_type)(**doc_args)
        self.temp_path = '~/.tmp/asciidoc/'+self.project_name

    def run(output_type):
        try:
            if os.path.exists(self.temp_path):
                os.makedirs(self.temp_path)
            os.chdir(self.temp_paths)
            template_info = self.template.collect_vars()
            with open('output.adoc','w') as output_file:
                output_file.write(self.template.render(**template_info))
            sh.asciidoc('--doctype=article','--backend=docbook45','output.adoc')
            if output_type == 'pdf':
                output_type = 'latex'
            sh.pandoc('--from=docbook','--to='+output_type,'--output='+self.dest,'output.xml')
        except IOError:
            print(Fore.RED+'No permission to create/access',self.temp_path,file=sys.stdout)
            sys.exit(1)
        except sh.ErrorReturnCode as error:
            print(Fore.RED+'Error Running asciidoc/pandoc',file=sys.stderr)
            print(Fore.RED+'stdout:',error.stdout)
            sys.exit(1)



