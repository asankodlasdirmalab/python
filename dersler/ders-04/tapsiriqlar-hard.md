# Python Dərs 4: Şərtlər (conditions)

### Tapşırıqlar



1. `Üçbucağın tərəflərini yaradın (a, b, c).`  Üçbucağın tərəflərini yaradın (a, b, c)Üçbucağın tipini tapın: bərabərtərəfli, bərabəryanlı və ya müxtəlifyanlı.
2. **Parol yoxlayıcısı:** `input()` ilə parol alın. Qaydalar:

   * uzunluq ən az 8 olmalıdır (`len()`),
   * boşluq olmamalıdır (`.count(" ")`),
   * ən az bir böyük hərf olmalıdır (`parol != parol.lower()`),
   * ən az bir kiçik hərf olmalıdır (`parol != parol.upper()`).

   Hər qaydanı ayrıca yoxlayın və pozulan qaydaları göstərin. Hamısı düzgündürsə `"Parol güclüdür"` yazın.
3. **`match-case` kalkulyator:** `input()` ilə iki ədəd (`float()`) və əməliyyat işarəsi alın (`+`, `-`, `*`, `/`, `//`, `%`, `**`). `match` ilə nəticəni hesablayın. `/`, `//` və `%` üçün ikinci ədəd `0` olarsa `case`-in içində `if` ilə `"Sıfıra bölmək olmaz"` yazdırın. Yanlış işarə üçün `case _` istifadə edin. Nəticəni `:.2f` ilə göstərin.
4. **Kvadrat tənlik:** `input()` ilə `a`, `b`, `c` alın. Əvvəlcə `a == 0` halını yoxlayın (kvadrat tənlik deyil). Sonra `D = b**2 - 4*a*c` hesablayın:

   * `D > 0`: iki kök (`(-b ± D**0.5) / (2*a)`),
   * `D == 0`: bir kök,
   * `D < 0`: `"Həqiqi kök yoxdur"`.

   Kökləri `:.2f` ilə göstərin.
5. **Bədən kütlə indeksi:** `input()` ilə çəki (kq) və boyu (metr) alın. `bmi = ceki / boy ** 2` hesablayın. Kateqoriyanı `if/elif/else` ilə təyin edin: `18.5`-dən az `"Arıq"`, `18.5`–`24.9` `"Normal"`, `25`–`29.9` `"Artıq çəki"`, `30` və yuxarı `"Obez"`. Nəticəni göstərin: `BMI: 22.86 -> Normal`. Çəki və ya boy `0` və ya mənfi olarsa xəta mesajı yazın.
6. **Email yoxlayıcısı:** `input()` ilə email alın (`.strip().lower()` ilə təmizləyin). `.find("@")` ilə `@`-in yerini tapın. Email düzgündür, əgər:

   * `@` var (`find() != -1`),
   * `@` birinci simvol deyil,
   * `@`-dən sonrakı hissədə `"."` var,
   * sonluq `".com"` və ya `".az"` ilə bitir (slicing: `[-4:]` və `[-3:]`).

   Düzgündürsə istifadəçi adını və domeni ayrı göstərin, deyilsə hansı şərtin pozulduğunu yazın.
7. **Truthy/falsy proqnozu:** Aşağıdakı ifadələrin nəticəsini  **əvvəlcə kağızda təxmin edin** , sonra `print()` ilə yoxlayın:

```
bool("0")      bool("False")    bool([0])      bool(0.0)
0 or "salam"   "" and 5         "a" and "b"    not ""
None or 0 or "son"
```

Sonra `or` və `and`-in niyə həmişə `True/False` yox, bəzən dəyərin özünü qaytardığını öz sözlərinizlə yazın (şərh kimi).

9. **İç-içə ternary:** `input()` ilə ədəd alın. Tək sətirdə ternary ilə `"müsbət"`, `"mənfi"` və ya `"sıfır"` təyin edin (iç-içə ternary). Sonra ikinci ternary ilə ədədin mütləq qiymətini tapın (`abs()` istifadə etmədən).
10. **Fəsillər və ayın günləri:** `input()` ilə ay nömrəsi (1–12) alın. `match` ilə `|` operatorundan istifadə edin: `case 12 | 1 | 2` → `"Qış"`, `case 3 | 4 | 5` → `"Yaz"` və s. `case _` ilə yanlış nömrəni tutun. Sonra ikinci `match` ilə ayın gün sayını göstərin. Fevral üçün il də alıb **1-ci tapşırıqdakı** kəbisə yoxlamasından istifadə edin.
11. **Endirim sistemi:** `input()` ilə məbləğ, üzvlük (`"bəli"/"xeyr"`) və kupon kodu alın (`.strip().lower()` ilə təmizləyin). Qaydalar:

    * məbləğ `200` və yuxarı: `20%` endirim, `100` və yuxarı: `10%`, qalanı `0%`,
    * üzv isə əlavə `5%`,
    * kupon `"py2024"` isə əlavə `5%`,
    * ümumi endirim `25%`-dən çox ola bilməz.

    Nəticəni göstərin: `Məbləğ: 250.00 | Endirim: 25% | Ödəniləcək: 187.50`.
