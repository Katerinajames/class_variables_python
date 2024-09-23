
class Student:
 count=0
	
 def __init__( self, first, last ):

  self.first = first
  self.last = last
  Student.count= Student.count+1
  print("Employee constructor for %s, %s"%(self.first,self.last)) 

 def __del__( self ):
	 Student.count=Student.count-1
	
 	

print("--------------------------")

p=Student("Tom","Jones")
p1=Student("Kat","Lee")
p2=Student("Tommy","Lee")
print("Number of students after instantiation %d"%(Student.count))

del p
print("Number of students after deletion %d"%(Student.count))





