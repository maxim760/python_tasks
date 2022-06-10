def main(str):
  replaced = str\
    .replace("<section> make", "")\
    .replace("<section> make", "")\
    .replace("</section>", "")\
    .replace("{", "")\
    .replace("}", "")\
    .replace("\n", "")\
    .replace("`", "")
  items = list(filter(lambda x: x != "", map(lambda x: x.strip(), replaced.split(";"))))
  res = {}
  for item in items:
    [value, key] = list(map(lambda x: x.strip(), item.split("=:")))
    res[key] = value
  return res

def var22(str):
  replaced = str\
    .replace(".do equ @", "")\
    .replace("||", "")
  items = list(filter(lambda x: x != "", map(lambda x: x.strip(), replaced.split(".end"))))
  res = {}
  for item in items:
    [key, data] = list(map(lambda x: x.strip(), item.split("::=")))
    key = key[1:-1]
    res[key] = []
    data = data[1:-1]
    data = data.strip()
    items = list(map(lambda x: int(x.strip()[1:]), data.split(",")))
    res[key] = items
  return res

res = var22("""|| .do equ @"gece_193" ::=[ #-9777,#230 ] .end .do equ @"aen_621" ::=[
#3654 , #504, #-2841, #9290 ] .end .do equ @"aleat" ::= [ #-9579 ,
#9596 , #7010, #3540 ] .end .do equ @"tein_351"::= [#1863, #7927
,#9600 ] .end||""")
print(res)
