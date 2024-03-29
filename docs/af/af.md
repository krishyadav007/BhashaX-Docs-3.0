# Welkom by BhashaJS in Afrikaans

# Gebruik

## Hoe om te registreer
### Op skootrekenaar
1. Klik op registreer teenwoordig in die boonste linkerhoek van die webwerf.
2. Dit sal 'n nuwe bladsy oopmaak met 'n vorm daarin.
3. Vul jou regte volle naam in die eerste spasie.
4. Vul e-posadres in die tweede leeg. As jy nie jou eie e-posadres het nie of minderjarig is, plaas jou ouers se e-posadres.
5. Plaas wagwoord vir jou rekening.
6. Tik weer dieselfde wagwoord vanaf die stap om die skepping van rekening te bevestig.
7. Klik dan op die blou gekleurde "Registreer" knoppie.

### Op selfoon
1. Klik op die hamburger/kieslys-ikoon wat in die boonste linkerhoek van die webwerf teenwoordig is.
2. Dit sal 'n lys van teks oopmaak, klik op registreer.
3. Dit sal 'n nuwe bladsy oopmaak met 'n vorm daarin.
4. Vul jou regte volle naam in die eerste spasie.
5. Vul e-posadres in die tweede leeg. As jy nie jou eie e-posadres het nie of minderjarig is, plaas jou ouers se e-posadres.
6. Plaas wagwoord vir jou rekening.
7. Tik weer dieselfde wagwoord vanaf die stap om die skepping van die rekening te bevestig.
8. Klik dan op die blou gekleurde "Registreer" knoppie.

## Hoe om aan te meld
# Interface
## Begin 'n kode
1. Klik op die groen knoppie met "Run", daarop geskryf.
2. Uitset sal sigbaar wees in die uitset afdeling.

## Vee die uitset uit
1. Klik op die blou knoppie met "Clear" daarop geskryf.
2. Al die uitset sal uitgevee word.

## Vee die kode uit
Jy moet al die kode kies en dit dan uitvee.

# Tutoriale
## Hello Wêreld
Kom ons begin met die heel basiese beginsels. Ons het die rekenaar nodig om "Hallo wêreld" te sê. Hiervoor sal ons moet skryf
None
@display("Hallo wêreld");
None

## Kommentaar
Kommentaar in BhashaX

Dus sal enigiets wat na `//` geskryf word, byvoorbeeld as kommentaar beskou word.
None
@display("Hallo wêreld"); // Hierdie reël sal hallo wêreld druk
None
Kommentaar is nuttig om verduidelikende inligting vir die kode te hê.

## Snaar
Teks word in die programmeringsterminologie genoem as string.

### Hoe skryf ons dit
Om stringe te skryf, skryf ons enige teks wat ek wil binne enkele `'` of dubbele aanhalings `"`.
Byvoorbeeld
None
"My naam is Allen"

'My naam is Ram'
None

## Veranderlikes
Veranderlikes is soos bokse. Hulle bêre alles wat jy in hulle sit. Jy kan alles wat jy bygevoeg het byvoeg of verwyder of selfs daardie blokkie uitvee/vernietig.

Nou kan daar soveel bokse as moontlik wees. Hoe sal ons hulle onderskei? Hiervoor voeg ons by die huis etikette by boks. Aangesien veranderlikes grootliks blokkies is, moet ons hulle ook noem.

Byvoorbeeld :-
None
$food = "Melk"
None
Hier is `$food` die naam van veranderlike. Wanneer ons 'n naam van veranderlike wil skryf.

## Kry insette
Om die insette van gebruiker te kry, gebruik ons
None
@input("Stel asseblief jou insette")
None

As jy die waarde van invoer in een of ander veranderlike wil stoor, kan jy dit doen deur

None
$input = @input("Vertel asseblief jou invoer")
$name = @input("Stel asseblief jou naam")
None

Maar wag, hoe sal rekenaar onderskei of die invoer wat jy wil deurgee `"4"` of `4` is, dit wil sê is dit 'n teks of 'n nommer. Al die invoer wat jy standaard na die rekenaar deurgee, word as nommer beskou. Ons moet hulle verander

