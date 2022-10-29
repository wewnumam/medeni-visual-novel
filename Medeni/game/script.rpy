image black = "#000"

define angga = Character("Angga", color="#ff0000")
define atma = Character("Atma", color="#0000ff")
define loka = Character("Loka", color="#00ff00")
define buyudi = Character("Bu Wahyudiyawati", color="#fff")

default A1 = False
default B1 = False
default C1 = False
default D1 = False
default E1 = False

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
    atma "Jujur aja gw gedek sama itu Bu Wahyudiyawati guru biologi. Dikit-dikit tugas. Suruh ini. Suruh itu. Kek babu."
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
    atma "Gak kaya Loka & Bu Wahyudiyawati yang sering kasih tau lu, habis itu ninggalin lu. Gua bakal tetep temenin lu. Apapun masalahnya. Di mana pun."

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
    atma "Atau gak. Kalo lu males ngedepin Loka & Bu Wahyudiyawati, lu kasih aja si Loka duit biar diem."

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

    $ D1 = True

    show angga at right
    with moveinleft
    angga "Sorry ya Lok! Salam buat Bu Wahyudiyawati. Hehe."
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
    angga "Gini aja, Lok. Biar kita sama-sama seneng. Gw kasih lu duit. Tapi lu bilang sama Bu Wahyudiyawati gw lagi di UKS. Oke?"
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

    scene bg canteen
    with fade

    show loka
    loka "Pokoknya nanti lu buka dulu Wikipedia trus cari daftar-daftarnya."
    hide loka

    show angga
    angga "..."
    hide angga

    show loka
    loka "Paham?"
    hide loka

    show angga
    angga "..."
    hide angga

    show loka
    loka "Lu dengerin gua gak sih? Dari tadi nengok jam terus. Ada apa sih?"
    hide loka

    show angga
    angga "Sebenernya gw lagi ditungguin Atma di luar. Gimana dong?"
    hide angga

    show loka
    loka "Hmm."
    loka "Gini. Gw bakal selalu ingetin lu buat mandiri & tanggung jawab sendiri sama diri lu. Keputusan lu harus lu sendiri yang buat."
    loka "Jadi sekarang gimana keputusan lu?"

    menu E:
        "Temui Atma. Obrolin saran Loka.":
            hide loka
            jump E1
        "Pergi ke perpustakaan bersama Loka":
            hide loka
            jump E2
        

label road:
    scene bg road
    with fade
    
    show angga
    angga "Inpo."
    hide angga

    show loka
    loka "Ke warung depan yuk!"
    hide loka

    show angga
    angga "Gas."
    hide angga

    jump school3

label E1:
    show angga
    angga "Oke. Makasih saran lu, Lok. Gw bakal obrolin dulu."
    angga "Kali ini beneran. Gw bakal berubah."
    hide angga

    show loka
    loka "Nah. Gitu dong."
    loka "Buat sekarang yang terpenting lu konsisten dulu."
    hide loka

    show angga
    angga "Oke. Kalo gitu gw ke depan dulu ya. Tenang gw gak kabur."
    hide angga
    with moveoutright

    show loka
    loka "Hmm. Keyakinan gw masih 50/50. Tapi yaudah lah."
    hide loka

    scene bg road
    with fade

    show angga
    angga "Yo Atma!"
    hide angga
    
    show atma
    atma "Gas yuk sekarang!"
    hide atma

    show angga
    angga "Bentar! Gw mau ngomong bentar."
    angga "Kayaknya gw gak dulu deh. Gw mau ngurang-ngurangin masalah gw."
    hide angga

    show atma angry
    atma "Ngapain! Masalah lama kelamaan juga ilang. Mending ngabisin waktu sama gw daripada murung tiap hari ngadepin masalah."
    hide atma

    show angga
    angga "Pokoknya gw mau coba dulu sesekali."
    hide angga

    show atma
    atma "Ujung-ujungnya lu bakal nyesel, yakin deh sama gw."
    hide atma

    show angga
    angga "Gw emang gak ngeraguin lu. Tapi kali ini gw mau bikin keputusan sendiri. Kalo lu beneran temen gw, lu harusnya dukung gw."
    hide angga
    with moveoutright
    angga "Bye."

    jump school3

