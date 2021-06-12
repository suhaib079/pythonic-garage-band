from abc import abstractmethod
from itertools import product


# class Band(Musician):

    
#     def __init__(self,name,members):
#         self.name =name
#         self.members =members
#         Band.member.append(name)

#     def play_solos(self):
#         turns = ['play your solo']
#         return (list(product(self.members,turns)))


#     def __str__(self):
#         return f"band(name:{self.name},member:{self.members})"    

#     # def __repr__(self):
#         # return f"{self.name} instance. Name = {self.members}" 

#     @staticmethod
#     def to_list():
#         return Band.member      

class Musician():
     def __init__(self,name):
        self.name=name


     def __str__(self):
        return self.name     

     def __repr__(self):
        return {self.name}    
    

class Guitarist(Musician):
    member =[]
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"My name is {self.name} and I play guitar"


    # def __repr__(self):
    #     return f"guiter: {self.name}"  
    def __repr__(self):
        
        return f"Guitarist instance. Name = {self.name}"   
    @staticmethod
    def get_instrument():
        return "guitar"
    @staticmethod    
    def play_solo():
        return "face melting guitar solo" 
        

class Bassist(Musician):
    def __init__(self,name,):
        self.name=name

    def __str__(self):
        return f"My name is {self.name} and I play bass"  


    # def __repr__(self):
    #     return f"bassist:{self.name}"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"      

    def play_solo(self):
        return "bom bom buh bom" 

    def get_instrument(self):
        return "bass"    


             

class Drummer(Musician):
    def __init__(self,name,):
        self.name=name

    def __str__(self):
        return f"My name is {self.name} and I play drums" 


    # def __repr__(self):
    #     return f"Drummer:{self.name}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"   

    def play_solo(self):
        return "bom bom buh bom"        

    def get_instrument(self):
        return "drums"






class Band(Musician):
    instances =[]
    
    def __init__(self,name,members):
        self.name =name
        self.members =members
        Band.instances.append(name)

    def play_solos(self):
        turns = ['face melting guitar solo']
        return (list(product(self.members,turns)))


    def __str__(self):
        return f"band(name:{self.name},member:{self.members})"    

    def __repr__(self):
        return f"{self.name} instance. Name = {self.members}" 

    # @staticmethod
    # def to_list():
    #     return Band.instances

    @classmethod
    def to_list(cls):
        return cls.instances

      

# # if __name__ == "__main__":
# #     suhaib =Guitarist("suhaib")
# #     print(suhaib.name)
# #     print(suhaib.play_solo())
# #     print(suhaib.get_instrument())
# #     emad = Bassist("emad")
# #     print(emad.name)
# #     print(emad.play_solo())
# #     print(emad.get_instrument())
# #     ahmad = Drummer("ahmad")
# #     print(ahmad.name)
# #     print(ahmad.play_solo())
    
# #     band1 = (Band("The Nobodies", [suhaib,emad, ahmad]))
    
# #     print(band1.member)
# #     print('The play solos method',band1.play_solos ())
# #     print('this is the to_list method',Band.to_list())       




