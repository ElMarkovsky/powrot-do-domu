Zadanie jest oparte na wykorzystaniu algorytmu Dijkstry, który ma pomóc w wyznaczeniu najoptymalniejszej trasy dojazdu z punktu A do B uwzględniając dodatkowe czynniki odcinków trasy, czyli np. spalanie.

Do dyspozycji są klasyczne pliki nagłówkowe iostream, cstdio czy vector. Dodatkowo można skorzystać z queue, dodaje potrzebna kolejkę priorytetową.
Dzięki temu pomijamy potrzebę pisania własnej kolejki, pozwalając skupić się na sednie problemu.

Testy sa podzielone na trzy grupy:
- test 00 to test jawny
- testy od 01 do 05 (random) to testy stworzone przy użyciu losowego ziarna
- testy od 06 do 10 (edge) to testy przypadków brzegowych, które powinny ujawnić nieoptymalne oraz niepoprawne rozwiązania
