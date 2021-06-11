from abc import abstractmethod, ABC
from itertools import product


class Band():
    member =[]
    
    def __init__(self,name,members):
        self.name =name
        self.members =members
        Band.member.append(name)

    def play_solos(self):
        turns = ['play your solo']
        return (list(product(self.members,turns)))


    def __str__(self):
        return f"band(name:{self.name},member:{self.members})"    

    def __repr__(self):
        return f"'name':{self.name},'members' :{self.members}"  


    @staticmethod
    def to_list():
        return Band.member      

class Musician():
     def __init__(self,name):
        self.name=name


     def __str__(self):
        return self.name     

     def __repr__(self):
        return f"am {self.name}"    


class Guitarist(Musician):
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"i am {self.name} the guitar guy"


    def __repr__(self):
        return f"guiter: {self.name}"     

    def play_solo(self):
        return f"brrrrrrrrrr"   
        
    def get_instrument(self):
        return f"Guitar"        

class Bassist(Musician):
    def __init__(self,name,):
        self.name=name

    def __str__(self):
        return f" i am {self.name} the bass guy"  


    def __repr__(self):
        return f"bassist:{self.name}"    

    def play_solo(self):
        return f"breeezzzzzzz" 

    def get_instrument(self):
        return "Bass"    


             

class Drummer(Musician):
    def __init__(self,name,):
        self.name=name

    def __str__(self):
        return f" i am {self.name} the drum guy" 


    def __repr__(self):
        return f"Drummer:{self.name}"

    def play_solo(self):
        return f"dom dom dom"        

    def get_instrument(self):
        return "Drums"




if __name__ == "__main__":
    suhaib =Guitarist("suhaib")
    print(suhaib.name)
    print(suhaib.play_solo())
    print(suhaib.get_instrument())
    emad = Bassist("emad")
    print(emad.name)
    print(emad.play_solo())
    print(emad.get_instrument())
    ahmad = Drummer("ahmad")
    print(ahmad.name)
    print(ahmad.play_solo())
    
    band1 = (Band("The Nobodies", [suhaib,emad, ahmad]))
    
    print(band1.member)
    print('The play solos method',band1.play_solos())
    print('this is the to_list method',Band.to_list())        