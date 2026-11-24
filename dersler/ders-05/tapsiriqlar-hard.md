## Python Dərs 5: List-lər (Siyahılar)

### Tapşırıqlar

1. `sebet = []` boş list yaradın. `input()` ilə listə 3 məhsul əlavə edin
2. `input()` ilə boşluqla ayrılmış ədədlər alın (məsələn: `4 8 15 16 23 42`). və onu listə çevirin
3. **Aşağıdakı kodu nəticəsi olacaq (izah edin)**

   python

   ```python
   a = [1, 2, 3]
   b = a
   c = a.copy()
   d = a[:]
   e = a + []
   b.append(4)
   c.append(5)
   d.append(6)
   e.append(7)
   print(a, b, c, d, e)
   print(a is b, a is c, a is d, a is e)
   ```
4. `cumle = "  python   çox   asan   dildir  "` verilib. Sözlərin sayını tapın
5. **Sadə qiymət jurnalı:** `adlar = ["Elnur", "Aysel", "Vüqar", "Leyla"]` və `ballar = [85, 92, 70, 66]` paralel listləri verilib. Aşağıdakıları edin:

   * ən yüksək balı `max()` ilə, tələbinin indeksini tapın
6. **Mətnin söz statistikası:** `text = "python is great python is easy python is fun"` verilib. `.split()` ilə listə çevirin. Tapın:

   * ümumi söz sayı,
   * `"python"` və `"is"` sözlərinin neçə dəfə keçdiyi (`.count()`),
   * ilk `"is"`-in indeksi, ikinci `"is"`-in indeksi (`.index("is", başlanğıc)` ikinci parametrini araşdırın),
   * `"python"` sözünü bütün yerlərdən silin (`.remove()` + `.count()` ilə),
   * yeni listin uzunluğu və qalan sözlər.
7. Aşağıdakı kodda **5 səhv** var. Tapın və düzəldin

   python

   ```python
   ededler = [5, 3, 9, 1]
   sirali = ededler.sort()
   print(sirali[0])
   ededler.append(2, 4)
   ededler.remove(100)
   print(ededler[10])
   cəm = sum(["1", "2", "3"])
   ```
8. **Sıra əməliyyatları:** `a = [1, 2, 3, 4, 5]` verilib.

   * ilk elementi sona keçirin
   * son elementi əvvələ keçirin
   * ortadakı elementi silin
   * `99`-u 2-ci indeksə əlavə edin
