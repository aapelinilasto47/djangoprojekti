# Ruokavarasto API
Tämä on Django REST Frameworkilla toteutettu backend-palvelin ruokavaraston hallintaan. 
Sovellus mahdollistaa tuotteiden skannaamisen EAN-koodilla, varastotilanteen seurannan ja automaattiset ilmoitukset pian vanhentuvista tuotteista.

## Ominaisuudet

- **Käyttäjien hallinta**: Rekisteröityminen ja Token-pohjainen kirjautuminen.
- **Tuotetunnistus**: EAN-koodiin perustuva haku (tietokannasta).
- **Varastonhallinta**: Käyttäjäkohtainen näkymä tuotteisiin, määriin ja sijainteihin (Jääkaappi, Pakastin, Kuivakaappi).
- **Älykkäät hälytykset**: Rajapinta, joka listaa automaattisesti seuraavan 3 päivän aikana vanhentuvat tuotteet.
- **CORS-tuki**: Valmis kytkettäväksi Frontend-sovellukseen (esim. React tai mobiili).

## Teknologiat

- [Python](https://www.python.org/) 3.x
- [Django](https://www.djangoproject.com/) & [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/) (Tietokanta)
- [Postman](https://www.postman.com/) (API-testaus)

## Käyttöönotto

### 1. Kloonaa projekti ja asenna riippuvuudet
```bash
# Aktivoi virtuaaliympäristö
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Asenna kirjastot
pip install -r requirements.txt

```

### 2. Tietokannan valmistelu

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 3. Palvelimen käynnistys

```bash
python manage.py runserver
```
Palvelin löytyy osoitteesta: 
http://127.0.0.1:8000/

## API-rajapinnat (Endpoints)

Polku,                          Metodi,         Kuvaus

/api/users/,                    POST,           Luo uusi käyttäjätunnus.


/api-token-auth/,               POST,           Kirjaudu ja hanki Authorization Token.


/api/tuotteet/<ean>/skannaa/,   GET,            Hae tuotteen tiedot koodilla.


/api/varastot/,                 GET,            Listaa omat varastotuotteet.


/api/varastot/,                 POST,           Lisää uusi tuote varastoon.


/api/varastot/vanhentuvat/,     GET,            Listaa pian vanhentuvat tuotteet.



Huom! Kaikki varastoon liittyvät pyynnöt vaativat headerin:

Authorization: Token <sinun_tokenisi>

## Tietoturva

Projekti käyttää Djangon omaa käyttäjämallia. 
Salasanat tallennetaan hashattuina, ja pääsy varastotietoihin on rajattu vain kirjautuneille käyttäjille IsAuthenticated-suojauksella.
