from docx import Document
from docx.shared import Pt, Inches, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# ── Page margins ──────────────────────────────────────────────────────────────
for section in doc.sections:
    section.top_margin    = Cm(2)
    section.bottom_margin = Cm(2)
    section.left_margin   = Cm(2.5)
    section.right_margin  = Cm(2)

# ── Helpers ───────────────────────────────────────────────────────────────────
def set_cell_bg(cell, hex_color):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd  = OxmlElement('w:shd')
    shd.set(qn('w:val'),   'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'),  hex_color)
    tcPr.append(shd)

def set_cell_border(cell, **kwargs):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for edge in ('top','left','bottom','right'):
        tag = OxmlElement(f'w:{edge}')
        tag.set(qn('w:val'),   kwargs.get('val',   'single'))
        tag.set(qn('w:sz'),    kwargs.get('sz',    '4'))
        tag.set(qn('w:space'), '0')
        tag.set(qn('w:color'), kwargs.get('color', '000000'))
        tcBorders.append(tag)
    tcPr.append(tcBorders)

def para_fmt(para, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=0):
    para.alignment = align
    para.paragraph_format.space_before = Pt(space_before)
    para.paragraph_format.space_after  = Pt(space_after)

def add_run(para, text, bold=False, italic=False, size=11, font='Times New Roman',
            color=None):
    run = para.add_run(text)
    run.bold   = bold
    run.italic = italic
    run.font.name = font
    run.font.size = Pt(size)
    if color:
        run.font.color.rgb = RGBColor(*color)
    return run

def add_code_block(doc, code_text):
    """Courier New, 12pt paragraph block — no background."""
    p = doc.add_paragraph()
    para_fmt(p, space_before=2, space_after=2)
    run = p.add_run(code_text)
    run.font.name = 'Courier New'
    run.font.size = Pt(12)
    return p

def add_output_block(doc, output_text):
    """Courier New, 12pt output block — no background."""
    p = doc.add_paragraph()
    para_fmt(p, space_before=2, space_after=6)
    run = p.add_run(output_text)
    run.font.name = 'Courier New'
    run.font.size = Pt(12)
    return p

def section_heading(doc, text, size=13):
    p = doc.add_paragraph()
    para_fmt(p, space_before=6, space_after=2)
    add_run(p, text, bold=True, size=size)
    return p

def body_text(doc, text, bold=False, size=11):
    p = doc.add_paragraph()
    para_fmt(p, space_before=2, space_after=2)
    add_run(p, text, bold=bold, size=size)
    return p

# ── College header (centered) ─────────────────────────────────────────────────
def college_header(doc):
    for line, sz, bold in [
        ("SUBBALAKSHMI LAKSHMIPATHY COLLEGE OF SCIENCE", 14, True),
        ("Affiliated to Madurai Kamaraj University", 11, False),
        ("Re-accredited with 'A+' Status by NAAC", 11, False),
        ("TVR NAGAR, ARUPPUKOTTAI ROAD, MADURAI-625022", 11, False),
        ("", 6, False),
        ("DEPARTMENT OF COMPUTER SCIENCE", 12, True),
        ("", 6, False),
        ("NoSQL Laboratory – 24DCS514 P", 12, True),
        ("DEPARTMENT OF COMPUTER SCIENCE", 11, False),
        ("(Data Science and Analytics)", 11, False),
        ("", 6, False),
        ("RECORD NOTE BOOK  2026 – 2027", 13, True),
    ]:
        p = doc.add_paragraph()
        para_fmt(p, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=2)
        add_run(p, line, bold=bold, size=sz)

