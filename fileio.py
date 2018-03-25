def Main():
    try:
     f = open("divya1.txt" , "r")
     for line in f:
        print(line)
     f.close()
    except:
            print("file not found")
    finally:
            print("Exiting")

if  __name__ == "__main__":
 Main()