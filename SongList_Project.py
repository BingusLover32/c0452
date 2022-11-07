import random

def view():
    with open('songlist.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            song, artist, playcount = data.split("|") #Split will look for "|" and return a list where all items between "|" are.
            print(song, "|", artist, "|", str(playcount), "Plays")

def add():
    song = input("Song Name: ")
    artist = input("Artist Name: ")
    playcount = random.randint(0,10000)

    with open('songlist.txt', 'a') as f:  # "with open()" opens a file. the first input is the name of the file,
    # the second input is the mode. (w: write, will clear file and make new one)(r: read, will only read file)(a: append, adds onto end of file or creates new file)
        f.write(song + "|" + artist + "|" + str(playcount) + "\n") #write() is just a glorified print() where it adds it to the file. "\n" is a linebreak

def remove():
    del_line_num = int(input("What number song do you want to remove? "))
    with open("songlist.txt") as file:
        lines = file.readlines()

    if (del_line_num <= len(lines)):
        RUSure = input ("are you sure? (Y or N): ").lower()
        if RUSure == "y":
            del lines[del_line_num - 1] 
            print("Line", del_line_num, "DELETED!")

            with open("songlist.txt", "w") as file:
                for line in lines:
                    file.write(line)
        else:
            print("Delete Cancelled")
        
        
    else:
        print("There is no song at the (", del_line_num, ") spot!")
        print ("There are", len(lines), "Songs")

print("---WELCOME TO OLLYS SPOTIFY---")
while True:
    print("--------------------------")
    Mode = input("would you like to (add) (view) (remove) or (quit): ").lower()
    print("--------------------------")
    if Mode == "add":
        add()
    elif Mode == "view":
        view()
    elif Mode == "remove":
        remove()
    elif Mode == "quit":
        print("Bye Bye!")
        quit()