# ── Certificate page ──────────────────────────────────────────────────────────
def certificate_page(doc):
    doc.add_page_break()
    college_header(doc)

    doc.add_paragraph()
    p = doc.add_paragraph()
    para_fmt(p, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10)
    add_run(p, "CERTIFICATE", bold=True, size=14)

    doc.add_paragraph()
    p = doc.add_paragraph()
    para_fmt(p, space_before=6, space_after=6)
    add_run(p,
        "This is to certify that ________________________ of III B.Sc. Computer Science (DSA) "
        "has successfully completed his/her Practicals in NoSQL Laboratory from the college "
        "during the year 2026-2027 and submitted for practical examinations held on ________________.",
        size=11)

    doc.add_paragraph()
    doc.add_paragraph()
    # Signature table
    tbl = doc.add_table(rows=2, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    labels = [["Faculty In-charge", "HOD"], ["Internal Examiner", "External Examiner"]]
    for r, row in enumerate(tbl.rows):
        for c, cell in enumerate(row.cells):
            cell.text = labels[r][c]
            cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in cell.paragraphs[0].runs:
                run.font.size = Pt(11)
                run.font.name = 'Times New Roman'

# ── Index table ───────────────────────────────────────────────────────────────
INDEX_DATA = [
    ("1",  "22/06/2026", "DATABASE OPERATIONS IN MONGODB"),
    ("2",  "29/06/2026", "COLLECTION OPERATIONS IN MONGODB"),
    ("3",  "06/07/2026", "CRUD OPERATIONS IN MONGODB"),
    ("4",  "13/07/2026", "AGGREGATION PIPELINE IN MONGODB"),
    ("5",  "20/07/2026", "ADVANCED AGGREGATION IN MONGODB"),
    ("6",  "27/07/2026", "ARRAY OPERATORS IN MONGODB"),
    ("7A", "03/08/2026", "INDEXING – BOOKS COLLECTION"),
    ("7B", "03/08/2026", "INDEXING – PRODUCTS COLLECTION"),
    ("8",  "10/08/2026", "SPATIAL INDEXING IN MONGODB"),
]

def index_page(doc):
    doc.add_page_break()
    p = doc.add_paragraph()
    para_fmt(p, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=6)
    add_run(p, "INDEX", bold=True, size=14)

    tbl = doc.add_table(rows=1, cols=5)
    tbl.style = 'Table Grid'
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Header row
    hdr = tbl.rows[0].cells
    for cell, txt in zip(hdr, ["S.NO", "DATE", "TOPIC", "PAGE NO", "SIGN"]):
        cell.text = txt
        cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in cell.paragraphs[0].runs:
            run.bold      = True
            run.font.size = Pt(10)
            run.font.name = 'Times New Roman'

    # Set column widths
    widths = [Cm(1.5), Cm(3), Cm(8), Cm(2), Cm(2)]
    for row in tbl.rows:
        for idx, cell in enumerate(row.cells):
            cell.width = widths[idx]

    # Data rows
    for sno, date, topic in INDEX_DATA:
        row = tbl.add_row()
        for cell, txt in zip(row.cells, [sno, date, topic, "", ""]):
            cell.text = txt
            cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in cell.paragraphs[0].runs:
                run.font.size = Pt(10)
                run.font.name = 'Times New Roman'
        # Set widths again for new rows
        for idx, cell in enumerate(row.cells):
            cell.width = widths[idx]

# ── Ex header table (2-column, like the DSA template) ────────────────────────
def ex_header(doc, ex_no, title, date):
    doc.add_paragraph()
    tbl = doc.add_table(rows=1, cols=2)
    tbl.style = 'Table Grid'
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER

    left  = tbl.rows[0].cells[0]
    right = tbl.rows[0].cells[1]

    left.width  = Cm(3)
    right.width = Cm(13)

    # Left cell: EX NO + date
    lp1 = left.paragraphs[0]
    lp1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_run(lp1, f"EX. NO. : {ex_no}", bold=True, size=12)
    lp2 = left.add_paragraph()
    lp2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_run(lp2, date, bold=False, size=12)

    # Right cell: title
    rp = right.paragraphs[0]
    rp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_run(rp, title, bold=True, size=14)

    return tbl

# ── AIM block ─────────────────────────────────────────────────────────────────
def aim_block(doc, aim_text):
    p = doc.add_paragraph()
    para_fmt(p, space_before=6, space_after=2)
    add_run(p, "AIM", bold=True, size=11)
    p2 = doc.add_paragraph()
    para_fmt(p2, space_before=0, space_after=4)
    add_run(p2, aim_text, size=11)

# ── RESULT block ──────────────────────────────────────────────────────────────
def result_block(doc, result_text):
    p = doc.add_paragraph()
    para_fmt(p, space_before=8, space_after=2)
    add_run(p, "RESULT", bold=True, size=12)
    p2 = doc.add_paragraph()
    para_fmt(p2, space_before=0, space_after=4)
    add_run(p2, result_text, size=12)

# ══════════════════════════════════════════════════════════════════════════════
#  EXERCISE CONTENT
# ══════════════════════════════════════════════════════════════════════════════

# ── EX 1 ──────────────────────────────────────────────────────────────────────
def ex1(doc):
    doc.add_page_break()
    ex_header(doc, "1", "DATABASE OPERATIONS IN MONGODB", "22/06/2026")
    aim_block(doc, "To create, switch, list, and delete databases in MongoDB.")

    section_heading(doc, "1. Create / Switch Database")
    body_text(doc, "Creates a new database named studentDB if it doesn't exist, or switches to it if it already does.")
    add_code_block(doc, "use studentDB")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "switched to db studentDB")

    section_heading(doc, "2. Insert First Document (Persist the Database)")
    body_text(doc, "MongoDB only creates a database on disk when the first document is inserted.")
    add_code_block(doc,
        'db.students.insertOne({\n'
        '    name: "John",\n'
        '    age: 20\n'
        '})')
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        '{\n'
        "  acknowledged: true,\n"
        "  insertedId: ObjectId('6ab1234567890abcdef12345')\n"
        '}')

    section_heading(doc, "3. Show Current Database")
    add_code_block(doc, "db")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "studentDB")

    section_heading(doc, "4. List All Databases")
    add_code_block(doc, "show dbs")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "admin      40.00 KiB\n"
        "config     60.00 KiB\n"
        "local      40.00 KiB\n"
        "studentDB   8.00 KiB")

    section_heading(doc, "5. Show Collections")
    add_code_block(doc, "show collections")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "students")

    section_heading(doc, "6. Delete Database")
    add_code_block(doc, "use studentDB\ndb.dropDatabase()")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "{ ok: 1, dropped: 'studentDB' }")

    result_block(doc,
        "Thus, a MongoDB database was created, verified, and deleted successfully using "
        "MongoDB shell commands.")

# ── EX 2 ──────────────────────────────────────────────────────────────────────
def ex2(doc):
    doc.add_page_break()
    ex_header(doc, "2", "COLLECTION OPERATIONS IN MONGODB", "29/06/2026")
    aim_block(doc, "To create, view, and delete collections in a MongoDB database.")

    section_heading(doc, "1. Create Database and Collection")
    body_text(doc, "Switches to CollegeDB and explicitly creates an empty collection called students.")
    add_code_block(doc, 'use CollegeDB\ndb.createCollection("students")')
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "switched to db CollegeDB\n{ ok: 1 }")

    section_heading(doc, "2. Auto-Create Collection on Insert")
    body_text(doc, "MongoDB automatically creates a collection when you insert into one that doesn't exist.")
    add_code_block(doc,
        'db.faculty.insertOne({\n'
        '    name: "Anitha",\n'
        '    department: "CSE"\n'
        '})')
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        '{\n'
        "  acknowledged: true,\n"
        "  insertedId: ObjectId('6ab1234567890abcdef12346')\n"
        '}')

    section_heading(doc, "3. View All Collections")
    add_code_block(doc, "show collections")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "faculty\nstudents")

    add_code_block(doc, "db.getCollectionNames()")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "[ 'faculty', 'students' ]")

    section_heading(doc, "4. Drop a Collection")
    add_code_block(doc, "db.students.drop()")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "true")

    result_block(doc,
        "Thus, collections were created explicitly and implicitly, listed, and deleted "
        "successfully in MongoDB.")

