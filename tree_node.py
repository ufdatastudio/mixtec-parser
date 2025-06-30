# CWDE615
# a file for parse tree nodes
import tokens
from abc import ABC, abstractmethod

class TreeNode(ABC):
    def __init__(self, first_token, children : list[object] = None):
        self.children : list[object] = children if children != None else []
        self.first_token : tokens.Token = first_token

    def add_children(self, chs):
        for ch in chs:
            self.children.append(ch)
    
    def get_children(self):
        return self.children
    
    def get_token(self):
        return self.first_token
    
    def is_first_token_type(self, exp : type):
        return type(self.first_token) == exp
     
    @abstractmethod
    def interpret(self) -> str:
        pass
    
class Start(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)

    def interpret(self) -> str:
        sentence_list : list[str] = []
        # the Start symbol should have an alternating sequence of Sent and end children.
        for sent_or_end in self.children:
            sentence_list.append(sent_or_end.interpret())

        return "".join(sentence_list)
        
class Sent(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self):
        sentence_list : list[str] = []

        if self.is_first_token_type(tokens.Human):
            return self.children[0].interpret() # Clause
       
        if self.is_first_token_type(tokens.Obj) or self.is_first_token_type(tokens.Year):
            sentence_list.append(self.children[0].interpret()) # obj || Date
            
            if len(self.children) > 2: # TODO: handle specific objects differently
                sentence_list.append(self.children[1].interpret()) # Date || obj
                sentence_list.append(self.children[2].interpret()) # Clause || Clause
            else:
                sentence_list.append(self.children[1].interpret()) # Clause || Clause
            
        return " ".join(sentence_list)

