# -*- coding: utf-8 -*-
# Convert Korean Bible in Text to EPUB
# input text was downloaded from http://hiswork.tistory.com/77
__version__ = "1.0.1"

title = u"개역한글"
cover_file = u"cover_개역한글.jpeg"
srcenc = "cp949"
#title = u"개역개정4판"
#cover_file = u"cover_개역개정.jpeg"
#srcenc = "utf-8"

# config
title_ko = {
    "gen":u"창세기",
    "exo":u"출애굽기",
    "lev":u"레위기",
    "num":u"민수기",
    "deu":u"신명기",
    "jos":u"여호수아",
    "jdg":u"사사기",
    "rut":u"룻기",
    "1sa":u"사무엘상",
    "2sa":u"사무엘하",
    "1ki":u"열왕기상",
    "2ki":u"열왕기하",
    "1ch":u"역대상",
    "2ch":u"역대하",
    "ezr":u"에스라",
    "neh":u"느헤미아",
    "est":u"에스더",
    "job":u"욥기",
    "psa":u"시편",
    "pro":u"잠언",
    "ecc":u"전도서",
    "sol":u"아가",
    "isa":u"이사야",
    "jer":u"예레미아",
    "lam":u"예레미아애가",
    "eze":u"에스겔",
    "dan":u"다니엘",
    "hos":u"호세아",
    "joe":u"요엘",
    "amo":u"아모스",
    "oba":u"오바댜",
    "jon":u"요나",
    "mic":u"미가",
    "nah":u"나훔",
    "hab":u"하박국",
    "zep":u"스바냐",
    "hag":u"학개",
    "zec":u"스가랴",
    "mal":u"말라기",
    "mat":u"마태복음",
    "mar":u"마가복음",
    "luk":u"누가복음",
    "joh":u"요한복음",
    "act":u"사도행전",
    "rom":u"로마서",
    "1co":u"고린도전서",
    "2co":u"고린도후서",
    "gal":u"갈라디아서",
    "eph":u"에베소서",
    "phi":u"빌립보서",
    "col":u"골로새서",
    "1th":u"데살로니가전서",
    "2th":u"데살로니가후서",
    "1ti":u"디모데전서",
    "2ti":u"디모데후서",
    "tit":u"디도서",
    "phm":u"빌레몬서",
    "heb":u"히브리서",
    "jam":u"야고보서",
    "1pe":u"베드로전서",
    "2pe":u"베드로후서",
    "1jo":u"요한1서",
    "2jo":u"요한2서",
    "3jo":u"요한3서",
    "jud":u"유다서",
    "rev":u"요한계시록"
}

abbr_en2ko = {
    "gen":u"창",
    "exo":u"출",
    "lev":u"레",
    "num":u"민",
    "deu":u"신",
    "jos":u"수",
    "jdg":u"삿",
    "rut":u"룻",
    "1sa":u"삼상",
    "2sa":u"삼하",
    "1ki":u"왕상",
    "2ki":u"왕하",
    "1ch":u"대상",
    "2ch":u"대하",
    "ezr":u"스",
    "neh":u"느",
    "est":u"에",
    "job":u"욥",
    "psa":u"시",
    "pro":u"잠",
    "ecc":u"전",
    "sol":u"아",
    "isa":u"사",
    "jer":u"렘",
    "lam":u"애",
    "eze":u"겔",
    "dan":u"단",
    "hos":u"호",
    "joe":u"욜",
    "amo":u"욘",
    "oba":u"옵",
    "jon":u"욘",
    "mic":u"미",
    "nah":u"나",
    "hab":u"합",
    "zep":u"습",
    "hag":u"학",
    "zec":u"슥",
    "mal":u"말",
    "mat":u"마",
    "mar":u"막",
    "luk":u"눅",
    "joh":u"요",
    "act":u"행",
    "rom":u"롬",
    "1co":u"고전",
    "2co":u"고후",
    "gal":u"갈",
    "eph":u"엡",
    "phi":u"빌",
    "col":u"골",
    "1th":u"살전",
    "2th":u"살후",
    "1ti":u"딤전",
    "2ti":u"딤후",
    "tit":u"딛",
    "phm":u"몬",
    "heb":u"히",
    "jam":u"약",
    "1pe":u"벧전",
    "2pe":u"벧후",
    "1jo":u"요일",
    "2jo":u"요이",
    "3jo":u"요삼",
    "jud":u"유",
    "rev":u"계"
}

