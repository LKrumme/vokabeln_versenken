import tkinter as tk
from tkinter.constants import ANCHOR, CENTER, RIGHT
import random
import json
import time

f = open("vokabeln_2.json", encoding="UTF-8")
voks = json.load(f)

random.seed()

root = tk.Tk()
root.title("Vokabeln versenken")
root.geometry("810x275") 
root.iconbitmap("kleines_logo.ico")
schiff_counter = 1
schiff_counter_2 = 1
schiff_register = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
schiff_register_e = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
turn = "s"
first_turn = True
schiff_button_list = []
schiff_button_list2 = []
canimakewhite = True
canimakewhite2 = True
bistdudran = 1

info_text_bottom = tk.StringVar()
info_text_bottom.set("Setze zuerst deine Schiffe!")
info = tk.Label(root, textvariable=info_text_bottom, wraplength=200)
überschrift_bild = tk.PhotoImage(file="kleines_logo.png")
überschrift = tk.Label(root, compound = "right", text="Vokabeln versenken", image=überschrift_bild, font="Times 50")
überschrift.grid(row=0, column=0, padx=100, columnspan=2)

schrift_unter_überschrift = tk.Label(root, text="Gegen wen möchtest du Spielen?", font="Times 25")
schrift_unter_überschrift.grid(row=1, column=0, padx=100, columnspan=2)

bot = tk.Button(root, text="Computer", width=10, height=1, borderwidth=5, font="Times 50", command=lambda: spielfeld_gui_build("bot"))
bot.grid(row=2, column=0)

spieler = tk.Button(root, text="Spieler", width=10, height=1, borderwidth=5, font="Times 50", command=lambda: spielfeld_gui_build("player"))
spieler.grid(row=2, column=1)

def vok_start(full_vok_dic, dude):
    print("hallo")
    if dude == 1:
        global auswahl
        random.seed()
        auswahl = random.choice(list(full_vok_dic.keys()))
        vok_la["text"] = auswahl
    elif dude == 2:
        global auswahl2
        random.seed()
        auswahl2 = random.choice(list(full_vok_dic.keys()))
        vok_lae["text"] = auswahl2

def vok_check(full_vok_dic, dude):
    global bistdudran
    if dude == 1 and bistdudran == 1:
        global richtig
        richtig = False
        for i in full_vok_dic[auswahl].split(", "):
            if vok_en.get().lower() == i.lower():
                    richtig = True
        if richtig:
            info_text_bottom.set("Richtig!")
            vok_en.delete(0, 'end')
            if global_player == "player":
                bistdudran = 2
            return True
        else:
            info_text_bottom.set("Leider Falsch. Jetzt können wir nicht schießen. Die Richtige Antwort wäre '"+full_vok_dic[auswahl]+"' gewesen")
            vok_en.delete(0, 'end')
            if global_player == "bot":
                richtig = False
                pew_pew = random.choice(fields)
                fields.remove(pew_pew)
                pew_num = field_to_num[pew_pew]
                if schiff_register[pew_num] == "s":
                    print("Treffer")
                    pew_pew["bg"] = "red"
                    pew_pew["text"] = "X"
                    pew_pew["command"] = ""
                    schiff_register[pew_num] = "x"
                    if not "s" in schiff_register:
                        for widget in root.winfo_children():
                            widget.destroy()
                        win_label = tk.Label(text="Leider verloren", font="Normal 80", height=5)
                        win_label.pack()
                elif schiff_register[pew_num] == "_":
                    print("Verfehlt")
                    pew_pew["bg"] = "light blue"
                    pew_pew["text"] = "O"
                    pew_pew["command"] = ""
                    schiff_register[pew_num] = "o"
                print(schiff_register)
                vok_start(voks["wortschatz-fabeln"], 1)
            elif global_player == "player":
                vok_start(voks["wortschatz-fabeln"], 2)
                bistdudran = 2
            return False
    elif dude == 2 and bistdudran == 2:
        global richtig2
        richtig2 = False
        for i in full_vok_dic[auswahl2].split(", "):
            if vok_ene.get().lower() == i.lower():
                    richtig2 = True
        if richtig2:
            info_text_bottom.set("Richtig!")
            vok_ene.delete(0, 'end')
            bistdudran = 1
            return True
        else:
            info_text_bottom.set("Falsch. Jetzt können wir nicht schießen. Die Richtige Antwort wäre '"+full_vok_dic[auswahl2]+"' gewesen")
            vok_ene.delete(0, 'end')
            vok_start(voks["wortschatz-fabeln"], 1)
            bistdudran = 1
            return False