## Bewerkings
Daar is baie operasies wat ons kan doen.
### Rekenkunde
#### Byvoeging
None
15 + 10
None

#### Aftrekking
None
15 - 10
None

#### Vermenigvuldiging
None
15 * 10
None

#### Afdeling
None
15/10
None

#### Modulus
Modulus is om die res van die verdeling te vind.
None
15 % 10 // Dit sal vir jou die res van die afdeling gee, 15 / 10 het res van 5.
None
### Relasioneel
#### Gelyk aan
Dit word gebruik om 2 waardes te vergelyk, ons gebruik Equal to opreaor. Dit word aangedui deur `==` twee gelyke simbole een na die ander sonder spasie. As die waarde aan die linkerkant en regterkant gelyk is, sal dit as waar wees, anders sal dit vals terugkeer.
None
@display(10 == 10) // Sal True druk
@display(15 == 10) // Sal Onwaar druk

$nommer1 = 5*2
@display(nommer1 == 10) // Sal True druk
None
#### Is groter
Is groter as simbool is of enigiets groter as iets is of nie.
None
15 > 10
None
#### Is minder
Is minder as simbool is of enigiets minder as iets is of nie.
None
15 < 10
None
#### Is nie gelyk nie
Kontroleer of die waarde aan die linkerkant nie gelyk is aan die waarde aan die regterkant nie.
None
15 != 10
None
#### Is groter as of gelyk aan
Die Is groter as of gelyk aan simbool is of enigiets groter as of gelyk aan iets is of nie.
None
15 >= 10
None
#### Is kleiner as of gelyk aan
Die Is kleiner as of gelyk aan simbool is of enigiets kleiner as of gelyk aan iets is of nie.
None
15 <= 10
None
### Opdragoperateur
Die toewysingsoperateurs word gebruik om veranderlikes 'n waarde of resultaat van 'n uitdrukking toe te ken.
None
// Sintaksis:
$variable_name = "waarde";
$my_nommer = 3.14159;
None
`=` is een van die assesseringsoperateurs.

#### Snelskrif-opdragoperateurs
Sê byvoorbeeld om `1` by `$my_nommer` te voeg, ons kan die volgende gebruik
None
$my_nommer = $my_nommer + 1;
None
hier verwys ons `$my_nommer` 2 keer, dit kan korter gemaak word deur die snelskrif-opdragoperateurs te gebruik.
None
$my_nommer += 1;
None
die `+=`, `-=`, `*=`, `/=`, `%=` is almal snelskrif-opdragoperateurs.

### Verhoog/Verminder operateurs
Inkrement- en dekrementoperateurs word gebruik om die waarde van 'n veranderlike met 1 eenheid te verhoog of te verlaag.

Voorbeeld: -
None
$my_nommer++;
None

<!-- Voeg logiese, bitsgewyse operateurs by -->

### As-anders
Joe is 'n 4-jarige seuntjie. As dit vandag reën, dan sal hy binne die huis bly en ludo speel, of anders gaan hy uit en krieket speel. Hier op grond van die omgewing besluit Joe die uitkoms van wat om te doen.

Baie keer wanneer ons kodeer, moet ons ook die uitkoms van wat ons moet doen kies op grond van die situasie/toestand. Dus gebruik ons ​​If else.

