image black = "#000"

define angga = Character("Angga", color="#ff0000")
define atma = Character("Atma", color="#0000ff")
define loka = Character("Loka", color="00ff00")

default A1 = False
default B1 = False

# The game starts here.

label start:
    scene black
    "Kring! kring! kring!"

    scene bg room
    with fade

    show angga sleep
    angga "Zzz..."
    show atma at right
    atma "Woy Angga! Buruan bangun!"
    angga "Hmm."
    atma "Matiin itu alarm! Berisik. Buruan siap-siap. Gw tunggu di depan."
    angga "Iya iya."

    scene black
    with fade
    "15 menit kemudian..."

    scene bg home
    
    show atma
    atma "Udah? Ayo berangkat!"
    hide atma
    
    show angga
    angga "Ayo! Kenapa gak nunggu di depan?"
    hide angga

    show atma
    atma "Tau dah."
    hide atma

    scene bg road
    with fade

    show atma
    atma "Bakal ngapain aja hari ini? Ada tugas kah?"
    hide atma

    show angga
    angga "Hmm."
    hide angga

    show angga shock
    angga "O iya! Hari ini kelas biologi ada tugas buat makalah soal otak."
    hide angga
    
    show angga
    angga "Untung kelas biologi mulai habis jam istirahat pertama."
    angga "Menurut lu kita harus gimana?"
    hide angga

    show atma angry
    atma "Jujur aja gw gedek sama itu guru biologi. Dikit-dikit tugas. Suruh ini. Suruh itu. Kek babu."
    hide atma

    show atma
    atma "Kita bolos aja. Gw temenin."
    hide atma

    show angga
    angga "Beneran? Kalo kita doang gak mau gw."
    hide angga

    show atma
    atma "Cuman bolos satu kelas doang kok. Ntar kita balik lagi habis kelas biologi selesai."
    hide atma

    show angga
    angga "Hmm."
    show loka at right
    with dissolve
    loka "Yo Angga!"
    angga "Yo Loka! Tumben dateng jam segini. Biasanya lu dateng pagi-pagi."
    hide angga

    show loka at center
    loka "Gw juga bingung. Kebetulan aja mungkin."
    loka "Eh gimana tugas biologi? Aman?"
    hide loka

    show angga
    angga "Gw lupa ngerjain. Hehe."
    hide angga

    show loka
    loka "Lu mah kebiasaan."

menu:
    "Ajak Loka bolos.":
        jump A1
    
    "Minta tolong Loka kerjain tugas.":
        jump A2

label A1:
    $ A1 = True

    hide loka
    show angga
    angga "Kelas biologi nanti temenin gw bolos mau gak? Gw traktir makan."
    hide angga

    show loka shock
    loka "Yang bener aja lu! Ogah."
    loka "Lu gak risih ya dimarahin mulu?"
    hide loka

    show angga
    angga "Makanya gw pingin bolos."
    hide angga

    show loka
    loka "Kalo ada masalah mending hadepin. Jangan malah kabur. Ntar pasti gw yang kena marah."
    hide loka

    show angga
    angga "Iya iya. Si paling mending."
    hide angga

    jump sekolah

label A2:
    hide loka
    show angga
    angga "Lu mau gak kerjain tugas gw. Ntar gw traktir di kantin."
    hide angga

    show loka
    loka "Kerjain sendiri lah! Asal lu niat ngerjain, gw bantu, gak perlu bayar. Gimana? Baik banget kan gw."
    hide loka

    show angga
    angga "Iya iya. Si paling baik."
    hide angga

    jump sekolah

label sekolah:
    with fade

    show angga
    show loka at right
    show atma at left
    "..."

    scene black
    with fade

    scene bg school
    with fade

    show angga
    show loka at right
    show atma at left
    "..."
    hide angga
    hide loka
    hide atma

    show atma
    atma "Angga sini bentar!"
    hide atma

    show angga
    show loka at right
    angga "Lu duluan aja, Lok. Gw mau ke toilet dulu."
    loka "Ok. Gw ingetin lagi. Jangan kabur lu!"
    angga "Hmm."
    hide angga
    hide loka

    scene bg toilet
    with fade
    
    if A1:
        show atma angry
        atma "Ngapain lu ngajak si Loka?!"
        hide atma

        show angga
        angga "Biar tenang kalo bolosnya rame-rame."
        hide angga

        show atma angry
        atma "Lu kan tau dia si paling rajin. Pasti gak mau. "
        atma "Dia jadi tau dong kita mau bolos."
        hide atma

        show angga
        angga "Hmm. Jadi mau lu gimana?"
        hide angga

    else:
        show atma angry
        atma "Ngapain lu dengerin saran si Loka?!"
        hide atma

        show angga
        angga "Apa salahnya? Dia mau bantu."
        hide angga

        show atma angry
        atma "Emang gua gak bantuin lu? Gua temenin lu bolos tau!"
        hide atma

        show angga
        angga "Hmm. Jadi mau lu gimana?"
        hide angga
    
    show atma
    atma "Ya lu dengerin gua dong."
    atma "Lu tanya ke gua. Gua bisa kasih saran ke lu."
    atma "Gak kaya Loka & guru biologi yang sering kasih tau lu, habis itu ninggalin lu. Gua bakal tetep temenin lu. Apapun masalahnya. Di mana pun."

menu:
    "Selalu dengarkan saran Atma":
        jump B1
    
    "Ikuti saran Atma tergantung situasinya":
        jump B2

label B1:
    $ B1 = True
    show atma happy
    atma "Nah gitu dong." 
    
    jump school2

label B2:
    show atma sad
    atma "Oke. Rasain sendiri resikonya."
    
    jump school2


label school2:
    "Kring!!!"

    show angga
    show atma at right
    "..."

    scene black
    with fade

    show bg classroom
    with fade
    "..."

    return