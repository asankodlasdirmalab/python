# Python Dərs 3: String ilə işləmə

### Tapşırıqlar

1. İstifadəçidən `input()` ilə yaşını alın və terminalda belə bir cümlə yazılsın `"Sizin 25 yaşınız var və beş ildən sonra 30 olacaq"`
2. `"  eLNUR   əLİYEV  "` Bu text elə edənki həm ətrafındakı boşluqlar silinsin və "Elnur Əliyev" şəklində yazılsın
3. `email = "user@example.com"` verilib. `.find()` ilə `@` simvolunun indeksini tapın, slicing ilə istifadəçi adını (`user`) və domeni (`example.com`) ayrı-ayrı götürün
4. `text = "Python rahatdır. Python böyükdür. Python maraqlıdır."` mətnində:

   * `"Python"` sözünün neçə dəfə olduğunu tapın,
   * `"Python"` sözünü `"Java"` ilə əvəz edin
5. hər hansı sözü tərsinə çevirin (`[::-1]`)
6. Üç dəyişən təyin edin: `mehsul = "noutbuk"`, `qiymet = 1250.5`, `say = 3`. Çoxsətirli f-string (`f"""..."""`) ilə qəbz yazdırın: məhsul adı, qiymət, say və ümumi məbləğ (`qiymet * say`).
7. `telefon = "+994 50 123 45 67"` verilib. Boşluqları `.replace()` ilə silin, yeni nömrənin uzunluğunu tapın
8. Dəyişən yaradın: `s = "Jython"`. `s[0] = "P"` yazıb nə baş verdiyini yoxlayın. Xətanın səbəbini izah edin və sözü `"Jython"` formasına salmağın düzgün yolunu tapın
9. `x = 10`, `y = 3` yaradın və f-stringlər bir cümlədə bunların toplamasını, vurmasını, bölməsini yazın
10. `s = "Pyhton çox asan dildir"` cümləsində `"Pyhton"` səhvini düzəldin.
11. `s = "Mən cay sevirəm, cay içirəm, cay alıram"` cümləsində əvvəlcə `"cay"` sözünün neçə dəfə keçdiyini `.count()` ilə tapın. Sonra `"cay"` sözünü `"kofe"` ilə əvəz edin
12. `s = "öyrənirəm Python mən"` cümləsində sözlərin sırası səhvdir. düzgün cümlə qurun: `Mən Python öyrənirəm`.
13. `data = "Bakı 22 Elnur"` verilib. Bu cümləni: `Mənim adım Elnur, yaşım 22-dir, şəhərim Bakıdır`. kimi yazın

### Suallar

* `text = "Python"` `text[-1]`, `text[-3:]` və `text[::-1]` nə qaytarır?
* `text[2:5]` ifadəsində 5-ci indeksdəki simvol nəticəyə daxil olurmu və niyə?
* `.find()` ilə `.count()` arasında fərq nədir? Hansı hallarda hansından istifadə edərdiniz?
* `"Salam".replace("a", "o")` ifadəsi neçə `a`-nı əvəz edir və orijinal sətir dəyişirmi?
* Üç dırnaqlı (`"""`) sətir ilə adi sətir arasında `print()` zamanı nə fərq var? `len()` bu sətirdə sətir keçidlərini də sayırmı?
* f-string ilə `+` birləşdirməsi arasında hansı üstünlük və çatışmazlıqlar var? Hansı hallarda f-string xəta verməyə bilər, `+` isə verər?
*
