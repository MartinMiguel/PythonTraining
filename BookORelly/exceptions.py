f = None
try:
    f = open("poem.txt")
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
        print("(Cleaning up: Closed the file)")
    print("Completed...")