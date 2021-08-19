This archive contains the necessary files to help typesetting papers for the Computer Science and Information Systems (ComSIS) journal with LaTeX:

comsis2.cls         - ComSIS document class
ComSIS-typeinst.dvi - author instructions in dvi format
ComSIS-typeinst.pdf - author instructions in pdf format
ComSIS-typeinst.tex - author instructions LaTeX source
empty.tex           - minimal LaTeX document; please use this to start your paper
example.bib         - example BibTeX file (referred to by ComSIS-typeinst.tex and empty.tex)
figure.eps          - example figure in eps format (referred to by ComSIS-typeinst.tex)
figure.pdf          - example figure in pdf format (referred to by ComSIS-typeinst.tex)
readme.txt          - this file
secdot.sty          - style for section numbers with dots (required by comsis.cls)
splncs03.bst        - Springer LNCS BibTeX style (referred to by ComSIS-typeinst.tex and empty.tex)


========
History:
========

---------------------------
10-Nov-2017 Minor update
---------------------------

empty.tex
  - Added footnote after title for declaring extended version of paper

ComSIS-typeinst.*
  - Added footnote after title for declaring extended version of paper

---------------------------
14-Aug-2017 Minor update
---------------------------

comsis2.cls  v2.02 (14-Aug-2017)
  - \footnotesize is no longer equal to \small
  - changed formatting of first-page header to fit the URL-style DOI

empty.tex
  - URL-style DOI on first-page header

ComSIS-typeinst.*
  - URL-style DOI on first-page header

---------------------------
26-Jul-2017 Minor update
---------------------------

empty.tex
  - added line numbering through use of lineno package

ComSIS-typeinst.*
  - added line numbering through use of lineno package

---------------------------
17-Jul-2013 Major update
---------------------------

comsis2.cls  v2.0 (17-Jul-2013)
  - Renamed new version of the document class from comsis.cls to comsis2.cls, in order to emphasize the importance of using the updated version
  - changed default text font from Helvetica to Times
  - printing area widened to 125mm x 197mm
  - footers removed, page numbers moved to the headers, and volume/number information to the first page header
  - removed placeholder for UDC
  - changed email font in affiliations to roman

empty.tex
  - updated in accordance with the changes to the document class
  - removed commands for (optional) insertion of a blank page at the end

ComSIS-typeinst.*
  - updated in accordance with the changes to the document class

---------------------------
17-Aug-2012 Minor update
---------------------------

comsis.cls   v1.02 (17-Aug-2012)
  - fixed incompatibility with hyperref package

ComSIS-typeinst.*
  - updated several URLs

---------------------------
19-May-2010 Minor update
---------------------------

comsis.cls   v1.01 (14-May-2010)
  - short captions are now set flushleft instead of centered

empty.tex
  - deleted the dot after year in footer

---------------------------
25-Dec-2009 Initial release
---------------------------
comsis.cls   v1.0 (21-Dec-2009)
secdot.sty   v2 (July 2000)
splncs03.bst (01-Apr-2009)
