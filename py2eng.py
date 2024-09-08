#!/usr/bin/env python3
# -*- coding: utf-8 -*
from pypinyin import pinyin, Style
import unicodedata

initial_rule = {
	"b" : "b",
	"p" : "p",
	"m" : "m",
	"f" : "f",
	"d" : "d",
	"t" : "t",
	"n" : "n",
	"l" : "l",
	"g" : "g",
	"k" : "k",
	"h" : "h",
	"j" : "j",
	"q" : "ch",
	"x" : "sh",
	"zh" : "j",
	"ch" : "ch",
	"sh" : "sh",
	"r" : "r",
	"z" : "z",
	"c" : "ts",
	"s" : "s",
	"y" : "y",
	"w" : "w"
}

finals_rule = {
	"" : "",
	"a" : "ah",
	"o" : "augh",
	"e" : "eh",
	"i" : "ea",
	"u" : "oo",
	"v" : "ew",
	"ai" : "igh",
	"ao" : "ao",
	"an" : "an",
	"ang" : "un",
	"ou" : "oh",
	"ong" : "ohn",
	"ei" : "ay",
	"er" : "err",
	"en" : "en",
	"eng" : "ehn",
	"ia" : "ee-ah",
	"iao" : "ee-ow",
	"ian" : "ee-ang",
	"ie" : "ear",
	"iu" : "yu",
	"in" : "ean",
	"ing" : "ing",
	"iang" : "ee-ahn",
	"iong" : "yong",
	"ua" : "oo-ah",
	"uai" : "oo-eye",
	"uan" : "oo-an",
	"uang" : "oo-ahn",
	"ve" : "wey",
	"ue" : "wey",
	"ui" : "ui",
	"un" : "oon",
	"vn" : "oon",
	"uo" : "oo-augh"
}

