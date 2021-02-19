#import the class
from logic import TruthTable



propA = input( "Please enter Proposition 1:")
propB = input( "Please enter Proposition 2:")

myTable1 = TruthTable(['p', 'q'], [propA])
myTable2 = TruthTable(['p', 'q'], [propB])

list1 = myTable1.table
list2 = myTable1.table
res=''