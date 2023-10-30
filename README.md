# HAMK Pilvipalvelut - Tehtävä 1, Docker

Tämä repo on HAMKin Pilvipalvelut kurssin docker tehtävän toteutus.

## Sisältö

- [Perustiedot](#perustiedot)
- [Rakenne](#rakenne)
- [Asennus](#asennus)
- [Käyttö](#käyttö)

## Perustiedot

Tehtävässä piti luoda 2 Docker-konttia, jotka vaihtavat tietoa keskenään.

### Server
Kontti generoi satunnaisdataa 1 kt verran ja tallentaa sen servervol -voluumiin nimellä data.txt. Sen jälkeen kontti laskee datalle tarkistussumman (MD5) ja kirjoittaa sen samaan voluumiin nimellä checksum.txt.

Tämän jälkeen kontti käynnistää uvicorn -http-palvelimen määrättyyn porttiin ja alkaa kuunnella kyselyitä tähän porttiin.

### Client
Kontti hakee Server-kontin uvicorn -palvelimelta generoidun satunnaisdatan ja sen tarkistussumman ja tallentaa ne clientvol -voluumiin. Sen jälkeen kontti laskee tarkistussumman datasta tarkistaa ladatun tarkistussumman avulla, onko data oikein.

## Rakenne

| Server
|-- servervol
  |-- /servervol
    |-- data.txt
    |-- checksum.txt

## Asennus

Lataa paketti palvelimelle komennolla
```
git clone https://github.com/rikeardi-hamk/cloud-services-docker1.git
```

## Käyttö

Paketin mukana tulee 2 skriptiä, create.sh ja destroy.sh.

Ajamalla create.sh komennon, luodaan kontit ja ajamalla destroy.sh komennon tuhotaan kontit.
```
./create.sh
```
```
./destroy.sh
```
create.sh kysyy ennen konttien luomista tarkemmat tiedot konteista.


&copy; Risto Lievonen