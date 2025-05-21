import xml.dom.minidom as minidom
from datetime import datetime
import xml.sax

# DOM
start_time = datetime.now()
go = minidom.parse("go_obo.xml")        # parse the file into a document file
terms = go.getElementsByTagName("term") # get information in tag <term>
# create a dictionary to store the three ontologies, the namespace and the counts.
max_is_a = {"molecular_function": ("" , 0) , "biological_process": ("" , 0) , "cellular_component": ("" , 0)}

for term in terms:
    id = term.getElementsByTagName("id")[0].firstChild.nodeValue
    namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue
    is_a = term.getElementsByTagName("is_a")
    count = len(is_a) # the number of <is_a> tags
    # compare whether the count is larger than the counts that have orignially been stored in the dictionary
    if namespace in max_is_a and count > max_is_a[namespace][1]:
        # if yes, replace the id and the counts
        max_is_a[namespace] = (id, count)

print(f"molecular_function: {max_is_a["molecular_function"][0]} with {max_is_a["molecular_function"][1]} <is_a> references")
print(f"biological_process: {max_is_a["biological_process"][0]} with {max_is_a["biological_process"][1]} <is_a> references")
print(f"cellular_component: {max_is_a["cellular_component"][0]} with {max_is_a["cellular_component"][1]} <is_a> references")

end_time = datetime.now()
print("DOM Time Taken:" , end_time - start_time)

# the DOM Time Taken is around 5 seconds


# SAX
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_namespace = ""
        self.current_id = ""
        self.is_a_count = 0
        self.current_tag = ""
        # # create a dictionary to store the three ontologies, the namespace and the counts.
        self.max_is_a = {"molecular_function": ("" , 0) , "biological_process": ("" , 0) , "cellular_component": ("" , 0)}

    def startElement(self, tag, attributes):
        self.current_tag = tag
        # read the start tag <tag>
        if tag == "term":
            self.current_namespace = ""
            self.current_id = ""
            self.is_a_count = 0
        # read the start tag <is_a> tag
        elif tag == "is_a":
            self.is_a_count += 1

    def endElement(self, tag):
        if tag == "term":
            # compare whether the count is larger than the counts that have orignially been stored in the dictionary
            if self.current_namespace in self.max_is_a and self.is_a_count > self.max_is_a[self.current_namespace][1]:
                # if yes, replace the id and the counts
                self.max_is_a[self.current_namespace] = (self.current_id, self.is_a_count)
        self.current_tag = ""
        
    def characters(self, content):
        if self.current_tag == "namespace":
            # store the content of namespace
            self.current_namespace = content
        elif self.current_tag == "id":
            # store the content of id
            self.current_id = content

start_time = datetime.now()

parser = xml.sax.make_parser()
Handler = GOHandler()
parser.setContentHandler(Handler)
parser.parse("go_obo.xml")

print(f"molecular_function: {Handler.max_is_a["molecular_function"][0]} with {Handler.max_is_a["molecular_function"][1]} <is_a> references")
print(f"biological_process: {Handler.max_is_a["biological_process"][0]} with {Handler.max_is_a["biological_process"][1]} <is_a> references")
print(f"cellular_component: {Handler.max_is_a["cellular_component"][0]} with {Handler.max_is_a["cellular_component"][1]} <is_a> references")

end_time = datetime.now()
print("SAX Time Taken:" , end_time - start_time)

# the SAX Time Taken is around 1 second

# SAX is quicker than DOM