special_rule = {
	"": {"": "", "ai": "eye", "e": "ehh", "o": "aw", "ei": "eigh"},
	"b": {"b": "b", "o": "aw", "ai": "ye", "ie": "ia", "iao": "iao", "ing": "ean"},
	"p": {"p": "p", "o": "aw", "ai": "ie", "ao": "ao", "ang": "ahn", "in": "in", "ie": "eer"},
	"m": {"m": "m", "o": "aw", "i": "e", "ing": "ean", "ai": "y", "ao": "ao", "ou": "ow", "iao": "eow", "iu": "u"},
	"f": {"f": "f", "a": "aah", "o": "aw", "ang": "un", "iao": "iao"},
	"d": {"d": "d", "e": "e", "ui": "uei", "ou": "ough", "ang": "own", "ong": "ome", "ai": "ie"},
	"t": {"t": "t", "a": "a", "e": "ehh", "ai": "hai", "ao": "au", "ou": "ow", "ong": "one", "ei": "ay", "ie": "ier", "iao": "iao"},
	"n": {"n": "n", "e": "eh", "ao": "ow", "ao": "ow", "ou": "o", "iu": "eo", "ie": "ia", "iao": "eow", "ian": "ea-ang", "iang": "ea-ahn", "uan": "uan", "ue": "ew-yeh", "ve": "ew-yeh"},
	"l": {"l": "l", "e": "uh", "o": "oh", "i": "ee", "iao": "iao", "ie": "eah", "ou": "ow", "ong": "one", "eng": "eng", "iu": "eo", "uan": "uahn", "ue": "yer", "ve": "yer"},
	"g": {"g": "g", "e": "uh", "ai": "uy", "ao": "ow", "an": "ang", "ang": "un", "ou": "o", "ong": "ong", "en": "ehn", "eng": "hen", "ua": "ua-ah", "uai": "ua-eye", "uan": "ua-ang", "uang": "uang", "ong": "ome", "ui": "wei", "un": "wen", "uo": "uo"},
	"k": {"k": "k", "ai": "ye", "ang": "han", "ou": "ho", "ong": "ong", "ei": "", "eng": "ern", "ua": "ua-ah", "uai": "ua-eye", "uan": "wan", "uang": "wang", "ui": "wei", "un": "oon"},
	"h": {"h": "h", "a": "a", "e": "er", "ao": "ow", "an": "ang", "ang": "un", "ou": "o", "ong": "one", "ei": "ey", "en": "en", "eng": "eng", "uan": "oo-ang", "uang": "oo-ahn", "ui": "oo-ei"},
	"j": {"j": "j", "an": "ang", "i": "ee", "u": "ew", "v": "ew", "iong": "yone", "iu": "ee-oh", "iang": "iang", "uan": "uon", "van": "uon", "ue": "u-ei", "ve": "u-ei"},
	"q": {"q": "ch", "i": "ee", "u": "ew", "v": "ew", "iong": "iown", "ie": "ia", "iu": "ee-oh", "uan": "uon", "van": "uon", "ue": "u-eh", "ve": "u-eh", "un": "uen"},
	"x": {"x": "sh", "i": "e", "u": "oe", "v": "ew", "iong": "iown", "ia": "e-ah", "ie": "ia", "iu": "eo", "uan": "uahn", "van": "uahn", "ue": "u-eh", "ve": "u-eh", "un": "oong"},
	"zh": {"zh": "j", "e": "ehh", "i": "ir", "u": "ew", "ai": "ye", "ao": "ao", "ou": "o", "ang": "ohn", "ei": "ay", "ong": "one"},
	"ch": {"ch": "ch", "e": "ehh", "i": "urr", "u": "ew", "ai": "ai", "ao": "ao", "ou": "o", "an": "an", "ang": "ohn", "ong": "one", "en": "en", "eng": "ehn"},
	"sh": {"sh": "sh", "e": "ehh", "a": "a", "i": "ur", "u": "oe", "uo": "ol", "ai": "y", "ei": "eh", "ao": "all", "ou": "ow", "an": "an", "ang": "ang", "en": "en", "eng": "eng"},
	"r": {"r": "r", "i": "er", "ou": "ow", "ui": "ay", "uo": "aw", "ong": "one"},
	"z": {"z": "z", "i": "ur", "u": "ew", "ai": "ye", "ao": "ao", "ou": "o", "ang": "ohn", "ei": "ay", "ong": "one"},
	"c": {"c": "ts", "i": "ur", "u": "ew", "ai": "ai", "ao": "ao", "ou": "o", "an": "an", "ang": "ahn", "ong": "own", "en": "en", "eng": "ehn"},
	"s": {"s": "s", "a": "a", "i": "ir", "e": "ehh", "u": "oo", "ong": "one", "ai": "y", "ei": "eh", "ao": "all", "ou": "ow", "an": "an", "ang": "ang", "en": "en", "eng": "eng"},
	"y": {"y": "y", "o": "aw", "i": "ee", "an": "an", "ang": "oung", "ou": "ou", "uan": "uen", "ue": "u-eh", "ong": "one"},
	"w": {"w": "w", "ai": "hy", "en": "hen", "ei": "ay"}
}

replacements = {
	"ni": "knee",
	"nian": "knee-ang",
	"niang": "knee-ahn",
	"kao": "cow",
	"kan": "can",
	"kuo": "quo",
	"hu": "who",
	"chui": "tree",
	"shua": "schwa",
	"xiao": "xiau",
	"kong": "cone",
	"nong": "known",
	"xue": "shuehh",
	"yu": "ew",
	"yv": "ew",
	"yin": "inn",
	"ying": "ing",
	"wang": "one",
	"cao": "tzow",
	"qiao": "qiau"
}

wordrep = {
	"wo he": "warhead",
	"sha bi": "shabby"
}

