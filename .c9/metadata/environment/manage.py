{"filter":false,"title":"manage.py","tooltip":"/manage.py","undoManager":{"mark":12,"position":12,"stack":[[{"start":{"row":5,"column":3},"end":{"row":5,"column":68},"action":"remove","lines":[" os.environ.setdefault(\"DJANGO_SETTINGS_MODULE\", \"blog.settings\")"],"id":2},{"start":{"row":5,"column":3},"end":{"row":5,"column":69},"action":"insert","lines":["  os.environ.setdefault(\"DJANGO_SETTINGS_MODULE\", \"blog.settings\")"]}],[{"start":{"row":5,"column":69},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":6,"column":0},"end":{"row":6,"column":5},"action":"insert","lines":["     "]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"remove","lines":[" "],"id":4},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"remove","lines":["    "]},{"start":{"row":5,"column":69},"end":{"row":6,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":5,"column":69},"end":{"row":5,"column":70},"action":"insert","lines":[":"],"id":5}],[{"start":{"row":5,"column":69},"end":{"row":5,"column":70},"action":"remove","lines":[":"],"id":6}],[{"start":{"row":5,"column":69},"end":{"row":5,"column":70},"action":"insert","lines":[";"],"id":7}],[{"start":{"row":5,"column":69},"end":{"row":5,"column":70},"action":"remove","lines":[";"],"id":8}],[{"start":{"row":5,"column":69},"end":{"row":5,"column":70},"action":"insert","lines":[","],"id":9}],[{"start":{"row":5,"column":69},"end":{"row":5,"column":70},"action":"remove","lines":[","],"id":10}],[{"start":{"row":5,"column":69},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":6,"column":0},"end":{"row":6,"column":5},"action":"insert","lines":["     "]}],[{"start":{"row":6,"column":4},"end":{"row":7,"column":4},"action":"remove","lines":[" ","    "],"id":12}],[{"start":{"row":4,"column":26},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":0,"column":0},"end":{"row":23,"column":0},"action":"remove","lines":["#!/usr/bin/env python","import os","import sys","","if __name__ == \"__main__\":","    ","     os.environ.setdefault(\"DJANGO_SETTINGS_MODULE\", \"blog.settings\")","    try:","        from django.core.management import execute_from_command_line","    except ImportError:","        # The above import may fail for some other reason. Ensure that the","        # issue is really that Django is missing to avoid masking other","        # exceptions on Python 2.","        try:","            import django","        except ImportError:","            raise ImportError(","                \"Couldn't import Django. Are you sure it's installed and \"","                \"available on your PYTHONPATH environment variable? Did you \"","                \"forget to activate a virtual environment?\"","            )","        raise","    execute_from_command_line(sys.argv)",""],"id":14},{"start":{"row":0,"column":0},"end":{"row":21,"column":39},"action":"insert","lines":["#!/usr/bin/env python","import os","import sys","","if __name__ == \"__main__\":","    os.environ.setdefault(\"DJANGO_SETTINGS_MODULE\", \"blog.settings\")","    try:","        from django.core.management import execute_from_command_line","    except ImportError:","        # The above import may fail for some other reason. Ensure that the","        # issue is really that Django is missing to avoid masking other","        # exceptions on Python 2.","        try:","            import django","        except ImportError:","            raise ImportError(","                \"Couldn't import Django. Are you sure it's installed and \"","                \"available on your PYTHONPATH environment variable? Did you \"","                \"forget to activate a virtual environment?\"","            )","        raise","    execute_from_command_line(sys.argv)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":21,"column":39},"end":{"row":21,"column":39},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":5,"state":"start","mode":"ace/mode/python"}},"timestamp":1569270686535,"hash":"bccbf73d70eb64dc392220f911fa17196a336c81"}