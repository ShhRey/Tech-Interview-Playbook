#=========== Design a Document Editor  eg: Google Docs ==============#

'''
# Define Requirements / Scope
- Users should be able to CRUD documents
- Will there be collaborative support? can multiple users work simultaneously?
- What are the types of data it will support to make it more scalable?   Tables / Images / Vidoes
- The updates should be reflected/visible in real-time
- Store or track cursor positions to avoid conflicts (different users)
- Document versions should be synced for every users (even though not instantly)

#==================== Create Classes and Define Methods ===================#

# Abstract Class
class Element()             class TxtElement(Element)               class ImgElement(Element) 
- render()                  - render()                              - render() 
# The element class here can be used to render different class extensions further: NewLine, TabSpace, Bold, Italic, Underline, etc.

class Document()
- ElementList []
- addElement(Element)
- render()



# Abstract Class
class Store()               class SaveToFile(Store)             class SaveToDB(Store)
- save()                    - save()                            - save()



class DocumentEditor()
- Document()
- Store() 
- addElement(TxtElement)
- addElement(ImgElement)
- render()
- save()

'''