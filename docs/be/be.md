# Welkom bij BhashaJS in het nederlands

# gebruik

## hoe kan je registreeren
### op je laptop
1. klik op register present in de linker bovenhoek van de website.
2. Er wordt een nieuwe pagina geopend met een formulier erin.
3. Vul uw echte volledige naam in de eerste blanco in.
4. Vul het e-mailadres in de tweede blanco in. Als je geen eigen e-mailadres hebt of minderjarig bent, vul dan het e-mailadres van je ouders in.
5. Voer een wachtwoord in voor uw account.
6. Typ opnieuw hetzelfde wachtwoord uit de stap om het aanmaken van een account te bevestigen.
7. Klik vervolgens op de blauw gekleurde knop "Registreren".

### op je gsm
1. Klik op het hamburger/menupictogram in de linkerbovenhoek van de website.
2. Er wordt een lijst met tekst geopend, klik op registreren.
3. Er wordt een nieuwe pagina geopend met een formulier erin.
4. Vul uw echte volledige naam in de eerste blanco in.
5. Vul het e-mailadres in de tweede blanco in. Als je geen eigen e-mailadres hebt of minderjarig bent, vul dan het e-mailadres van je ouders in.
6. Voer een wachtwoord in voor uw account.
7. Typ opnieuw hetzelfde wachtwoord uit de stap om het aanmaken van een account te bevestigen.
8. Klik vervolgens op de blauw gekleurde knop "Registreren".

## Hoe in te loggen
# Koppel
## Een code uitvoeren
1. Klik op de groene knop met "Uitvoeren", erop geschreven.
2. Uitvoer is zichtbaar in het uitvoergedeelte.

## De uitvoer wissen
1. Klik op de blauwe knop met "Clear" erop geschreven.
2. Alle uitvoer wordt gewist.

## Verwijder de code
U moet alle code selecteren en vervolgens verwijderen.

# Zelfstudies
## Hallo Wereld
Laten we beginnen bij de basis. We hebben de computer nodig om "Hallo wereld" te zeggen. Hiervoor zouden we moeten schrijven
```
@display("Hallo wereld");
```
## Opmerking
Opmerkingen in BhashaX

Dus alles dat na `//` wordt geschreven, wordt bijvoorbeeld als commentaar beschouwd.
```
@display("Hallo wereld"); // Deze regel zal hallo wereld afdrukken
```
Opmerkingen zijn handig om verklarende informatie voor de code te hebben.

## Snaar
Tekst wordt in de programmeerterminologie aangeroepen als string.

### Hoe schrijven we het?
Om strings te schrijven, schrijven we de tekst die ik wil binnen enkele `'` of dubbele qoutes `"`.
Bijvoorbeeld
```
"Mijn naam is Allen"

'Mijn naam is Ram'
```

## Variabelen
Variabelen zijn als dozen. Ze bewaren alles wat je erin stopt. Je kunt toevoegen of verwijderen wat je erin hebt toegevoegd of zelfs dat vak verwijderen / vernietigen.

Nu kunnen er zoveel mogelijk dozen zijn. Hoe gaan we ze differentiëren? Hiervoor doen we thuis labels aan doos. Omdat variabelen grotendeels boxen zijn, moeten we ze ook een naam geven.

Bijvoorbeeld :-
```
$voedsel = "Melk"
```
Hier is `$food` de naam van de variabele. Wanneer we een naam van variabele willen schrijven.

## Input krijgen
Om de input van de gebruiker te krijgen gebruiken we
```
@input("Vertel alstublieft uw invoer")
```

Als u de waarde van de invoer in een variabele wilt opslaan, kunt u dit doen door:

```
$input = @input("Vertel alstublieft uw invoer")
$name = @input("Vertel alstublieft uw naam")
```

Maar wacht, hoe zal de computer bepalen of de invoer die u wilt doorgeven `"4"` of `4` is, d.w.z. is het een tekst of een nummer. Alle invoer die u standaard aan de computer doorgeeft, wordt als een getal beschouwd. We moeten ze veranderen

## Activiteiten
Er zijn veel operaties die we kunnen doen.
### Rekenen
#### Toevoeging
```
15 + 10
```