def com_but(button, num):
    global richtig, schiff_counter, turn, first_turn, info, schiff_counter_2, canimakewhite, pew_pew, pew_num

    if global_player == "bot":
        if schiff_counter >= 5 and richtig:
            if schiff_register_e[num] == "s":
                info_text_bottom.set("Treffer")
                button["bg"] = "red"
                button["text"] = "X"
                button["command"] = ""
                schiff_register_e[num] = "x"
                if not "s" in schiff_register_e:
                    for widget in root.winfo_children():
                        widget.destroy()
                    win_label = tk.Label(text="Gewonnen!", font="Normal 100", height=5)
                    win_label.pack()
            elif schiff_register_e[num] == "_":
                info_text_bottom.set("Verfehlt")
                button["bg"] = "light blue"
                button["text"] = "O"
                button["command"] = ""
            richtig = False
            pew_pew = random.choice(fields)
            fields.remove(pew_pew)
            pew_num = field_to_num[pew_pew]
            if schiff_register[pew_num] == "s":
                print("Treffer")
                pew_pew["bg"] = "red"
                pew_pew["text"] = "X"
                pew_pew["command"] = ""
                schiff_register[pew_num] = "x"
                if not "s" in schiff_register:
                    for widget in root.winfo_children():
                        widget.destroy()
                    win_label = tk.Label(text="Leider verloren", font="Normal 80", height=5)
                    win_label.pack()
            elif schiff_register[pew_num] == "_":
                print("Verfehlt")
                pew_pew["bg"] = "light blue"
                pew_pew["text"] = "O"
                pew_pew["command"] = ""
                schiff_register[pew_num] = "o"
            print(schiff_register)
            vok_start(voks["wortschatz-fabeln"], 1)
    elif global_player == "player":
        try:
            if turn == "s":
                if schiff_counter_2 == 6 and canimakewhite == True:
                    print("yes")
                    for i in schiff_button_list2:
                        i["bg"] = "SystemButtonFace"
                        i["text"] = " "
                        print("Weiß wien Meista")
                        canimakewhite = False
                if schiff_counter_2 <= 5:
                    if turn == "b":
                        if schiff_register[num] == "s":
                            raise("lmao")
                        else:
                            schiff_register[num] = "s"
                    elif turn == "s":
                        if schiff_register_e[num] == "s":
                            raise("lmao")
                        else:
                            schiff_register_e[num] = "s"
                    schiff_counter_2 += 1
                    button["bg"] = "blue"
                    button["text"] = "S"
                    schiff_button_list2.append(button)
                if schiff_counter >= 5 and richtig:
                    if schiff_register_e[num] == "s":
                        info_text_bottom.set("Treffer")
                        button["bg"] = "red"
                        button["text"] = "X"
                        button["command"] = ""
                        schiff_register_e[num] = "x"
                        if not "s" in schiff_register_e:
                            for widget in root.winfo_children():
                                widget.destroy()
                            win_label = tk.Label(text="Gewonnen!", font="Normal 100", height=5)
                            win_label.pack()
                    elif schiff_register_e[num] == "_":
                        info_text_bottom.set("Verfehlt")
                        button["bg"] = "light blue"
                        button["text"] = "O"
                        button["command"] = ""
                    richtig = False
                    vok_start(voks["wortschatz-fabeln"], 2)
        except:
            pass

