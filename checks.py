from datetime import datetime

with open('daylogs.txt',mode='r') as logs:
    levent = logs.readline()
pass

#timedate = datetime.now().strftime(" [%Y-%m-%d %H:%M:%S]")

switch = {
    't' : "Telefonat mit ",
    '@' : "Mail an ",
    'u' : "Update von ",
    'c' : "Commit in ",
    '<' : "Eingang: ",
    '>' : "Nachricht an ",
    'fg' : "Fenster geöffnet im ",
    'fs' : "Fenster geschlossen im ",
    'p' : "Es läuft gerade: ",
    'ws': "Starte Arbeit an",
    'wf': "Beende Arbeit an"
    }

def longForShort(c):
    return switch.get(c, c + " ")

def dialog():
    print("Log your events \n","last event: \n")
    print(levent)
pass

def addevent(name):
    with open('daylogs.txt') as logdata:
        data = logdata.read()
    logfile = open("daylogs.txt","w")
    timedate = datetime.now().strftime(" [%Y-%m-%d %H:%M:%S]")
    finlog = ("%s %s")%(timedate, name)
    logfile.write(str(finlog))
    logfile.write('\n')
    logfile.write(data)
    logfile.close()

pass

def run():
    dialog()
    name = input("eventname ?")
    split_name = name.split(" ")
    prefix = split_name[0]
    name = longForShort(prefix) + " ".join(split_name[1:])
    addevent(name)
    
def show_help():
    print("Just type in occurring events for logging in the text file.")
    print("Available prefixes:\n===============")
    for k, v in switch.items():
        print(k, v)

if __name__ == "__main__":
    while True:
        run()
        userinput2 = input("Next? Type q for quit. ")
        if userinput2 == "h":
            show_help()
            continue
        if userinput2 == "q":
            break