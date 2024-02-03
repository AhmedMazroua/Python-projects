# creates an informatic about a millitary officer. Function to be implemented in a millitary style game or app
class Operator:
    #initialized function and parameters
    def __init__(self, name ,branch, mos, status):
        self.branch = branch
        self.mos = mos
        self.name = name
        self.status = status
    #occupation
    def occupation(self):
        print('\n{} serves in the {}, corresponding MOS is "{}", Millitary Status: {}.\n'.format(self.name.title(), self.branch.title(), self.mos.title(), self.status.upper()))
    #active country  
    def active(self, country):
        self.country = country
        print('\n Operator is currently active in {} \n'.format(self.country))

#examles of how class can be utilized:
my_op = Operator('Leon Spots', 'UsMC', 'weapons tech', 'active')
mother = Operator('Jason Borne', 'n/a', 'n/a', 'Classified')

print(my_op.occupation(), my_op.active("District of Columbia"))