class Clause(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self) -> str:
        i = 0
        l_human_list : list[str] = []
        l_pose_list : list[int] = []
        l_orientation_list : list[int] = []
        l_gender_list : list[int] = []

        while i < len(self.children) and self.children[i].is_first_token_type(tokens.Human):
            i_first_token = self.children[i].first_token
            l_human_list.append(self.children[i].interpret())
            l_pose_list.append(i_first_token.pose)
            l_orientation_list.append(i_first_token.orientation)
            l_gender_list.append(i_first_token.gender)

            i += 1

        obj_tail = None
        date_tail = None

        # get the possible Obj_tail or Date_tail. These may have their own human_list to consider. 
        if i < len(self.children) and self.children[i].is_first_token_type(tokens.Obj):
            obj_tail = self.children[i].interpret()
        elif i < len(self.children) and self.children[i].is_first_token_type(tokens.Year):
            date_tail = self.children[i].interpret()

        # real_tail is a tuple if either of the ifs above executed. Otherwise, it is None
        real_tail = obj_tail if obj_tail != None else date_tail
        # bit records whether obj_tail is None.
        # If real_tail is a tuple and tail_bit is 1, then real_tail corresponds to a date_tail tuple.
        tail_bit = 0 if obj_tail != None else 1

        # All of the following are UD and set to None if there is no tail for this Clause (real_tail == None)
        tail_list = None
        r_pose_list = None
        r_orientation_list = None
        r_gender_list = None
        obj_string = None
        date_string = None
        human_string = None

        if real_tail != None:
            tail_string, r_pose_list, r_orientation_list, r_gender_list = real_tail

            tail_list = tail_string.split('@')

            if len(tail_list) == 1:
                obj_string = tail_list[0]
                date_string = None
                human_string = None
            if len(tail_list) == 2:
                obj_string = tail_list[0]
                date_string = None
                human_string = tail_list[1]
            elif len(tail_list) == 3:
                obj_string = tail_list[0]
                date_string = tail_list[1]
                human_string = tail_list[2]

            if tail_bit == 1: # Clause has a Date_tail
                tmp = obj_string
                obj_string = date_string
                date_string = tmp

        check_for_date = lambda result_string : result_string if date_string == None else " ".join([date_string, result_string])
        check_for_obj = lambda result_string : result_string if obj_string == None else " ".join([result_string, "near a", obj_string])
        check_date_obj = lambda result_string : check_for_obj(check_for_date(result_string))

        def handle_two_human_figures(
            l_pose : int,
            l_orientation: int,
            l_gender : int, 
            l_human : str,
            r_pose : int,
            r_orientation : int,
            r_gender : int,
            r_human : str
        ):
            # These have the form [Lord/Lady # Symbol, NearObjIdentity]
            l_name_near_obj = l_human.split('$')
            r_name_near_obj = r_human.split('$')
            
            # the figures are facing the same direction
            if l_orientation == r_orientation:
                result_l = l_name_near_obj[0] if len(l_name_near_obj) == 1 else f"{l_name_near_obj[0]} with a {l_name_near_obj[1]}" 
                result_r = r_name_near_obj[0] if len(r_name_near_obj) == 1 else f"{r_name_near_obj[0]} with a {r_name_near_obj[1]}"
                
                # For there to be a r_human_list, there must be a right Clause_f+ in the AST, implying that there must also
                # be some kind of tail. Include it with the output.
                return check_date_obj(" ".join(["there was", result_l, "and", result_r, "near", obj_string]))

            # beyond this point, orientation is different
            # handle the rare case that two figures are drawn facing away from each
            # other in a scene.
            if l_orientation == 0 and r_orientation == 1:
                result_l = l_name_near_obj[0] if len(l_name_near_obj) == 1 else f"{l_name_near_obj[0]} with a {l_name_near_obj[1]}" 
                result_r = r_name_near_obj[0] if len(r_name_near_obj) == 1 else f"{r_name_near_obj[0]} with a {r_name_near_obj[1]}"
                return check_date_obj(" ".join(["there was", result_l, "and", result_r]))
            
            # beyond this point, the two human figures are facing one another.
            # This usually implies interaction between the two of them, and there
            # are several interesting cases.

            # tail has table or house obj and two h with opposite gender are sitting. This is usually taken to
            # mean that the two figures were married, and is common in genealogical segments.
            if obj_string in ["house", "table"] and l_gender is not r_gender and l_pose == 0 and r_pose == 0:
                return check_for_date(" ".join([l_name_near_obj[0], "married", r_name_near_obj[0]]))
            
            # There is no object between the figures, and one is sitting while the other is standing. This normally indicates
            # that the stander is consulting with the sitter. The sitter often appears on a throne, which will appear as a near_obj
            # token and is handled.
            if l_pose is not r_pose:
                sitter = l_name_near_obj if l_pose == 0 else r_name_near_obj
                stander = r_name_near_obj if l_pose == 0 else l_name_near_obj
                sit_gender = l_gender if l_pose == 0 else r_gender
                possessive = "his" if sit_gender == 0 else "her" 

                if len(sitter) == 2 and sitter[1] == "throne":
                    result_a = " ".join([stander[0], "consulted", sitter[0], f"sitting on {possessive}", sitter[1]])
                else:
                    result_a = " ".join([stander[0], "consulted", sitter[0]])

                return check_date_obj(result_a)
            
            # At this point, the two figures are either both sitting or both standing in addition to facing one
            # another. 

            # Both are sitting. This usually implies a seance, ritual or conversation. The generic verb 'communed' is chosen to reflect
            # the idea that the two are communicating on equal terms, possibly with unmentioned third parties.  
            if l_pose == 0 and r_pose == 0:
                return check_date_obj(" ".join([l_name_near_obj[0], "communed with", r_name_near_obj[0]]))
        
            # Both are standing. Typical interpretations depend on the near_obj of the two actors. A generic interpretation is also given.

            # sacrificed_animal near either person implies that the two are involved in ritual sacrifice.
            if "sacrificed_animal" in l_name_near_obj or "sacrificed_animal" in r_name_near_obj:
                return check_date_obj(" ".join([l_name_near_obj[0], "and", r_name_near_obj[0], "participated in a ritual sacrifice"]))
            
            # At this point, neither human can have a sacrificed animal near_obj. This disambiguates what is happening
            # should either or both of them have weapons. If not to kill an animal, they must be using the weapons on each other.
            if "weapon" in l_name_near_obj or "shield" in l_name_near_obj or "weapon" in r_name_near_obj or 'shield' in r_name_near_obj:
                return check_date_obj(" ".join([l_name_near_obj[0], "fought", r_name_near_obj[0]]))
            
            # Catch all return case to prevent fall through to other if statements. It is known that two humans are standing and facing
            # one another in this sentence, and that neither of them holds a weapon, shield or sacrificed animal. Simply say they  met. 
            return check_date_obj(" ".join([l_name_near_obj[0], "met", r_name_near_obj[0]]))
        
        if human_string != None:
            r_human_list = human_string.split('#')
        else: # no human_string means there is either no tail, or the tail is just a Date or obj
            return_list : list[str] = []
            
            if len(l_human_list) == 1:
                result_a = f"there was {l_human_list[0].split('$')[0]}"
            
            elif len(l_human_list) == 2:
                return handle_two_human_figures(
                    l_pose = l_pose_list[0],
                    l_orientation = l_orientation_list[0],
                    l_gender = l_gender_list[0],
                    l_human = l_human_list[0],
                    r_pose = l_pose_list[1],
                    r_orientation = l_orientation_list[1],
                    r_gender = l_gender_list[1],
                    r_human = l_human_list[1]
                )

            else:
                l_standing = True
                l_same = True
                direction = None
                
                for l in l_pose_list:
                    if l == 0:
                        l_standing = False

                for dir in l_orientation_list:
                    if direction == None:
                        direction = dir
                    else:
                        if dir != direction:
                            l_same = False
                            break 

                for human in l_human_list:
                    h_nd_near = human.split('$') # [(Lady/Lord # Symbol OR a Lady/Lord)] OR [(Lady/Lord # Symbol OR a Lady/Lord), NearObjIdentity]
                    return_list.append(h_nd_near[0])

                joined_return_list = ", ".join(return_list[0:-1])
                joined_return_list = ", and ".join([joined_return_list, return_list[-1]])
                
                if l_same and l_standing:
                    result_a = " ".join(["there was a procession or journey including", joined_return_list])
                if not l_same and l_standing:
                    result_a = " ".join(["there was a gathering including", joined_return_list])

                result_a = " ".join(["there were", joined_return_list])

            # if there really is tail, then there is either an obj associated with the clause or date. Figure out which
            # and annotate accordingly.
            if real_tail != None:
                if tail_bit == 0: # Obj_tail without second Clause_f+
                    return " near a(n) ".join([result_a, obj_string])
                else: # Date_tail without a second Clause_f+
                    return " ".join([result_a, date_string]) # simply join the result_a with the date string, since Date formats itself.
            
            # Here, real_tail == None, so there really was no tail, and the interpretation of the one Clause_f sequence is returned.
            return result_a
        
        r_human_list : list[str] = human_string.split("#")

        # one figure on either side.
        if len(l_human_list) == 1 and len(r_human_list) == 1:
            return handle_two_human_figures(
                l_pose = l_pose_list[0],
                l_orientation = l_orientation_list[0],
                l_gender = l_gender_list[0],
                l_human = l_human_list[0],
                
                r_pose = r_pose_list[0],
                r_orientation = r_orientation_list[0],
                r_gender = r_gender_list[0],
                r_human = r_human_list[0],
            )

        # one to many or many to one TODO

        # many to many TODO

        # ERROR: NO INTERPRETATION MATCHES
        return "<ERROR: Clause is in grammar but no interpretation exists for it.>"

