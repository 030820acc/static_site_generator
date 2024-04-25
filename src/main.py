from textnode import TextNode

def main():
    a = TextNode('pog', 'bold', 'www.google.com')
    b = TextNode('pog', 'bold', 'www.google.com')
    c = TextNode('pogler', 'italic', 'www.google.org')

    print(a.__eq__(b))
    print(a.__eq__(c))
    print(a.__repr__())


main()
