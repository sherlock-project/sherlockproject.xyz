# clone the https://github.com/sherlock-project/sherlock-project.github.io
# git clone:github.com/sherlock-project/sherlock.gi
# change the working directory to sherlock
# cd sherlock https://github.com/sherlock-project/sherlock-project.github.io
# install the requirements
# python3 -m pip install -r requirements.txt
# python3 sherlock georgia.is.onmymind visuals.by.georgia --nsfw

from enum import Enum
class QueryResult():
     def _init_ (self, username, site_name, site_url_user, status, query_time=None,context=None):                                                                  
         class QueryStatus(Enum):
            def _str_ (self):
                return self.value