label E2:
    show angga
    angga "Oke. Makasih saran lu, Lok. Kali ini beneran. Gw bakal berubah."
    hide angga

    show loka
    loka "Nah. Gitu dong."
    loka "Buat sekarang yang terpenting lu konsisten dulu."
    hide loka

    show angga
    angga "Oke."
    hide angga

    show loka
    loka "Yuk ke perpus!"
    hide loka

    show angga
    angga "Ayo."
    hide angga

    jump school3

label school3:
    if D1:
        scene black
        with fade
        "Kelas dimulai."

        scene bg classroomfull
        with fade

        show buyudi
        buyudi "Ada yang tau kemana Angga?"
        buyudi "Loka, ke mana si Angga?"
        hide buyudi

        show loka
        loka "Dia kabur bu. Belum ngerjain tugas."
        hide loka

        show buyudi angry
        buyudi "Kenapa kamu biarin! Kasih tau dong!"
        hide buyudi

        show loka
        loka "Sudah bu. Sudah saya kasih tau."
        hide loka

        show buyudi angry
        buyudi "Arghh!"
        hide buyudi

        scene black
        with fade

        "Kelas biologi berakhir."

        scene bg classroom
        with fade

        show angga
        with moveinright
        angga "Hehe. Sorry ya, Lok."
        hide angga

        show loka angry
        loka "Capek gw, Ngga."
        hide loka

        show angga
        angga "Jangan marah gitu dong, Lok. Ntar pulang sekolah gw traktir di intimart deh."
        hide angga

        show loka angry
        loka "Gw bingung. Sebenernya apa sih yang lu cari?"
        hide loka

        show angga
        angga "Ya nikmatin hari-hari. Bareng si Atma."
        hide angga

        show loka angry
        loka "Maksud lu sendirian?"
        hide loka
        show loka
        loka "Eh.."
        hide loka

        show angga
        angga "Sendirian?"
        hide angga
        
    else:
        scene black
        with fade
        "Loka dan Angga menyelesaikan tugas. Setelah itu kelas dimulai."

        scene bg classroomfull
        with fade

        show buyudi
        buyudi "Kerjaanmu bagus Angga. Buat sendiri apa nyontek?"
        hide buyudi

        show angga sad
        angga "Sendiri Bu."
        hide angga

        show loka
        loka "Angga ngerjain sendiri kok, Bu. Tadi sama saya di perpus."
        hide loka

        show buyudi
        buyudi "Akhirnya! Kamu mulai niat sekolah ya Angga."
        buyudi "Tingkatkan! Selalu kasih arahan ya, Lok."
        hide buyudi

        show loka
        loka "Siap bu."
        loka "Angga, tanggepin dong."
        hide loka

        show angga sad
        angga "Iya Bu... Siap."
        hide angga

        scene black
        with fade

        "Kelas biologi berakhir."

        scene bg classroom
        with fade

        show loka
        loka "Yo Angga! Kenapa lu? Dipuji-puji malah murung."
        hide loka

        show angga
        angga "Gw juga bingung. Gw ngerasa kosong."
        hide angga

        show loka
        loka "Emang apa sih yang lu cari?"
        hide loka

        show angga
        angga "Kayaknya gw perlu ngajak Atma deh. Gw gak bisa nikmatin hasilnya sendirian."
        hide angga
    
    jump ending


label ending:
    show loka
    loka "Hmm. Gimana ya ngomongnya. Gini..."
    loka "Sebenernya gw pingin ngomong ini dari lama."
    loka "Atma itu siapa?"
    hide loka

    show angga
    angga "Temen gw. Tadi pagi kita berangkat bareng. Masa lu sadar sih."
    hide angga

    show loka
    loka "Hmm. Gini deh. Lu bisa gak jelasin latar belakang dia?"
    hide loka

    show angga
    angga "Atma itu orang yang..."
    angga "yang... hmm...."
    hide angga

    show loka
    loka "Gini, Ngga. Lu tau gak kalo Atma itu gak ada?"
    hide loka

    show angga
    angga "..."
    atma "Angga..."
    hide angga

    scene black
    with fade
    angga "Hmm."
    
    scene bg room
    with fade

    show atma
    atma "Woy Angga! Buruan bangun!"
    angga "Hmm."
    atma "Matiin itu alarm! Berisik. Buruan siap-siap. Gw tunggu di depan."
    angga "Hah."

    return