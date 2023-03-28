# uzywano w Python 3.8
# uruchamianie w Emacs-ie -> M-x run-python
import re


def wyodr_naglowki(tekst):
    """
    wyodrebnia wszystkie naglowki (w kolejnosci wyst w tekscie html)
    Input:
    ---
        tag - Str (tekst html)

    Output:
    ---
        List of Str (lista naglowkow kazdy w postaci '<h1 id="...>')
    """

    return re.findall(r"<h\d .*", tekst)


def wyodr_level(tag):
    """
    wyodrebnia poziom naglowka z tagu
    Input:
    ---
        tag - Str w postaci '<h1 id="...>'

    Output:
    ---
        Int - poziom naglowka
    """

    # regex z positive lookbehind (?<=)
    return int(re.search(r"(?<=<h)\d", tag).group(0))


def wyodr_id(tag):
    """
    wyodrebnia id z tagu (naglowka)
    Input:
    ---
        tag - Str w postaci '<h1 id="...>'

    Output:
    ---
        Str - id naglowka
    """

    # regex z lookbehind positive (?<=) z lookahead positive (?=)
    return re.search(r'(?<=id=").+?(?=")', tag).group(0)


def wyodr_tekst(tag):
    """
    wyodrebnia tekst z tag-u (naglowka) z pomiedzy >tekst<
    Input:

        tag - Str w postaci '<h1 id="...>'

    Output:
    ---
        Str - tekst z naglowka
    """

    # regex z lookbehind positive (?<=) z lookahead positive (?=)
    return re.search(r"(?<=>).+?(?=<)", tag).group(0)


def zwroc_kotwice(tag, wciecie=4):
    """
    Zwraca kotwice do danego tagu (naglowek) na podstawie tego tagu
    Dodaje "&nbsp;" przed kotwica 4 x (poziom naglowka - 1)
    Input:
    ---
        tag - Str w postaci '<h1 id="...>'
        wciecie - Int, ile "&nbsp;" na dany poziom naglowka (ponizej h1)

    Output:
    ---
        kotwica - Str w postaci <a href="#...>...</a>"
    """
    ile_nbsp = wciecie * (wyodr_level(tag) - 1)
    id_tag = wyodr_id(tag)
    tekst_tag = wyodr_tekst(tag)
    kotwica = "&nbsp;" * ile_nbsp
    kotwica += '<a href="#' + id_tag + '">'
    kotwica += tekst_tag + "</a>"

    return kotwica


def zwroc_toc_content(naglowki):
    """
    buduje zawartosc table of contents (toc),
    czyli hiperlinki do naglowkow
    Input:
    ---
        naglowki - List of Str (naglowki) kazdy w postaci '<h1 id="...>'

    Output:
    ---
        Str - anchory dla kazdego z naglowkow
    """
    kotwice = [zwroc_kotwice(naglowek) for naglowek in naglowki]
    kotwice = "<br>".join(kotwice)

    return kotwice


def zwroc_toc(naglowki):
    """
    zwraca toc (div-a z H1 i anchorami)
    Input:
    ---
        naglowki - List of Str (naglowki) kazdy w postaci '<h1 id="...>'

    Output:
    ---
        Str - TOC do wklejenia pod body w dokumencie html
    """
    toc = '<div id="toc-short">' + "\n"
    toc += '<div class="toc-hm"></div>' * 3
    toc += '<div id="toc-full"'
    toc += 'style="margin-left: 6em; color: blue; font-size: 1.3em">\n'
    toc += "<h1>Table of Contents</h1>"
    toc += zwroc_toc_content(naglowki)
    toc += "\n" + "</div>" + "</div>\n" + "<br>"

    return toc


def zwroc_toc_css_style():
    res = """<style>

    div .toc-hm {
    width: 35px;
    height: 5px;
    background-color: blue;
    margin: 6px 0;
    }

    #toc-short {
    position: fixed;
    right: 1%;
    top: 1%;
    background-color:#FFF;
    z-index:99;
    }

    #toc-short #toc-full { display: none; } /* default: hide full TOC */

    #toc-short:hover .toc-hm { display: none; }

    #toc-short:hover #toc-full {
    display: block; /* Show TOC on hover */
    }
    </style>"""

    return res


def zwroc_html_z_toc(tekst_html):
    """
    zwraca html ze wstawionym Table of Contents (toc)
    Input:
    ---
        tekst_html - Str (tresc pliku html w ktorym sa naglowki)

    Output:
    ---
        Str - html z toc do zpisania do pliku html na dysku
    """
    naglowki = wyodr_naglowki(tekst_html)
    toc = zwroc_toc(naglowki)
    toc_css = zwroc_toc_css_style()
    all = toc + "\n" + toc_css

    return re.sub(r"(<body.*)", r"\1" + all, tekst_html)


# with open("./test.html") as file:
#    x = file.read()
#    file.close()
#
# with open("./test2.html", "w") as file:
#    file.write(zwroc_html_z_toc(x))
#    file.close()
