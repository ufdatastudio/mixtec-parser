// Generated from c:/Users/cwell/Documents/mixtec-parser/mixtec-parser/Scene.g4 by ANTLR 4.13.1
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
		H=1, Y=2, ND=3, OBJ=4, NEAR_OBJ=5, END=6, WS=7;
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
		public List<SentContext> sent() {
			return getRuleContexts(SentContext.class);
		}
		public SentContext sent(int i) {
			return getRuleContext(SentContext.class,i);
		}
		public List<TerminalNode> END() { return getTokens(SceneParser.END); }
		public TerminalNode END(int i) {
			return getToken(SceneParser.END, i);
		}
		public SContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).enterS(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).exitS(this);
		}
	}

	public final SContext s() throws RecognitionException {
		SContext _localctx = new SContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_s);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(16);
				sent();
				setState(17);
				match(END);
				}
				}
				setState(21); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 22L) != 0) );
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).enterSent(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).exitSent(this);
		}
	}

	public final SentContext sent() throws RecognitionException {
		SentContext _localctx = new SentContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_sent);
		try {
			setState(37);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case H:
				enterOuterAlt(_localctx, 1);
				{
				setState(23);
				clause();
				}
				break;
			case OBJ:
				enterOuterAlt(_localctx, 2);
				{
				setState(24);
				match(OBJ);
				setState(29);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case Y:
					{
					setState(25);
					date();
					setState(26);
					clause();
					}
					break;
				case H:
					{
					setState(28);
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
				setState(31);
				date();
				setState(35);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case OBJ:
					{
					setState(32);
					match(OBJ);
					setState(33);
					clause();
					}
					break;
				case H:
					{
					setState(34);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).enterClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).exitClause(this);
		}
	}

	public final ClauseContext clause() throws RecognitionException {
		ClauseContext _localctx = new ClauseContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_clause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(39);
				clause_f();
				}
				}
				setState(42); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==H );
			setState(46);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Y:
				{
				setState(44);
				date_tail();
				}
				break;
			case OBJ:
				{
				setState(45);
				obj_tail();
				}
				break;
			case END:
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).enterDate_tail(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).exitDate_tail(this);
		}
	}

	public final Date_tailContext date_tail() throws RecognitionException {
		Date_tailContext _localctx = new Date_tailContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_date_tail);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			date();
			setState(60);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OBJ:
				{
				setState(49);
				match(OBJ);
				setState(51); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(50);
					clause_f();
					}
					}
					setState(53); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==H );
				}
				break;
			case H:
				{
				setState(56); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(55);
					clause_f();
					}
					}
					setState(58); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==H );
				}
				break;
			case END:
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).enterObj_tail(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).exitObj_tail(this);
		}
	}

	public final Obj_tailContext obj_tail() throws RecognitionException {
		Obj_tailContext _localctx = new Obj_tailContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_obj_tail);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			match(OBJ);
			setState(74);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Y:
				{
				setState(63);
				date();
				setState(65); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(64);
					clause_f();
					}
					}
					setState(67); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==H );
				}
				break;
			case H:
				{
				setState(70); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(69);
					clause_f();
					}
					}
					setState(72); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==H );
				}
				break;
			case END:
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).enterDate(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).exitDate(this);
		}
	}

	public final DateContext date() throws RecognitionException {
		DateContext _localctx = new DateContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_date);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(Y);
			setState(78);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ND) {
				{
				setState(77);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).enterClause_f(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).exitClause_f(this);
		}
	}

	public final Clause_fContext clause_f() throws RecognitionException {
		Clause_fContext _localctx = new Clause_fContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_clause_f);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			match(H);
			setState(83);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ND:
				{
				setState(81);
				match(ND);
				}
				break;
			case NEAR_OBJ:
				{
				setState(82);
				near_date();
				}
				break;
			case H:
			case Y:
			case OBJ:
			case END:
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).enterNear_date(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SceneListener ) ((SceneListener)listener).exitNear_date(this);
		}
	}

	public final Near_dateContext near_date() throws RecognitionException {
		Near_dateContext _localctx = new Near_dateContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_near_date);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(NEAR_OBJ);
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ND) {
				{
				setState(86);
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
		"\u0004\u0001\u0007Z\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0004\u0000\u0014\b\u0000\u000b\u0000\f"+
		"\u0000\u0015\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001\u001e\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001$\b\u0001\u0003\u0001&\b\u0001\u0001\u0002\u0004"+
		"\u0002)\b\u0002\u000b\u0002\f\u0002*\u0001\u0002\u0001\u0002\u0003\u0002"+
		"/\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0004\u00034\b\u0003\u000b"+
		"\u0003\f\u00035\u0001\u0003\u0004\u00039\b\u0003\u000b\u0003\f\u0003:"+
		"\u0003\u0003=\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0004\u0004"+
		"B\b\u0004\u000b\u0004\f\u0004C\u0001\u0004\u0004\u0004G\b\u0004\u000b"+
		"\u0004\f\u0004H\u0003\u0004K\b\u0004\u0001\u0005\u0001\u0005\u0003\u0005"+
		"O\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006T\b\u0006\u0001"+
		"\u0007\u0001\u0007\u0003\u0007X\b\u0007\u0001\u0007\u0000\u0000\b\u0000"+
		"\u0002\u0004\u0006\b\n\f\u000e\u0000\u0000e\u0000\u0013\u0001\u0000\u0000"+
		"\u0000\u0002%\u0001\u0000\u0000\u0000\u0004(\u0001\u0000\u0000\u0000\u0006"+
		"0\u0001\u0000\u0000\u0000\b>\u0001\u0000\u0000\u0000\nL\u0001\u0000\u0000"+
		"\u0000\fP\u0001\u0000\u0000\u0000\u000eU\u0001\u0000\u0000\u0000\u0010"+
		"\u0011\u0003\u0002\u0001\u0000\u0011\u0012\u0005\u0006\u0000\u0000\u0012"+
		"\u0014\u0001\u0000\u0000\u0000\u0013\u0010\u0001\u0000\u0000\u0000\u0014"+
		"\u0015\u0001\u0000\u0000\u0000\u0015\u0013\u0001\u0000\u0000\u0000\u0015"+
		"\u0016\u0001\u0000\u0000\u0000\u0016\u0001\u0001\u0000\u0000\u0000\u0017"+
		"&\u0003\u0004\u0002\u0000\u0018\u001d\u0005\u0004\u0000\u0000\u0019\u001a"+
		"\u0003\n\u0005\u0000\u001a\u001b\u0003\u0004\u0002\u0000\u001b\u001e\u0001"+
		"\u0000\u0000\u0000\u001c\u001e\u0003\u0004\u0002\u0000\u001d\u0019\u0001"+
		"\u0000\u0000\u0000\u001d\u001c\u0001\u0000\u0000\u0000\u001e&\u0001\u0000"+
		"\u0000\u0000\u001f#\u0003\n\u0005\u0000 !\u0005\u0004\u0000\u0000!$\u0003"+
		"\u0004\u0002\u0000\"$\u0003\u0004\u0002\u0000# \u0001\u0000\u0000\u0000"+
		"#\"\u0001\u0000\u0000\u0000$&\u0001\u0000\u0000\u0000%\u0017\u0001\u0000"+
		"\u0000\u0000%\u0018\u0001\u0000\u0000\u0000%\u001f\u0001\u0000\u0000\u0000"+
		"&\u0003\u0001\u0000\u0000\u0000\')\u0003\f\u0006\u0000(\'\u0001\u0000"+
		"\u0000\u0000)*\u0001\u0000\u0000\u0000*(\u0001\u0000\u0000\u0000*+\u0001"+
		"\u0000\u0000\u0000+.\u0001\u0000\u0000\u0000,/\u0003\u0006\u0003\u0000"+
		"-/\u0003\b\u0004\u0000.,\u0001\u0000\u0000\u0000.-\u0001\u0000\u0000\u0000"+
		"./\u0001\u0000\u0000\u0000/\u0005\u0001\u0000\u0000\u00000<\u0003\n\u0005"+
		"\u000013\u0005\u0004\u0000\u000024\u0003\f\u0006\u000032\u0001\u0000\u0000"+
		"\u000045\u0001\u0000\u0000\u000053\u0001\u0000\u0000\u000056\u0001\u0000"+
		"\u0000\u00006=\u0001\u0000\u0000\u000079\u0003\f\u0006\u000087\u0001\u0000"+
		"\u0000\u00009:\u0001\u0000\u0000\u0000:8\u0001\u0000\u0000\u0000:;\u0001"+
		"\u0000\u0000\u0000;=\u0001\u0000\u0000\u0000<1\u0001\u0000\u0000\u0000"+
		"<8\u0001\u0000\u0000\u0000<=\u0001\u0000\u0000\u0000=\u0007\u0001\u0000"+
		"\u0000\u0000>J\u0005\u0004\u0000\u0000?A\u0003\n\u0005\u0000@B\u0003\f"+
		"\u0006\u0000A@\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000CA\u0001"+
		"\u0000\u0000\u0000CD\u0001\u0000\u0000\u0000DK\u0001\u0000\u0000\u0000"+
		"EG\u0003\f\u0006\u0000FE\u0001\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000"+
		"HF\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000IK\u0001\u0000\u0000"+
		"\u0000J?\u0001\u0000\u0000\u0000JF\u0001\u0000\u0000\u0000JK\u0001\u0000"+
		"\u0000\u0000K\t\u0001\u0000\u0000\u0000LN\u0005\u0002\u0000\u0000MO\u0005"+
		"\u0003\u0000\u0000NM\u0001\u0000\u0000\u0000NO\u0001\u0000\u0000\u0000"+
		"O\u000b\u0001\u0000\u0000\u0000PS\u0005\u0001\u0000\u0000QT\u0005\u0003"+
		"\u0000\u0000RT\u0003\u000e\u0007\u0000SQ\u0001\u0000\u0000\u0000SR\u0001"+
		"\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000T\r\u0001\u0000\u0000\u0000"+
		"UW\u0005\u0005\u0000\u0000VX\u0005\u0003\u0000\u0000WV\u0001\u0000\u0000"+
		"\u0000WX\u0001\u0000\u0000\u0000X\u000f\u0001\u0000\u0000\u0000\u000f"+
		"\u0015\u001d#%*.5:<CHJNSW";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}