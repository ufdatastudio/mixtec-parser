// Generated from c:/Users/cwell/Documents/mixtec-parser/mixtec-parser/Scene.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class SceneLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		H=1, Y=2, ND=3, OBJ=4, NEAR_OBJ=5, END=6, WS=7;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"H", "Y", "ND", "OBJ", "NEAR_OBJ", "END", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, "'<End/>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "H", "Y", "ND", "OBJ", "NEAR_OBJ", "END", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public SceneLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Scene.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0007\u0094\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0005\u0000\u0019\b\u0000\n\u0000\f\u0000"+
		"\u001c\t\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0005\u0001/\b\u0001\n\u0001\f\u00012\t\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0005\u0002H\b\u0002\n\u0002\f\u0002K\t\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003"+
		"`\b\u0003\n\u0003\f\u0003c\t\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004w\b\u0004\n\u0004\f\u0004"+
		"z\t\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0004\u0006\u008f\b\u0006\u000b\u0006\f\u0006"+
		"\u0090\u0001\u0006\u0001\u0006\u0005\u001a0Iax\u0000\u0007\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u0001"+
		"\u0000\u0001\u0005\u0000  \\\\nnrrtt\u0099\u0000\u0001\u0001\u0000\u0000"+
		"\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000"+
		"\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000"+
		"\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0001"+
		"\u000f\u0001\u0000\u0000\u0000\u0003&\u0001\u0000\u0000\u0000\u0005;\u0001"+
		"\u0000\u0000\u0000\u0007X\u0001\u0000\u0000\u0000\tk\u0001\u0000\u0000"+
		"\u0000\u000b\u0086\u0001\u0000\u0000\u0000\r\u008e\u0001\u0000\u0000\u0000"+
		"\u000f\u0010\u0005<\u0000\u0000\u0010\u0011\u0005H\u0000\u0000\u0011\u0012"+
		"\u0005u\u0000\u0000\u0012\u0013\u0005m\u0000\u0000\u0013\u0014\u0005a"+
		"\u0000\u0000\u0014\u0015\u0005n\u0000\u0000\u0015\u0016\u0005>\u0000\u0000"+
		"\u0016\u001a\u0001\u0000\u0000\u0000\u0017\u0019\t\u0000\u0000\u0000\u0018"+
		"\u0017\u0001\u0000\u0000\u0000\u0019\u001c\u0001\u0000\u0000\u0000\u001a"+
		"\u001b\u0001\u0000\u0000\u0000\u001a\u0018\u0001\u0000\u0000\u0000\u001b"+
		"\u001d\u0001\u0000\u0000\u0000\u001c\u001a\u0001\u0000\u0000\u0000\u001d"+
		"\u001e\u0005<\u0000\u0000\u001e\u001f\u0005/\u0000\u0000\u001f \u0005"+
		"H\u0000\u0000 !\u0005u\u0000\u0000!\"\u0005m\u0000\u0000\"#\u0005a\u0000"+
		"\u0000#$\u0005n\u0000\u0000$%\u0005>\u0000\u0000%\u0002\u0001\u0000\u0000"+
		"\u0000&\'\u0005<\u0000\u0000\'(\u0005Y\u0000\u0000()\u0005e\u0000\u0000"+
		")*\u0005a\u0000\u0000*+\u0005r\u0000\u0000+,\u0005>\u0000\u0000,0\u0001"+
		"\u0000\u0000\u0000-/\t\u0000\u0000\u0000.-\u0001\u0000\u0000\u0000/2\u0001"+
		"\u0000\u0000\u000001\u0001\u0000\u0000\u00000.\u0001\u0000\u0000\u0000"+
		"13\u0001\u0000\u0000\u000020\u0001\u0000\u0000\u000034\u0005<\u0000\u0000"+
		"45\u0005/\u0000\u000056\u0005Y\u0000\u000067\u0005e\u0000\u000078\u0005"+
		"a\u0000\u000089\u0005r\u0000\u00009:\u0005>\u0000\u0000:\u0004\u0001\u0000"+
		"\u0000\u0000;<\u0005<\u0000\u0000<=\u0005N\u0000\u0000=>\u0005a\u0000"+
		"\u0000>?\u0005m\u0000\u0000?@\u0005e\u0000\u0000@A\u0005D\u0000\u0000"+
		"AB\u0005a\u0000\u0000BC\u0005t\u0000\u0000CD\u0005e\u0000\u0000DE\u0005"+
		">\u0000\u0000EI\u0001\u0000\u0000\u0000FH\t\u0000\u0000\u0000GF\u0001"+
		"\u0000\u0000\u0000HK\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000"+
		"IG\u0001\u0000\u0000\u0000JL\u0001\u0000\u0000\u0000KI\u0001\u0000\u0000"+
		"\u0000LM\u0005<\u0000\u0000MN\u0005/\u0000\u0000NO\u0005N\u0000\u0000"+
		"OP\u0005a\u0000\u0000PQ\u0005m\u0000\u0000QR\u0005e\u0000\u0000RS\u0005"+
		"D\u0000\u0000ST\u0005a\u0000\u0000TU\u0005t\u0000\u0000UV\u0005e\u0000"+
		"\u0000VW\u0005>\u0000\u0000W\u0006\u0001\u0000\u0000\u0000XY\u0005<\u0000"+
		"\u0000YZ\u0005O\u0000\u0000Z[\u0005b\u0000\u0000[\\\u0005j\u0000\u0000"+
		"\\]\u0005>\u0000\u0000]a\u0001\u0000\u0000\u0000^`\t\u0000\u0000\u0000"+
		"_^\u0001\u0000\u0000\u0000`c\u0001\u0000\u0000\u0000ab\u0001\u0000\u0000"+
		"\u0000a_\u0001\u0000\u0000\u0000bd\u0001\u0000\u0000\u0000ca\u0001\u0000"+
		"\u0000\u0000de\u0005<\u0000\u0000ef\u0005/\u0000\u0000fg\u0005O\u0000"+
		"\u0000gh\u0005b\u0000\u0000hi\u0005j\u0000\u0000ij\u0005>\u0000\u0000"+
		"j\b\u0001\u0000\u0000\u0000kl\u0005<\u0000\u0000lm\u0005N\u0000\u0000"+
		"mn\u0005e\u0000\u0000no\u0005a\u0000\u0000op\u0005r\u0000\u0000pq\u0005"+
		"O\u0000\u0000qr\u0005b\u0000\u0000rs\u0005j\u0000\u0000st\u0005>\u0000"+
		"\u0000tx\u0001\u0000\u0000\u0000uw\t\u0000\u0000\u0000vu\u0001\u0000\u0000"+
		"\u0000wz\u0001\u0000\u0000\u0000xy\u0001\u0000\u0000\u0000xv\u0001\u0000"+
		"\u0000\u0000y{\u0001\u0000\u0000\u0000zx\u0001\u0000\u0000\u0000{|\u0005"+
		"<\u0000\u0000|}\u0005/\u0000\u0000}~\u0005N\u0000\u0000~\u007f\u0005e"+
		"\u0000\u0000\u007f\u0080\u0005a\u0000\u0000\u0080\u0081\u0005r\u0000\u0000"+
		"\u0081\u0082\u0005O\u0000\u0000\u0082\u0083\u0005b\u0000\u0000\u0083\u0084"+
		"\u0005j\u0000\u0000\u0084\u0085\u0005>\u0000\u0000\u0085\n\u0001\u0000"+
		"\u0000\u0000\u0086\u0087\u0005<\u0000\u0000\u0087\u0088\u0005E\u0000\u0000"+
		"\u0088\u0089\u0005n\u0000\u0000\u0089\u008a\u0005d\u0000\u0000\u008a\u008b"+
		"\u0005/\u0000\u0000\u008b\u008c\u0005>\u0000\u0000\u008c\f\u0001\u0000"+
		"\u0000\u0000\u008d\u008f\u0007\u0000\u0000\u0000\u008e\u008d\u0001\u0000"+
		"\u0000\u0000\u008f\u0090\u0001\u0000\u0000\u0000\u0090\u008e\u0001\u0000"+
		"\u0000\u0000\u0090\u0091\u0001\u0000\u0000\u0000\u0091\u0092\u0001\u0000"+
		"\u0000\u0000\u0092\u0093\u0006\u0006\u0000\u0000\u0093\u000e\u0001\u0000"+
		"\u0000\u0000\u0007\u0000\u001a0Iax\u0090\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}