# ── EX 3 ──────────────────────────────────────────────────────────────────────
def ex3(doc):
    doc.add_page_break()
    ex_header(doc, "3", "CRUD OPERATIONS IN MONGODB", "06/07/2026")
    aim_block(doc, "To perform Create, Read, Update, and Delete (CRUD) operations on a MongoDB collection.")

    section_heading(doc, "1. Create – insertOne")
    add_code_block(doc,
        'db.students.insertOne({\n'
        '    rollNo: 101,\n'
        '    name: "Arun",\n'
        '    department: "CSE",\n'
        '    marks: 85\n'
        '})')
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        '{\n'
        "  acknowledged: true,\n"
        "  insertedId: ObjectId('6ab1234567890abcdef12347')\n"
        '}')

    section_heading(doc, "2. Create – insertMany")
    add_code_block(doc,
        'db.students.insertMany([\n'
        '    { rollNo: 102, name: "Priya", marks: 90 },\n'
        '    { rollNo: 103, name: "Rahul", marks: 88 }\n'
        '])')
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        '{\n'
        "  acknowledged: true,\n"
        "  insertedIds: {\n"
        "    '0': ObjectId('6ab1234567890abcdef12348'),\n"
        "    '1': ObjectId('6ab1234567890abcdef12349')\n"
        "  }\n"
        '}')

    section_heading(doc, "3. Read – find()")
    add_code_block(doc, "db.students.find()")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ _id: ObjectId('...'), rollNo: 101, name: 'Arun', department: 'CSE', marks: 85 }\n"
        "{ _id: ObjectId('...'), rollNo: 102, name: 'Priya', marks: 90 }\n"
        "{ _id: ObjectId('...'), rollNo: 103, name: 'Rahul', marks: 88 }")

    section_heading(doc, "4. Read – findOne()")
    add_code_block(doc, "db.students.findOne({ rollNo: 101 })")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ _id: ObjectId('...'), rollNo: 101, name: 'Arun', department: 'CSE', marks: 85 }")

    section_heading(doc, "5. Read – find() with filter ($gt)")
    add_code_block(doc, "db.students.find({ marks: { $gt: 85 } })")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ _id: ObjectId('...'), rollNo: 102, name: 'Priya', marks: 90 }\n"
        "{ _id: ObjectId('...'), rollNo: 103, name: 'Rahul', marks: 88 }")

    section_heading(doc, "6. Update – updateOne()")
    add_code_block(doc,
        "db.students.updateOne(\n"
        "    { rollNo: 101 },\n"
        "    { $set: { marks: 92 } }\n"
        ")")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ acknowledged: true, matchedCount: 1, modifiedCount: 1, upsertedCount: 0 }")

    section_heading(doc, "7. Delete – deleteOne()")
    add_code_block(doc, "db.students.deleteOne({ rollNo: 101 })")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "{ acknowledged: true, deletedCount: 1 }")

    result_block(doc,
        "Thus, CRUD operations — insertOne, insertMany, find, findOne, updateOne, and deleteOne "
        "— were performed successfully on a MongoDB collection.")

