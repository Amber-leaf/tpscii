# tpscii
The Toki Pona standard code for information interchange.   
(note that this document is correctly formated in raw text mode)

## Premise
This document outlines a standard for computer communications using the constructed language [Toki Pona](https://sona.pona.la/wiki/Toki_Pona). It is primarily focused on the transmission and display of the *[sitelen pona](https://sona.pona.la/wiki/sitelen_pona)* writing system.

## Description
sitelen pona is a logographic writing system, so each word comprises one character. This, along with the fact that Toki Pona contains only around 200 "common" words at the most extreme makes it ideal for encoding with a single byte per word. However, problems arise from the *[nimi sin](https://sona.pona.la/wiki/nimi_sin)*, community created words. There are an astronomically large number of mostly unused and forgotten nimi sin that have been created over Toki Pona's 20+ year history, but any protocol would do well to support them. Thus, the naive implementation of each "commonly used" word getting a byte could fail to represent even common texts 5 years from now, if the number of common nimi sin grows significantly. However, this is not a particularly likely outcome, so any method of encoding nimi sin should not add significant complexity or require too much transmission time. I have thus decided to use a 1-byte shift and 2-byte selector sequence, which could be easily expanded upon if required but already allows for `0xff` * USHRT_MAX (16711425) possible nimi sin.
Proper nouns are handled by the "proper noun mode" control code `0xfe`. It is relatively equivalent to an open / close cartouche in normal sitelen pona. See the control code section for more details.


Core vs. Common vs. Uncommon was determined from [lipu Linku](https://api.linku.la/v1/words), a statistical tool and database for Toki Pona.

## Standard
The encoding is as follows.  

Standard ASCII control codes and punctuation (0x00 - 0x3f)    

NUL                   -> 0x00   
SOH                   -> 0x01           
STX                   -> 0x02  
...   
\=                    -> 0x3d    
\>                    -> 0x3e     
\?                    -> 0x3f    

Latin Symbols (0x40 - 0x50)  
@                    -> 0x40  
\[                   -> 0x41  
\]                   -> 0x42  
\\                   -> 0x43  
\-                   -> 0x44  
\`                   -> 0x45  
\{                   -> 0x46  
\|                   -> 0x47  
\}                   -> 0x48  
~                    -> 0x49  
DEL                  -> 0x50  

Core words: (0x51 - 0xc5)  
a                    -> 0x51  
akesi                -> 0x52  
ala                  -> 0x53  
alasa                -> 0x54  
ale                  -> 0x55  
anpa                 -> 0x56  
ante                 -> 0x57  
anu                  -> 0x58  
awen                 -> 0x59  
e                    -> 0x5a  
en                   -> 0x5b  
esun                 -> 0x5c  
ijo                  -> 0x5d  
ike                  -> 0x5e  
ilo                  -> 0x5f  
insa                 -> 0x60  
jaki                 -> 0x61  
jan                  -> 0x62  
jelo                 -> 0x63  
jo                   -> 0x64  
kala                 -> 0x65  
kalama               -> 0x66  
kama                 -> 0x67  
kasi                 -> 0x68  
ken                  -> 0x69  
kepeken              -> 0x6a  
kili                 -> 0x6b  
kiwen                -> 0x6c  
ko                   -> 0x6d  
kon                  -> 0x6e  
kule                 -> 0x6f  
kulupu               -> 0x70  
kute                 -> 0x71  
la                   -> 0x72  
lape                 -> 0x73  
laso                 -> 0x74  
lawa                 -> 0x75  
len                  -> 0x76  
lete                 -> 0x77  
li                   -> 0x78  
lili                 -> 0x79  
linja                -> 0x7a  
lipu                 -> 0x7b  
loje                 -> 0x7c  
lon                  -> 0x7d  
luka                 -> 0x7e  
lukin                -> 0x7f  
lupa                 -> 0x80  
ma                   -> 0x81  
mama                 -> 0x82  
mani                 -> 0x83  
mi                   -> 0x84  
moku                 -> 0x85  
moli                 -> 0x86  
monsi                -> 0x87  
mu                   -> 0x88  
mun                  -> 0x89  
musi                 -> 0x8a  
mute                 -> 0x8b  
nanpa                -> 0x8c  
nasa                 -> 0x8d  
nasin                -> 0x8e  
nena                 -> 0x8f  
ni                   -> 0x90  
nimi                 -> 0x91  
noka                 -> 0x92  
o                    -> 0x93  
olin                 -> 0x94  
ona                  -> 0x95  
open                 -> 0x96  
pakala               -> 0x97  
pali                 -> 0x98  
palisa               -> 0x99  
pan                  -> 0x9a  
pana                 -> 0x9b  
pi                   -> 0x9c  
pilin                -> 0x9d  
pimeja               -> 0x9e  
pini                 -> 0x9f  
pipi                 -> 0xa0  
poka                 -> 0xa1  
poki                 -> 0xa2  
pona                 -> 0xa3  
pu                   -> 0xa4  
sama                 -> 0xa5  
seli                 -> 0xa6  
selo                 -> 0xa7  
seme                 -> 0xa8  
sewi                 -> 0xa9  
sijelo               -> 0xaa  
sike                 -> 0xab  
sin                  -> 0xac  
sina                 -> 0xad  
sinpin               -> 0xae  
sitelen              -> 0xaf  
sona                 -> 0xb0  
soweli               -> 0xb1  
suli                 -> 0xb2  
suno                 -> 0xb3  
supa                 -> 0xb4  
suwi                 -> 0xb5  
tan                  -> 0xb6  
taso                 -> 0xb7  
tawa                 -> 0xb8  
telo                 -> 0xb9  
tenpo                -> 0xba  
toki                 -> 0xbb  
tomo                 -> 0xbc  
tu                   -> 0xbd  
unpa                 -> 0xbe  
uta                  -> 0xbf  
utala                -> 0xc0  
walo                 -> 0xc1  
wan                  -> 0xc2  
waso                 -> 0xc3  
wawa                 -> 0xc4  
weka                 -> 0xc5  
wile                 -> 0xc6  
  
0xc7 - 0xcf reserved.
  
Common words: (0xd0 - 0xdc)  
kijetesantakalu      -> 0xd0  
kin                  -> 0xd1  
kipisi               -> 0xd2  
ku                   -> 0xd3  
leko                 -> 0xd4  
meli                 -> 0xd5  
mije                 -> 0xd6  
misikeke             -> 0xd7  
monsuta              -> 0xd8  
n                    -> 0xd9  
namako               -> 0xda  
soko                 -> 0xdb  
tonsi                -> 0xdc  
  
0xdd - 0xe4 reserved.  
  
Uncommon words: (0xe5 - 0xee)  
ali                  -> 0xe5  
epiku                -> 0xe6  
jasima               -> 0xe7  
lanpan               -> 0xe8  
linluwi              -> 0xe9  
majuna               -> 0xea  
meso                 -> 0xeb  
nimisin              -> 0xec  
oko                  -> 0xed  
su                   -> 0xee  
  
0xef - 0xfd reserved.  
  
Control:  
Proper noun toggle   -> 0xfe  
This control code toggles "proper noun mode", in which each sent word is treated as a phoneme in a name.   
e.g, sending `0xb5` (suwi), `0xfe` (proper noun mode), `0xe6` (epiku), `0xa8` (seme), `0x60` (insa), `0xfe` (proper noun mode dissable) would be the text equivalent of "suwi Esi".  
This is more or less equivalent to a cartouche open / close in normal sitelen pona.  

nimi sin page switch -> 0xff  
nimi sin page switch switches what word page should be used.
it is followed by an unsigned short (2 bytes) of data indicating which page of nimi sin should be selected.  
This allows for `0xff` * USHRT_MAX (16711425) nimi sin to be represented.

## nimi sin Pages
Every nimi sin page is referred to by an ID, e.g. page `0x0000`, page `0x0001`, and so on. Each page contains `0xff` nimi sin.
To switch to a given nimi sin page, you write a `0xff` byte, then a two byte unsigned short of the desired page's ID.
The decoder will then switch to that page's word space.

### Page Definitions
Hex ID | Page Name       | 				  	  Page Description			 |  
\---------------------------------------------------------------   
0x0000   | Default	     | 		The standard page shown above    |   
0x0001   | Base nimisin	 | 		The list of `obscure` nimisin    |   

### nimi sin page 0x01, Base nimisin.

Obscure words: (0x00 - 0x24)  
apeja                -> 0x0  
isipin               -> 0x1  
jami                 -> 0x2  
kamalawala           -> 0x3  
kapesi               -> 0x4  
kiki                 -> 0x5  
kokosila             -> 0x6  
konwe                -> 0x7  
kulijo               -> 0x8  
melome               -> 0x9  
mijomi               -> 0xa  
misa                 -> 0xb  
nja                  -> 0xc  
ojuta                -> 0xd  
oke                  -> 0xe  
omekapo              -> 0xf  
owe                  -> 0x10  
pake                 -> 0x11  
penpo                -> 0x12  
pika                 -> 0x13  
po                   -> 0x14  
powe                 -> 0x15  
puwa                 -> 0x16  
san                  -> 0x17  
soto                 -> 0x18  
sutopatikuna         -> 0x19  
taki                 -> 0x1a  
te                   -> 0x1b  
teje                 -> 0x1c  
to                   -> 0x1d  
unu                  -> 0x1e  
usawi                -> 0x1f  
wa                   -> 0x20  
wasoweli             -> 0x21  
wekama               -> 0x22  
wuwojiti             -> 0x23  
yupekosi             -> 0x24  

Sandbox words: (0x25 - 0xda)  
Pingo                -> 0x25  
aka                  -> 0x26  
ako                  -> 0x27  
aku                  -> 0x28  
alente               -> 0x29  
alu                  -> 0x2a  
an                   -> 0x2b  
anta                 -> 0x2c  
antikontitutonelema  -> 0x2d  
apelo                -> 0x2e  
api                  -> 0x2f  
apoko                -> 0x30  
awase                -> 0x31  
eki                  -> 0x32  
eliki                -> 0x33  
enepi                -> 0x34  
enko                 -> 0x35  
epikule              -> 0x36  
ete                  -> 0x37  
ewe                  -> 0x38  
i                    -> 0x39  
iki                  -> 0x3a  
ini                  -> 0x3b  
inisa                -> 0x3c  
inta                 -> 0x3d  
ipi                  -> 0x3e  
iseki                -> 0x3f  
itomi                -> 0x40  
iwa                  -> 0x41  
ja                   -> 0x42  
jaku                 -> 0x43  
jalan                -> 0x44  
jans                 -> 0x45  
jatu                 -> 0x46  
je                   -> 0x47  
jepi                 -> 0x48  
jipi                 -> 0x49  
jonke                -> 0x4a  
josuta               -> 0x4b  
ju                   -> 0x4c  
jule                 -> 0x4d  
jume                 -> 0x4e  
juna                 -> 0x4f  
jupi                 -> 0x50  
ka                   -> 0x51  
ka1                  -> 0x52  
ka2                  -> 0x53  
kajo                 -> 0x54  
kalamARR             -> 0x55  
kalapisituji         -> 0x56  
kalijopilale         -> 0x57  
kan                  -> 0x58  
kana                 -> 0x59  
kankuli              -> 0x5a  
kapa                 -> 0x5b  
kasan                -> 0x5c  
ke                   -> 0x5d  
kelo                 -> 0x5e  
kepa                 -> 0x5f  
kepen                -> 0x60  
kese                 -> 0x61  
kewe                 -> 0x62  
kewi                 -> 0x63  
ki                   -> 0x64  
kikolo               -> 0x65  
kikulo               -> 0x66  
kisa                 -> 0x67  
kokoliko             -> 0x68  
kolin                -> 0x69  
kolo                 -> 0x6a  
konsi                -> 0x6b  
konsuno              -> 0x6c  
kosan                -> 0x6d  
kosikosa             -> 0x6e  
kulaso               -> 0x6f  
kulu                 -> 0x70  
kuntu                -> 0x71  
kutopoma             -> 0x72  
lajotu               -> 0x73  
lan                  -> 0x74  
lapan                -> 0x75  
lenke                -> 0x76  
lijokuku             -> 0x77  
likujo               -> 0x78  
lipasa               -> 0x79  
lisa                 -> 0x7a  
lo                   -> 0x7b  
loka                 -> 0x7c  
lokon                -> 0x7d  
loku                 -> 0x7e  
lonsi                -> 0x7f  
lu                   -> 0x80  
lu1                  -> 0x81  
masalo               -> 0x82  
masenta              -> 0x83  
me                   -> 0x84  
molusa               -> 0x85  
mulapisu             -> 0x86  
nalanja              -> 0x87  
natu                 -> 0x88  
ne                   -> 0x89  
neja                 -> 0x8a  
nele                 -> 0x8b  
nowi                 -> 0x8c  
nu                   -> 0x8d  
nu1                  -> 0x8e  
nun                  -> 0x8f  
nusun                -> 0x90  
nuwa                 -> 0x91  
okepuma              -> 0x92  
oki                  -> 0x93  
olala                -> 0x94  
omekalike            -> 0x95  
omen                 -> 0x96  
oni                  -> 0x97  
onono                -> 0x98  
opasan               -> 0x99  
pa                   -> 0x9a  
pakola               -> 0x9b  
panke                -> 0x9c  
papa                 -> 0x9d  
papa1                -> 0x9e  
papa2                -> 0x9f  
pasila               -> 0xa0  
pata                 -> 0xa1  
patu                 -> 0xa2  
pela                 -> 0xa3  
peta                 -> 0xa4  
peto                 -> 0xa5  
pipo                 -> 0xa6  
pipolo               -> 0xa7  
pokasi               -> 0xa8  
polinpin             -> 0xa9  
pomotolo             -> 0xaa  
poni                 -> 0xab  
positu               -> 0xac  
potesu               -> 0xad  
pulaso               -> 0xae  
saja                 -> 0xaf  
salu                 -> 0xb0  
samu                 -> 0xb1  
sapelipope           -> 0xb2  
se                   -> 0xb3  
se1                  -> 0xb4  
sikako               -> 0xb5  
sikomo               -> 0xb6  
silapa               -> 0xb7  
sipi                 -> 0xb8  
sipije               -> 0xb9  
siwala               -> 0xba  
slape                -> 0xbb  
snoweli              -> 0xbc  
sole                 -> 0xbd  
su1                  -> 0xbe  
suke                 -> 0xbf  
sulaso               -> 0xc0  
sunta                -> 0xc1  
suwili               -> 0xc2  
ta                   -> 0xc3  
take                 -> 0xc4  
tankala              -> 0xc5  
tasun                -> 0xc6  
teki                 -> 0xc7  
ten                  -> 0xc8  
tenkala              -> 0xc9  
tokana               -> 0xca  
toma                 -> 0xcb  
tona                 -> 0xcc  
towoki               -> 0xcd  
tuli                 -> 0xce  
u                    -> 0xcf  
uka                  -> 0xd0  
umesu                -> 0xd1  
waken                -> 0xd2  
waleja               -> 0xd3  
wawajete             -> 0xd4  
we                   -> 0xd5  
we1                  -> 0xd6  
wi                   -> 0xd7  
wisa                 -> 0xd8  
wiwi                 -> 0xd9  
yutu                 -> 0xda

0xdb - 0xff reserved.

## Example Sequences
Say we want to write: "mi pona e Pingo kijetesantakalu mi" (I repair my raccon-like car).
The first part of the sequence is trivial:
`0x84` (mi), `0xa3` (pona), `0x5e` (e).
However, we now need to insert `0xff` (nimi sin page switch), `0x00` (ID high byte), `0x01` (ID low byte). This switches us to nimi sin page 1, where Pingo is encoded.
We can then simply output `0x25` (Pingo). Now, we need to switch back to the normal page. This is the same procedure, but with a different page ID: 
`0xff` (nimi sin page switch), `0x00` (ID high byte), `0x00` (ID low byte). Now we can continue like normal. `0xd0` (kijetesantakalu), `0x84` (mi).



