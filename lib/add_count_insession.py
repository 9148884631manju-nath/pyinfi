def add_count_insession(s,v):
 res=""
 skey=v.get("skey")
 sid=v.get("sid")
 samn=v.get("samn")
 sqty=v.get("sqty")
 sadto=v.get("sadto")
 sact=v.get("sact")
 if sact=="yes":
  tot = int(s.get(skey)[sid][samn]) * int(sqty)
  s[sadto]=tot
  res=str(tot)
 else:
  s[sadto]=sqty
  res="0"
 return res