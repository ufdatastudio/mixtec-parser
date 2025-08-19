// Generated from c:/Users/cwell/Documents/mixtec-parser/mixtec-parser/antlr/Scene.g4 by ANTLR 4.13.1
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
		Y=1, H=2, ND=3, OBJ=4, NEAR_OBJ=5, WS=6, XML_DECL=7, SCENE_OPEN=8, SCENE_CLOSE=9;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"Y", "H", "ND", "OBJ", "NEAR_OBJ", "WS", "XML_DECL", "SCENE_OPEN", "SCENE_CLOSE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "'<scene>'", "'</scene>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "Y", "H", "ND", "OBJ", "NEAR_OBJ", "WS", "XML_DECL", "SCENE_OPEN", 
			"SCENE_CLOSE"
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
		"\u0004\u0000\t\u008e\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u0000\u001b\b\u0000\n"+
		"\u0000\f\u0000\u001e\t\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0005\u0001+\b\u0001\n\u0001\f\u0001.\t\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0005\u0002?\b\u0002\n\u0002\f\u0002B\t"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003M\b\u0003\n\u0003"+
		"\f\u0003P\t\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004`\b\u0004\n\u0004"+
		"\f\u0004c\t\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0004"+
		"\u0005i\b\u0005\u000b\u0005\f\u0005j\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0005\u0006v\b\u0006\n\u0006\f\u0006y\t\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0006\u001c,@Naw\u0000\t\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f"+
		"\b\u0011\t\u0001\u0000\u0001\u0003\u0000\t\n\r\r  \u0094\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000"+
		"\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000"+
		"\u0000\u0001\u0013\u0001\u0000\u0000\u0000\u0003\"\u0001\u0000\u0000\u0000"+
		"\u00052\u0001\u0000\u0000\u0000\u0007F\u0001\u0000\u0000\u0000\tT\u0001"+
		"\u0000\u0000\u0000\u000bh\u0001\u0000\u0000\u0000\rn\u0001\u0000\u0000"+
		"\u0000\u000f}\u0001\u0000\u0000\u0000\u0011\u0085\u0001\u0000\u0000\u0000"+
		"\u0013\u0014\u0005<\u0000\u0000\u0014\u0015\u0005y\u0000\u0000\u0015\u0016"+
		"\u0005e\u0000\u0000\u0016\u0017\u0005a\u0000\u0000\u0017\u0018\u0005r"+
		"\u0000\u0000\u0018\u001c\u0001\u0000\u0000\u0000\u0019\u001b\t\u0000\u0000"+
		"\u0000\u001a\u0019\u0001\u0000\u0000\u0000\u001b\u001e\u0001\u0000\u0000"+
		"\u0000\u001c\u001d\u0001\u0000\u0000\u0000\u001c\u001a\u0001\u0000\u0000"+
		"\u0000\u001d\u001f\u0001\u0000\u0000\u0000\u001e\u001c\u0001\u0000\u0000"+
		"\u0000\u001f \u0005/\u0000\u0000 !\u0005>\u0000\u0000!\u0002\u0001\u0000"+
		"\u0000\u0000\"#\u0005<\u0000\u0000#$\u0005h\u0000\u0000$%\u0005u\u0000"+
		"\u0000%&\u0005m\u0000\u0000&\'\u0005a\u0000\u0000\'(\u0005n\u0000\u0000"+
		"(,\u0001\u0000\u0000\u0000)+\t\u0000\u0000\u0000*)\u0001\u0000\u0000\u0000"+
		"+.\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000,*\u0001\u0000\u0000"+
		"\u0000-/\u0001\u0000\u0000\u0000.,\u0001\u0000\u0000\u0000/0\u0005/\u0000"+
		"\u000001\u0005>\u0000\u00001\u0004\u0001\u0000\u0000\u000023\u0005<\u0000"+
		"\u000034\u0005n\u0000\u000045\u0005a\u0000\u000056\u0005m\u0000\u0000"+
		"67\u0005e\u0000\u000078\u0005_\u0000\u000089\u0005d\u0000\u00009:\u0005"+
		"a\u0000\u0000:;\u0005t\u0000\u0000;<\u0005e\u0000\u0000<@\u0001\u0000"+
		"\u0000\u0000=?\t\u0000\u0000\u0000>=\u0001\u0000\u0000\u0000?B\u0001\u0000"+
		"\u0000\u0000@A\u0001\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000AC\u0001"+
		"\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000CD\u0005/\u0000\u0000DE\u0005"+
		">\u0000\u0000E\u0006\u0001\u0000\u0000\u0000FG\u0005<\u0000\u0000GH\u0005"+
		"o\u0000\u0000HI\u0005b\u0000\u0000IJ\u0005j\u0000\u0000JN\u0001\u0000"+
		"\u0000\u0000KM\t\u0000\u0000\u0000LK\u0001\u0000\u0000\u0000MP\u0001\u0000"+
		"\u0000\u0000NO\u0001\u0000\u0000\u0000NL\u0001\u0000\u0000\u0000OQ\u0001"+
		"\u0000\u0000\u0000PN\u0001\u0000\u0000\u0000QR\u0005/\u0000\u0000RS\u0005"+
		">\u0000\u0000S\b\u0001\u0000\u0000\u0000TU\u0005<\u0000\u0000UV\u0005"+
		"n\u0000\u0000VW\u0005e\u0000\u0000WX\u0005a\u0000\u0000XY\u0005r\u0000"+
		"\u0000YZ\u0005_\u0000\u0000Z[\u0005o\u0000\u0000[\\\u0005b\u0000\u0000"+
		"\\]\u0005j\u0000\u0000]a\u0001\u0000\u0000\u0000^`\t\u0000\u0000\u0000"+
		"_^\u0001\u0000\u0000\u0000`c\u0001\u0000\u0000\u0000ab\u0001\u0000\u0000"+
		"\u0000a_\u0001\u0000\u0000\u0000bd\u0001\u0000\u0000\u0000ca\u0001\u0000"+
		"\u0000\u0000de\u0005/\u0000\u0000ef\u0005>\u0000\u0000f\n\u0001\u0000"+
		"\u0000\u0000gi\u0007\u0000\u0000\u0000hg\u0001\u0000\u0000\u0000ij\u0001"+
		"\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000jk\u0001\u0000\u0000\u0000"+
		"kl\u0001\u0000\u0000\u0000lm\u0006\u0005\u0000\u0000m\f\u0001\u0000\u0000"+
		"\u0000no\u0005<\u0000\u0000op\u0005?\u0000\u0000pq\u0005x\u0000\u0000"+
		"qr\u0005m\u0000\u0000rs\u0005l\u0000\u0000sw\u0001\u0000\u0000\u0000t"+
		"v\t\u0000\u0000\u0000ut\u0001\u0000\u0000\u0000vy\u0001\u0000\u0000\u0000"+
		"wx\u0001\u0000\u0000\u0000wu\u0001\u0000\u0000\u0000xz\u0001\u0000\u0000"+
		"\u0000yw\u0001\u0000\u0000\u0000z{\u0005?\u0000\u0000{|\u0005>\u0000\u0000"+
		"|\u000e\u0001\u0000\u0000\u0000}~\u0005<\u0000\u0000~\u007f\u0005s\u0000"+
		"\u0000\u007f\u0080\u0005c\u0000\u0000\u0080\u0081\u0005e\u0000\u0000\u0081"+
		"\u0082\u0005n\u0000\u0000\u0082\u0083\u0005e\u0000\u0000\u0083\u0084\u0005"+
		">\u0000\u0000\u0084\u0010\u0001\u0000\u0000\u0000\u0085\u0086\u0005<\u0000"+
		"\u0000\u0086\u0087\u0005/\u0000\u0000\u0087\u0088\u0005s\u0000\u0000\u0088"+
		"\u0089\u0005c\u0000\u0000\u0089\u008a\u0005e\u0000\u0000\u008a\u008b\u0005"+
		"n\u0000\u0000\u008b\u008c\u0005e\u0000\u0000\u008c\u008d\u0005>\u0000"+
		"\u0000\u008d\u0012\u0001\u0000\u0000\u0000\b\u0000\u001c,@Najw\u0001\u0006"+
		"\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}