# ── EX 4 ──────────────────────────────────────────────────────────────────────
def ex4(doc):
    doc.add_page_break()
    ex_header(doc, "4", "AGGREGATION PIPELINE IN MONGODB", "13/07/2026")
    aim_block(doc, "To demonstrate aggregation pipeline stages: $match, $group, $project, $sort, and $limit in MongoDB.")

    section_heading(doc, "Database & Collection Setup")
    add_code_block(doc, "use studentDB\ndb.createCollection(\"students\")")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "switched to db studentDB\n{ ok: 1 }")

    section_heading(doc, "Insert Sample Data (8 students)")
    add_code_block(doc,
        'db.students.insertMany([\n'
        '    { name: "Arun",  department: "CSE",  marks: 85 },\n'
        '    { name: "Priya", department: "CSE",  marks: 92 },\n'
        '    { name: "Rahul", department: "CSE",  marks: 76 },\n'
        '    { name: "Divya", department: "ECE",  marks: 88 },\n'
        '    { name: "Karan", department: "ECE",  marks: 73 },\n'
        '    { name: "Sneha", department: "MECH", marks: 91 },\n'
        '    { name: "Arjun", department: "MECH", marks: 69 },\n'
        '    { name: "Meena", department: "MECH", marks: 84 }\n'
        '])')
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "{ acknowledged: true, insertedIds: { '0': ObjectId('...'), ... } }")

    section_heading(doc, "1. $match  – Filter Students with marks > 80")
    add_code_block(doc, "db.students.aggregate([\n    { $match: { marks: { $gt: 80 } } }\n])")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ name: 'Arun',  department: 'CSE',  marks: 85 }\n"
        "{ name: 'Priya', department: 'CSE',  marks: 92 }\n"
        "{ name: 'Divya', department: 'ECE',  marks: 88 }\n"
        "{ name: 'Sneha', department: 'MECH', marks: 91 }\n"
        "{ name: 'Meena', department: 'MECH', marks: 84 }")

    section_heading(doc, "2. $group  – Average Marks per Department")
    add_code_block(doc,
        "db.students.aggregate([\n"
        "    {\n"
        "        $group: {\n"
        '            _id: "$department",\n'
        '            averageMarks: { $avg: "$marks" }\n'
        "        }\n"
        "    }\n"
        "])")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ _id: 'CSE',  averageMarks: 84.33 }\n"
        "{ _id: 'ECE',  averageMarks: 80.5  }\n"
        "{ _id: 'MECH', averageMarks: 81.33 }")

    section_heading(doc, "3. $project – Show Only name and marks")
    add_code_block(doc,
        "db.students.aggregate([\n"
        "    { $project: { _id: 0, name: 1, marks: 1 } }\n"
        "])")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ name: 'Arun',  marks: 85 }\n"
        "{ name: 'Priya', marks: 92 }\n"
        "{ name: 'Rahul', marks: 76 }\n"
        "{ name: 'Divya', marks: 88 }\n"
        "{ name: 'Karan', marks: 73 }\n"
        "{ name: 'Sneha', marks: 91 }\n"
        "{ name: 'Arjun', marks: 69 }\n"
        "{ name: 'Meena', marks: 84 }")

    section_heading(doc, "4. $sort  – Sort by marks Descending")
    add_code_block(doc, "db.students.aggregate([\n    { $sort: { marks: -1 } }\n])")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ name: 'Priya', department: 'CSE',  marks: 92 }\n"
        "{ name: 'Sneha', department: 'MECH', marks: 91 }\n"
        "{ name: 'Divya', department: 'ECE',  marks: 88 }\n"
        "{ name: 'Arun',  department: 'CSE',  marks: 85 }\n"
        "{ name: 'Meena', department: 'MECH', marks: 84 }\n"
        "...")

    section_heading(doc, "5. $limit  – Top 3 Students")
    add_code_block(doc,
        "db.students.aggregate([\n"
        "    { $sort:  { marks: -1 } },\n"
        "    { $limit: 3 }\n"
        "])")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ name: 'Priya', department: 'CSE',  marks: 92 }\n"
        "{ name: 'Sneha', department: 'MECH', marks: 91 }\n"
        "{ name: 'Divya', department: 'ECE',  marks: 88 }")

    result_block(doc,
        "Thus, the aggregation pipeline stages $match, $group, $project, $sort, and $limit "
        "were demonstrated successfully on the students collection.")

# ── EX 5 ──────────────────────────────────────────────────────────────────────
def ex5(doc):
    doc.add_page_break()
    ex_header(doc, "5", "ADVANCED AGGREGATION IN MONGODB", "20/07/2026")
    aim_block(doc, "To demonstrate advanced aggregation operations: $group/$avg, $lookup (join), $unwind, and a combined $lookup + $unwind pipeline in MongoDB.")

    section_heading(doc, "Setup – Students Collection")
    add_code_block(doc,
        "use studentDB\n"
        "db.students.insertMany([\n"
        "    { rollNo: 101, name: \"Arun\",  department: \"CSE\", marks: 85,\n"
        "      courseId: 201, subjects: [\"DBMS\", \"Python\"] },\n"
        "    { rollNo: 102, name: \"Priya\", department: \"ECE\", marks: 90,\n"
        "      courseId: 202, subjects: [\"C Programming\", \"Signals\"] }\n"
        "])")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ acknowledged: true, insertedIds: { '0': ObjectId('...'), '1': ObjectId('...') } }")

    section_heading(doc, "Setup – Courses Collection")
    add_code_block(doc,
        "db.courses.insertMany([\n"
        "    { _id: 201, courseName: \"Computer Science\" },\n"
        "    { _id: 202, courseName: \"Electronics\" }\n"
        "])")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ acknowledged: true, insertedIds: { '0': 201, '1': 202 } }")

    section_heading(doc, "1. $group + $avg  – Average Marks per Department")
    add_code_block(doc,
        "db.students.aggregate([\n"
        "    {\n"
        "        $group: {\n"
        '            _id: "$department",\n'
        '            averageMarks: { $avg: "$marks" }\n'
        "        }\n"
        "    }\n"
        "])")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ _id: 'CSE', averageMarks: 85 }\n"
        "{ _id: 'ECE', averageMarks: 90 }")

    section_heading(doc, "2. $lookup  – Join students with courses")
    add_code_block(doc,
        "db.students.aggregate([\n"
        "    {\n"
        "        $lookup: {\n"
        '            from:         "courses",\n'
        '            localField:   "courseId",\n'
        '            foreignField: "_id",\n'
        '            as:           "courseDetails"\n'
        "        }\n"
        "    }\n"
        "])")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{\n"
        "  rollNo: 101, name: 'Arun', department: 'CSE', marks: 85, courseId: 201,\n"
        "  subjects: [ 'DBMS', 'Python' ],\n"
        "  courseDetails: [ { _id: 201, courseName: 'Computer Science' } ]\n"
        "}\n"
        "{\n"
        "  rollNo: 102, name: 'Priya', department: 'ECE', marks: 90, courseId: 202,\n"
        "  subjects: [ 'C Programming', 'Signals' ],\n"
        "  courseDetails: [ { _id: 202, courseName: 'Electronics' } ]\n"
        "}")

    section_heading(doc, "3. $unwind  – Flatten the subjects Array")
    add_code_block(doc,
        "db.students.aggregate([\n"
        '    { $unwind: "$subjects" }\n'
        "])")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ rollNo: 101, name: 'Arun', ..., subjects: 'DBMS'          }\n"
        "{ rollNo: 101, name: 'Arun', ..., subjects: 'Python'         }\n"
        "{ rollNo: 102, name: 'Priya',..., subjects: 'C Programming'  }\n"
        "{ rollNo: 102, name: 'Priya',..., subjects: 'Signals'        }")

    section_heading(doc, "4. $lookup + $unwind  – Join and Flatten")
    add_code_block(doc,
        "db.students.aggregate([\n"
        "    {\n"
        "        $lookup: {\n"
        '            from: "courses", localField: "courseId",\n'
        '            foreignField: "_id", as: "courseDetails"\n'
        "        }\n"
        "    },\n"
        '    { $unwind: "$courseDetails" }\n'
        "])")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{\n"
        "  rollNo: 101, name: 'Arun', subjects: ['DBMS','Python'],\n"
        "  courseDetails: { _id: 201, courseName: 'Computer Science' }\n"
        "}\n"
        "{\n"
        "  rollNo: 102, name: 'Priya', subjects: ['C Programming','Signals'],\n"
        "  courseDetails: { _id: 202, courseName: 'Electronics' }\n"
        "}")

    result_block(doc,
        "Thus, advanced aggregation stages — $group/$avg, $lookup, $unwind, and $lookup "
        "combined with $unwind — were demonstrated successfully in MongoDB.")

