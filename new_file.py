def create_file(filename, mode):    
             
    a = open(filename,mode)
    a.write("my first line\n")
    a.write("my second line\n")
    a.close()
    
create_file("Sample.txt","a")
