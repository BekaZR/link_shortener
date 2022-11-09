from pyshorteners import Shortener

s = Shortener()


def short():
    link = input("Enter the link to be shortened: ")
    shortened_link = s.tinyurl.short(link)
    print("\n")
    print("The Shortened Link is: " + shortened_link)

short()