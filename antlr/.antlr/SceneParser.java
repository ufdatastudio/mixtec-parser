// Generated from c:/Users/cwell/Documents/mixtec-parser/mixtec-parser/antlr/Scene.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class SceneParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		Y=1, H=2, ND=3, OBJ=4, NEAR_OBJ=5, WS=6, XML_DECL=7, SCENE_OPEN=8, SCENE_CLOSE=9;
	public static final int
		RULE_s = 0, RULE_sent = 1, RULE_clause = 2, RULE_date_tail = 3, RULE_obj_tail = 4, 
		RULE_date = 5, RULE_clause_f = 6, RULE_near_date = 7;
	private static String[] makeRuleNames() {
		return new String[] {
			"s", "sent", "clause", "date_tail", "obj_tail", "date", "clause_f", "near_date"
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

	@Override
	public String getGrammarFileName() { return "Scene.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SceneParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SContext extends ParserRuleContext {
		public TerminalNode XML_DECL() { return getToken(SceneParser.XML_DECL, 0); }
		public List<TerminalNode> SCENE_OPEN() { return getTokens(SceneParser.SCENE_OPEN); }
		public TerminalNode SCENE_OPEN(int i) {
			return getToken(SceneParser.SCENE_OPEN, i);
		}
		public List<SentContext> sent() {
			return getRuleContexts(SentContext.class);
		}
		public SentContext sent(int i) {
			return getRuleContext(SentContext.class,i);
		}
		public List<TerminalNode> SCENE_CLOSE() { return getTokens(SceneParser.SCENE_CLOSE); }
		public TerminalNode SCENE_CLOSE(int i) {
			return getToken(SceneParser.SCENE_CLOSE, i);
		}
		public SContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s; }
	}

	public final SContext s() throws RecognitionException {
		SContext _localctx = new SContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_s);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(16);
			match(XML_DECL);
			setState(21); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(17);
				match(SCENE_OPEN);
				setState(18);
				sent();
				setState(19);
				match(SCENE_CLOSE);
				}
				}
				setState(23); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==SCENE_OPEN );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentContext extends ParserRuleContext {
		public ClauseContext clause() {
			return getRuleContext(ClauseContext.class,0);
		}
		public TerminalNode OBJ() { return getToken(SceneParser.OBJ, 0); }
		public DateContext date() {
			return getRuleContext(DateContext.class,0);
		}
		public SentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sent; }
	}

	public final SentContext sent() throws RecognitionException {
		SentContext _localctx = new SentContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_sent);
		try {
			setState(39);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case H:
				enterOuterAlt(_localctx, 1);
				{
				setState(25);
				clause();
				}
				break;
			case OBJ:
				enterOuterAlt(_localctx, 2);
				{
				setState(26);
				match(OBJ);
				setState(31);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case Y:
					{
					setState(27);
					date();
					setState(28);
					clause();
					}
					break;
				case H:
					{
					setState(30);
					clause();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case Y:
				enterOuterAlt(_localctx, 3);
				{
				setState(33);
				date();
				setState(37);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case OBJ:
					{
					setState(34);
					match(OBJ);
					setState(35);
					clause();
					}
					break;
				case H:
					{
					setState(36);
					clause();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ClauseContext extends ParserRuleContext {
		public List<Clause_fContext> clause_f() {
			return getRuleContexts(Clause_fContext.class);
		}
		public Clause_fContext clause_f(int i) {
			return getRuleContext(Clause_fContext.class,i);
		}
		public Date_tailContext date_tail() {
			return getRuleContext(Date_tailContext.class,0);
		}
		public Obj_tailContext obj_tail() {
			return getRuleContext(Obj_tailContext.class,0);
		}
		public ClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clause; }
	}

	public final ClauseContext clause() throws RecognitionException {
		ClauseContext _localctx = new ClauseContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_clause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(41);
				clause_f();
				}
				}
				setState(44); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==H );
			setState(48);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Y:
				{
				setState(46);
				date_tail();
				}
				break;
			case OBJ:
				{
				setState(47);
				obj_tail();
				}
				break;
			case SCENE_CLOSE:
				break;
			default:
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Date_tailContext extends ParserRuleContext {
		public DateContext date() {
			return getRuleContext(DateContext.class,0);
		}
		public TerminalNode OBJ() { return getToken(SceneParser.OBJ, 0); }
		public List<Clause_fContext> clause_f() {
			return getRuleContexts(Clause_fContext.class);
		}
		public Clause_fContext clause_f(int i) {
			return getRuleContext(Clause_fContext.class,i);
		}
		public Date_tailContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_date_tail; }
	}

	public final Date_tailContext date_tail() throws RecognitionException {
		Date_tailContext _localctx = new Date_tailContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_date_tail);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			date();
			setState(62);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OBJ:
				{
				setState(51);
				match(OBJ);
				setState(53); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(52);
					clause_f();
					}
					}
					setState(55); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==H );
				}
				break;
			case H:
				{
				setState(58); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(57);
					clause_f();
					}
					}
					setState(60); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==H );
				}
				break;
			case SCENE_CLOSE:
				break;
			default:
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Obj_tailContext extends ParserRuleContext {
		public TerminalNode OBJ() { return getToken(SceneParser.OBJ, 0); }
		public DateContext date() {
			return getRuleContext(DateContext.class,0);
		}
		public List<Clause_fContext> clause_f() {
			return getRuleContexts(Clause_fContext.class);
		}
		public Clause_fContext clause_f(int i) {
			return getRuleContext(Clause_fContext.class,i);
		}
		public Obj_tailContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_obj_tail; }
	}

	public final Obj_tailContext obj_tail() throws RecognitionException {
		Obj_tailContext _localctx = new Obj_tailContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_obj_tail);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(OBJ);
			setState(76);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Y:
				{
				setState(65);
				date();
				setState(67); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(66);
					clause_f();
					}
					}
					setState(69); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==H );
				}
				break;
			case H:
				{
				setState(72); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(71);
					clause_f();
					}
					}
					setState(74); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==H );
				}
				break;
			case SCENE_CLOSE:
				break;
			default:
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DateContext extends ParserRuleContext {
		public TerminalNode Y() { return getToken(SceneParser.Y, 0); }
		public TerminalNode ND() { return getToken(SceneParser.ND, 0); }
		public DateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_date; }
	}

	public final DateContext date() throws RecognitionException {
		DateContext _localctx = new DateContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_date);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(Y);
			setState(80);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ND) {
				{
				setState(79);
				match(ND);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Clause_fContext extends ParserRuleContext {
		public TerminalNode H() { return getToken(SceneParser.H, 0); }
		public TerminalNode ND() { return getToken(SceneParser.ND, 0); }
		public Near_dateContext near_date() {
			return getRuleContext(Near_dateContext.class,0);
		}
		public Clause_fContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clause_f; }
	}

	public final Clause_fContext clause_f() throws RecognitionException {
		Clause_fContext _localctx = new Clause_fContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_clause_f);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(H);
			setState(85);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ND:
				{
				setState(83);
				match(ND);
				}
				break;
			case NEAR_OBJ:
				{
				setState(84);
				near_date();
				}
				break;
			case Y:
			case H:
			case OBJ:
			case SCENE_CLOSE:
				break;
			default:
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Near_dateContext extends ParserRuleContext {
		public TerminalNode NEAR_OBJ() { return getToken(SceneParser.NEAR_OBJ, 0); }
		public TerminalNode ND() { return getToken(SceneParser.ND, 0); }
		public Near_dateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_near_date; }
	}

	public final Near_dateContext near_date() throws RecognitionException {
		Near_dateContext _localctx = new Near_dateContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_near_date);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(NEAR_OBJ);
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ND) {
				{
				setState(88);
				match(ND);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\t\\\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0004\u0000\u0016"+
		"\b\u0000\u000b\u0000\f\u0000\u0017\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001 \b\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001&\b\u0001\u0003\u0001"+
		"(\b\u0001\u0001\u0002\u0004\u0002+\b\u0002\u000b\u0002\f\u0002,\u0001"+
		"\u0002\u0001\u0002\u0003\u00021\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0004\u00036\b\u0003\u000b\u0003\f\u00037\u0001\u0003\u0004\u0003"+
		";\b\u0003\u000b\u0003\f\u0003<\u0003\u0003?\b\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0004\u0004D\b\u0004\u000b\u0004\f\u0004E\u0001\u0004"+
		"\u0004\u0004I\b\u0004\u000b\u0004\f\u0004J\u0003\u0004M\b\u0004\u0001"+
		"\u0005\u0001\u0005\u0003\u0005Q\b\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0003\u0006V\b\u0006\u0001\u0007\u0001\u0007\u0003\u0007Z\b\u0007"+
		"\u0001\u0007\u0000\u0000\b\u0000\u0002\u0004\u0006\b\n\f\u000e\u0000\u0000"+
		"g\u0000\u0010\u0001\u0000\u0000\u0000\u0002\'\u0001\u0000\u0000\u0000"+
		"\u0004*\u0001\u0000\u0000\u0000\u00062\u0001\u0000\u0000\u0000\b@\u0001"+
		"\u0000\u0000\u0000\nN\u0001\u0000\u0000\u0000\fR\u0001\u0000\u0000\u0000"+
		"\u000eW\u0001\u0000\u0000\u0000\u0010\u0015\u0005\u0007\u0000\u0000\u0011"+
		"\u0012\u0005\b\u0000\u0000\u0012\u0013\u0003\u0002\u0001\u0000\u0013\u0014"+
		"\u0005\t\u0000\u0000\u0014\u0016\u0001\u0000\u0000\u0000\u0015\u0011\u0001"+
		"\u0000\u0000\u0000\u0016\u0017\u0001\u0000\u0000\u0000\u0017\u0015\u0001"+
		"\u0000\u0000\u0000\u0017\u0018\u0001\u0000\u0000\u0000\u0018\u0001\u0001"+
		"\u0000\u0000\u0000\u0019(\u0003\u0004\u0002\u0000\u001a\u001f\u0005\u0004"+
		"\u0000\u0000\u001b\u001c\u0003\n\u0005\u0000\u001c\u001d\u0003\u0004\u0002"+
		"\u0000\u001d \u0001\u0000\u0000\u0000\u001e \u0003\u0004\u0002\u0000\u001f"+
		"\u001b\u0001\u0000\u0000\u0000\u001f\u001e\u0001\u0000\u0000\u0000 (\u0001"+
		"\u0000\u0000\u0000!%\u0003\n\u0005\u0000\"#\u0005\u0004\u0000\u0000#&"+
		"\u0003\u0004\u0002\u0000$&\u0003\u0004\u0002\u0000%\"\u0001\u0000\u0000"+
		"\u0000%$\u0001\u0000\u0000\u0000&(\u0001\u0000\u0000\u0000\'\u0019\u0001"+
		"\u0000\u0000\u0000\'\u001a\u0001\u0000\u0000\u0000\'!\u0001\u0000\u0000"+
		"\u0000(\u0003\u0001\u0000\u0000\u0000)+\u0003\f\u0006\u0000*)\u0001\u0000"+
		"\u0000\u0000+,\u0001\u0000\u0000\u0000,*\u0001\u0000\u0000\u0000,-\u0001"+
		"\u0000\u0000\u0000-0\u0001\u0000\u0000\u0000.1\u0003\u0006\u0003\u0000"+
		"/1\u0003\b\u0004\u00000.\u0001\u0000\u0000\u00000/\u0001\u0000\u0000\u0000"+
		"01\u0001\u0000\u0000\u00001\u0005\u0001\u0000\u0000\u00002>\u0003\n\u0005"+
		"\u000035\u0005\u0004\u0000\u000046\u0003\f\u0006\u000054\u0001\u0000\u0000"+
		"\u000067\u0001\u0000\u0000\u000075\u0001\u0000\u0000\u000078\u0001\u0000"+
		"\u0000\u00008?\u0001\u0000\u0000\u00009;\u0003\f\u0006\u0000:9\u0001\u0000"+
		"\u0000\u0000;<\u0001\u0000\u0000\u0000<:\u0001\u0000\u0000\u0000<=\u0001"+
		"\u0000\u0000\u0000=?\u0001\u0000\u0000\u0000>3\u0001\u0000\u0000\u0000"+
		">:\u0001\u0000\u0000\u0000>?\u0001\u0000\u0000\u0000?\u0007\u0001\u0000"+
		"\u0000\u0000@L\u0005\u0004\u0000\u0000AC\u0003\n\u0005\u0000BD\u0003\f"+
		"\u0006\u0000CB\u0001\u0000\u0000\u0000DE\u0001\u0000\u0000\u0000EC\u0001"+
		"\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000FM\u0001\u0000\u0000\u0000"+
		"GI\u0003\f\u0006\u0000HG\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000"+
		"JH\u0001\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000KM\u0001\u0000\u0000"+
		"\u0000LA\u0001\u0000\u0000\u0000LH\u0001\u0000\u0000\u0000LM\u0001\u0000"+
		"\u0000\u0000M\t\u0001\u0000\u0000\u0000NP\u0005\u0001\u0000\u0000OQ\u0005"+
		"\u0003\u0000\u0000PO\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000\u0000"+
		"Q\u000b\u0001\u0000\u0000\u0000RU\u0005\u0002\u0000\u0000SV\u0005\u0003"+
		"\u0000\u0000TV\u0003\u000e\u0007\u0000US\u0001\u0000\u0000\u0000UT\u0001"+
		"\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000V\r\u0001\u0000\u0000\u0000"+
		"WY\u0005\u0005\u0000\u0000XZ\u0005\u0003\u0000\u0000YX\u0001\u0000\u0000"+
		"\u0000YZ\u0001\u0000\u0000\u0000Z\u000f\u0001\u0000\u0000\u0000\u000f"+
		"\u0017\u001f%\',07<>EJLPUY";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}