# ── EX 6 ──────────────────────────────────────────────────────────────────────
def ex6(doc):
    doc.add_page_break()
    ex_header(doc, "6", "ARRAY OPERATORS IN MONGODB", "27/07/2026")
    aim_block(doc, "To demonstrate MongoDB array query operators ($in, $nin, $all, $size, $elemMatch) and update operators ($push, $addToSet, $pop, $pull, $pullAll, $each, $slice, $position) on a students collection.")

    section_heading(doc, "Initial Data")
    add_code_block(doc,
        'use("studentDB")\n'
        "db.students.insertMany([\n"
        '    { studentId: "S0501", name: "Arun",  skills: ["Python","Java","SQL","MongoDB"] },\n'
        '    { studentId: "S0502", name: "Bala",  skills: ["Python","SQL"] },\n'
        '    { studentId: "S0503", name: "Cathy", skills: ["Java","MongoDB"] }\n'
        "])")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ acknowledged: true, insertedIds: { '0': ObjectId('...'), '1': ..., '2': ... } }")

    # Query operators
    ops_query = [
        ("1. $in   – Skills in [Python, Java]",
         'db.students.find({ skills: { $in: ["Python","Java"] } })',
         "Returns Arun (Python, Java), Bala (Python), Cathy (Java)  →  all 3 documents"),
        ("2. $nin  – Skills NOT containing Java",
         'db.students.find({ skills: { $nin: ["Java"] } })',
         "{ studentId: 'S0502', name: 'Bala', skills: ['Python','SQL'] }"),
        ("3. $all  – Skills containing Java, SQL AND MongoDB",
         'db.students.find({ skills: { $all: ["Java","SQL","MongoDB"] } })',
         "{ studentId: 'S0501', name: 'Arun', skills: ['Python','Java','SQL','MongoDB'] }"),
        ("4. $size – Exactly 2 skills",
         'db.students.find({ skills: { $size: 2 } })',
         "{ studentId: 'S0502', name: 'Bala',  skills: ['Python','SQL'] }\n"
         "{ studentId: 'S0503', name: 'Cathy', skills: ['Java','MongoDB'] }"),
        ("5. $elemMatch – Element matches $in [Python, SQL]",
         'db.students.find({ skills: { $elemMatch: { $in: ["Python","SQL"] } } })',
         "Returns Arun and Bala"),
    ]
    for title, code, output in ops_query:
        section_heading(doc, title)
        add_code_block(doc, code)
        body_text(doc, "Output:", bold=True)
        add_output_block(doc, output)

    # Update operators
    ops_update = [
        ("6. $push – Add JavaScript to Arun's skills",
         'db.students.updateOne(\n    { studentId: "S0501" },\n    { $push: { skills: "JavaScript" } }\n)',
         "skills: ['Python','Java','SQL','MongoDB','JavaScript']"),
        ("7. $addToSet – Add Python (already exists; no duplicate)",
         'db.students.updateOne(\n    { studentId: "S0501" },\n    { $addToSet: { skills: "Python" } }\n)',
         "skills: ['Python','Java','SQL','MongoDB']  ← unchanged"),
        ("8. $pop: 1 – Remove last element",
         'db.students.updateOne(\n    { studentId: "S0501" },\n    { $pop: { skills: 1 } }\n)',
         "skills: ['Python','Java','SQL']"),
        ("9. $pop: -1 – Remove first element",
         'db.students.updateOne(\n    { studentId: "S0501" },\n    { $pop: { skills: -1 } }\n)',
         "skills: ['Java','SQL','MongoDB']"),
        ("10. $pull – Remove SQL",
         'db.students.updateOne(\n    { studentId: "S0501" },\n    { $pull: { skills: "SQL" } }\n)',
         "skills: ['Python','Java','MongoDB']"),
        ("11. $pullAll – Remove Java and SQL",
         'db.students.updateOne(\n    { studentId: "S0501" },\n    { $pullAll: { skills: ["Java","SQL"] } }\n)',
         "skills: ['Python','MongoDB']"),
        ("12. $push + $each – Add multiple elements",
         'db.students.updateOne(\n    { studentId: "S0501" },\n'
         '    { $push: { skills: { $each: ["Python","Java","SQL"] } } }\n)',
         "skills: ['Python','Java','SQL','MongoDB','Python','Java','SQL']"),
        ("13. $addToSet + $each – Add without duplicates",
         'db.students.updateOne(\n    { studentId: "S0501" },\n'
         '    { $addToSet: { skills: { $each: ["Python","MongoDB","SQL"] } } }\n)',
         "skills: ['Python','Java','SQL','MongoDB']  ← no duplicates added"),
        ("14. $push + $slice – Keep only first 5",
         'db.students.updateOne(\n    { studentId: "S0501" },\n'
         '    { $push: { skills: { $each: ["React","Node.js"], $slice: 5 } } }\n)',
         "skills: ['Python','Java','SQL','MongoDB','React']"),
        ("15. $push + $position – Insert at index 0",
         'db.students.updateOne(\n    { studentId: "S0501" },\n'
         '    { $push: { skills: { $each: ["Python"], $position: 0 } } }\n)',
         "skills: ['Python','Python','Java','SQL','MongoDB']"),
    ]
    for title, code, output in ops_update:
        section_heading(doc, title)
        add_code_block(doc, code)
        body_text(doc, "Output:", bold=True)
        add_output_block(doc, output)

    result_block(doc,
        "Thus, MongoDB array query operators ($in, $nin, $all, $size, $elemMatch) and array "
        "update operators ($push, $addToSet, $pop, $pull, $pullAll, $each, $slice, $position) "
        "were demonstrated successfully.")

