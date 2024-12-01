# CWDE615
# Parser for a limited Mixtec Grammar. Check the README for this grammar.
import tokens
import tree_node

class Parser():

    # HELPERS
    @staticmethod
    def match(exp : type, cand : tokens.Token):
        if not type(cand) == exp:
            print(f"Error in match: {type(cand)} does not match {exp}")
            assert False

    @staticmethod
    def raise_error(mes : str): # TODO: make more robust in reporting error metadata
        print(f"Error: {mes}")
        assert False
    
    @staticmethod
    def call_descent_method(c: list[tree_node.TreeNode], m):
        c.append(m())

    def consume(self, exp : type):
        top : tokens.Token = self.tks[-1]
        self.match(exp, top)
        self.tks.pop()
        return top

    def next_token_type(self, token_type : type):
        return type(self.tks[-1]) == token_type
    
    def next_token(self):
        return self.tks[-1]
    
    def consume_next_token(self, c : list[tree_node.TreeNode], exp : type):
        c.append(self.tks[-1])
        self.consume(exp)

    # RECURSIVE DESCENT METHODS
    def start(self):
        children : list[tree_node.TreeNode] = []
        first_token : tokens.Token = self.next_token()

        sent_id = 0 # A bit of a hack. Debug information added to end token nodes. 

        while len(self.tks) > 0:
            self.call_descent_method(children, self.sent)
            self.consume_next_token(children, tokens.End)
            children[-1].sent_id = sent_id
            sent_id += 1

        return tree_node.Start(first_token, children)

    def sent(self):
        children : list[tree_node.TreeNode] = []
        first_token : tokens.Token = self.next_token()

        if self.next_token_type(tokens.Human):
            self.call_descent_method(children, self.clause)
        elif self.next_token_type(tokens.Obj):
            self.consume_next_token(children, tokens.Obj)
            
            if self.next_token_type(tokens.Year):
                self.call_descent_method(children, self.date)
                self.call_descent_method(children, self.clause)
            elif self.next_token_type(tokens.Human):
                self.call_descent_method(children, self.clause)
            else:
                self.raise_error("Error in Sent. Expected Date or Clause after obj first token.")
        
        elif self.next_token_type(tokens.Year):
            self.call_descent_method(children, self.date)

            if self.next_token_type(tokens.Obj):
                self.consume_next_token(children, tokens.Obj)
                self.call_descent_method(children, self.clause)
            elif self.next_token_type(tokens.Human):
                self.call_descent_method(children, self.clause)
            else:
                self.raise_error("Error in Sent. Expected obj or Clause after Date first symbol.")
        else:
            self.raise_error(f"Error in Sent. Expected a Sent to begin with a human, object, or year and got {type(self.next_token())}.")

        return tree_node.Sent(first_token, children)
       
    def clause(self):
        children : list[tree_node.TreeNode] = []
        first_token : tokens.Token = self.next_token()
        
        # The current next token must be a person. If not, then Error.
        self.match(tokens.Human, self.next_token())

        while self.next_token_type(tokens.Human):
            self.call_descent_method(children, self.clause_f)
        
        if self.next_token_type(tokens.Year):
            self.call_descent_method(children, self.date_tail)
        elif self.next_token_type(tokens.Obj):
            self.call_descent_method(children, self.obj_tail)
        
        return tree_node.Clause(first_token, children)

    def date_tail(self):
        children : list[tree_node.TreeNode] = []
        first_token : tokens.Token = self.next_token()

        self.call_descent_method(children, self.date)

        if self.next_token_type(tokens.Obj):
            self.consume_next_token(children, tokens.Obj)

            self.match(tokens.Human, self.next_token())

            while self.next_token_type(tokens.Human):
                self.call_descent_method(children, self.clause_f)
        
        elif self.next_token_type(tokens.Human):
            # No need to match before the loop, since we can only get here if there is at least 1 Clause_f
            while self.next_token_type(tokens.Human):
                self.call_descent_method(children, self.clause_f)

        return tree_node.DateTail(first_token, children)
    
    def obj_tail(self):
        children : list[tree_node.TreeNode] = []
        first_token : tokens.Token = self.next_token()

        self.consume_next_token(children, tokens.Obj)

        if self.next_token_type(tokens.Year):
            self.call_descent_method(children, self.date)

            self.match(tokens.Human, self.next_token())

            while self.next_token_type(tokens.Human):
                self.call_descent_method(children, self.clause_f)
        
        elif self.next_token_type(tokens.Human):
            # No need to match before the loop, since we can only get here if there is at least 1 Clause_f
            while self.next_token_type(tokens.Human):
                self.call_descent_method(children, self.clause_f)

        return tree_node.ObjTail(first_token, children)

    def date(self):
        children : list[tree_node.TreeNode] = []
        first_token : tokens.Token = self.next_token()

        self.consume_next_token(children, tokens.Year)

        if self.next_token_type(tokens.NameDate):
            self.consume_next_token(children, tokens.NameDate)
        
        return tree_node.Date(first_token, children)

    def clause_f(self):
        children : list[tree_node.TreeNode] = []
        first_token : tokens.Token = self.next_token()

        self.consume_next_token(children, tokens.Human)

        if self.next_token_type(tokens.NameDate):
            self.consume_next_token(children, tokens.NameDate)
        elif self.next_token_type(tokens.NearObj):
            self.call_descent_method(children, self.near_date)
        
        return tree_node.ClauseF(first_token, children)

    def near_date(self):
        children : list[tree_node.TreeNode] = []
        first_token : tokens.Token = self.next_token()

        self.consume_next_token(children, tokens.NearObj)

        if self.next_token_type(tokens.NameDate):
            self.consume_next_token(children, tokens.NameDate)
        
        return tree_node.NearDate(first_token, children)

    # PARSE FUNCTION
    def parse(self, tks : list[tokens.Token]) -> tree_node.Start:
        self.tks = tks
        self.tks.reverse()
        return self.start()
    
    def __call__(self, tks : list[tokens.Token]) -> tree_node.Start:
        return self.parse(tks)