debug = [
	"八波逼不白包班帮杯奔崩标边憋斌冰𰻝",
	"啪泼批噗拍抛潘乓呸喷嘭漂偏瞥拼乒",
	"妈摸么米木买猫慢忙某没门懵喵面咩缪民名",
	"发佛夫翻方否飞分封",
	"搭得低督呆刀担当都东嘚扥灯嗲刁颠爹丢丁端堆吨多",
	"它特踢突胎涛摊汤偷通忒疼挑天贴听湍推吞脱",
	"拿呢你奴女乃孬男囊耨浓内嫩能鸟年娘捏牛您宁暖虐黁挪",
	"拉咯乐里撸绿来捞兰狼楼龙雷楞俩聊连良列留林玲卵略论罗",
	"嘎哥姑该高甘刚勾工给跟羹瓜乖关光龟滚锅",
	"卡科哭开尻堪康抠空剋肯坑夸块宽框亏昆阔",
	"哈呵呼嗨蒿憨夯猴轰黑很哼花怀环荒灰婚豁",
	"鸡局家胶间皆鸠金晶姜囧捐撅军",
	"七区掐敲千切秋亲氢枪琼圈缺群",
	"唏嘘瞎骁先歇修新星箱凶宣靴勋",
	"扎蛰蜘蛛摘招沾张周中这真争抓拽专装追谆捉",
	"叉车吃出拆超掺昌抽冲陈蛏欻揣穿窗吹春戳",
	"杀奢师叔筛烧山伤收伸声刷摔栓双水顺说",
	"热日如绕然瓤肉容人扔挼软瑞润弱",
	"砸则兹租栽遭簪脏邹宗贼怎增钻最尊做",
	"擦测呲粗猜操餐苍凑从岑层窜崔村搓",
	"仨色丝苏塞骚三桑搜松森僧酸虽孙梭",
	"压哟衣淤腰烟央优佣音英冤约晕",
	"挖窝乌歪弯汪危闻翁"
]

def pinyin2eng(pinyin3):
	po = pinyin3.replace("ü", "v")
	if po[-1] in "012345":
		tone = int(po[-1])
		po = po[:-1]
	else:
		tone = 0
	try:
		return replacements[po]
	except KeyError:
		pass
	if po in finals_rule:
		try:
			return special_rule[""][po]
		except KeyError:
			return finals_rule[po]
	try:
		spec_dict = special_rule[po[:2]]
		len_ini = 2
	except KeyError:
		try:
			spec_dict = special_rule[po[:1]]
			len_ini = 1
		except KeyError:
			spec_dict = {}
			len_ini = 0
	try:
		pron_ini = spec_dict[po[:len_ini]]
		pron_fin = spec_dict[po[len_ini:]]
		return f'{pron_ini}{pron_fin}'
	except KeyError:
		pass
	try:
		pron_ini = initial_rule[po[:2]]
		len_ini = 2
	except KeyError:
		try:
			pron_ini = initial_rule[po[:1]]
			len_ini = 1
		except KeyError:
			pron_ini = ""
			len_ini = 0
	try:
		pron_fin = finals_rule[po[len_ini:]]
	except KeyError:
		return pinyin3
	return "%s%s" % (pron_ini, pron_fin)

def sentence2eng(sentence, return_pinyin = False):
	def check_pinyin_identical(l1, l2):
		if len(l1) != len(l2): return False
		for i in range(len(l1)):
			p1 = l1[i]
			p2 = l2[i]
			if p1[-1].isnumeric(): p1 = p1[:-1]
			if p2[-1].isnumeric(): p2 = p2[:-1]
			if p1 != p2: return False
		return True
	if sentence == 'debug': sentence = ", ".join(debug)
	sentence = sentence.replace("<", "《").replace(">", "》")
	sentence = unicodedata.normalize('NFKC', sentence)
	spinyin = [p[0] for p in pinyin(sentence, style=Style.TONE3, neutral_tone_with_five=True, errors=lambda x: '!' + x)]
	prep = []
	i = 0
	while i < len(spinyin):
		replaced = False
		for combination, replacement in wordrep.items():
			cbl = combination.split(' ')
			if check_pinyin_identical(cbl, spinyin[i:i + len(cbl)]):
				prep += [replacement]
				i += len(cbl)
				replaced = True
				break
		if not replaced:
			prep += [spinyin[i]]
			i += 1
	tosay = [ pinyin2eng(p) if p[0] != '!' else p[1:] for p in prep ]
	finalsay = " ".join(tosay).replace("？", "?").replace("！", "!").replace("，", ",").replace("、", ",").replace("。", ".")
	while "  " in finalsay: finalsay = finalsay.replace("  ", " ")
	if return_pinyin:
		return finalsay, " ".join([ p if p[0] != '!' else p[1:] for p in spinyin ])
	else:
		return finalsay

def usage():
	print("用法：py2eng <输入一些包含汉字的中文句子>")
	print("基于拼音，使用一些英文单词发音组合来尝试生成读起来像中文句子的英文。")
	exit()

if __name__ == '__main__':
	import sys
	if len(sys.argv) <= 1:
		usage()
	print(sentence2eng(" ".join(sys.argv[1:])))
