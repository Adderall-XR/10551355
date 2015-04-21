import re
from random import shuffle

minlen = 3 #it's better this way
NUMBER_OF_WORDS = 50

subs = [
	#almost entirely senseless variation
	('sics', '6'),
	('nein', '9'),
    ('ue', '00'),
    ('ah', '44'),
    ('ew', '300'),
    ('owe', '0'),
    ('oh', '0'),
    ('oe', '0'),
    #numberHomophones:number
    ('won', '1'),
	('too', '2'),
    ('to', '2'),
    ('for', '4'),
    #('fore', '4'), #fore is represented as 43
    ('ate', '8'),
    #number spelt in word:number(s) - Theoretically infinite
    ('one', '1'),
	('two', '2'),
	('three', '3'),
    ('four', '4'),
	('five', '5'),
	('six', '6'),
	('seven', '7'),
	('eight', '8'),
    ('nine', '9'),
    ('ten', '10'),
    #increase in complexity/bizzareness (don't actually do anything)
    #('eleven', '11'),
    #('twelve', '12'),
    #('thirteen', '13'),
    #('fourteen', '14'),
    #1:1 letter:number(s)
	('b', '13'), #adds complication
	('z', '2'),
    ('g', '6'),
    ('l', '1'),
    ('o', '0'),
    ('s', '5'),
    ('t', '7'),
    ('e', '3'),
    ('a', '4'),
]

reHexWord = re.compile("[0-9]*")
gue = re.compile("gue") #removing phonetically dissimlar 'ue's
fWords = open('/usr/share/dict/words', 'r')
output = open("output.html", 'w')
output.write("""<html>
					<style>	.spoiler{
								color:white;}
							.pure-button{
								font-family: inherit;
								font-size: 100%;
								padding: .5em 1em;
								color: #444;
								color: rgba(0,0,0,.8);
								border: 1px solid #999;
								border: 0 rgba(0,0,0,0);
								background-color: #E6E6E6;
								text-decoration: none;
								border-radius: 2px;
								position: fixed;
								margin-right:5px;}
							.pure-button:active{
								background-color:red;}
							#ian{
								right: 60;
							}
							#will{
								right: 150;
							}
							#fin{
								right: 0;
							}
					</style>
					<script>
						var willScore = 0;
						var ianScore = 0;
						function ian()
						{
							++ianScore;
						}
						function will()
						{
							++willScore;
						}
						function show()
						{
							alert("Will scored " + willScore.toString() + "; Ian scored " + ianScore.toString());
						}
					</script>
					<a href="#" id="fin" class="pure-button" onclick="show()">
						end
					</a>
					<a href="#" id="will" class="pure-button" onclick="will()">
						willPoint
					</a>
					<a href="#" id="ian" class="pure-button" onclick="ian()">
						ianPoint
					</a>
					<table  border=1 frame=void rules=rows>""")
end = []
for w in fWords.xreadlines():
    w = w.strip()
    z = w
    for old, new in subs:
        w = w.replace(old, new)
    if len(w) >= minlen:
        match = reHexWord.search(w)
        if match and match.group() == w and not gue.search(z):
            end.append("<td class=\"spoiler\" onclick=\"this.style.color=\'black\'\">%s </td><td> %s </td>\n" % (z,w))
output.write("There were %d words; here are %d:" % (len(end), NUMBER_OF_WORDS))
shuffle(end) #If you've seen the list, it's no longer a game
output.write("".join(["<tr id=\"%d\"><td>%d</td>%s</tr>" % (i+1, i+1, j) for i, j in enumerate(end)][:NUMBER_OF_WORDS]))
output.write("</table></html>")