def get_sample_tokens():
    samples : dict[str, tokens.Token] = {
        'lord-standing-right' : tokens.Human(0,0,0,1,1),
        'lord-standing-left' : tokens.Human(0,0,0,1,0),
        'lord-sitting-right' : tokens.Human(0,0,0,0,1),
        'lord-sitting-left' : tokens.Human(0,0,0,0,0),
        'lady-standing-right' : tokens.Human(0,0,1,1,1),
        'lady-standing-left' : tokens.Human(0,0,1,1,0),
        'lady-sitting-right' : tokens.Human(0,0,1,0,1),
        'lady-sitting-left' : tokens.Human(0,0,1,0,0),
        'year-1-reed' : tokens.Year(0, 0, 'Reed', 1),
        'year-5-house' : tokens.Year(0,0,'House', 5),
        'year-13-rabbit' : tokens.Year(0,0, 'Rabbit', 13),
        'date-4-wind' : tokens.NameDate(0,0, 'Wind', 4),
        'date-6-death' : tokens.NameDate(0,0, 'Death', 6),
        'date-3-flint' : tokens.NameDate(0,0,'Flint', 3),
        'date-10-serpent' : tokens.NameDate(0,0,'Serpent',10),
        'table' : tokens.Obj(0, 0, "table"),
        'house' : tokens.Obj(0, 0, 'house'),
        'weapon' : tokens.NearObj(0,0, 'weapon'),
        'shield' : tokens.NearObj(0,0, "shield"),
        'throne' : tokens.NearObj(0,0, "throne"),
        'sacrificed_animal': tokens.NearObj(0,0, "sacrificed_animal"),
        'incense' : tokens.Obj(0,0, 'incense'),
        'river' : tokens.Obj(0,0,'river'),
        'water' : tokens.Obj(0,0, 'water'),
        'end' : tokens.End(0,0,0),
    }
    
    return samples

def construct_from_samples(sample_keys : list[str]):
    samples = get_sample_tokens()
    result : list[tokens.Token] = []

    for k in sample_keys:
        result.append(samples[k])

    return result
        
def test1():
    test_case : list[tokens.Token] = construct_from_samples([
        'year-5-house', 
        'lord-standing-right',
        'date-4-wind',
        'lady-sitting-left',
        'date-10-serpent',
        'end'
    ])
    
    parser = Parser()
    root : tree_node.TreeNode = parser(tks=test_case)
    return root

def run_tests():
    test1()

if __name__ == "__main__":
    run_tests()
            