# ── EX 7A ─────────────────────────────────────────────────────────────────────
def ex7a(doc):
    doc.add_page_break()
    ex_header(doc, "7A", "INDEXING – BOOKS COLLECTION", "03/08/2026")
    aim_block(doc, "To create and use single-field, text, and compound indexes on a books collection and compare query performance before and after indexing.")

    section_heading(doc, "Database & Sample Data")
    add_code_block(doc, "use bookDB\ndb.books.insertMany([...])  // 10 book documents")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "{ acknowledged: true, insertedIds: { '0': ObjectId('...'), ... } }")

    queries = [
        ("1. Find All Books (title only)",
         "db.books.find({}, { title: 1, _id: 0 })",
         "[ { title: 'MongoDB Basics' }, { title: 'Learning Python' },\n"
         "  { title: 'Java Fundamentals' }, { title: 'Data Science Handbook' },\n"
         "  { title: 'Machine Learning Essentials' }, { title: 'SQL Complete Guide' },\n"
         "  { title: 'Node.js in Action' }, { title: 'Deep Learning' },\n"
         "  { title: 'MongoDB Advanced' }, { title: 'Python for Data Analysis' } ]"),
        ("2. Find Books by John Smith",
         'db.books.find({ author: "John Smith" })',
         "{ bookId: 101, title: 'MongoDB Basics',  author: 'John Smith', year: 2023 }\n"
         "{ bookId: 109, title: 'MongoDB Advanced', author: 'John Smith', year: 2024 }"),
        ("3. Find Books Published by Tech Press",
         'db.books.find({ publisher: "Tech Press" })',
         "{ bookId: 101, title: 'MongoDB Basics',  publisher: 'Tech Press', ... }\n"
         "{ bookId: 109, title: 'MongoDB Advanced', publisher: 'Tech Press', ... }"),
        ("4. Books Published After 2022",
         "db.books.find({ year: { $gt: 2022 } }, { title: 1, year: 1, _id: 0 })",
         "{ title: 'MongoDB Basics',             year: 2023 }\n"
         "{ title: 'Data Science Handbook',       year: 2023 }\n"
         "{ title: 'Machine Learning Essentials', year: 2024 }\n"
         "{ title: 'Node.js in Action',           year: 2023 }\n"
         "{ title: 'Deep Learning',               year: 2024 }\n"
         "{ title: 'MongoDB Advanced',            year: 2024 }\n"
         "{ title: 'Python for Data Analysis',    year: 2023 }"),
    ]
    for title, code, output in queries:
        section_heading(doc, title)
        add_code_block(doc, code)
        body_text(doc, "Output:", bold=True)
        add_output_block(doc, output)

    section_heading(doc, "5. Single-Field Index on category (before/after)")
    add_code_block(doc, 'db.books.find({ category: "Database" }).explain("executionStats")')
    body_text(doc, "Output (before index):", bold=True)
    add_output_block(doc, "totalDocsExamined: 10")
    add_code_block(doc, "db.books.createIndex({ category: 1 })")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "category_1")
    add_code_block(doc, 'db.books.find({ category: "Database" }).explain("executionStats")')
    body_text(doc, "Output (after index):", bold=True)
    add_output_block(doc, "totalDocsExamined: 3")

    section_heading(doc, "6. Drop an Index")
    add_code_block(doc, "db.books.createIndex({ title: 1 })\ndb.books.dropIndex(\"title_1\")")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "title_1\n{ nIndexesWas: 3, ok: 1 }")

    section_heading(doc, "7. Text Index on author – Search for James Gosling")
    add_code_block(doc,
        'db.books.createIndex({ author: "text" })\n'
        'db.books.find({ $text: { $search: "James Gosling" } }, { _id:0, title:1, author:1 })')
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ title: 'Java Fundamentals', author: 'James Gosling' }")

    section_heading(doc, "8. Compound Index on author + year (before/after)")
    add_code_block(doc, 'db.books.find({ author: "John Smith" }).explain("executionStats")')
    body_text(doc, "Output (before):", bold=True)
    add_output_block(doc, "totalDocsExamined: 10")
    add_code_block(doc, "db.books.createIndex({ author: 1, year: 1 })")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "author_1_year_1")
    add_code_block(doc, 'db.books.find({ author: "John Smith" }).explain("executionStats")')
    body_text(doc, "Output (after):", bold=True)
    add_output_block(doc, "totalDocsExamined: 2")

    result_block(doc,
        "Thus, single-field, text, and compound indexes were created on the books collection, "
        "and query performance improvement was verified using explain().")