def spielfeld_button(button, nummer, player):
    global schiff_counter, turn, first_turn, info, canimakewhite2

    try:
        if turn == player:
            if schiff_counter <= 5:
                if turn == "s":
                    if schiff_register[nummer] == "s":
                        raise("lmao")
                    else:
                        schiff_register[nummer] = "s"
                elif turn == "b":
                    if schiff_register_e[nummer] == "s":
                        raise("lmao")
                    else:
                        schiff_register_e[nummer] = "s"
                schiff_counter += 1
                button["bg"] = "blue"
                button["text"] = "S"
                schiff_button_list.append(button)
            if schiff_counter == 6: 
                if first_turn:
                    first_turn = False
                    if global_player == "bot":
                        for i in range(5):
                            while True:
                                try:
                                    ship = random.randint(0, 24)
                                    if schiff_register_e[ship] == "s":
                                        raise("halt stop")
                                    else:
                                        schiff_register_e[ship] = "s"
                                        print(schiff_register_e)
                                        break
                                except:
                                    print("Kaboom!")
                        info_text_bottom.set("Der Computer hat seine Schiffe gesetzt")
                    vok_start(voks["wortschatz-fabeln"], 1)
            if global_player != "bot":
                if schiff_counter == 6 and canimakewhite2 == True:
                    print(schiff_button_list)
                    for i in schiff_button_list:
                        print("deine Mudda")
                        i["bg"] = "SystemButtonFace"
                        i["text"] = " "
                        canimakewhite2 = False
            if schiff_counter_2 >= 5 and richtig2:
                    if schiff_register[nummer] == "s":
                        info_text_bottom.set("Treffer")
                        button["bg"] = "red"
                        button["text"] = "X"
                        button["command"] = ""
                        schiff_register[nummer] = "x"
                        if not "s" in schiff_register:
                            for widget in root.winfo_children():
                                widget.destroy()
                            win_label = tk.Label(text="Gewonnen!", font="Normal 100", height=5)
                            win_label.pack()
                    elif schiff_register[nummer] == "_":
                        info_text_bottom.set("Verfehlt")
                        button["bg"] = "light blue"
                        button["text"] = "O"
                        button["command"] = ""
                    vok_start(voks["wortschatz-fabeln"], 1)
                
    except:
        pass


