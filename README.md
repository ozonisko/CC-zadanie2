# CC-zadanie2
Task 2: Minimum effort

Po poznaniu treści zadania od razu pomyślałem o teorii grafów. Przeszukując różne algorytmy zdecydowałem się na
algorytm Dijkstry do znajdowania najkrótszej ścieżki z pojedynczego źródła w grafie o nieujemnych wagach krawędzi.
Gdzie źródłem był element w górnym lewym rogu, a celem element w dolnym prawym rogu.

Elementy macierzy były wierzchołkami grafu, a każdy wierzchołek był połączony krawędzią z wierzchołkiem z dołu i z prawej strony
(ruch tylko w dół i w prawo). 

Linie 82 - 104 Przygotowanie macierzy
Wszystkie linie z pliku są wczytywane do 'data'
Pierwsza liczba mówi ile następnych linii połączyć w macierz. Gdy licznik dojdzie do zera macierz jest wysyłana do funkcji tworzącej graf. Jeżeli nie nastąpił koniec pliku to czynność powtarza się.

Linie 68 - 80 Tworzenie grafu
W pierwszej pętli tworzone są wierzchołki o nazwach kolejno 1,2,3...len(matrix)
W następnej krawędzie poziomie i pionowe w taki sposób aby nie wyjść poza rozmiar macierzy. Krawędzie mają wartość równą wartości kosztu wierzchołka do którego prowadzą.

Tak przygotowany graf wysyłany jest do funkcji znajdującej najmniej kosztowną ścieżkę, a na końcu dodawana jest wartość pierwszego elementu, do którego nie prowadzi żadna krawędź.

Tego typu problemy i ich złożoność obliczeniowa będą z pewnością tematem przedmiotu 'badania operacyjne', który będę realizował w tym semestrze. 
