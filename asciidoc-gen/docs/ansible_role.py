import sys
from colorama import Fore
import yaml
import os

class ansible_role:
    schema = {
        'variables':{
            'type':dict,
            'schema':{
                'name': str,
                'type': ['optional','required','override'],
                'description'
            },
        }
        'example':{
            'type':str
        },
        'notes':{
            'type':str
        }
    }
    
    example_playbook = '/meta/documentation.yml'

    def __init__(self,location):
        self.location = location    

    # collect and return a dict of comments ready to be templated into asciidocs
    def collect_vars(self):
        with open(self.location+self.example_playbook) as docs:
            documentation = yaml.safe_load(docs)
        self.verify_schema(documentation, documentation.keys())
    # 
    def verify_schema(self,level_keys,top_level_key,recurse=False):
        for schema in level_keys:
            if type(schema['type']) == dict:
                self.verify_schema(self.schema[].keys(),schema,recurse=True)
            elif type(documentation[schema]) == type(self.schema[top_level_key][schema] and recurse):
                print(Fore.GREEN+'[*]SCHEMA: '+schema,'VALID')
            elif type(documentation[schema]) == type(self.schema[schema] and not recurse):
                print(Fore.GREEN+'[*]SCHEMA: '+schema,'VALID')
            else:
                print(Fore.RED+'[*]SCHEMA:'+schema,'INVALID!',file=sys.stderr)
                sys.exit(1)
