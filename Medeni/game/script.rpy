image black = "#000"

define angga = Character("Angga", color="#ff0000")
define atma = Character("Atma", color="#0000ff")
define loka = Character("Loka", color="00ff00")

default A1 = False
default B1 = False
default C1 = False
default D1 = False

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

menu A:
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

menu B:
    "Selalu dengarkan saran Atma":
        jump B1
    
    "Ikuti saran Atma tergantung situasinya":
        jump B2

label B1:
    $ B1 = True

    hide atma
    show angga
    angga "Iya iya. Gw bakal dengerin lu kok."
    hide angga
    
    show atma happy
    atma "Nah gitu dong. Gw kan temenin lu ke mana-mana" 
    hide atma
    
    jump school2

label B2:
    show angga
    angga "Ya tergantung situasinya. Gw ikut saran yang beneran dukung gw."
    hide angga

    show atma sad
    atma "Oke. Rasain sendiri resikonya. Jangan bawa-bawa gw kalo sarannya bukan dari gw."
    hide atma
    
    jump school2


label school2:
    
    show angga
    show atma at right
    "Kring!!!"

    scene black
    with fade

    show bg classroom
    with fade
    "..."
    show angga
    with moveinleft
    "..."
    hide angga

    show bg classroomfull
    with dissolve
    "2 jam kemudian ..."

    show bg classroom
    with fade
    "Kring!!!"

    if A1:
        show angga
        angga "Jadinya kita mau pergi kemana?"
        hide angga

        show atma
        atma "Yang penting kita ke depan dulu. Ayo!"
        hide atma

    else:
        show atma
        atma "Ayo buruan pergi! Si Loka ke sini. Gw yakin bakal ceramahin lu."
        hide atma

        if B1:
            show angga
            angga "Iya iya, sabar. Beresin tas dulu."
            hide angga

            show atma
            atma "Udah? Ayo."
            hide atma

            show angga
            angga "Gas."
            hide angga
            
        else:
            show angga
            angga "Si Loka doang mah gpp. Takut banget lu."
            hide angga

            show atma
            atma "Hih. Ngeyel banget sih lu."
            hide atma

            show angga
            show loka at right
            with dissolve
            loka "Yo Angga! Ke perpus yuk. Tugas lu belum kan? Gua bantuin."
    
    if A1 or B1:
        show angga
        with moveinleft
        show loka at right
        with zoomin
        loka "Hayo... Mau kemana lu?"
        angga "Hehe."
        loka "Lu mau bolos ya?"
        
    loka "Udah, ayo ke perpus! Kelarin tugas lu. Gw gak mau kena marah."
    angga "Eeeh..."
    hide loka
    with moveoutright
    hide angga
    with moveoutright
    angga "Kenapa gw diseret-seret?"

    scene bg school
    with dissolve

    show angga
    show loka at right
    show atma at left
    atma "Sstt.. Angga. Lu beneran mau ke perpus?"
    atma "Gw kasih tau sesuatu. Tapi jangan kedengeran Loka."

menu C:
    "Ikut Loka ke perpus?":
        jump C1

    "Ke toilet dulu. Dengarkan Atma.":
        jump C2


label C1:
    if C1:
        scene bg toilet
        show angga
        show atma at left
    
    $ C1 = True

    angga "Gw mau ke perpus. Tapi gw mau kantin dulu."
    show atma angry
    atma "Ngapain sih? Emang lu masih ada waktu?"
    atma "Pokoknya gw mau ke depan sekolah. Kalo lu nanti gak dateng, gw gak bakal temenin lu lagi."
    atma "Awas aja lu kalo sampe gak dateng!"
    hide atma
    with moveoutleft

    jump canteen    

label C2:
    angga "Bentar Lok. Gw kebelet kencing."
    show loka angry
    loka "Jangan banyak alesan."
    angga "Sumpah Lok. Kalo gak percaya gua kencingin lu mau?"
    loka "Yaudah. Gw tungguin di depan pintu. Biar lu gak kabur."
    hide angga
    hide atma
    hide loka

    scene bg toilet
    with fade
    
    show angga
    angga "Atma, jadi gimana?"
    hide angga

    show atma
    atma "Tenang. Lu ngumpet di belakang orang gendut ini. Trus kabur."
    atma "Atau gak. Kalo lu males ngedepin Loka & guru biologi, lu kasih aja si Loka duit biar diem."

menu D:
    "Kabur":
        $ D1 = True
        jump D1

    "Nego ke Loka":
        jump D2

    "Ikut Loka ke perpus":
        $ C1 = True
        jump C1
        

label D1:
    if D1:
        scene bg school
        with fade

    show angga at right
    with moveinleft
    angga "Sorry ya Lok! Salam buat pak biologi. Hehe."
    hide angga
    with moveoutright

    show loka
    loka "Sial. Kegocek gw."
    hide loka

    jump road

label D2:
    scene bg school
    with fade
    
    show angga
    angga "Gini aja, Lok. Biar kita sama-sama seneng. Gw kasih lu duit. Tapi lu bilang sama guru biologi gw lagi di UKS. Oke?"
    hide angga

    show loka
    loka "Hmm. Kan! Mulai lagi ni anak."
    hide loka
    
    show angga
    angga "Ayolah, Lok."
    hide angga

    show loka
    loka "Tanggung jawab sendiri lah, Ngga. Mau sampe kapan lu kaya gini."
    hide loka

    show angga
    angga "Gw bukan mau denger ceramah lu. Jadi, mau gak?"
    hide angga

    show loka
    loka "Hmm. 1 miliyar. Bisa?"
    hide loka

    show angga
    angga "Lu mah gitu. Si paling harga diri. "
    angga "Terpaksa, rencana B."
    hide angga

    show loka
    loka "Rencana B?"
    hide loka

    jump D1

label canteen:
    scene bg school
    with fade

    show angga
    angga "Ke kantin dulu yuk, Lok! Laper nih. Gw traktir."
    hide angga

    show loka
    loka "Hmm. Ada maunya nih."
    hide loka

    show angga
    angga "Kali ini gak ada maksud apa-apa, sumpah."
    hide angga

    show loka
    loka "Okelah. Pokoknya harus cepet. Kalo sampe ada siasat, gw aduin lu."
    hide loka

label road:
    scene bg road
    with fade
    
    "..."

    return