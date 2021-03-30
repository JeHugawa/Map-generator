# Vaatimusmäärittely

## Sovellus

Sovelluksen tarkoituksena on generoida karttoja satunnais avainten avulla (random seed). Sovellus palauttaa käyttäjälle tiedoston missä on kartta.


## perusversion tarjoama toiminnallisuus

- Käyttäjä voi syöttää ohjelmalle satunnaisavaimen (random seed) ja ohjelma generoi kartan sen perusteella.

- Käyttäjä voi tallentaa kartan tiedostoon.

- Ohjelma tukee kartan generoinnin parametrejä (esimerkiksi käyttäjä voi rajoittaa vuorien määärää tai rajoittaa maaston korkeutta).

- Käyttäjä voi tarkastella generoitua karttaa sovelluksessa.
  - Käyttäjä voi myös syöttää aikaisemmin luotuja karttoja.


## käyttöliittymäluonnos

Sovelluksessa on kolme päänäkymää:

<img src="https://raw.githubusercontent.com/JeHugawa/ot-harjoitustyo/master/dokumentaatio/Kuvat/kayttoliittyma.jpg" width="750">

Sovelluksen alkunäkymässä käyttäjä voi joko antaa seedin tai avata asetusnäkymän. asetusnäkymässä käyttäjä voi muokata erilaisia kartan ominaisuuksia. Siitä voi palata takaisin aloitusnäkymään. Aloitusnäkymästä voi jatkaa generointinäkymään, mistä käyttäjä voi tutkia luotua karttaa ja siitä tallentaa sen ja palata takaisin alkuun.

## Jatkokehitysideoita
Ominaisuuksia mitä voidaan lisätä perustoiminnallisuuden jälkeen. Lista ei ole erityisessä järjestyksessä.


- Kartat voi viedä (export) tiedostoja [Tiled](https://www.mapeditor.org/) karttaeditoriin.
  - Mahdollisesti muita formaatteja aikataulusta riippuen.

- Käyttäjä voi kertoa mitä maastoelementtejä halutaan ottaa mukaan generaatioon.

- Ohjelma antaa analyysin kartasta (esim. montako prosenttia kartasta on vettä).

- Käyttäjä voi tehdä perusmuokkauksia karttaan käsin.

- 
