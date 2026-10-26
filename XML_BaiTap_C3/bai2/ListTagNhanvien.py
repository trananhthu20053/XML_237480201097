
import xml.etree.ElementTree as ET

tree = ET.parse("hoso.xml")
root = tree.getroot()

for element in root.iter():
    # dòng dưới là dòng để lấy thuộc tính bên trong thẻ
    if element.text and element.text.strip():
        print(element.text.strip())