#### Aftrekken
```
15 - 10
```

#### Vermenigvuldiging
```
15 * 10
```

#### Divisie
```
15 / 10
```

#### Modulus
Modulus vindt de rest van de deling.
```
15 % 10 // Dit geeft je de rest van de deling, 15 / 10 heeft een rest van 5.
```
### Relationeel
#### Gelijk aan
Het wordt gebruikt om 2 waarden te vergelijken, we gebruiken Gelijk aan opreaor. Het wordt aangeduid met `==` twee gelijke symbolen de een na de ander zonder spatie. Als de waarde aan de linkerkant en de rechterkant gelijk zijn, zal het resultaat waar zijn, anders wordt het onwaar geretourneerd.
```
@display(10 == 10) // Zal True afdrukken
@display(15 == 10) // Zal False afdrukken

$getal1 = 5*2
@display(number1 == 10) // Zal True afdrukken
```
#### Is groter
Is groter dan symbool is als iets groter is dan iets of niet.
```
15 > 10
```
#### Is minder
Is kleiner dan symbool is als iets kleiner is dan iets of niet.
```
15 < 10
```
#### Is niet gelijk
Controleert of de waarde aan de linkerkant niet gelijk is aan de waarde aan de rechterkant.
```
15 != 10
```
#### Is groter dan of gelijk aan
Het symbool Is groter dan of gelijk aan is of iets groter is dan of gelijk is aan iets of niet.
```
15 >= 10
```
#### Is kleiner dan of gelijk aan
Het symbool Is kleiner dan of gelijk aan is als iets kleiner is dan of gelijk is aan iets of niet.
```
15 <= 10
```
### Opdrachtoperator
De toewijzingsoperatoren worden gebruikt om variabelen een waarde of resultaat van een uitdrukking toe te kennen.
```
// Syntaxis:
$variable_name = "waarde";
$mijn_nummer = 3.14159;
```
`=` is een van de toewijzingsoperatoren.
#### Verkorte opdracht operators
Zeg bijvoorbeeld om '1' toe te voegen aan '$my_number', we kunnen het volgende gebruiken:
```
$mijn_nummer = $mijn_nummer + 1;
```
hier verwijzen we 2 keer naar `$my_number`, dit kan korter gemaakt worden door de verkorte toewijzingsoperatoren te gebruiken.
```
$mijn_nummer += 1;
```
de `+=`, `-=`, `*=`, `/=`, `%=` zijn allemaal verkorte toewijzingsoperatoren.

### Operatoren verhogen/verlagen
Increment- en decrement-operators worden gebruikt om de waarde van een variabele met 1 eenheid te verhogen of te verlagen.

Voorbeeld :-
```
$mijn_nummer++;
```

<!-- Logische, bitsgewijze operators toevoegen -->

### Als-anders
Joe is een jongen van 4 jaar. Als het vandaag regent, blijft hij binnen en speelt hij ludo, of anders gaat hij naar buiten om cricket te spelen. Hier bepaalt Joe op basis van de omgeving wat hij gaat doen.

Vaak moeten we bij het coderen ook de uitkomst kiezen van wat we moeten doen op basis van de situatie/conditie. Daarom gebruiken we If else.

```
$number_of_chocolates = 20
if (aantal_chocolade == 20) {
  @display("Je hebt 20 chocolaatjes");
}
anders {
  @display("Je hebt geen 20 chocolaatjes");
}
```

Het else-blok is optioneel, het kan worden weggelaten als we niets in het else-blok willen schrijven.
#### Meerdere voorwaarden
Als we meerdere voorwaarden willen controleren, kunnen we de 'else if'-ladder gebruiken. De Else if-ladder wordt gebruikt om meerdere voorwaarden te controleren.
U wilt bijvoorbeeld controleren of het aantal bonbons minder dan 10 is, als het minder dan 10 is, dan wilt u zeggen: "U heeft minder dan 10 bonbons, we hebben meer chocolade nodig!", anders wilt u controleren of u minder dan 50 chocolaatjes hebt, dan wil je zeggen "Je hebt genoeg chocolaatjes", anders wil je zeggen: "Je hebt meer dan 50 chocolaatjes, dat is veel chocola! vergeet niet te delen".