# ── EX 7B ─────────────────────────────────────────────────────────────────────
def ex7b(doc):
    doc.add_page_break()
    ex_header(doc, "7B", "INDEXING – PRODUCTS COLLECTION", "03/08/2026")
    aim_block(doc, "To create single-field, unique, compound, and text indexes on a products collection and measure query performance improvement.")

    section_heading(doc, "Sample Data")
    add_code_block(doc,
        "db.products.insertMany([\n"
        '    { productid: "P101", name: "Laptop",        category: "Electronics", price: 55000 },\n'
        '    { productid: "P102", name: "Mobile Phone",  category: "Electronics", price: 25000 },\n'
        '    { productid: "P103", name: "Office Chair",  category: "Furniture",   price:  8500 },\n'
        '    { productid: "P104", name: "Refrigerator",  category: "Appliances",  price: 45000 },\n'
        '    { productid: "P105", name: "Study Table",   category: "Furniture",   price:  7000 }\n'
        "])")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "{ acknowledged: true, insertedIds: { '0': ObjectId('...'), ... } }")

    steps = [
        ("1. Single-Field Index on category",
         'db.products.find({ category: "Electronics" }).explain("executionStats")',
         "stage: 'COLLSCAN'\nnReturned: 2\ntotalDocsExamined: 5",
         "db.products.createIndex({ category: 1 })",
         "category_1",
         'db.products.find({ category: "Electronics" }).explain("executionStats")',
         "stage: 'IXSCAN'\nnReturned: 2\ntotalDocsExamined: 2"),
        ("2. Unique Index on productid",
         'db.products.find({ productid: "P101" }).explain("executionStats")',
         "stage: 'COLLSCAN'\nnReturned: 1\ntotalDocsExamined: 5",
         "db.products.createIndex({ productid: 1 }, { unique: true })",
         "productid_1",
         'db.products.find({ productid: "P101" }).explain("executionStats")',
         "stage: 'IXSCAN'\nnReturned: 1\ntotalDocsExamined: 1"),
    ]
    for (title, q_before, out_before, create_q, create_out, q_after, out_after) in steps:
        section_heading(doc, title)
        add_code_block(doc, q_before)
        body_text(doc, "Output (before):", bold=True)
        add_output_block(doc, out_before)
        add_code_block(doc, create_q)
        body_text(doc, "Output:", bold=True)
        add_output_block(doc, create_out)
        add_code_block(doc, q_after)
        body_text(doc, "Output (after):", bold=True)
        add_output_block(doc, out_after)

    section_heading(doc, "3. Find Products Priced Above 10000")
    add_code_block(doc, "db.products.find({ price: { $gt: 10000 } }, { _id: 0 })")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{ productid: 'P101', name: 'Laptop',       category: 'Electronics', price: 55000 }\n"
        "{ productid: 'P102', name: 'Mobile Phone', category: 'Electronics', price: 25000 }\n"
        "{ productid: 'P104', name: 'Refrigerator', category: 'Appliances',  price: 45000 }")

    section_heading(doc, "4. Compound Index on category (asc) + price (desc)")
    add_code_block(doc, 'db.products.find({ category: "Furniture", price: { $lt: 10000 } }).explain("executionStats")')
    body_text(doc, "Output (before):", bold=True)
    add_output_block(doc, "stage: 'COLLSCAN'\nnReturned: 2\ntotalDocsExamined: 5")
    add_code_block(doc, "db.products.createIndex({ category: 1, price: -1 })")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "category_1_price_-1")
    add_code_block(doc, 'db.products.find({ category: "Furniture", price: { $lt: 10000 } }).explain("executionStats")')
    body_text(doc, "Output (after):", bold=True)
    add_output_block(doc, "stage: 'IXSCAN'\nnReturned: 2\ntotalDocsExamined: 2")

    section_heading(doc, "5. Text Index on name – Search for Laptop")
    add_code_block(doc,
        'db.products.find({ name: "Laptop" }).explain("executionStats")')
    body_text(doc, "Output (before):", bold=True)
    add_output_block(doc, "stage: 'COLLSCAN'\nnReturned: 1\ntotalDocsExamined: 5")
    add_code_block(doc, 'db.products.createIndex({ name: "text" })')
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "name_text")
    add_code_block(doc, 'db.products.find({ $text: { $search: "Laptop" } }).explain("executionStats")')
    body_text(doc, "Output (after):", bold=True)
    add_output_block(doc, "stage: 'TEXT'\nnReturned: 1\ntotalDocsExamined: 1")

    result_block(doc,
        "Thus, single-field, unique, compound, and text indexes were created on the products "
        "collection and performance improvements were verified using explain().")

