'''
This Script creates a Map Book using:
- Data Driven Page PDF generated using ArcGIS
- Title Page
- Overview Page
- Graphs Page

Developed to create a Map Book of Zulia State - Venezuela
By: Marco Portillo
'''

# Import libraries
import arcpy, os

# Create an output location variable
outDir = r"C:\Users\Marco\Desktop\MDP_project"  

# Create a new, empty pdf document in the specified output location folder
finalpdf_filename = outDir + r"\Zulia_St_MapBook_and_reports.pdf"
if os.path.exists(finalpdf_filename):
  os.remove(finalpdf_filename)
finalPdf = arcpy.mapping.PDFDocumentCreate(finalpdf_filename) 


# Add the title page to the pdf
finalPdf.appendPages(r"C:\Users\Marco\Desktop\MDP_project\title.pdf")

# Add the overview map to the pdf
finalPdf.appendPages(r"C:\Users\Marco\Desktop\MDP_project\overview.pdf")

# Export the Data Driven Pages to a temporary pdf and then add it to the
# final pdf. Alternately, if your Data Driven Pages have already been
# exported, simply append that document to the final pdf.

temp_filename = r"C:\Users\Marco\Desktop\MDP_project\Zulia_State_MapBook.pdf"

finalPdf.appendPages(temp_filename)

# Insert the pdf pages containing the reports and graphs into the final pdf

finalPdf.insertPages(r"C:\Users\Marco\Desktop\MDP_project\graphs.pdf", 2)


# Update the properties of the final pdf
finalPdf.updateDocProperties(pdf_open_view="USE_THUMBS",
                             pdf_layout="SINGLE_PAGE")

# Save your result
finalPdf.saveAndClose()

# Delete variables
del finalPdf

print '***///***Script successfully executed***///***'

