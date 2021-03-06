#!/usr/bin/python
#
# Archimate Libray Constants
#
__author__ = u'morrj140'
__VERSION__ = u'0.1'

import os
import time

#
# Script to reset Neo4J
#
#resetNeo4J = u"/Users/morrj140/Development/neo4j/bin/reset.sh"
resetNeo4J = u"/home/james.morris/bin/reset.sh"

#
# IP of Neo4J Graph
#
LocalGBD  = u"http://localhost:7474/db/data/"
RemoteGDB = u"http://10.92.82.60:7574/db/data/"
gdb = LocalGBD
gdbTest = LocalGBD

#
# Archimate XML
#
NS_MAP={u'xsi': u'http://www.w3.org/2001/XMLSchema-instance', u'archimate': u'http://www.archimatetool.com/archimate'}
XML_NS         =  NS_MAP[u"xsi"]
ARCHIMATE_NS   =  NS_MAP[u"archimate"]
ARCHI_TYPE = u"{%s}type" % NS_MAP[u"xsi"]

#
# Directory for Archimate File
#
dirTest = os.getcwd() + os.sep + u"test" + os.sep
dirRun = os.getcwd() + os.sep
directory = dirRun

fileArchimateTest   = dirTest + u"Testing.archimate"
fileArchimateModel  = directory + u'archi.archimate'
fileArchimateImport = directory + u"import_artifacts.archimate"
fileArchimateZipFileTest  = dirTest + u"Testing2.archimate"
fileArchimateDedupInput   = dirTest + u"testDup.archimate"
fileArchimateDedupOutput  = dirTest + u"dedup.archimate"

#
# Concept Files Used
#
fileConceptsArch           = directory + u"archi.p"
fileConceptsPPTX           = directory + u"pptx.p"
fileConceptsExport         = directory + u"export.p"
fileConceptsImport         = directory + u"export.p"
fileConceptsBatches        = directory + u"batches.p"
fileConceptsTraversal      = directory + u"traversal.p"
fileConceptsEstimation     = directory + u"Estimation.p"
fileConceptsRequirements   = directory + u"reqs.p"
fileConceptsDeDups         = directory + u"dedups.p"
fileConceptsRelations      = directory + u"rel.p"
fileConceptsDocuments      = directory + u"documents.p"
fileConceptsChunks         = directory + u"chunks.p"
fileConceptsNodes          = directory + u"nodes.p"
fileConceptsNGramsSubject  = directory + u"ngramsubject.p"
fileConceptsNGramFile      = directory + u"ngrams.p"
fileConceptsNGramScoreFile = directory + u"ngramscore.p"

#
# Common Filenames
#

filePPTXIn    = directory + u"test_in.pptx"
filePPTXOut   = directory + u"test_out.pptx"

fileExcelIn  = directory + u'Template_Estimate.xlsx'
fileExcelOut = directory + u'Template_Estimate_new.xlsx'

fileCSVExport = directory + u"export.csv"
fileCSVExportTime = directory + u"export" + time.strftime(u"%Y%d%m_%H%M%S") + u".csv"

fileReportExport     = directory + u"report.csv"
fileReportExportTime = directory + u"report" + time.strftime(u"%Y%d%m_%H%M%S") + u".csv"

fileCSVQueryExport      = directory + u"ExportQuery.csv"
fileCSVQueryExportTime  = directory + u"ExportQuery" + time.strftime(u"%Y%d%m_%H%M%S") + u".csv"

fileImageExport      = directory + u"export.png"
fileImageExportTime  = directory + u"export" + time.strftime(u"%Y%d%m_%H%M%S") + u".png"

#
# Archimate Edges
#
relations = {u"TriggeringRelationship" : u"archimate:TriggeringRelationship",
                    u"UsedByRelationship" : u"archimate:UsedByRelationship",
                    u"AccessRelationship" : u"archimate:AccessRelationship",
                    u"FlowRelationship" : u"archimate:FlowRelationship",
                    u"AssignmentRelationship" : u"archimate:AssignmentRelationship",
                    u"AssociationRelationship" : u"archimate:AssociationRelationship",
                    u"RealisationRelationship" : u"archimate:RealisationRelationship",
                    u"CompositionRelationship" : u"archimate:CompositionRelationship",
                    u"AggregationRelationship": u"archimate:AggregationRelationship",
                    u"SpecialisationRelationship" : u"archimate:SpecialisationRelationship"}