12. **Mətn analizi:** `input()` ilə cümlə alın. `.strip()` etdikdən sonra boşdursa (truthy/falsy ilə) `"Boş mətn"` yazıb dayandırın. Boş deyilsə hesabat çıxarın:

    * ilk hərf böyükdürmü? (`s[0] == s[0].upper()`),
    * son simvol `.`, `?` və ya `!`-dirmi? (`s[-1]`),
    * söz sayı (`.count(" ") + 1`),
    * ternary ilə `"uzun"` (50 simvoldan çox) və ya `"qısa"`.
13. **Üçrəqəmli ədəd:** `input()` ilə ədədi **string kimi** alın. `len()` ilə 3 rəqəmli olub-olmadığını yoxlayın. Sonra:

    * palindromdurmu? (`[::-1]`),
    * rəqəmlərin cəmi (`int(s[0]) + int(s[1]) + int(s[2])`),
    * cəm cütdürmü, tək?
    * ədəd özü `7`-yə bölünürmü?

    Hamısını f-string ilə göstərin.
14. **Daş-Qayçı-Kağız:** İki oyunçudan `input()` ilə `"daş"`, `"qayçı"` və ya `"kağız"` alın (`.strip().lower()`). Əvvəlcə hər iki giriş düzgündürmü yoxlayın (`or` ilə). Sonra qalibi `if/elif/else` və `and/or` ilə təyin edin: daş qayçını, qayçı kağızı, kağız daşı udur. Bərabərlik halını da nəzərə alın.
15. **Mini ATM:** `balans = 500` verilib. `input()` ilə əməliyyat seçin: `1` balans, `2` pul çıxarma, `3` pul əlavə, `4` çıxış. Seçimi `match` ilə idarə edin. Pul çıxarma üçün:

    * məbləğ `0`-dan böyük olmalıdır,
    * balansdan çox ola bilməz,
    * `10`-un misli olmalıdır (`%`).

    Hər xəta üçün ayrıca mesaj yazın. Uğurlu əməliyyatdan sonra yeni balansı f-string ilə göstərin. Yanlış seçim üçün `case _` istifadə edin.

### Suallar

* `if x = 5:` yazsaq nə baş verir və niyə?
* `1 < x < 10` ifadəsi Python-da necə işləyir? Digər dillərdən nə ilə fərqlənir?
* `x == 1 or 2` ifadəsi niyə həmişə `True` sayılır? Düzgün yazılışı necədir?
* `True or False and False` nə qaytarır? `not`, `and`, `or` arasında üstünlük sırası necədir?
* `0 or "salam"` və `"" and 5` nə qaytarır? Python niyə burada `True/False` yox, dəyərin özünü qaytarır? (short-circuit)
* `bool("False")` nə verir və niyə?
* Ardıcıl bir neçə `if` ilə `if-elif-else` arasında nəticə baxımından nə fərq var? Nümunə ilə izah edin.
* `"10" == 10` nə qaytarır? `"10" < "9"` nə qaytarır və niyə?
* `"Z" < "a"` nəticəsi nədir? Python string-ləri necə müqayisə edir?
* `not x == 5` ilə `x != 5` eynidirmi?
* `0.1 + 0.2 == 0.3` nə qaytarır və niyə? Belə hallarda müqayisəni necə etmək olar?
* İç-içə ternary hansı hallarda pis praktika sayılır? Onu hansı konstruksiya ilə əvəz etmək olar?
* `print("a" if False else "b" if False else "c")` nə çap edəcək?
* `match-case` ilə `if-elif` arasında fərq nədir? Hansı hallarda `match` daha rahatdır?
* `case 1 | 2 | 3:` nə deməkdir? `case _:` ən sonda olmasa nə baş verər?
* `match`-də bir `case` işləyəndən sonra növbəti `case`-lər də yoxlanılırmı?
* `None == False` nə qaytarır? `bool(None)` ilə fərqi nədir?
* Şərt blokunda indentation səhv olarsa nə baş verir? `else` hansı `if`-ə aid olur?
* Eyni məsələni `and/or` ilə yazmaq yaxşıdır, yoxsa iç-içə `if` ilə? Hansı hallarda hansını seçərdiniz?
