from anytree import Node, RenderTree


def print_tree(elements):
    root = Node(elements[0])
    current_node = root
    for path in elements[1:]:
        current_node = Node(path, parent=current_node)

    for pre, _, node in RenderTree(root):
        print("%s%s" % (pre, node.name))


if __name__ == "__main__":
    elements = [
        "https://pl.wikipedia.org/wiki/Bumerang",
        "https://pl.wikipedia.org/wiki/Pocisk",
        "https://pl.wikipedia.org/wiki/Haubica",
        "https://pl.wikipedia.org/wiki/Lufa",
        "https://pl.wikipedia.org/wiki/Bro%C5%84_palna",
        "https://pl.wikipedia.org/wiki/Rewolwer",
        "Rewolwer",
    ]
    print_tree(elements)
