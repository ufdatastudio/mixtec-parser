#!/usr/bin/env python3
"""
Test file for XML interpretation of Mixtec parser tokens.
This file tests that the to_xml() methods are working correctly and that
the parser can interpret tokens by generating XML output.
"""

import tokens as tokens
import recursive_descent.parser as parser
import tree_node as tree_node
from recursive_descent.interpreter import Interpreter

def get_sample_tokens():
    """Get sample tokens for testing"""
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
        'sacrificed-animal': tokens.NearObj(0,0, "sacrificed_animal"),
        'incense' : tokens.Obj(0,0, 'incense'),
        'river' : tokens.Obj(0,0,'river'),
        'water' : tokens.Obj(0,0, 'water'),
        'end' : tokens.End(0,0,0),
    }
    
    return samples

def construct_from_samples(sample_keys : list[str]):
    """Construct a list of tokens from sample keys"""
    samples = get_sample_tokens()
    result : list[tokens.Token] = []

    for k in sample_keys:
        result.append(samples[k])

    return result

def generate_xml_from_tokens(token_list: list[tokens.Token]) -> str:
    """Generate XML representation from a list of tokens"""
    xml_parts = ['<?xml version="1.0" encoding="UTF-8"?>', '<scene>']
    
    for token in token_list:
        xml_parts.append('  ' + token.to_xml())
    
    xml_parts.append('</scene>')
    return '\n'.join(xml_parts)

def test_individual_token_xml():
    """Test that individual tokens generate correct XML"""
    print("Testing individual token XML generation...")
    
    samples = get_sample_tokens()
    
    # Test Human tokens
    assert samples['lord-standing-right'].to_xml() == '<human x="0" y="0" gender="Lord" pose="standing" orientation="right"/>'
    assert samples['lady-sitting-left'].to_xml() == '<human x="0" y="0" gender="Lady" pose="sitting" orientation="left"/>'
    
    # Test Year tokens
    assert samples['year-1-reed'].to_xml() == '<year x="0" y="0" symbol="Reed" number="1"/>'
    assert samples['year-13-rabbit'].to_xml() == '<year x="0" y="0" symbol="Rabbit" number="13"/>'
    
    # Test NameDate tokens
    assert samples['date-4-wind'].to_xml() == '<name_date x="0" y="0" symbol="Wind" number="4"/>'
    
    # Test Object tokens
    assert samples['table'].to_xml() == '<object x="0" y="0" identity="table"/>'
    assert samples['house'].to_xml() == '<object x="0" y="0" identity="house"/>'
    
    # Test NearObj tokens
    assert samples['weapon'].to_xml() == '<near_object x="0" y="0" identity="weapon"/>'
    assert samples['throne'].to_xml() == '<near_object x="0" y="0" identity="throne"/>'
    
    # Test End token
    assert samples['end'].to_xml() == '<end x="0" y="0" sent_id="0"/>'
    
    print("✓ All individual token XML tests passed!")

def test_xml_generation_from_samples():
    """Test XML generation from sample token lists"""
    print("\nTesting XML generation from sample token lists...")
    
    # Test case 1: Simple sentence with year and humans
    test_case_1 = construct_from_samples([
        'year-5-house', 
        'lord-standing-right',
        'date-4-wind',
        'lady-sitting-left',
        'date-10-serpent',
        'end'
    ])
    
    xml_1 = generate_xml_from_tokens(test_case_1)
    print("Test Case 1 XML:")
    print(xml_1)
    print()
    
    # Test case 2: Scene with objects and near objects
    test_case_2 = construct_from_samples([
        'table',
        'lord-sitting-right',
        'throne',
        'date-3-flint',
        'lady-standing-left',
        'weapon',
        'end'
    ])
    
    xml_2 = generate_xml_from_tokens(test_case_2)
    print("Test Case 2 XML:")
    print(xml_2)
    print()
    
    # Test case 3: Complex scene with multiple elements
    test_case_3 = construct_from_samples([
        'year-13-rabbit',
        'date-6-death',
        'house',
        'lord-standing-left',
        'shield',
        'lady-sitting-right',
        'incense',
        'end'
    ])
    
    xml_3 = generate_xml_from_tokens(test_case_3)
    print("Test Case 3 XML:")
    print(xml_3)
    print()
    
    print("✓ XML generation tests completed!")

def test_parser_with_xml_output():
    """Test that the parser can work with XML output"""
    print("\nTesting parser with XML output...")
    
    # Use the same test case as in the original parser
    test_case = construct_from_samples([
        'year-5-house', 
        'lord-standing-right',
        'date-4-wind',
        'lady-sitting-left',
        'date-10-serpent',
        'end'
    ])
    
    # Generate XML from the tokens
    xml_output = generate_xml_from_tokens(test_case)
    print("XML representation of input tokens:")
    print(xml_output)
    print()
    
    # Parse the tokens using the existing parser
    parser_instance = parser.Parser()
    parse_tree = parser_instance(test_case)
    
    # Get the traditional interpretation
    interpreter = Interpreter()
    traditional_result = interpreter(parse_tree)
    
    print("Traditional interpretation result:")
    print(traditional_result)
    print()
    
    print("✓ Parser with XML output test completed!")

def run_all_tests():
    """Run all XML interpretation tests"""
    print("=" * 60)
    print("XML INTERPRETATION TESTS")
    print("=" * 60)
    
    try:
        test_individual_token_xml()
        test_xml_generation_from_samples()
        test_parser_with_xml_output()
        
        print("\n" + "=" * 60)
        print("ALL TESTS PASSED! ✓")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n Test failed with error: {e}")
        raise

if __name__ == "__main__":
    run_all_tests() 