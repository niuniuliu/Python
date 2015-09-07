zoo = ['lion', "elephant", 'monkey']

if __name__ == "main":
    f = open("output.txt", a)

    for i in zoo:
        # add the whole zoo to the output.txt
        f.write(i)


    # close the file
    f.close()