```js
$number_of_chocolates = parseInt(@input("Vertel het aantal chocolaatjes"));
// de functie parseInt wordt gebruikt om de tekenreeks naar een geheel getal te converteren.

if ($aantal_van_chocolade < 10) {
  @display("Je hebt minder dan 10 chocolaatjes, we hebben meer chocola nodig!");
}
else if ($aantal_chocolades < 50) {
  @display("Je hebt genoeg chocolaatjes");
}
anders {
  @display("Je hebt meer dan 50 chocolaatjes, dat is veel chocola! vergeet niet te delen");
}
```
Eerst wordt het `$number_of_chocolates < 10` gecontroleerd, als het waar is, dan wordt het `@display("Je hebt minder dan 10 chocolaatjes, we hebben meer chocolade nodig!")` uitgevoerd. Als het onwaar is, wordt het `$aantal_chocolades < 50` gecontroleerd, als het waar is, wordt het `@display("Je hebt genoeg chocolaatjes")' uitgevoerd. Als het niet waar is, wordt de `@display("Je hebt meer dan 50 chocolaatjes, dat is veel chocola! vergeet niet te delen")` uitgevoerd.

### Lussen
Soms als we dingen verkeerd doen, geeft de leraar ons de straf om hetzelfde woord 10 of 100 keer te schrijven. Stel je voor dat je nu dezelfde zin op de computer moet schrijven. Een manier waarop u dit kunt doen, is door hetzelfde bericht keer op keer te kopiëren en te plakken.
```js
@display("Ik ben een programmeur");
@display("Ik ben een programmeur");
@display("Ik ben een programmeur");
@display("Ik ben een programmeur");
@display("Ik ben een programmeur");
...
@display("Ik ben een programmeur");
```
Of gebruik lussen, die worden gebruikt om dezelfde code meerdere keren te herhalen.
Er zijn 2 verschillende loops, `for` en `while`, laten we eens kijken naar de for-lus.
De `for`-lus accepteert de initialisatie, voorwaarde en increment.
1. Initialisatie: Dit is de code die wordt uitgevoerd voordat de lus begint, `$i = 0` is de initialisatie, het creëert een nieuwe variabele `$i` en stelt deze in op 0.
2. Voorwaarde: Dit is de code die wordt uitgevoerd voordat de lus wordt uitgevoerd, `$i < 10` is de voorwaarde, het controleert of de waarde van `$i` kleiner is dan 10.
3. Increment: Dit is de code die wordt uitgevoerd nadat de lus is uitgevoerd, `$i++` is de increment, het verhoogt de waarde van `$i` met 1.

```js
// Print "Ik ben een programmeur" 10 keer
voor ($i = 0; $i < 10; $i++) {
  @display("Ik ben een programmeur");
}
```

er is nog een manier om hetzelfde te doen, we kunnen de `while`-lus gebruiken. De `while`-lus accepteert alleen de voorwaarde.
```js
$i = 0;
terwijl ($ ik < 10) {
  @display("Ik ben een programmeur");
  $i++;
}
```
Dit is hetzelfde als de bovenstaande for-lus, alleen de syntaxis is anders.

### Arrays
Beschouw Array als trein. Je hebt een motor en daarna draaistellen achter de motor. Je kunt blijven toevoegen zoals je wilt. Dan kun je ook enkele draaistellen verwijderen. Mensen kunnen uit een draaistel komen en gaan, enzovoort.

Array is een speciale variabele die meer dan één waarde kan bevatten:

```js
$arr = [0,0,0,"heesh"];
```

### Functies
Functie is een codeblok dat is ontworpen om een ​​bepaalde taak uit te voeren.

# Fouten

# Voorbeeldcode
## Rekenmachine
```js
$number1 = parseInt(@input("Vertel het eerste nummer1"));
$number2 = parseInt(@input("Vertel het eerste nummer2"));

$som = $nummer1 + $nummer2;

@display(“De som is : ”);
@display($som);
// DIT IS VAN MIJ
```
