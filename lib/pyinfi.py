# PYINFI V 01 (2026 May) 
# A Web Application Framework for Developers to develop N number of Micro Services, Addons, Tools etc...
# No Need of Learning Core Python, a universal Language JSON is UI/UX and Backend
# All Rights Reserved by Manjunath K, Code Designer 9343945143
from http.cookies import SimpleCookie
import requests
from lib.read_json import rjson
from lib.add_count_insession import add_count_insession
class PYINFI:
 def __init__(self,pd,host,fl,path,headers,reqs,sxs):
  self.ss = sxs
  self.pd = pd
  self.host=host
  self.path=path
  self.headers=headers
  self.reqs=reqs
  self.sxs=sxs
  self.fl = fl
  conf="lib/config.json"
  da = rjson(conf)
  self.app_url = da["app_url"]
  

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
    match k:
     case "src":
      res+=k+'="'+self.app_url+v+'" '
     case _:
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
  return ses
 
 def add_delim(self,v):
  res=""
  content=v.get("content","")
  splix=v.get("splix","")
  adsplix=v.get("adsplix","")
  dfor=v.get("dfor","")
  delim=v.get("delim","")
  vars=v.get("vars","")
  theme=v.get("theme","")
  if splix=="":
   res=content.replace(dfor,delim)
  else:
   ex=content.split(splix)
   for i,da in enumerate(ex):
    res+=da.replace(dfor,delim)+adsplix
   adlen = len(adsplix)
  return res[:-adlen]

 def a(self,v):
  res='<a '+self.get_attr(v,["content"])+'>'+v.get("content")+'</a>'
  return res
 def img(self,v):
  res='<img '+self.get_attr(v,["content"])+' />'
  return res

 def aimg(self,v):
  res=""
  ha=v.get("a")
  hi=v.get("image")
  res='<a '+self.get_attr(ha,["content"])+'>'+'<img '+self.get_attr(hi,["content"])+' /> '+ha.get("content")+'</a>'
  return res
 
 def apicall(self,v):
  res=""
  url=v.get("url")
  xheaders = v.get("get")
  xdata = dict(v.get("jd"))
  res = requests.get(url, headers=xheaders, data=xdata)
  return str(res)
 
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
     res+=self.a(v)
    case "add_count_insession":
     res+=add_count_insession(self.ss,v)
    case "add_delim":
     res+=self.add_delim(v)
    case "aimg":
     res+=self.aimg(v)
    case "apicall":
     res+=self.apicall(v)
    case "block":
     res+=self.html(v+".json")
    case "content":
     res+=v
    case "setsession":
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