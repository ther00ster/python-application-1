class Document(object):

    def serialize(self):
        """serialize function"""

    def __str__(self):
        # return super().__str__()
        return "This is a document"

doc = Document()
print(doc)