# Graphviz rendering of parser ASTs for the Streamlit demo.
"""Render an abstract syntax tree as Graphviz DOT, echoing Figure 3 of the paper.

Nonterminal nodes carry the grammar's rule names and, where the partial
interpretation is a plain string, the reading that the interpreter assembles
at that node. Terminal nodes are colored by token kind.
"""

import tokens
import tree_node

# Categorical accents for token kinds, checked with the dataviz six-checks
# validator for colorblind separation and contrast on the parchment surface.
HUMAN_ACCENT = "#9E2B25"
DATE_ACCENT = "#B97A24"
OBJECT_ACCENT = "#0E7CA6"
NEAR_OBJECT_ACCENT = "#2F8B4E"
END_ACCENT = "#8A8378"

HUMAN_TINT = "#F6DEDA"
DATE_TINT = "#F6E7CE"
OBJECT_TINT = "#D8EAF2"
NEAR_OBJECT_TINT = "#DDF0E2"
END_TINT = "#ECE7DC"

RULE_FILL = "#2E2A27"
RULE_TEXT = "#FAF6EE"
INK = "#221D18"
EDGE_COLOR = "#8A8378"

_RULE_LABELS = {
    tree_node.Start: "S",
    tree_node.Sent: "Sent",
    tree_node.Clause: "Clause",
    tree_node.DateTail: "Date_tail",
    tree_node.ObjTail: "Obj_tail",
    tree_node.Date: "Date",
    tree_node.ClauseF: "Clause_f",
    tree_node.NearDate: "Near_date",
}

# Rule nodes whose interpret() returns a display-safe string. The tails return
# tuples with meta-characters, so they are annotated only through their parents.
_ANNOTATED_RULES = (tree_node.Date, tree_node.ClauseF, tree_node.NearDate)


def _token_style(token: tokens.Token) -> tuple[str, str, str]:
    """Return the label, fill tint, and accent color for a terminal node."""
    if isinstance(token, tokens.Human):
        gender = token.gender_dict[token.gender]
        pose = token.pose_dict[token.pose]
        orientation = token.orientation_dict[token.orientation]
        return f"h\n{gender} · {pose} · facing {orientation}", HUMAN_TINT, HUMAN_ACCENT
    if isinstance(token, tokens.Year):
        return f"y\nYear {token.number} {token.symbol}", DATE_TINT, DATE_ACCENT
    if isinstance(token, tokens.NameDate):
        return f"nd\n{token.number} {token.symbol}", DATE_TINT, DATE_ACCENT
    if isinstance(token, tokens.NearObj):
        return f"near_obj\n{token.identity}", NEAR_OBJECT_TINT, NEAR_OBJECT_ACCENT
    if isinstance(token, tokens.Obj):
        return f"obj\n{token.identity}", OBJECT_TINT, OBJECT_ACCENT
    if isinstance(token, tokens.End):
        return "end", END_TINT, END_ACCENT
    return type(token).__name__, END_TINT, END_ACCENT


def _rule_label(node: tree_node.TreeNode) -> str:
    label = _RULE_LABELS.get(type(node), type(node).__name__)
    if isinstance(node, _ANNOTATED_RULES):
        reading = node.interpret().replace("$", " + ")
        label = f"{label}\n“{reading}”"
    return label


def _escape(label: str) -> str:
    return label.replace('"', '\\"').replace("\n", "\\n")


def to_dot(root: tree_node.TreeNode) -> str:
    """Serialize the AST rooted at root into a Graphviz DOT digraph."""
    lines = [
        "digraph AST {",
        '  bgcolor="transparent";',
        "  rankdir=TB;",
        '  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, margin="0.18,0.09", penwidth=1.6];',
        f'  edge [color="{EDGE_COLOR}", arrowsize=0.6];',
    ]
    counter = [0]

    def visit(node) -> str:
        node_id = f"n{counter[0]}"
        counter[0] += 1

        if isinstance(node, tokens.Token):
            label, fill, accent = _token_style(node)
            lines.append(
                f'  {node_id} [label="{_escape(label)}", fillcolor="{fill}", color="{accent}", fontcolor="{INK}"];'
            )
            return node_id

        label = _rule_label(node)
        lines.append(
            f'  {node_id} [label="{_escape(label)}", fillcolor="{RULE_FILL}", color="{RULE_FILL}", fontcolor="{RULE_TEXT}"];'
        )
        for child in node.get_children():
            child_id = visit(child)
            lines.append(f"  {node_id} -> {child_id};")
        return node_id

    visit(root)
    lines.append("}")
    return "\n".join(lines)
