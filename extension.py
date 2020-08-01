def extension(string):
   """ It gives the information of the extension of file """

    #created a dictionary to store data for extensions
    full_extension = {

        "py":"Python file",

        "java":"Java file",

        "c":"C file or C++ file",

        "txt":"Text file",

        "pdf":"PDF file",

        "js":"Javascript file",

        "html":"HTML file",

        "css":"Cascade Style Sheet",

        "ai":"Adobe Illustrator file",

        "kt":"Kotlin file",

    }

    #sliced the string to get extension part

    i = string.index(".")

    string = string[i+1:]

    #checking wether extension is available in full_extension

    if string in full_extension.keys():

        return full_extension[string]

    else:

        return 0


file = input("Enter the file name with extension: ")

if extension(file)==0:

    print("Sorry no information for input file")

else:

    print("The input file has an extension of",extension(file))
