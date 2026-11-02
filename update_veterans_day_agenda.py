from pathlib import Path
import re,sys
p=Path(sys.argv[1] if len(sys.argv)>1 else 'index.html')
s=p.read_text(encoding='utf-8')
start=s.index('<div class="ceremony-grid">',s.index('id="program"'))
end=s.index('</div></div></section>',start)
first=re.findall(r'<article class="ceremony-card reveal">.*?</article>',s[start:end],re.S)[:2]
if len(first)!=2: raise ValueError('Unable to locate original first two ceremony entries')
first[0] = first[0].replace('<h3>Welcome &amp; Invocation</h3>', '<h3>Welcome</h3>').replace('<h3>Welcome & Invocation</h3>', '<h3>Welcome</h3>').replace('<p>Opening remarks and a moment of reflection.</p>', '<p>Opening welcome to guests, veterans, and the Callaway community.</p>')
data=[('Invocation','Cadet Major Keelonna Sanders'),('Welcome Remarks','Cadet Lieutenant Colonel Makayla Baldwin'),('JROTC Creed','Cadet Lieutenant Colonel Makayla Baldwin'),('Musical Selection','CHS Choir'),('Guest Speaker Introduction','Cadet Maliya Harris'),('Guest Speaker Remarks','Honorable Eleanor Faye Peterson'),('Guest Speaker Appreciation','Cadet Lieutenant Colonel Makayla Baldwin'),('Recognition of Veterans',"Cadet Ja’Miyah Allen"),('Recognition of Adventure Training Cadets',''),('Recognition of Battalion Staff',"Cadet Ja’Miyah Allen"),('Taps – Moment of Silence','')]
from html import escape
cards=[]
for n,(title,presenter) in enumerate(data,3):
    stage='Closing' if n==13 else ('Recognition' if n>=9 else 'Program')
    cards.append(f'<article class="ceremony-card reveal"><span class="card-time">{stage}</span><h3>{escape(title)}</h3><p>{escape(presenter) if presenter else "&nbsp;"}</p><span class="card-index">{n}</span></article>')
new='<div class="ceremony-grid">'+''.join(first+cards)
p.write_text(s[:start]+new+s[end:],encoding='utf-8')
print('Updated',p,'with 13 agenda entries.')
