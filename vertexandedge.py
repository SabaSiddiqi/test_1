class VertexAndEdge (object):
    
    vertices=[]
    edges=[]
    
    def vertex(self, street_coor):
        if street_coor not in self.vertices:
            self.vertices.append(street_coor)
            
    def edge(self,vertex1,vertex2):
        #sorting to arrange the edge points
            edge_points=sorted([vertex1,vertex2])
            #check if edge points already exists
            if edge_points not in self.edges:
                self.edges.append(edge_points)    
            
    def vertex_index(self,street_coor):
        index=[]
        if street_coor in self.vertices:
            index=self.vertices.index(street_coor)
            return index+1
        else:
            pass
        
    # this will appear on printing the class
    
    def __str__(self):
        
        #print vertices
        #+str() indicates that a sign should be used for both positive as well as negative numbers
        
        # To display number of vertices
        nof=len(self.vertices)
        display = "V = { \n "
        for ver in range(nof):
            point=self.vertices[ver]
            b= "(" +str(point[0])+ "," + str(point[1]) + ")"
            display += " " + str(ver+1) + ": " + b + "\n"
        display += "} \n"
        
        # To display number of edges
        display += "E = { \n" 
        for edge_points in self.edges:   
            c= "<" + str(edge_points[0]) + "," + str(edge_points[1]) + ">"
            display += " " + c + ", \n"
        display += "} \n"
        
        
        return display
            
             
        
        
        
            
            
    
            