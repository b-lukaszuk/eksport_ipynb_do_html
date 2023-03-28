# uzywano w Python3.8

## wczytanie plikow *.ipynb
import wstaw_toc_do_html as t2html
import glob
pliki_ipynb = glob.glob("./*.ipynb")

## usuniecie z nich kodu
import json
import os
import sys

## ustawianie aktualnej working directory na tak w ktorej jest ten plik,
## za: https://stackoverflow.com/questions/1432924/
## python-change-the-scripts-working-directory-to-the-scripts-own-directory
abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)


# tworzymy folder "eksport_do_html"
# do ktorego bedziemy zapisywac wyeksprotowane pliki html
os.mkdir("./eksport_do_html")

# przejscie po wszystkich plikach ipynb
# usuniecie z nich kodu
# zapis ipynb do folderu "eksport_do_html"
for plik_ipynb in pliki_ipynb:
    json_plik = open(plik_ipynb)
    json_data = json_plik.read()
    json_plik.close()
    data = json.loads(json_data)
    komorki = data["cells"]

    # znajdz komorki z kodem
    for i in komorki:
        if i['cell_type'] == "code":
            # usun kod
            i['source'] = ""

    # zapisz wyczyszczony plik
    with open('./eksport_do_html/'+ plik_ipynb, 'w') as outfile:
        json.dump(data, outfile, indent = 4)

# przejscie do folderu "eksport_do_html"
os.chdir("./eksport_do_html/")

# eksport plikow *.ipynb z folderu "eksport_do_html" do html
komenda_konwertujaca = "jupyter nbconvert --execute --to html "

for plik_ipynb in pliki_ipynb:
    os.system(komenda_konwertujaca + plik_ipynb)

# usuniecie niepotrzebnych plikow *.ipynb
for plik_ipynb in pliki_ipynb:
    os.remove(plik_ipynb)

## dodanie spisu tresci do plikow html

# wczytanie wszystkich plikow html
pliki_html = glob.glob("*.html")

# wstawienie spisow tresci do kazdego z plikow html
for plik_html in pliki_html:
    # wczytanie pliku
    f_odczyt = open(plik_html)
    f_text = f_odczyt.read()
    f_odczyt.close()

    # dodanie do tekstu z pliku html toc-a
    html_z_toc = t2html.zwroc_html_z_toc(f_text)

    # nadpisanie pliku html
    f_zapis = open(plik_html, "w")
    f_zapis.write(html_z_toc)
    f_zapis.close()



dzis = os.popen("date '+%d_%m_%Y'").read().strip()
# dodamy jeszcze plik o tym, ze jest to nowy eksport (timestamp)
f_nowy = open("./" + "nowy_" + dzis + ".txt", "w")
f_nowy.write("nowy_" + dzis)
f_nowy.close()
