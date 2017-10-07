#------------------Import-----------------#
import sys
import re
#------------------Import-----------------#

#------------------Import Functions/Modules-----------------#
from reg_exp import reg_exp
from extract_coor import extract_coor
from intersection import intersection
from vertexandedge import VertexAndEdge
from numpy import *
from display_graph import display_graph
#------------------Import Functions/Modules-----------------#


#--------------Street List - Class-----------------#
#Street class to manage coordinates and names of streets

class StreetList (object):
    def __init__(self,street_name,street_coor):
        self.street_name=street_name
        self.street_coor=street_coor

#--------------Street Class-----------------#

#-----------Function - Error and output-----------------#
def show_error(error):
    sys.stderr.write("%s\n" % error) 

def show_output(output):
    sys.stderr.write("%s\n" % output) 

#-----------Function - Error and output-----------------#

street_temp=[]
coor=[]
vne=VertexAndEdge()



# -----Main------ Write your code here

def main():
    
    while True:
        
        #fetch the input
        input_command=raw_input('Enter you command here: ')
        
        #check the input
        a,c,r,g= reg_exp(input_command)
        
        # if input is in correct format 
        if a or c or r or g:
            
            #extract street names from class StreetList
            names_list = [ temp.street_name for temp in street_temp] 
            coor_list = [ temp.street_coor for temp in street_temp]
            
            if a or c:
                #extract coordinates
                street_name = re.findall('\".+\"',input_command)[0]
                street_name = street_name.lower()
                street_coor=extract_coor(input_command)

                if a:
                 
                    if street_name in names_list:
                        show_error("Error: Street already exists, cannot add.")
                    else:
                        street_temp.append(StreetList(street_name,street_coor))
                        #show_output("Street added.")
                        
                if c:
                    if street_name in names_list:
                        #extract index of street to be changed and change coordinates
                        street_temp[names_list.index(street_name)].street_coor = street_coor
                        #show_output("Street changed.")
                    else:
                        show_error("Error: Street doesn't exist, cannot change.")
                
            if r:
                street_name = re.findall('\".+\"',input_command)[0]
                
                if street_name in names_list:
                    del street_temp[names_list.index(street_name)]
                    #show_output("Street removed.")
                else:
                    show_error("Error: Street doesn't exist, cannot remove.")
            
            if g:
                display_graph(coor_list)
                vne.vertices = []
                vne.edges = []
                #extracting number of streets for for loops
                nos=len(street_temp)
                for first_street in range (nos-1):
                    #extracting number of coordinates for desired street
                    noc_1=len(street_temp[first_street].street_coor)
                    for coor_num_1 in range (noc_1-1):
                        for second_street in range (first_street+1,nos):
                            noc_2=len(street_temp[second_street].street_coor)
                            for coor_num_2 in range (noc_2-1):
                                line1_src=street_temp[first_street].street_coor[coor_num_1]
                                line1_des=street_temp[first_street].street_coor[coor_num_1+1]
                                line2_src=street_temp[second_street].street_coor[coor_num_2]
                                line2_des=street_temp[second_street].street_coor[coor_num_2+1] 
                                intersect_point=intersection(array(line1_src),array(line1_des),array(line2_src),array(line2_des)) 

                                if intersect_point is not None:
                                    vne.vertex(line1_src)
                                    vne.vertex(line1_des)
                                    vne.vertex(line2_src)
                                    vne.vertex(line2_des)
                                    vne.vertex(intersect_point)
                                    
                                    #extract index of respective coordinates for edges
                                    p1=vne.vertex_index(line1_src)
                                    p2=vne.vertex_index(line1_des)
                                    p3=vne.vertex_index(line2_src)                        
                                    p4=vne.vertex_index(line2_des)
                                    pi=vne.vertex_index(intersect_point)
                                    # adding edges 
                                    vne.edge(p1,pi)
                                    vne.edge(p2,pi)
                                    vne.edge(p3,pi)
                                    vne.edge(p4,pi)
                
                print (vne)                     
                #print intersect_point            
                                
                                    
            

        
        # if input is not in correct format 
        else:
            show_error("Error: Incorrect input format, please try again.")

    
    sys.exit(0)

#------------------ Call Main -----------------#
if __name__=='__main__':
    main()
#------------------ Call Main -----------------#