def spielfeld_gui_build(player):
    global vok_en, vok_ene, vok_la, vok_lae, vok_bu, vok_bue, a1, a2, a3, a4, a5, b1, b2, b3, b4, b5, c1, c2, c3, c4, c5, d1, d2, d3, d4, d5, e1, e2, e3, e4, e5, field_to_num, fields, global_player

    global_player = player

    überschrift.destroy()
    schrift_unter_überschrift.destroy()
    bot.destroy()
    spieler.destroy()

    root.geometry("850x450")
    leer = tk.Label(root, text=" ", width=6, height=2)
    A = tk.Label(root, text="A", width=6, height=2)
    B = tk.Label(root, text="B", width=6, height=2)
    C = tk.Label(root, text="C", width=6, height=2)
    D = tk.Label(root, text="D", width=6, height=2)
    E = tk.Label(root, text="E", width=6, height=2)

    eins = tk.Label(root, text="1", width=6, height=2)
    zwei = tk.Label(root, text="2", width=6, height=2)
    drei = tk.Label(root, text="3", width=6, height=2)
    vier = tk.Label(root, text="4", width=6, height=2)
    fünf = tk.Label(root, text="5", width=6, height=2)

    a1 = tk.Button(root, text=" ", width=6, height=2, state="normal")
    a2 = tk.Button(root, text=" ", width=6, height=2)
    a3 = tk.Button(root, text=" ", width=6, height=2)
    a4 = tk.Button(root, text=" ", width=6, height=2)
    a5 = tk.Button(root, text=" ", width=6, height=2)

    a1["command"] = lambda: spielfeld_button(a1, 0, "s")
    a2["command"] = lambda: spielfeld_button(a2, 1, "s")
    a3["command"] = lambda: spielfeld_button(a3, 2, "s")
    a4["command"] = lambda: spielfeld_button(a4, 3, "s")
    a5["command"] = lambda: spielfeld_button(a5, 4, "s")

    b1 = tk.Button(root, text=" ", width=6, height=2)
    b2 = tk.Button(root, text=" ", width=6, height=2)
    b3 = tk.Button(root, text=" ", width=6, height=2)
    b4 = tk.Button(root, text=" ", width=6, height=2)
    b5 = tk.Button(root, text=" ", width=6, height=2)

    b1["command"] = lambda: spielfeld_button(b1, 5, "s")
    b2["command"] = lambda: spielfeld_button(b2, 6, "s")
    b3["command"] = lambda: spielfeld_button(b3, 7, "s")
    b4["command"] = lambda: spielfeld_button(b4, 8, "s")
    b5["command"] = lambda: spielfeld_button(b5, 9, "s")

    c1 = tk.Button(root, text=" ", width=6, height=2)
    c2 = tk.Button(root, text=" ", width=6, height=2)
    c3 = tk.Button(root, text=" ", width=6, height=2)
    c4 = tk.Button(root, text=" ", width=6, height=2)
    c5 = tk.Button(root, text=" ", width=6, height=2)
    
    c1["command"] = lambda: spielfeld_button(c1, 10, "s")
    c2["command"] = lambda: spielfeld_button(c2, 11, "s")
    c3["command"] = lambda: spielfeld_button(c3, 12, "s")
    c4["command"] = lambda: spielfeld_button(c4, 13, "s")
    c5["command"] = lambda: spielfeld_button(c5, 14, "s")

    d1 = tk.Button(root, text=" ", width=6, height=2)
    d2 = tk.Button(root, text=" ", width=6, height=2)
    d3 = tk.Button(root, text=" ", width=6, height=2)
    d4 = tk.Button(root, text=" ", width=6, height=2)
    d5 = tk.Button(root, text=" ", width=6, height=2)

    d1["command"] = lambda: spielfeld_button(d1, 15, "s")
    d2["command"] = lambda: spielfeld_button(d2, 16, "s")
    d3["command"] = lambda: spielfeld_button(d3, 17, "s")
    d4["command"] = lambda: spielfeld_button(d4, 18, "s")
    d5["command"] = lambda: spielfeld_button(d5, 19, "s")

    e1 = tk.Button(root, text=" ", width=6, height=2)
    e2 = tk.Button(root, text=" ", width=6, height=2)
    e3 = tk.Button(root, text=" ", width=6, height=2)
    e4 = tk.Button(root, text=" ", width=6, height=2)
    e5 = tk.Button(root, text=" ", width=6, height=2)

    e1["command"] = lambda: spielfeld_button(e1, 20, "s")
    e2["command"] = lambda: spielfeld_button(e2, 21, "s")
    e3["command"] = lambda: spielfeld_button(e3, 22, "s")
    e4["command"] = lambda: spielfeld_button(e4, 23, "s")
    e5["command"] = lambda: spielfeld_button(e5, 24, "s")

    vok_la = tk.Label(root, text="Vokabel", wraplength=100)
    vok_en = tk.Entry(root, width=25)
    vok_bu = tk.Button(root, text="ok", width=6, command= lambda: vok_check(voks["wortschatz-fabeln"], 1))

    field_to_num = {
    a1:0,
    a2:1,
    a3:2,
    a4:3,
    a5:4,
    b1:5,
    b2:6,
    b3:7,
    b4:8,
    b5:9,
    c1:10,
    c2:11,
    c3:12,
    c4:13,
    c5:14,
    d1:15,
    d2:16,
    d3:17,
    d4:18,
    d5:19,
    e1:20,
    e2:21,
    e3:22,
    e4:23,
    e5:24,

    }
    fields = [a1, a2, a3, a4, a5, b1, b2, b3, b4, b5, c1, c2, c3, c4, c5, d1, d2, d3, d4, d5, e1, e2, e3, e4, e5]


    #------------------------------------------------
    #------------------------------------------------
    #------------------------------------------------

    leere = tk.Label(root, text=" ", width=6, height=2)
    Ae = tk.Label(root, text="A", width=6, height=2)
    Be = tk.Label(root, text="B", width=6, height=2)
    Ce = tk.Label(root, text="C", width=6, height=2)
    De = tk.Label(root, text="D", width=6, height=2)
    Ee = tk.Label(root, text="E", width=6, height=2)

    einse = tk.Label(root, text="1", width=6, height=2)
    zweie = tk.Label(root, text="2", width=6, height=2)
    dreie = tk.Label(root, text="3", width=6, height=2)
    viere = tk.Label(root, text="4", width=6, height=2)
    fünfe = tk.Label(root, text="5", width=6, height=2)

    a1e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(a1e, 0))
    a2e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(a2e, 1))
    a3e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(a3e, 2))
    a4e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(a4e, 3))
    a5e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(a5e, 4))

    b1e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(b1e, 5))
    b2e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(b2e, 6))
    b3e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(b3e, 7))
    b4e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(b4e, 8))
    b5e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(b5e, 9))

    c1e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(c1e, 10))
    c2e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(c2e, 11))
    c3e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(c3e, 12))
    c4e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(c4e, 13))
    c5e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(c5e, 14))

    d1e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(d1e, 15))
    d2e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(d2e, 16))
    d3e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(d3e, 17))
    d4e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(d4e, 18))
    d5e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(d5e, 19))

    e1e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(e1e, 20))
    e2e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(e2e, 21))
    e3e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(e3e, 22))
    e4e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(e4e, 23))
    e5e = tk.Button(root, text=" ", width=6, height=2, command=lambda: com_but(e5e, 24))

    if player == "player":

        vok_lae = tk.Label(root, text="Vokabel", wraplength=100)
        vok_ene = tk.Entry(root, width=25)
        vok_bue = tk.Button(root, text="ok", width=6, command= lambda: vok_check(voks["wortschatz-fabeln"], 2))


    elif player == "bot":

        bot_label = tk.Label(root, text="Computer", font="normal 15")

    #------------------------------------------------
    #------------------------------------------------
    #------------------------------------------------

    leer.grid(row=0, column=0)
    eins.grid(row=0, column=1)
    zwei.grid(row=0, column=2)
    drei.grid(row=0, column=3)
    vier.grid(row=0, column=4)
    fünf.grid(row=0, column=5)

    A.grid(row=1, column=0)
    B.grid(row=2, column=0)
    C.grid(row=3, column=0)
    D.grid(row=4, column=0)
    E.grid(row=5, column=0)

    a1.grid(row=1, column=1)
    a2.grid(row=1, column=2)
    a3.grid(row=1, column=3)
    a4.grid(row=1, column=4)
    a5.grid(row=1, column=5)

    b1.grid(row=2, column=1)
    b2.grid(row=2, column=2)
    b3.grid(row=2, column=3)
    b4.grid(row=2, column=4)
    b5.grid(row=2, column=5)

    c1.grid(row=3, column=1)
    c2.grid(row=3, column=2)
    c3.grid(row=3, column=3)
    c4.grid(row=3, column=4)
    c5.grid(row=3, column=5)

    d1.grid(row=4, column=1)
    d2.grid(row=4, column=2)
    d3.grid(row=4, column=3)
    d4.grid(row=4, column=4)
    d5.grid(row=4, column=5)

    e1.grid(row=5, column=1)
    e2.grid(row=5, column=2)
    e3.grid(row=5, column=3)
    e4.grid(row=5, column=4)
    e5.grid(row=5, column=5)

    vok_la.grid(row=6, column=0, columnspan=2, pady=40)
    vok_en.grid(row=6, column=2, columnspan=3, pady=40)
    vok_bu.grid(row=6, column=5, pady=40)
    info.grid(row=6, column=7)

    #------------------------------------------------
    #------------------------------------------------
    #------------------------------------------------

    leere.grid(row=0, column=7, padx=80)
    einse.grid(row=0, column=8)
    zweie.grid(row=0, column=9)
    dreie.grid(row=0, column=10)
    viere.grid(row=0, column=11)
    fünfe.grid(row=0, column=12)

    Ae.grid(row=1, column=13)
    Be.grid(row=2, column=13)
    Ce.grid(row=3, column=13)
    De.grid(row=4, column=13)
    Ee.grid(row=5, column=13)

    a1e.grid(row=1, column=8)
    a2e.grid(row=1, column=9)
    a3e.grid(row=1, column=10)
    a4e.grid(row=1, column=11)
    a5e.grid(row=1, column=12)

    b1e.grid(row=2, column=8)
    b2e.grid(row=2, column=9)
    b3e.grid(row=2, column=10)
    b4e.grid(row=2, column=11)
    b5e.grid(row=2, column=12)

    c1e.grid(row=3, column=8)
    c2e.grid(row=3, column=9)
    c3e.grid(row=3, column=10)
    c4e.grid(row=3, column=11)
    c5e.grid(row=3, column=12)

    d1e.grid(row=4, column=8)
    d2e.grid(row=4, column=9)
    d3e.grid(row=4, column=10)
    d4e.grid(row=4, column=11)
    d5e.grid(row=4, column=12)

    e1e.grid(row=5, column=8)
    e2e.grid(row=5, column=9)
    e3e.grid(row=5, column=10)
    e4e.grid(row=5, column=11)
    e5e.grid(row=5, column=12)

    if player == "player":

        vok_lae.grid(row=6, column=8, columnspan=2, pady=40)
        vok_ene.grid(row=6, column=10, columnspan=3, pady=40)
        vok_bue.grid(row=6, column=13, pady=40)

    elif player == "bot":

        bot_label.grid(row=6, column=8, columnspan=5)


root.mainloop()