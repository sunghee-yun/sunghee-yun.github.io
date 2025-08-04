"""
User-defined commands defined by \\def, \\newcommand
"""

from latex_parser.latex_elements.latex_element_base import LaTeXElementBase
from latex_parser.tokenizers.tokens.command_token_base import CommandTokenBase


class UserDefinedCommandToken(CommandTokenBase):
    num_instances: int = 0

    COMMANDS_CALLED: set[str] = set()
    COMMANDS_IGNORED_WHEN_CONVERTED_TO_MARKDOWN: set[str] = set()
    NUM_ARGS: dict[str, tuple[bool, int, int]] = dict(
        algclosure=(True, 1, 0),
        alg=(True, 0, 0),
        algk=(True, 1, 0),
        algB=(True, 0, 0),
        algC=(True, 0, 0),
        algF=(True, 0, 0),
        algR=(True, 0, 0),
        algX=(True, 0, 0),
        algY=(True, 0, 0),
        bigpropercone=(True, 0, 0),
        collk=(True, 1, 0),
        classk=(True, 1, 0),
        cara=(True, 0, 0),
        complexes=(True, 0, 0),
        coll=(True, 0, 0),
        collB=(True, 0, 0),
        collF=(True, 0, 0),
        cemph=(True, 1, 0),
        compl=(True, 1, 0),
        eemph=(True, 1, 0),
        etc=(True, 0, 0),
        eg=(True, 0, 0),
        feq=(True, 0, 0),
        fie=(True, 0, 0),
        figref=(True, 1, 0),
        fobj=(True, 0, 0),
        iaoi=(True, 0, 0),
        ie=(True, 0, 0),
        integers=(True, 0, 0),
        lbdseqk=(True, 1, 0),
        minvolcoveringdualfcn=(True, 1, 0),
        notation=(True, 1, 0),
        ntsdir=(True, 0, 0),
        nuseqk=(True, 1, 0),
        openconv=(True, 0, 0),
        optfeasset=(True, 0, 0),
        posdefset=(True, 1, 0),
        possemidefset=(True, 1, 0),
        pprealk=(True, 1, 0),
        prealk=(True, 1, 0),
        tXJ=(True, 0, 0),
        tJ=(True, 0, 0),
        tS=(True, 0, 0),
        reals=(True, 0, 0),
        optdomain=(True, 0, 0),
        ppreals=(True, 0, 0),
        preals=(True, 0, 0),
        rationals=(True, 0, 0),
        seqk=(True, 2, 0),
        seqscr=(True, 3, 0),
        shrinkspacewithintheoremslike=(True, 0, 0),
        shrinkspacewithintheoremslikehalf=(True, 0, 0),
        shrinkspacewithintheoremsliket=(True, 0, 0),
        slen=(True, 0, 0),
        slenk=(True, 1, 0),
        symset=(True, 1, 0),
        theoremslikepostvspace=(True, 0, 0),
        wrt=(True, 0, 0),
        vfillt=(True, 0, 0),
        vfillfi=(True, 0, 0),
        xdomain=(True, 0, 0),
        xeq=(True, 0, 0),
        xie=(True, 0, 0),
        xobj=(True, 0, 0),
        indexedcol=(True, 1, 0),
        primefield=(True, 1, 0),
        ideal=(True, 1, 0),
        perm=(True, 1, 0),
        sdirk=(True, 1, 0),
        seq=(True, 1, 0),
        graystrikethrough=(True, 1, 0),
        define=(True, 1, 0),
        emph=(True, 1, 0),
        fact=(True, 1, 0),
        name=(True, 1, 0),
        closure=(True, 1, 0),
        interior=(True, 1, 0),
        subsetset=(True, 1, 0),
        plifting=(False, 1, 0),
        pliftingsmallest=(False, 1, 0),
        proofref=(False, 1, 0),
        commutativediagram=(False, 1, 0),
        foilref=(False, 1, 0),
        dualconef=(False, 1, 0),
        dualcones=(False, 1, 0),
        dualitygraphbase=(False, 1, 0),
        dualitygraphone=(False, 1, 0),
        dualitygraphtwo=(False, 1, 0),
        dualitygraphthree=(False, 1, 0),
        dualitygraphfour=(False, 1, 0),
        dualitygraphfive=(False, 1, 0),
        dualitygraphunitsize=(False, 1, 0),
        embeddingextensionf=(False, 1, 0),
        embeddingextensions=(False, 1, 0),
        embeddingextensiont=(False, 1, 0),
        asdf=(False, 1, 0),
        efgh=(False, 1, 0),
        ijkl=(False, 1, 0),
        butterfly=(False, 1, 0),
        entmax=(False, 1, 0),
        largecommutativediagram=(False, 8, 0),
        factorring=(False, 1, 0),
        fieldextensions=(False, 1, 0),
        galoisf=(False, 1, 0),
        galoiss=(False, 1, 0),
        idxfig=(False, 1, 0),
        idxtodo=(False, 1, 0),
        idxrevisit=(False, 1, 0),
        idximportant=(False, 1, 0),
        lssollineqs=(False, 1, 0),
        measu=(True, 2, 0),
        innerp=(True, 2, 0),
        pair=(True, 2, 0),
        bigsetl=(True, 2, 0),
        metrics=(True, 2, 0),
        topos=(True, 2, 0),
        mypsfrag=(True, 2, 0),
        set=(True, 2, 0),
        restrict=(True, 2, 0),
        frobmap=(False, 2, 0),
        finitefield=(False, 2, 0),
        refertocounterpart=(False, 2, 0),
        meast=(True, 3, 0),
        meas=(True, 3, 0),
        onelineoptprob=(False, 3, 0),
        xseqk=(True, 1, 0),
    )
    NUM_ARGS['"'] = (True, 1, 0)

    NO_ARG_STRING_MAP: dict[str, str] = dict(
        etc="<i>etc.</i>",
        ie="<i>i.e.</i>",
        eg="<i>e.g.</i>",
        iaoi="if and only if",
        wrt="with respect to",
        cara="Carathe&#776;odory",
        vfillt="",
        vfillfi="",
        shrinkspacewithintheoremslike="",
        shrinkspacewithintheoremslikehalf="",
        shrinkspacewithintheoremsliket="",
        theoremslikepostvspace="",
    )

    ENSUREMATH_MATH_COMMANDS: set[str] = {
        "alg",
        "algclosure",
        "algk",
        "algB",
        "algC",
        "algF",
        "algR",
        "algX",
        "algY",
        "bigpropercone",
        "bigsetl",
        "closure",
        "collk",
        "coll",
        "collB",
        "collF",
        "classk",
        "compl",
        "complexes",
        "feq",
        "fie",
        "fobj",
        "ideal",
        "integers",
        "interior",
        "innerp",
        "indexedcol",
        "lbdseqk",
        "measu",
        "metrics",
        "meas",
        "meast",
        "minvolcoveringdualfcn",
        "nuseqk",
        "ntsdir",
        "openconv",
        "optdomain",
        "optfeasset",
        "pair",
        "perm",
        "posdefset",
        "possemidefset",
        "pprealk",
        "ppreals",
        "prealk",
        "preals",
        "primefield",
        "reals",
        "rationals",
        "restrict",
        "sdirk",
        "seq",
        "seqscr",
        "seqk",
        "set",
        "slen",
        "slenk",
        "subsetset",
        "symset",
        "finitefield",
        "frobmap",
        "topos",
        "tJ",
        "tS",
        "tXJ",
        "xdomain",
        "xeq",
        "xie",
        "xobj",
        "xseqk",
    }

    assert len(set(NO_ARG_STRING_MAP).intersection(ENSUREMATH_MATH_COMMANDS)) == 0, set(
        NO_ARG_STRING_MAP
    ).intersection(ENSUREMATH_MATH_COMMANDS)

    def __init__(self, string: str, line_num: int) -> None:
        super().__init__(string, line_num)
        UserDefinedCommandToken.num_instances += 1

    def _latex_command_to_markdown_str(
        self, arg_list: list[str], opt_arg_list: list[str], max_num_opt_arg_list: int
    ) -> str:
        num_arg_list: int = len(arg_list)

        if self.string[1:] in self.ENSUREMATH_MATH_COMMANDS:
            arg_str: str = "".join(["{" + arg + "}" for arg in arg_list])
            opt_arg_str: str = "".join([f"[{opt_arg}]" for opt_arg in opt_arg_list])
            return f"${self.string}{opt_arg_str}{arg_str}$"

        if num_arg_list == 0 and max_num_opt_arg_list == 0:
            return self.NO_ARG_STRING_MAP[self.string[1:]]

        if num_arg_list == 1 and max_num_opt_arg_list == 0:
            arg: str = LaTeXElementBase.process_markdown_string(arg_list[0])

            if self.string == r"\figref":
                return "the figure"

            if self.string == r"\graystrikethrough":
                return f'<span style="color: rgb(60,60,60);"><s>{arg}</s></span>'

            if self.string == r"\define":
                return f'<span class="define">{arg}</span>'

            if self.string == r"\emph":
                return f"<i>{arg}</i>"

            if self.string == r"\cemph":
                return f'<span class="emph">{arg}</span>'

            if self.string == r"\eemph":
                return f'<span class="eemph">{arg}</span>'

            if self.string == r"\fact":
                return f'<span class="fact-font">{arg}</span>'

            if self.string == r"\name":
                return f'<span class="name-font">{arg}</span>'

            if self.string == r"\notation":
                return f'<span class="notation">{arg}</span>'

            if self.string == '\\"':
                assert len(arg.strip()) == 1, arg.strip()
                return f"{arg.strip()}&#776;"

        if num_arg_list == 2 and max_num_opt_arg_list == 0:
            if self.string == "\\mypsfrag":
                return ""

        raise NotImplementedError(self.string)