# ── EX 8 ──────────────────────────────────────────────────────────────────────
def ex8(doc):
    doc.add_page_break()
    ex_header(doc, "8", "SPATIAL INDEXING IN MONGODB", "10/08/2026")
    aim_block(doc, "To implement geospatial data storage and perform location-based queries using MongoDB.")

    section_heading(doc, "1. Database Creation")
    add_code_block(doc, "use GeoDB")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "switched to db GeoDB")

    section_heading(doc, "2. Collection Creation")
    add_code_block(doc, 'db.createCollection("places")')
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "{ ok: 1 }")

    section_heading(doc, "3. Insert 5 Records")
    add_code_block(doc,
        "db.places.insertMany([\n"
        '  { name: "Central Park",          category: "Park",      location: { type: "Point", coordinates: [-73.9654, 40.7829] } },\n'
        '  { name: "Times Square",          category: "Landmark",  location: { type: "Point", coordinates: [-73.9855, 40.7580] } },\n'
        '  { name: "Brooklyn Bridge",       category: "Bridge",    location: { type: "Point", coordinates: [-73.9969, 40.7061] } },\n'
        '  { name: "Empire State Building", category: "Building",  location: { type: "Point", coordinates: [-73.9857, 40.7484] } },\n'
        '  { name: "Statue of Liberty",     category: "Monument",  location: { type: "Point", coordinates: [-74.0445, 40.6892] } }\n'
        "])")
    body_text(doc, "Output:", bold=True)
    add_output_block(doc,
        "{\n"
        "  acknowledged: true,\n"
        "  insertedIds: {\n"
        "    '0': ObjectId('6acc593d44cc774a3656e31c'),\n"
        "    '1': ObjectId('6acc593d44cc774a3656e31d'),\n"
        "    '2': ObjectId('6acc593d44cc774a3656e31e'),\n"
        "    '3': ObjectId('6acc593d44cc774a3656e31f'),\n"
        "    '4': ObjectId('6acc593d44cc774a3656e320')\n"
        "  }\n"
        "}")

    section_heading(doc, "4. Create Geospatial Index")
    add_code_block(doc, 'db.places.createIndex({ location: "2dsphere" })')
    body_text(doc, "Output:", bold=True)
    add_output_block(doc, "location_2dsphere")

    section_heading(doc, "5. Geospatial Queries")

    geo_queries = [
        ("Query 1: Display All Records",
         "db.places.find()",
         "Returns all 5 documents: Central Park, Times Square, Brooklyn Bridge,\nEmpire State Building, Statue of Liberty"),
        ("Query 2: Find Places Near Times Square",
         "db.places.find({\n"
         "  location: {\n"
         "    $near: {\n"
         "      $geometry: { type: \"Point\", coordinates: [-73.9855, 40.7580] }\n"
         "    }\n"
         "  }\n"
         "})",
         "Times Square → Empire State Building → Central Park  (nearest first)"),
        ("Query 3: Find Places Within 5 km of Times Square",
         "db.places.find({\n"
         "  location: {\n"
         "    $near: {\n"
         "      $geometry: { type: \"Point\", coordinates: [-73.9855, 40.7580] },\n"
         "      $maxDistance: 5000\n"
         "    }\n"
         "  }\n"
         "})",
         "Times Square, Empire State Building, Central Park  (within 5 km)"),
        ("Query 4: Find Places Within 3 km of Central Park",
         "db.places.find({\n"
         "  location: {\n"
         "    $geoWithin: {\n"
         "      $centerSphere: [ [-73.9654, 40.7829], 3 / 6378.1 ]\n"
         "    }\n"
         "  }\n"
         "})",
         "{ name: 'Central Park', category: 'Park', location: { type: 'Point',\n"
         "  coordinates: [-73.9654, 40.7829] } }"),
        ("Query 5: Nearest Place to Brooklyn Bridge Within 10 km",
         "db.places.find({\n"
         "  location: {\n"
         "    $near: {\n"
         "      $geometry: { type: \"Point\", coordinates: [-73.9969, 40.7061] },\n"
         "      $maxDistance: 10000\n"
         "    }\n"
         "  }\n"
         "}).limit(1)",
         "{ name: 'Brooklyn Bridge', category: 'Bridge',\n"
         "  location: { type: 'Point', coordinates: [-73.9969, 40.7061] } }"),
        ("Query 6: Find Places Within a Polygon",
         "db.places.find({\n"
         "  location: {\n"
         "    $geoWithin: {\n"
         "      $geometry: {\n"
         "        type: \"Polygon\",\n"
         "        coordinates: [[ [-74.05,40.68],[-73.95,40.68],\n"
         "                        [-73.95,40.80],[-74.05,40.80],[-74.05,40.68] ]]\n"
         "      }\n"
         "    }\n"
         "  }\n"
         "})",
         "Returns all 5 places within the specified bounding polygon:\n"
         "Statue of Liberty, Times Square, Central Park,\nEmpire State Building, Brooklyn Bridge"),
    ]

    for title, code, output in geo_queries:
        section_heading(doc, title)
        add_code_block(doc, code)
        body_text(doc, "Output:", bold=True)
        add_output_block(doc, output)

    result_block(doc,
        "Thus, a MongoDB database and collection were created, five geospatial records were "
        "inserted, a 2dsphere index was created, and location-based queries were performed "
        "using $near, $geoWithin, $centerSphere, and $geometry operators.")

# ══════════════════════════════════════════════════════════════════════════════
#  BUILD DOCUMENT
# ══════════════════════════════════════════════════════════════════════════════

# Title / cover
college_header(doc)

# Certificate
certificate_page(doc)

# Index
index_page(doc)

# Exercises
ex1(doc)
ex2(doc)
ex3(doc)
ex4(doc)
ex5(doc)
ex6(doc)
ex7a(doc)
ex7b(doc)
ex8(doc)

# Save
out_path = r"c:\Users\Yugesh\Desktop\sem5\NoSQL\NoSQL_Record.docx"
doc.save(out_path)
print(f"Saved: {out_path}")
