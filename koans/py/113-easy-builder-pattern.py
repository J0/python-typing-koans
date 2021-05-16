"""
Koan to learn annotating the self instance
"""
# This is called builder pattern or fluent interface. You can read about in the following posts
# https://kracekumar.com/post/100897281440/fluent-interface-in-python/
# https://python-patterns.guide/gang-of-four/builder/


class Poem:
    def __init__(self, content: str):
        self.content = content

    # Annotate the method to return the instance of Poem class
    def _clone(self, content: str) -> Poem:
        return Poem(content=content)

    # Annotate the method to return the instance of Poem class
    def indent(self, spaces: int = 4) -> Poem:
        content = " " * spaces + self.content
        return self._clone(content)

    # Annotate the method to return the instance of Poem class
    def suffix(self, content: str) -> Poem:
        content = self.content + " - {}".format(content)
        return self._clone(content)

    def __str__(self) -> str:
        return self.content


def main() -> None:
    content = """
    The old pond
    A frog leaps in.
    Sound of the water.
    """
    p: Poem = Poem(content)
    q: Poem = p.indent(4)
    r: Poem = p.indent(2)
    print(str(q) == str(r))
    print(id(q), id(r))


if __name__ == "__main__":
    main()
