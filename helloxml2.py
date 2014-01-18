print "This version of the script will pull the root and child node values and",
print "tags from the xml file on your computer named in the script."
#The below line will is where you define the variable as a filename.  This
filetoread = "/Users/David/Desktop/Testreader/testxmlfile.xml"
#The two lines below will just open the file and print it as text if you want to add them back
#txt_again = open(filetoread)
#print txt_again.read()
#The below line pulls in the element tree functions in python and renames it ET
import xml.etree.ElementTree as ET
#Below pulls the tree as an object (I think)
tree = ET.parse(filetoread)
#Below pulls the root element of the parsed string
root = tree.getroot()
#The root object has child nodes 
#below loop iterates over all nodes and sub nodes etc. under the root object
for attribute in root.iter():
	print attribute.text, attribute.tag,