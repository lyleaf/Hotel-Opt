from lxml import etree


schema_tree = etree.parse("siteindex.xsd")
schema_root = etree.XML(etree.tostring(schema_tree.getroot()))
schema = etree.XMLSchema(schema_root)
parser = etree.XMLParser(schema = schema)

tree = etree.parse("YXLAX116.xml",parser)

root = tree.getroot()


review_link = tree.get('loc')#[0].get('href')#//*[@id="rn392764024"]



root = etree.fromstring(etree.tostring(tree.getroot()),parser)



etree.tostring(tree.getroot())