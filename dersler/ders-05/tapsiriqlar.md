### Tapşırıqlar

1. `meyveler` adlı list yaradın: `"alma"`, `"armud"`, `"nar"`, `"üzüm"`
2. Yuxarıdakı listdən ilk elementi, son elementi (`-1`), sondan ikinci elementi (`-2`) və 3-cü elementi (`[2]`) çıxarıb göstərin.
3. `ededler = [10, 20, 30]` listinə `.append()` ilə `40` əlavə edin.
4. Daha sonra həmin listə `.insert()` ilə `0` indeksinə `5` əlavə edin. Listi göstərin fərqinə baxın
5. `a = [1, 2, 3]` və `b = [4, 5, 6]` listləri verilib. `extend()` funksiyası ilə listləri birləşdirin
6. `renglər = ["qırmızı", "goy", "yaşıl", "sarı", "mavi"]` listindən göy və sarı rəngləri silin (remove)
7. `ededler = [5, 10, 15, 20, 25]` listindən 1-ci indeksdəki elementi silin (pop)),
8. Həmin listi  `.clear()` ilə listi tam silin
9. `ededler = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` listində slicing ilə çıxarın: ilk 3 element, son 3 element
10. `x = [1, 2, 3]` və `y = [4, 5]` listlərini `+` ilə birləşdirib `z` dəyişəninə yazın. Sonra `[0] * 5` və `[1, 2] * 3` ifadələrinin nəticəsini yoxlayın.
11. `a = [1, 2, 3]` yazın. `b = a` edin, sonra `b.append(4)` yazın və hər iki listi göstərin. Nə görürsünüz? Sonra `c = a.copy()` edib `c.append(5)` yazın və `a`, `c` listlərini göstərin. Fərqi şərh (`#`) ilə izah edin.
12. `ededler = [5, 2, 8, 1, 9, 3]` verilib. Ədədləri azdan çoxa sıralayın və daha çoxdan aza sıralayın (sort)
13. `herfler = ["a", "b", "c", "d"]` listini tərsinə çevirin (reverse)
14. `ededler = [4, 7, 2, 7, 9, 7, 1]` listində 7 rəqəmini sayını tapın (count)
15. `produktlar = ["telefon", "paltar", "meyve"]` verilib. Listdə paltar-ın olub olmadığnın yoxlayın (in). Əgər varsa  "paltar. var" yazılsın yoxdursa "paltar yoxdur" yazılsın
16. `cumle = "Mən Python öyrənirəm və çox sevirəm"` cümləsini `.split()` ilə listə çevirin. Söz sayını `len()` ilə tapın, ilk və son sözü göstərin.
17. `ballar = [85, 92, 70, 66, 100]` listi verilib. `len()`, `min()`, `max()`, `sum()` ilə say, ən kiçik, ən böyük və cəmi tapın və orta balı hesablayın
18. `adlar = ["Elnur", "Aysel", "Vüqar"]` listin kopyasını çıxarın (copy)

### Suallar

* List nədir və necə yaradılır? Eyni listdə müxtəlif tipli elementlər ola bilərmi?
* List elementlərinə hansı indekslə müraciət olunur? İndekslər neçədən başlayır?
* Mənfi indeks nə deməkdir? `a[-1]` nəyi qaytarır?
* `.append()`, `.insert()` və `.extend()` arasında fərq nədir?
* `a.append([4, 5])` ilə `a.extend([4, 5])` nəticəsi necə fərqlənir?
* `.remove()`, `.pop()` və `del` arasında fərq nədir? Hansı silinən elementi qaytarır?
* `.remove()` elementi tapmasa nə baş verir? Eyni elementdən bir neçə dənə varsa hansını silir?
* `.clear()` ilə `del a` arasında fərq nədir?
* `b = a` yazdıqda nə baş verir? Bu niyə problem yarada bilər?
* `.copy()` nə edir və `b = a`-dan nə ilə fərqlənir?
* `.sort()` ilə `sorted()` arasında fərq nədir? Hansı orijinal listi dəyişir və hansı nə qaytarır?
* `a.sort()` yazıb `print(a.sort())` etsək nə çıxar və niyə?
* `.reverse()` ilə `[::-1]` arasında fərq nədir?
* `.index()` ilə `.count()` nə edir? Element listdə yoxdursa nə baş verir?
* `in` və `not in` operatorları nə qaytarır və harada istifadə olunur?
* `.split()` nə edir? Parametrsiz və `.split("-")` kimi parametrlə fərqi nədir?
* `.split()` nəticəsində alınan elementlərin tipi nədir? Onlarla riyazi əməliyyat aparmaq üçün nə etmək lazımdır?
* `len()`, `min()`, `max()`, `sum()` nə edir? Listdə sözlər olarsa `sum()` işləyərmi?
* Slicing zamanı `a[1:3]` yeni list qaytarır, yoxsa orijinalı dəyişir?
