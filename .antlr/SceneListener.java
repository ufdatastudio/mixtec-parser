// Generated from c:/Users/cwell/Documents/mixtec-parser/mixtec-parser/Scene.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link SceneParser}.
 */
public interface SceneListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link SceneParser#s}.
	 * @param ctx the parse tree
	 */
	void enterS(SceneParser.SContext ctx);
	/**
	 * Exit a parse tree produced by {@link SceneParser#s}.
	 * @param ctx the parse tree
	 */
	void exitS(SceneParser.SContext ctx);
	/**
	 * Enter a parse tree produced by {@link SceneParser#sent}.
	 * @param ctx the parse tree
	 */
	void enterSent(SceneParser.SentContext ctx);
	/**
	 * Exit a parse tree produced by {@link SceneParser#sent}.
	 * @param ctx the parse tree
	 */
	void exitSent(SceneParser.SentContext ctx);
	/**
	 * Enter a parse tree produced by {@link SceneParser#clause}.
	 * @param ctx the parse tree
	 */
	void enterClause(SceneParser.ClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link SceneParser#clause}.
	 * @param ctx the parse tree
	 */
	void exitClause(SceneParser.ClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link SceneParser#date_tail}.
	 * @param ctx the parse tree
	 */
	void enterDate_tail(SceneParser.Date_tailContext ctx);
	/**
	 * Exit a parse tree produced by {@link SceneParser#date_tail}.
	 * @param ctx the parse tree
	 */
	void exitDate_tail(SceneParser.Date_tailContext ctx);
	/**
	 * Enter a parse tree produced by {@link SceneParser#obj_tail}.
	 * @param ctx the parse tree
	 */
	void enterObj_tail(SceneParser.Obj_tailContext ctx);
	/**
	 * Exit a parse tree produced by {@link SceneParser#obj_tail}.
	 * @param ctx the parse tree
	 */
	void exitObj_tail(SceneParser.Obj_tailContext ctx);
	/**
	 * Enter a parse tree produced by {@link SceneParser#date}.
	 * @param ctx the parse tree
	 */
	void enterDate(SceneParser.DateContext ctx);
	/**
	 * Exit a parse tree produced by {@link SceneParser#date}.
	 * @param ctx the parse tree
	 */
	void exitDate(SceneParser.DateContext ctx);
	/**
	 * Enter a parse tree produced by {@link SceneParser#clause_f}.
	 * @param ctx the parse tree
	 */
	void enterClause_f(SceneParser.Clause_fContext ctx);
	/**
	 * Exit a parse tree produced by {@link SceneParser#clause_f}.
	 * @param ctx the parse tree
	 */
	void exitClause_f(SceneParser.Clause_fContext ctx);
	/**
	 * Enter a parse tree produced by {@link SceneParser#near_date}.
	 * @param ctx the parse tree
	 */
	void enterNear_date(SceneParser.Near_dateContext ctx);
	/**
	 * Exit a parse tree produced by {@link SceneParser#near_date}.
	 * @param ctx the parse tree
	 */
	void exitNear_date(SceneParser.Near_dateContext ctx);
}