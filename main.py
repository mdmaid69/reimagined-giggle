import xml.etree.ElementTree as ET
root = ET.Element("root")
doc = ET.SubElement(root, "doc")
ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"
tree = ET.ElementTree(root)
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius