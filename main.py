import xml.etree.ElementTree as ET
root = ET.Element("root")
doc = ET.SubElement(root, "doc")
ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"
tree = ET.ElementTree(root)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list