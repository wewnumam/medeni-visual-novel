image black = "#000"

define angga = Character("Angga")
define atma = Character("Atma")
define loka = Character("Loka")

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

    show atma
    atma "Matiin itu alarm! Berisik. Buruan siap-siap. Ku tunggu di depan."

    show angga sleepy
    angga "Iya iya."

    scene black
    with fade
    "15 menit kemudian..."

    scene bg home
    
    show atma
    atma "Udah? Ayok berangkat."
    
    show angga
    angga "Ayok. Kenapa gak nunggu di depan?"

    hide angga
    show atma
    atma "Tau dah."

    scene bg road
    with fade

    show atma
    atma "Bakal ngapain aja hari ini? Ada tugas kah?"

    show angga
    angga "Hmm."

    show angga shock
    angga "O iya! Hari ini kelas biologi ada tugas buat makalah soal otak."
    
    show angga
    angga "Untung kelas biologi mulai habis jam istirahat pertama."
    angga "Menurutmu kita harus gimana?"

    hide angga
    show atma angry
    atma "Jujur aja gw gedek sama itu guru biologi. Dikit-dikit tugas. Suruh ini. Suruh itu. Kek babu."

    show atma
    atma "Kita bolos aja. Gw temenin."

    show angga
    angga "Beneran? Kalo kita doang gak mau gw."

    hide angga
    show atma
    atma "Cuman bolos satu kelas doang kok. Ntar kita balik lagi habis kelas biologi selesai."

    show angga
    angga "Hmm."

    show loka at right
    with dissolve

    loka "Yo Angga!"

    return