#
# Archimate Nodes
#
entities = {
            u"BusinessActor" : u"archimate:BusinessActor",
            u"BusinessRole" : u"archimate:BusinessRole",
            u"BusinessEvent" : u"archimate:BusinessEvent",
            u"BusinessObject" : u"archimate:BusinessObject",
            u"BusinessProcess" : u"archimate:BusinessProcess",
            u"BusinessFunction" : u"archimate:BusinessFunction",
            u"Business Collaboration" : u"archimate:BusinessCollaboration",
            u"Business Interface" : u"archimate:BusinessInterface",
            u"Contract" : u"archimate:Contract",
            u"Representation" : u"archimate:Representation",
            u"Business Service" : u"archimate:BusinessService" ,
            u"Location" : u"archimate:Location",
            u"Value" : u"archimate:Value",
            u"Meaning" : u"archimate:Meaning",
            u"Product" : u"archimate:Product",
            u"ApplicationService" : u"archimate:ApplicationService",
            u"ApplicationComponent" : u"archimate:ApplicationComponent",
            u"ApplicationFunction" : u"archimate:ApplicationFunction",
            u"ApplicationInterface" : u"ApplicationInterface",
            u"Application Collaboration" : u"archimate:ApplicationCollaboration",
            u"Application Interaction" : u"archimate:ApplicationInteraction",
            u"DataObject" : u"archimate:DataObject",
            u"Artifact" : u"archimate:Artifact",
            u"Communication Path" : u"archimate:CommunicationPath",
            u"Network" : u"archimate:Network",
            u"Infrastructure Interface" : u"archimate:InfrastructureInterface",
            u"System Software" : u"archimate:SystemSoftware",
            u"Node" : u"archimate:Node",
            u"Infrastructure Service" : u"archimate:InfrastructureService",
            u"Infrastructure Function" : u"archimate:InfrastructureFunction",
            u"Device" : u"archimate:Device",
            u"Driver" : u"archimate:Driver",
            u"Assessment" : u"archimate:Assessment",
            u"Goal" : u"archimate:Goal",
            u"Principle" : u"archimate:Principle",
            u"Requirement" : u"archimate:Requirement",
            u"Work Package" : u"archimate:WorkPackage",
            u"Deliverable" : u"archimate:Deliverable",
            u"Plateau" : u"archimate:Plateau",
            u"Gap" : u"archimate:Gap",
}

entityFolders = {u"BusinessEvent" : u"Business",
            u"BusinessObject" : u"Business",
            u"BusinessService" : u"Business",
            u"BusinessProcess" : u"Business",
            u"BusinessFunction" : u"Business",
            u"Representation" : u"Business",
            u"BusinessActor" : u"Business",
            u"BusinessRole" : u"Business",
            u"BusinessCollaboration" : u"Business",
            u"Product" : u"Business",
            u"Contract" : u"Application",
            u"ApplicationService" : u"Application",
            u"ApplicationComponent" : u"Application",
            u"ApplicationFunction" : u"Application",
            u"ApplicationInterface" : u"Application",
            u"SystemSoftware" : u"Implementation & Migration",
            u"Plateau" : u"Implementation & Migration",
            u"Artifact" : u"Implementation & Migration",
            u"Assessment" : u"Motivation",
            u"Goal" : u"Motivation",
            u"Gap" : u"Motivation",
            u"Driver" : u"Motivation",
            u"Constraint" : u"Motivation",
            u"Principle" : u"Motivation",
            u"DataObject" : u"Application",
            u"Requirement" : u"Motivation",
            u"Stakeholder" : u"Motivation",
            u"WorkPackage" : u"Motivation"}


folders = {u"Business", u"Application", u"Technology", u"Motivation", u"Implementation & Migration", u"Connectors", u"Relations" }

DIAGRAM_MODEL = u"archimate:ArchimateDiagramModel"
DIAGRAM_OBJECT = u"archimate:DiagramObject"
NOTE = u"archimate:Note"
SYSTEM_SOFTWARE = u"archimate:SystemSoftware"

# Reset Script for Neo4j
from sys import platform as _platform
if _platform == "linux" or _platform == "linux2":
    resetNeo4J = u"/home/james.morris/bin/reset.sh"
elif _platform == "darwin":
    resetNeo4J = u"/Users/morrj140/Development/neo4j/bin/reset.sh"
elif _platform == "win32":
    resetNeo4J = "n/a"

ID = u"id"
NAME = u"name"
CHILD = u"child"
PARENT = u"parent"
ENTITY = u"Entity"