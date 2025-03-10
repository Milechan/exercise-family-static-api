
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        memberpersonalizado=member
        memberpersonalizado["id"]=self._generateId()
        self._members.append(memberpersonalizado)
        return memberpersonalizado

    def delete_member(self, id):
        nueva_lista = [miembro for miembro in self._members if miembro["id"] != id]
        
        if len(nueva_lista) < len(self._members):
            self._members = nueva_lista
            return  True
        
        return False


    def get_member(self, id):
        # fill this method and update the return
        miembro=[miembro for miembro in self._members if miembro["id"] == id]
    
        if len(miembro) ==0:
            return None
        return miembro [0]
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
