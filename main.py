import xml.etree.ElementTree as ET
root = ET.Element("root")
doc = ET.SubElement(root, "doc")
ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"
tree = ET.ElementTree(root)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))