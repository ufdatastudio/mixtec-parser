import xml.etree.ElementTree as ET
from tokens import *
from antlr.SceneLexer import SceneLexer  # Make sure to use your lexer here

class TokenConvertor:
    # Map ANTLR token type (int) to Token class
    tokenTypeMap = {
        "H": Human,
        "Y": Year,
        "ND": NameDate,
        "OBJ": Obj,
        "NEAR_OBJ": NearObj,
        "END": End,
    }

    @staticmethod
    def convert_token(token):
        token_name = SceneLexer.symbolicNames[token.type] if token.type > 0 else "<INVALID>"
        token_text = token.text

        if token_name not in TokenConvertor.tokenTypeMap:
            raise ValueError(f"Unknown token type: {token_name}")

        TokenClass = TokenConvertor.tokenTypeMap[token_name]

        try:
            elem = ET.fromstring(token_text)
            attrib = elem.attrib
            x = int(attrib.get("x", 0))
            y = int(attrib.get("y", 0))

            # Instantiate based on class
            if TokenClass == Human:
                gender = 0 if attrib["gender"] == "Lord" else 1
                pose = 0 if attrib["pose"] == "sitting" else 1
                orientation = 0 if attrib["orientation"] == "left" else 1
                return Human(x, y, gender, pose, orientation)

            elif TokenClass == Year:
                return Year(x, y, attrib["symbol"], int(attrib["number"]))

            elif TokenClass == NameDate:
                return NameDate(x, y, attrib["symbol"], int(attrib["number"]))

            elif TokenClass == Obj:
                return Obj(x, y, attrib["identity"])

            elif TokenClass == NearObj:
                return NearObj(x, y, attrib["identity"])

            elif TokenClass == End:
                return End(x, y, int(attrib["sent_id"]))
            else:
                raise ValueError(f"Token does not match any token type")

        except Exception as e:
            raise ValueError(f"Failed to convert token: {token_text}. Error: {e}")
