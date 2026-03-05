### Co program dělá

Program funguje jako automatický generátor a analyzátor matematických grafů. Celý proces se dá popsat v těchto krocích:

1. **Příprava vzorečků:** Ze souboru `functions.py` si načte definice matematických funkcí.
2. **Tvorba dat:** Pomocí knihovny NumPy si vytvoří osu `x` – přesně 1000 čísel v rozmezí od -10 do 10.
3. **Výpočty a hledání extrémů:** Tyto hodnoty dosadí do funkcí, čímž získá osu `y`. Zároveň (díky Možnosti C ze zadání) u každé funkce najde její nejvyšší a nejnižší hodnotu na daném intervalu (maximum a minimum).
4. **Kreslení a ukládání:** Pomocí knihovny Matplotlib funkce postupně nakreslí, přidá k nim mřížku, popisky os, legendu a červenou tečkou vyznačí nalezená minima a maxima.
5. **Výsledek:** Vygeneruje 5 samostatných grafů a 1 kombinovaný, vytvoří složku `images/` (pokud ještě neexistuje) a všechny grafy do ní rovnou uloží jako obrázky ve formátu PNG.

---

### Jak ho spustit

Je to velmi přímočaré. Postupuj podle těchto kroků:

1. **Příprava souborů:** Ujisti se, že máš kód uložený ve dvou souborech (`functions.py` a `main.py`) a že jsou oba ve stejné složce.
2. **Instalace knihoven:** Otevři si terminál (příkazovou řádku) a nainstaluj potřebné nástroje tímto příkazem:
`pip install numpy matplotlib`
3. **Spuštění:** V terminálu se pomocí příkazu `cd` přesuň do složky, kde máš soubory uložené, a zadej:
`python main.py`
4. **HOTOVO:** Program proběhne během vteřiny a v tvé složce se objeví nová složka `images/` s hotovými grafy.

---

### Jaké funkce vykresluje

V kódu jsou funkce napsané tak, aby přijímaly různé parametry. Pro samotné vykreslení jsem v souboru `main.py` přednastavil tyto konkrétní tvary:

* **Lineární funkce:** `f(x) = 2x + 3` (rostoucí přímka posunutá na ose y na hodnotu 3)
* **Kvadratická funkce:** `f(x) = x^2 - 2x - 5` (klasická "U" parabola, jejíž vrchol je posunutý mimo střed)
* **Sinus:** `f(x) = 2 * sin(x)` (sinusoida, která je dvakrát vyšší než ta standardní)
* **Exponenciální funkce:** `f(x) = 0.5 * e^x` (rostoucí křivka, která stoupá o něco pomaleji než čisté e^x)
* **Absolutní hodnota:** `f(x) = |x|` (graf ve tvaru písmene "V")
* **Kombinovaný graf:** Zobrazuje najednou jinou lineární funkci (`0.5x + 2`), zrychlený sinus (`3 * sin(0.5x)`) a absolutní hodnotu, aby bylo vidět, jak se dají grafy skládat přes sebe.