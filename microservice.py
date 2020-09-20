#Microservice RESTFul API Using Bottle Framework
from xml.dom import minidom
import xml.etree.ElementTree as ET
from bottle import run, route, template, request, post, get


@route('/') #Route the Client Side Template to the
def index():
    return template('venv//Lib//template//Template')

@get('/getjourney', method='GET') # Get Journey Method.
def getjourney():
    jname=request.GET.get('journey')  #Extract the the Journeyname from URL as jname.
    with open('JourneyData/' +jname + '.xml','r') as journeyxml: #Open the file .xml extension from directory JourneyData for read process
        journeyxml =journeyxml.read() #Read the the XML file from the directory
        return journeyxml #Return the file to the client side
        #return template('plan_journey_map.html', journeyxml)


@post('/savejourney')
def savejourney():
    jname = request.GET.get('journey') #Extract the XML file From the URL as janame
    JourneyXml = minidom.parseString(jname) #Parse the xml file received from the client using minidom
    root = ET.fromstring(jname) # change the XMl file into element tree
    fileName = root[0].attrib['name'] #Extract the Name of the Journey
    with open('JourneyData/' +fileName + '.xml', "w+") as xmlfile: #Open file with .xml extension to save the Recieved XML file.
        xmlfile.write(JourneyXml.toxml()) #Write the XML object in the directory JourneyData

#run(host='localhost', port=8080, debug=True)
run(host='localhost', port=8080, debug=True)
