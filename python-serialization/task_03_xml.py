import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)  # Hər şeyi stringə çeviririk, çünki XML üçün uyğundur

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True

    except Exception as e:
        print(f"Serialization to XML failed: {e}")
        return False


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except ET.ParseError as e:
        print(f"XML parsing failed: {e}")
        return None
    except Exception as e:
        print(f"Deserialization from XML failed: {e}")
        return None