class DateTail(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    # TODO: Check that returning a tuple like this doesn't break the interface.
    def interpret(self) -> tuple[str, list[int], list[int]]:
        date_string : str = self.children[0].interpret()

        if len(self.children) > 1:
            obj_string : str | None = None
            i : int = 1
            
            if self.children[1].is_first_token_type(tokens.Obj):
                obj_string = self.children[1].interpret()
                i += 1

            r_human_list = []
            r_pose_list : list[int] = []
            r_orientation_list : list[int] = []
            r_gender_list : list[int] = []
            
            while i < len(self.children) and self.children[i].is_first_token_type(tokens.Human):
                i_first_token = self.children[i].first_token
                r_human_list.append(self.children[i].interpret())
                r_pose_list.append(i_first_token.pose)
                r_orientation_list.append(i_first_token.orientation)
                r_gender_list.append(i_first_token.gender)

                i += 1 
    
            human_string = "#".join(r_human_list)

            # Note that, according to the grammar, it's not actually possible
            # for the human_string to be empty.
            if obj_string == None:
                return "@".join([date_string, human_string]), r_pose_list, r_orientation_list, r_gender_list
            else:
                return "@".join(date_string, obj_string, human_string), r_pose_list, r_orientation_list, r_gender_list

        else:
            return date_string, [], [], []


class ObjTail(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self) -> tuple[str, list[int], list[int]]:
        obj_string = self.first_token.interpret()

        if len(self.children) > 1:
            date_string : str | None = None
            i : int = 1
            
            if self.children[1].is_first_token_type(tokens.Year):
                date_string = self.children[1].interpret()
                i += 1

            r_human_list = []
            r_pose_list : list[int] = []
            r_orientation_list : list[int] = []
            r_gender_list : list[int] = []

            while i < len(self.children) and self.children[i].is_first_token_type(tokens.Human):
                i_first_token = self.children[i].first_token
                r_human_list.append(self.children[i].interpret())
                r_pose_list.append(i_first_token.pose)
                r_orientation_list.append(i_first_token.orientation)
                r_gender_list.append(i_first_token.gender)

                i += 1 
    
            human_string = "#".join(r_human_list)

            # Note that, according to the grammar, it's not actually possible
            # for the human_string to be empty.
            if date_string == None:
                return "@".join([obj_string, human_string]), r_pose_list, r_orientation_list, r_gender_list
            else:
                return "@".join(obj_string, date_string, human_string), r_pose_list, r_orientation_list, r_gender_list

        else:
            return obj_string, [], [], []

class Date(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self):
        
        year_string : str = self.first_token.interpret() # interpret the year

        if len(self.children) > 1:
            date_string : str = self.children[1].interpret() # nd

            return " ".join(["in Year", year_string, "Day", date_string])
        else:
            return " ".join(["in Year", year_string])


class ClauseF(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self):
        h_string : str = self.first_token.interpret() # h

        # there is a tail.
        if len(self.children) > 1:
            tail_string : str = self.children[1].interpret()
            nd_near_obj : list[str] = tail_string.split("$")

            # tail starts with a name date
            if self.children[1].is_first_token_type(tokens.NameDate):
                
                return f'{h_string} {nd_near_obj[0]}' # Lord/Lady # Symbol
            
            # tail starts with a NearObj.
            elif self.children[1].is_first_token_type(tokens.NearObj):
                
                # if it starts with a NearObj, there could be a NameDate
                # associated with the parent h token after it. Handle
                # accordingly.
                if len(nd_near_obj) == 2:
                    return "$".join([f'{h_string} {nd_near_obj[1]}',f'{nd_near_obj[0]}']) # Lord/Lady # Symbol$NearObjIdentity 
                else:
                    return "$".join([f'a {h_string}',f'{nd_near_obj[0]}']) # a Lord/Lady$NearObjIdentity
        
        else:
            # h is alone, without a tail. Corresponds to nameless person not associated with a near_obj token.
            return f'a {h_string}' # 'a Lord' or 'a Lady' since they have no name-date.

class NearDate(TreeNode):
    def __init__(self, first_token, children = None):
        super().__init__(first_token, children)
    
    def interpret(self) -> str:
        near_obj_string : str = self.first_token.interpret() # near_obj

        # somewhat bends the rules of the interpretation interface by inserting a meta-character '$'
        # to represent that the two pieces of information provided are not meant to be in sequence.
        if len(self.children) > 1:
            name_date_string : str = self.children[1].interpret() # nd
        
            return "$".join([near_obj_string, name_date_string])
        else:
            return near_obj_string
            
class LeafNode(TreeNode):
    def __init__(self, token: tokens.Token):
        super().__init__(token, children=None)

    def interpret(self) -> str:
        # For leaf nodes, interpretation is just the token's interpretation
        return self.first_token.interpret()

    def to_xml(self) -> str:
        return self.first_token.to_xml()
            
    
