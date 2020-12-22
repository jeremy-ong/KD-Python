# Generated from KDParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .KDParser import KDParser
else:
    from KDParser import KDParser

# This class defines a complete listener for a parse tree produced by KDParser.
class KDParserListener(ParseTreeListener):

    # Enter a parse tree produced by KDParser#tagList.
    def enterTagList(self, ctx:KDParser.TagListContext):
        pass

    # Exit a parse tree produced by KDParser#tagList.
    def exitTagList(self, ctx:KDParser.TagListContext):
        pass


    # Enter a parse tree produced by KDParser#tag.
    def enterTag(self, ctx:KDParser.TagContext):
        pass

    # Exit a parse tree produced by KDParser#tag.
    def exitTag(self, ctx:KDParser.TagContext):
        pass


    # Enter a parse tree produced by KDParser#value.
    def enterValue(self, ctx:KDParser.ValueContext):
        pass

    # Exit a parse tree produced by KDParser#value.
    def exitValue(self, ctx:KDParser.ValueContext):
        pass


    # Enter a parse tree produced by KDParser#stringLiteral.
    def enterStringLiteral(self, ctx:KDParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by KDParser#stringLiteral.
    def exitStringLiteral(self, ctx:KDParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by KDParser#blockString.
    def enterBlockString(self, ctx:KDParser.BlockStringContext):
        pass

    # Exit a parse tree produced by KDParser#blockString.
    def exitBlockString(self, ctx:KDParser.BlockStringContext):
        pass


    # Enter a parse tree produced by KDParser#blockRawString.
    def enterBlockRawString(self, ctx:KDParser.BlockRawStringContext):
        pass

    # Exit a parse tree produced by KDParser#blockRawString.
    def exitBlockRawString(self, ctx:KDParser.BlockRawStringContext):
        pass


    # Enter a parse tree produced by KDParser#blockRawAltString.
    def enterBlockRawAltString(self, ctx:KDParser.BlockRawAltStringContext):
        pass

    # Exit a parse tree produced by KDParser#blockRawAltString.
    def exitBlockRawAltString(self, ctx:KDParser.BlockRawAltStringContext):
        pass


    # Enter a parse tree produced by KDParser#duration.
    def enterDuration(self, ctx:KDParser.DurationContext):
        pass

    # Exit a parse tree produced by KDParser#duration.
    def exitDuration(self, ctx:KDParser.DurationContext):
        pass


    # Enter a parse tree produced by KDParser#quantity.
    def enterQuantity(self, ctx:KDParser.QuantityContext):
        pass

    # Exit a parse tree produced by KDParser#quantity.
    def exitQuantity(self, ctx:KDParser.QuantityContext):
        pass


    # Enter a parse tree produced by KDParser#rangeOp.
    def enterRangeOp(self, ctx:KDParser.RangeOpContext):
        pass

    # Exit a parse tree produced by KDParser#rangeOp.
    def exitRangeOp(self, ctx:KDParser.RangeOpContext):
        pass


    # Enter a parse tree produced by KDParser#intRange.
    def enterIntRange(self, ctx:KDParser.IntRangeContext):
        pass

    # Exit a parse tree produced by KDParser#intRange.
    def exitIntRange(self, ctx:KDParser.IntRangeContext):
        pass


    # Enter a parse tree produced by KDParser#longRange.
    def enterLongRange(self, ctx:KDParser.LongRangeContext):
        pass

    # Exit a parse tree produced by KDParser#longRange.
    def exitLongRange(self, ctx:KDParser.LongRangeContext):
        pass


    # Enter a parse tree produced by KDParser#floatRange.
    def enterFloatRange(self, ctx:KDParser.FloatRangeContext):
        pass

    # Exit a parse tree produced by KDParser#floatRange.
    def exitFloatRange(self, ctx:KDParser.FloatRangeContext):
        pass


    # Enter a parse tree produced by KDParser#doubleRange.
    def enterDoubleRange(self, ctx:KDParser.DoubleRangeContext):
        pass

    # Exit a parse tree produced by KDParser#doubleRange.
    def exitDoubleRange(self, ctx:KDParser.DoubleRangeContext):
        pass


    # Enter a parse tree produced by KDParser#decimalRange.
    def enterDecimalRange(self, ctx:KDParser.DecimalRangeContext):
        pass

    # Exit a parse tree produced by KDParser#decimalRange.
    def exitDecimalRange(self, ctx:KDParser.DecimalRangeContext):
        pass


    # Enter a parse tree produced by KDParser#durationRange.
    def enterDurationRange(self, ctx:KDParser.DurationRangeContext):
        pass

    # Exit a parse tree produced by KDParser#durationRange.
    def exitDurationRange(self, ctx:KDParser.DurationRangeContext):
        pass


    # Enter a parse tree produced by KDParser#dateTimeRange.
    def enterDateTimeRange(self, ctx:KDParser.DateTimeRangeContext):
        pass

    # Exit a parse tree produced by KDParser#dateTimeRange.
    def exitDateTimeRange(self, ctx:KDParser.DateTimeRangeContext):
        pass


    # Enter a parse tree produced by KDParser#versionRange.
    def enterVersionRange(self, ctx:KDParser.VersionRangeContext):
        pass

    # Exit a parse tree produced by KDParser#versionRange.
    def exitVersionRange(self, ctx:KDParser.VersionRangeContext):
        pass


    # Enter a parse tree produced by KDParser#charRange.
    def enterCharRange(self, ctx:KDParser.CharRangeContext):
        pass

    # Exit a parse tree produced by KDParser#charRange.
    def exitCharRange(self, ctx:KDParser.CharRangeContext):
        pass


    # Enter a parse tree produced by KDParser#stringRange.
    def enterStringRange(self, ctx:KDParser.StringRangeContext):
        pass

    # Exit a parse tree produced by KDParser#stringRange.
    def exitStringRange(self, ctx:KDParser.StringRangeContext):
        pass


    # Enter a parse tree produced by KDParser#quantityRange.
    def enterQuantityRange(self, ctx:KDParser.QuantityRangeContext):
        pass

    # Exit a parse tree produced by KDParser#quantityRange.
    def exitQuantityRange(self, ctx:KDParser.QuantityRangeContext):
        pass


    # Enter a parse tree produced by KDParser#range_.
    def enterRange_(self, ctx:KDParser.Range_Context):
        pass

    # Exit a parse tree produced by KDParser#range_.
    def exitRange_(self, ctx:KDParser.Range_Context):
        pass


    # Enter a parse tree produced by KDParser#blob.
    def enterBlob(self, ctx:KDParser.BlobContext):
        pass

    # Exit a parse tree produced by KDParser#blob.
    def exitBlob(self, ctx:KDParser.BlobContext):
        pass


    # Enter a parse tree produced by KDParser#valueList.
    def enterValueList(self, ctx:KDParser.ValueListContext):
        pass

    # Exit a parse tree produced by KDParser#valueList.
    def exitValueList(self, ctx:KDParser.ValueListContext):
        pass


    # Enter a parse tree produced by KDParser#attribute.
    def enterAttribute(self, ctx:KDParser.AttributeContext):
        pass

    # Exit a parse tree produced by KDParser#attribute.
    def exitAttribute(self, ctx:KDParser.AttributeContext):
        pass


    # Enter a parse tree produced by KDParser#attributeList.
    def enterAttributeList(self, ctx:KDParser.AttributeListContext):
        pass

    # Exit a parse tree produced by KDParser#attributeList.
    def exitAttributeList(self, ctx:KDParser.AttributeListContext):
        pass


    # Enter a parse tree produced by KDParser#nsName.
    def enterNsName(self, ctx:KDParser.NsNameContext):
        pass

    # Exit a parse tree produced by KDParser#nsName.
    def exitNsName(self, ctx:KDParser.NsNameContext):
        pass


    # Enter a parse tree produced by KDParser#list_.
    def enterList_(self, ctx:KDParser.List_Context):
        pass

    # Exit a parse tree produced by KDParser#list_.
    def exitList_(self, ctx:KDParser.List_Context):
        pass


    # Enter a parse tree produced by KDParser#pair.
    def enterPair(self, ctx:KDParser.PairContext):
        pass

    # Exit a parse tree produced by KDParser#pair.
    def exitPair(self, ctx:KDParser.PairContext):
        pass


    # Enter a parse tree produced by KDParser#map_.
    def enterMap_(self, ctx:KDParser.Map_Context):
        pass

    # Exit a parse tree produced by KDParser#map_.
    def exitMap_(self, ctx:KDParser.Map_Context):
        pass


    # Enter a parse tree produced by KDParser#annotation.
    def enterAnnotation(self, ctx:KDParser.AnnotationContext):
        pass

    # Exit a parse tree produced by KDParser#annotation.
    def exitAnnotation(self, ctx:KDParser.AnnotationContext):
        pass


    # Enter a parse tree produced by KDParser#annotationList.
    def enterAnnotationList(self, ctx:KDParser.AnnotationListContext):
        pass

    # Exit a parse tree produced by KDParser#annotationList.
    def exitAnnotationList(self, ctx:KDParser.AnnotationListContext):
        pass


    # Enter a parse tree produced by KDParser#dateTime.
    def enterDateTime(self, ctx:KDParser.DateTimeContext):
        pass

    # Exit a parse tree produced by KDParser#dateTime.
    def exitDateTime(self, ctx:KDParser.DateTimeContext):
        pass



del KDParser