title_en = {
    "gen":"Genesis",
    "exo":"Exodus",
    "lev":"Leviticus",
    "num":"Numbers",
    "deu":"Deuteronomy",
    "jos":"Joshua",
    "jdg":"Judges",
    "rut":"Ruth",
    "1sa":"1 Samuel",
    "2sa":"2 Samuel",
    "1ki":"1 Kings",
    "2ki":"2 Kings",
    "1ch":"1 Chronicles",
    "2ch":"2 Chronicles",
    "ezr":"Ezra",
    "neh":"Nehemiah",
    "est":"Esther",
    "job":"Job",
    "psa":"Psalms",
    "pro":"Proverbs",
    "ecc":"Ecclesiastes",
    "sol":"Song of Solomon",
    "isa":"Isaiah",
    "jer":"Jeremiah",
    "lam":"Lamentations",
    "eze":"Ezekiel",
    "dan":"Daniel",
    "hos":"Hosea",
    "joe":"Joel",
    "amo":"Amos",
    "oba":"Obadiah",
    "jon":"Jonah",
    "mic":"Micah",
    "nah":"Nahum",
    "hab":"Habbakuk",
    "zep":"Zephaniah",
    "hag":"Haggai",
    "zec":"Zechariah",
    "mal":"Malachi",
    "mat":"Matthew",
    "mar":"Mark",
    "luk":"Luke",
    "joh":"John",
    "act":"Acts",
    "rom":"Romans",
    "1co":"1 Corinthians",
    "2co":"2 Corinthians",
    "gal":"Galatians",
    "eph":"Ephesians",
    "phi":"Philippians",
    "col":"Colossians",
    "1th":"1 Thessalonians",
    "2th":"2 Thessalonians",
    "1ti":"1 Timothy",
    "2ti":"2 Timothy",
    "tit":"Titus",
    "phm":"Philemon",
    "heb":"Hebrews",
    "jam":"James",
    "1pe":"1 Peter",
    "2pe":"2 Peter",
    "1jo":"1 John",
    "2jo":"2 John",
    "3jo":"3 John",
    "jud":"Jude",
    "rev":"Revelation"
}

#-------------------------------------------------
import os
import re

def bibtxt2xhtml(ifname, odir):
    global title_ko, title_en
    global abbr_en2ko
    book_ptn = re.compile("^ *(.{3}) 0*1:0*1\s",re.U|re.M)
    chap_ptn = re.compile("^ *.{3} 0*(\d*):0*1\s",re.U|re.M)
    verse_ptn = re.compile("^ *.{3} 0*(\d*):0*(\d*)\s+(.*)$",re.M)

    chap_mark = re.compile('<h2 class="chapter" id="ch(\d+)">')

    txt = open(ifname,'r').read().decode(srcenc)

    # (1) split large string to list
    bkidx = 0
    for txt2 in book_ptn.sub(r'@@@ \g<0>',txt).split('@@@ ')[1:]:
        bkidx += 1
        # (2) convert text to html
        bkabbr = book_ptn.search(txt2).group(1).lower()
        bkname = title_ko[bkabbr]
        bkabbr2 = abbr_en2ko[bkabbr]

        html = txt2
        html = chap_ptn.sub(ur'  <h2 class="chapter" id="ch\g<1>">\g<1></h2>\n  <table>\n\g<0>', html)
        html = verse_ptn.sub(ur'    <tr><td class="versenum">\g<2></td><td class="verse">\g<3></td></tr>', html)

        # (3) insert header after wrapping <h2> with <div>
        doc = []
        for line in html.splitlines():
            query = chap_mark.search(line)
            if query:
                chap_num = int(query.group(1))
                if doc:
                    doc.append('  </table>\n</div>\n')
                doc.append(u'<div>')
                doc.append(u'  <div class="header">{0:s} 제{1:d}장</div>'.format(bkname,chap_num))
            doc.append(line)
        doc.append('  </table>\n</div>')

        # (4) insert html prologue & epilogue
        doc.insert(0,
ur"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html lang="ko" xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
  <title>{0:s}</title>
  <link rel="stylesheet" href="../style/style.css" type="text/css"/>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</head>
<body>
<h1 id="bk{1:d}">{0:s}</h1>
""".format(bkname,bkidx))
        doc.append(
ur"""</body>
</html>""")

	html = '\n'.join(doc)

        # (5) insert html prologue & epilogue
        ofname = os.path.join(odir, "OEBPS", "text", "{0:02d}_{1:s}.xhtml".format(bkidx,bkabbr))
        open(ofname,'w').write( html.encode('utf-8') )
        print u"{0:s} is generated".format(ofname).encode('utf-8')

#-------------------------------------------------
def gen_bibtoc(odir):
    # (1) content.opf
    xml = open("content.opf").read().decode("utf-8").replace("@@@TITLE@@@", u"성경 ({0:s})".format(title) )
    open( os.path.join(odir, "OEBPS", "content.opf"),"w").write(xml.encode("utf-8"))
    print "content.opf is generated"
    # (2) toc.ncx
    xml = open("toc.ncx").read().decode("utf-8").replace("@@@TITLE@@@", u"성경 ({0:s})".format(title) )
    open( os.path.join(odir, "OEBPS", "toc.ncx"),"w").write(xml.encode("utf-8"))
    print "toc.ncx is generated"

#-------------------------------------------------
if __name__ == "__main__":
    import os
    import shutil
    work_dir = u'epub'
    ofname = u"성경_{0:s}.epub".format(title)
    # (1) convert txt to xhtml 
    bibtxt2xhtml(title+".txt",work_dir)
    # (2) content.opf+toc.ncx
    gen_bibtoc(work_dir)
    # (3) copy cover image
    shutil.copyfile(cover_file, os.path.join(work_dir, "OEBPS", "cover.jpeg"))
    # (4) create epub
    import epubpack
    epubpack.epubpack(work_dir, ofname)
    print u"DONE: {0:s} is generated".format(ofname).encode('utf-8')

# vim:sw=4:sts=4:et
