import json

myKey = ['mal_id', 'url', 'image_url', 'trailer_url', 'title', 'title_en', 'title_jp', 'title_synonyms', 'type', 'source', 'episodes', 'status', 'airing', 'aired_start', 'aired_end', 'premiered', 'broadcast', 'episode_duration', 'synopsis', 'background', 'mal_rating', 'mal_score', 'mal_reviewer', 'mal_rank', 'mal_popularity', 'mal_members', 'mal_favorites', 'related', 'producers', 'licensors', 'studios', 'genres', 'opening_themes', 'ending_themes']

def readJsonFile(fname):
  s = open(fname).read()
  ss = json.loads(s)
  return ss

def menuOne(ss):
  print(len(ss))

def menuTwo(ss, p, q, startchar):
  for i in range(p, q+1):
    if ss[i]['title'][0] == startchar:
      print(f"{i} : {ss[i]['title']}")

def menuThree(ss, p, q, mtype):
  count, myMaxScore, myMaxFav = 0, -999, -999
  for i in range(p, q+1):
    if ss[i]['type'] == mtype:
      count += 1
      try:
        sc, fv = float(ss[i]['mal_score']), float(ss[i]['mal_favorites'])
      except TypeError as e:
        continue
      if sc > myMaxScore:
        myMaxScore = sc
      if fv > myMaxFav:
        myMaxFav = fv
  print(f'{mtype} : {count}')
  sc, fav = False, False
  for i in range(p, q+1):
    if not sc and float(ss[i]['mal_score']) == myMaxScore:
      print(f"Most scores: {ss[i]['title']}")
      sc = True
      if sc and fav:
        break
    if not fav and float(ss[i]['mal_favorites']) == myMaxFav:
      print(f"Most favorites: {ss[i]['title']}")
      fav = True
      if sc and fav:
        break
  
def menuFour(ss, p, q, source, status, malSc):
  #p,q = 0,20
  #source, status = 'Manga', 'Finished Airing'
  #malSc = 8
  for i in range(p, q+1):
    try:
      if ss[i]['source'] == source and ss[i]['status'] == status and float(ss[i]['mal_score']) > malSc: 
        print(f"{i:<2}: {ss[i]['title']}")
    except TypeError as e:
      continue

def menuFive(ss, p, q, season):
  #p,q = 0,20
  #season = 'Fall'
  res = 0
  for i in range(p,q+1):
    try:
      sea = ss[i]['premiered'].split()[0].strip()
    except AttributeError as e:
      continue
    if sea == season:
      res += 1
  print(f'{season} : {res}')

def menuSix(ss, p, q):
  #p,q = 0,20
  airedStart,airedEnd,sameYear = [],[],0
  #for i in range(len(ss)):
  for i in range(p,q+1):
    airs = ss[i]['aired_start']
    aire = ss[i]['aired_end']
    if airs not in airedStart:
      airedStart.append(airs)
    if aire not in airedEnd:
      airedEnd.append(aire) 
    try: 
      if airs.split('-')[0]==aire.split('-')[0]:
        sameYear += 1
    except AttributeError as e:
      continue
  #print(airedStart[:10])
  #print(airedEnd[:10])
  print(f'Find: {sameYear}')

def menuSeven(ss, title):
  #title = 'Naruto'
  for i in ss:
    if i['title'] == title:
      print(i['mal_rating'])

def menuEight(ss, p, q):
  #p,q = 0,20
  syn = []
  for i in range(p, q+1):
    try:
      nbWords = len(ss[i]['synopsis'].split(' '))
    except AttributeError as e:
      continue
    if nbWords not in syn:
      syn.append(nbWords)
  myMax = sorted(syn,reverse=True)[0]
  for i in range(p, q+1):
    try:
      nbWords = len(ss[i]['synopsis'].split(' '))
    except AttributeError as e:
      continue
    if nbWords==myMax:
      print(f'{i} : {ss[i]["title"]}') 

### main begins here
#fname = input('Filename : ')
fname = 'MyAnimeList_Anime_2021_05_16.json'
ss = readJsonFile(fname)

## Note that we will first observe/filter the corresponding json fields
## that can help answering the question, and then develop the step by step
## answer to the solution.
## Ref: https://elab.cpe.ku.ac.th/elab/lab/1023/12027/

#menuOne(ss)
#menuTwo(ss, 0, 20, 'N')
#menuThree(ss, 0, 20, 'TV')
#menuFour(ss, 0, 20, 'Manga', 'Finished Airing', 8)
#menuFive(ss, 0, 20, 'Fall')
#menuSix(ss,0,20)
#menuSeven(ss, 'Naruto')
menuEight(ss, 0, 20)
