# Eksport plikow *.ipynb do *.html

Eksportuje pliki *.ipynb z danego folderu do plikow *.html<br>
Z plikow *.html usuwa komorki z kodem (ale zostawia ich output)<br>
Do plikow *.html dodaje spis tresci<br>
<br>
Uzycie:
1. Wchodze do katalogu w ktorym sa pliki *.ipynb (1 lub wiecej), `usun_wyeksportuj.py`, `wstaw_toc_do_html.py`
2. Wpisuje konende bashowa:
```bash
python3 usun_wyeksportuj.py
```
i voila, tworzy mi folder `eksport_do_html` w ktorym sa pliki *.html (pliki oryginalne sa nie zmienione).

Dziala na pliki *.ipynb w obrebie folderu w ktorym jestesmy (nie wchodzi w podfoldery)

Jesli jednak chcemy tez zmian w podfolderach to mozemy wykorzystac (patrz pozycja 2 ponizej):

Przydatne komendy bashowe:
1. wykonuje wszystkie komorki z danego pliku *.ipynb na wszystkich znalezionych plikach w (pod)folderach z obecnego folderu
```bash
find -name '*.ipynb' -execdir jupyter nbconvert --to notebook --inplace --execute {} +
```
2. wykonuje plik usun_wyeksportuj.py w kazdym folderze w ktorym on sie znajduje w (pod)folderach z obecnego folderu
```bash
find -name usun_wyeksportuj.py -execdir python3 {} +
```
## Do użytku własnego, nie powinno być używane przez nikogo innego.

## For personal use only, should not be used by anyone else.