None
$aantal_sjokolade = 20
if(aantal_sjokolade == 20) {
@display("Jy het 20 sjokolades");
None
anders {
@display("Jy het nie 20 sjokolades nie");
None
None

Die else blok is opsioneel, dit kan weggelaat word as ons niks in else blok wil skryf nie.

#### Veelvuldige toestande
As ons veelvuldige voorwaardes wil nagaan, kan ons die `else if`-leer gebruik. Die Else if-leer word gebruik om verskeie toestande na te gaan.
Jy wou byvoorbeeld kyk of die aantal sjokolade minder as 10 is, as dit minder as 10 is, dan wil jy sê "Jy het minder as 10 sjokolades, ons het meer sjokolade nodig!", anders wil jy kyk of jy minder as 50 sjokolade het, dan wil jy sê "Jy het genoeg sjokolade", anders wil jy sê "Jy het meer as 50 sjokolades, dis baie sjokolade! moenie vergeet om te deel nie".

```js
$number_of_chocolates = parseInt(@input("Stel asseblief die aantal sjokolades"));
// die parseInt-funksie word gebruik om die string na heelgetal om te skakel.

if ($aantal_sjokolade < 10) {
@display("Jy het minder as 10 sjokolades, ons het meer sjokolade nodig!");
None
anders as ($aantal_sjokolade < 50) {
@display("Jy het genoeg sjokolade");
None
anders {
@display("Jy het meer as 50 sjokolades, dis baie sjokolade! moenie vergeet om te deel nie");
None
None
Eers sal die `$aantal_sjokolade < 10` gemerk word, as dit waar is, dan sal die `@display("Jy het minder as 10 sjokolades, ons het meer sjokolade nodig!")` uitgevoer word. As dit vals is, sal die `$aantal_sjokolade < 50` gekontroleer word, as dit waar is, sal die `@display("Jy het genoeg sjokolade")` uitgevoer word. As dit vals is, sal die `@display("Jy het meer as 50 sjokolade, dit is baie sjokolade! moenie vergeet om te deel nie")` uitgevoer word.

### Lusse
Soms wanneer ons dinge verkeerd doen, gee onderwyser ons die straf om dieselfde woord 10 of 100 keer te skryf. Stel jou nou voor jy moet dieselfde sin in rekenaar skryf. Een manier wat jy kan doen, is om dieselfde boodskap weer en weer te kopieer en plak.
```js
@display("Ek is 'n programmeerder");
@display("Ek is 'n programmeerder");
@display("Ek is 'n programmeerder");
@display("Ek is 'n programmeerder");
@display("Ek is 'n programmeerder");
None
@display("Ek is 'n programmeerder");
None
Of gebruik lusse, wat gebruik word om dieselfde kode verskeie kere te herhaal.
Daar is 2 verskillende lusse, `vir` en `while`, kom ons kyk na die for-lus.
Die `vir`-lus aanvaar die inisialisering, toestand en inkrement.
1. Inisialisering: Dit is die kode wat uitgevoer word voor die lus begin, `$i = 0` is die inisialisering, dit skep 'n nuwe veranderlike `$i` en stel dit op 0.
2. Toestand: Dit is die kode wat uitgevoer word voordat die lus uitgevoer word, `$i < 10` is die voorwaarde, dit kyk of die waarde van `$i` minder as 10 is.
3. Inkrement: Dit is die kode wat uitgevoer word nadat die lus uitgevoer is, `$i++` is die inkrement, dit verhoog die waarde van `$i` met 1.

```js
// Druk "Ek is 'n programmeerder" 10 keer
vir ($i = 0; $i < 10; $i++) {
@display("Ek is 'n programmeerder");
None
None

daar is nog een manier om dieselfde ding te doen, ons kan die `while` lus gebruik. Die `while`-lus aanvaar slegs die voorwaarde.
```js
$i = 0;
while ($i < 10) {
@display("Ek is 'n programmeerder");
$i++;
None
None

Dit is dieselfde as die bogenoemde vir lus, net die sintaksis is anders.

### Skikkings
Beskou Array as trein. Jy het enjin, en dan draaistelle na die enjin. Jy kan aanhou byvoeg soos boggies jy wil. Dan kan jy ook 'n paar draaistellen verwyder. Mense kan uit 'n bogie kom en gaan en so aan.

Skikking is 'n spesiale veranderlike, wat meer as een waarde kan hou:

```js
$arr = [0,0,0,"heesh"];
None

### Funksies
Funksie is 'n blok kode wat ontwerp is om 'n spesifieke taak uit te voer.

# Foute

# Voorbeeldkode
## Sakrekenaar
```js
$number1 = parseInt(@input("Vertel asseblief die eerste nommer1"));
$number2 = parseInt(@input("Vertel asseblief die eerste nommer2"));

$som = $nommer1 + $nommer2;

@display("Die som is: ");
@vertoon($som);
// DIT IS DEUR MY
None
