from http.cookies import SimpleCookie
from lib.read_json import rjson
from lib.add_count_insession import add_count_insession
import requests
from http.cookies import SimpleCookie
import uuid
import urllib.parse
import pprint

SESSION_STORAGE = {}

class PYINFI:
 def __init__(self,fl,path,headers,reqs,ses):
  self.ss = requests.Session()
  self.path=path
  self.headers=headers
  self.reqs=reqs
  self.ses=ses
  self.fl = fl
  self.ss={}

 def __str__(self):
  return self.html(self.fl)
 
 def html(self,f):
  da=rjson(f)
  res=""
  for i, itm in enumerate(da):
   res+=self.render_html(itm)
  return res
 
 def get_attr(self,attr,ary):
  res=""
  for k,v in attr.items():
   if k in ary:
    res+=""
   else:
    res+=k+'="'+v+'" '
  return res
 
 def setsession(self,v):
  res=""
  sty = v.get("sty")
  ses = v.get("ses")
  sva = v.get("sva")
  for i,itm in enumerate(sty):
   match itm:
    case "set":
     self.ss[ses[i]] = sva[i]
    case _:
     if ses[i] in self.ss:
      del self.ss[ses[i]]
  return res
 
 def viewheaders(self):
  hos = str(self.headers.get("host"))
  pat = str(self.path)
  hed = str(self.headers)
  ses = str(self.ss)
  req = str(self.reqs)
  return "path: "+hos+pat+"<hr/>Requests : "+req+"<hr/>Sessions : "+ses+"<hr/>All Headers : "+hed
 
 def viewsessions(self,v):
  ses = str(self.ss.get(v))
  return "Sessions : "+ses
 
 def render_html(self,itm):
  res="" 
  attr=""
  if itm.get("attr"):
   attr=self.get_attr(itm.get("attr"),[])
  else:
   attr=""

  if itm.get("class"):
   res='<div class="'+itm.get("class")+'" '+attr+' >'
  else:
   res=""

  for k,v in itm.items():
   match k:
    case "a":
     res+='<a '+self.get_attr(v,["content"])+'>'+v.get("content")+'</a>'
    case "add_count_insession":
     session = requests.Session()
     res+=add_count_insession(session,v)
    case "block":
     res+=self.html(v+".json")
    case "content":
     res+=v
    case "setsession":
     session = requests.Session()
     res+=self.setsession(v)
    case "viewsessions":
     res+=self.viewsessions(v)
    case "viewheaders":
     res+=self.viewheaders()
    case _:
     res+=""
  if itm.get("class"):
   res+='</div>'
  else:
   res+=""

  return res  