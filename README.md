# Eksport plikow *.ipynb do *.html

Eksportuje pliki *.ipynb z danego folderu do plikow *.html<br>
Do plikow *.html dodaje spis tresci<br>
<br>
Przydatne komendy bashowe:
- egzekuje wszystkie komorki z danego pliku *.ipynb na wszystkich znalezionych plikach w (pod)folderach z obecnego folderu
```bash
find -name '*.ipynb' -execdir jupyter nbconvert --to notebook --inplace --execute {} +
```
- wykonuje plik usun_wyeksportuj.py w kazdym folderze w ktorym on sie znajduje w (pod)folderach z obecnego folderu
```bash
find -name usun_wyeksportuj.py -execdir python3 {} +
```
## Do użytku własnego, nie powinno być używane przez nikogo innego.

## For personal use only, should not be used by anyone else.
