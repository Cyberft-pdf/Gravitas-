# Gravitas-


1. Dolní hranice filtru
~10 Hz: Tato hodnota je běžně používána pro detekci gravitačních vln z binárních systémů černých děr a neutronových hvězd, protože signály z těchto zdrojů často začínají v této oblasti.
~50 Hz: Můžeš zvážit nastavení dolní hranice na 50 Hz, což pomůže odstranit nízkofrekvenční šum, například ten způsobený seismickou aktivitou.

3. Horní hranice filtru
~300 Hz: Tato hodnota je často používána jako kompromis mezi šumem a detekcí relevantních signálů, například ze spirálujících černých děr.
~400 Hz a více: Pokud chceš zahrnout události jako jsou supernovy nebo formování neutronových hvězd, můžeš zvýšit horní hranici na 400 Hz nebo i výše. Měj ale na paměti, že vyšší frekvence mohou zahrnovat více šumu.

4. Experimentování s hodnotami
Můžeš začít s širším pásmem, například 50 Hz až 400 Hz, a analyzovat data. Pokud zjistíš, že obsahuje příliš mnoho šumu, můžeš horní hranici snížit, případně použít pokročilejší metody filtrace.
Příklad použití filtru
python

Bandpass filtr pro odstranění šumu, s dolní a horní hranicí
filtered_data = data.bandpass(50, 400)  # Dolní hranice 50 Hz, horní hranice 400 Hz

Tento filtr by měl zachytit většinu relevantních signálů z binárních systémů, supernov a jiných astrofyzikálních jevů, zatímco by měl odstranit část šumu. Pokud si všimneš příliš mnoha falešných poplachů, můžeš horní hranici snížit na 300 Hz.
